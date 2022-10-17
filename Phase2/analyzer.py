import requests
import os
import json
from google.cloud import language_v1
import pandas as pd

# imports the contents of utils folder
from utils.utils import (
    check_empty_str_in_dict,
    json_check,
    masked_dict_vals,
)

class APIConnections:

    # these are the keys that are stored as environment variables
    def __init__(
        self,
        twitter_consumer_key=os.environ.get("CONSUMER_KEY"),
        twitter_consumer_secret=os.environ.get("CONSUMER_SECRET"),
        twitter_bearer_token=os.environ.get("BEARER_TOKEN"),
        twitter_access_token=os.environ.get("ACCESS_TOKEN"),
        twitter_access_secret=os.environ.get("ACCESS_SECRET"),
        rapidapi_key=os.environ.get("RAPIDAPI_KEY"),
        google_application_credentials=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
        verbose=False,
    ) -> None:

        # set the keys into dictionaries corresponding to twitter, rapid api, and google

        # -- Twitter API Connections
        #
        self.twitter_keys = {
            "consumer_key": str(twitter_consumer_key),
            "consumer_secret": str(twitter_consumer_secret),
            "bearer_token": str(twitter_bearer_token),
            "access_token": str(twitter_access_token),
            "access_token_secret": str(twitter_access_secret),
        }
        # ensure there are not empty strings for values
        check_empty_str_in_dict(self.twitter_keys)

        # checks the connection
        self.check_twitter_connection()

        self.rapid_api_keys = {"rapidapi_key": str(rapidapi_key)}

        # ensures there are not empty strings for values
        check_empty_str_in_dict(self.rapid_api_keys)

        # checks the connection
        self.check_rapidapi_connection()

        self.google_application_credentials = {
            "GOOGLE_APPLICATION_CREDENTIALS": str(google_application_credentials)
        }
        # ensures there are not empty strings for values
        check_empty_str_in_dict(self.google_application_credentials)

        # checks the the json exists
        json_check(
            self.google_application_credentials["GOOGLE_APPLICATION_CREDENTIALS"]
        )
        # checks the connection
        self.check_google_connection()

        if verbose:
            print("The (masked) API keys: \n")
            print(json.dumps(masked_dict_vals(api_conns.twitter_keys), indent=4))
            print(json.dumps(masked_dict_vals(api_conns.rapid_api_keys), indent=4))
            print(
                json.dumps(
                    masked_dict_vals(api_conns.google_application_credentials), indent=4
                )
            )
            print("\n")

        return

    def check_google_connection(self):

        # Instantiates a client
        client = language_v1.LanguageServiceClient()

        # Detects the sentiment of the text
        _ = client.analyze_sentiment(
            request={
                "document": language_v1.Document(
                    content="Hello, world!", type_=language_v1.Document.Type.PLAIN_TEXT
                )
            }
        ).document_sentiment


class HashtagAnalyzer:
    def __init__(
        self,
        api_conns,
        search_url="https://api.twitter.com/2/tweets/search/recent",
        hashtag="#halloween",
        start_time="2022-10-10T00:00:00Z",
        end_time="2022-10-16T00:00:00Z",
        max_result="15",
        no_retweets=False,
        verbose=False,
    ) -> None:

        # setting the variables
        self.api_conns = api_conns
        self.search_url = search_url
        self.hashtag = hashtag
        self.start_time = start_time
        self.end_time = end_time
        self.max_result = max_result
        self.no_retweets = no_retweets
        self.verbose = verbose

        # gets the tweets
        self.tweets_data = self._get_tweets()
        if verbose:
            print(
                "self.tweets_data: \n \n",
                json.dumps(self.tweets_data, indent=4, sort_keys=True),
                "\n ------- \n \n",
            )

        # creates a dataframe from self.tweets_data
        self.tweets_df = self._generate_df()

        if verbose:
            print("self.tweets_df: \n \n", self.tweets_df, "\n ------- \n \n")

    def _bearer_oauth(self, r):
        # passes the headers
        r.headers[
            "Authorization"
        ] = f"Bearer {self.api_conns.twitter_keys['bearer_token']}"
        r.headers["User-Agent"] = "v2FullArchiveSearchPython"

        return r

    # conncts to endpoint after authenticating, or prints exception if it fails
    def _connect_endpoint(self, search_url, params):
        response = requests.request(
            "GET", search_url, auth=self._bearer_oauth, params=params
        )
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def _generate_df(self):
        # create a dataframe
        df = pd.json_normalize(self.tweets_data["data"])

        if self.no_retweets:
            return df[~df["text"].astype(str).str.startswith("RT ")].reset_index(
                drop=True
            )
        else:
            return df

    # gets tweets using hashtag
    def _get_tweets(self):
        query_params = {
            "query": self.hashtag,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "max_results": self.max_result,
        }

        print("query parameters:", json.dumps(query_params, indent=4, sort_keys=True))

        jsn_resp = self._connect_endpoint(self.search_url, query_params)

        # check if tweets are returned
        if jsn_resp["meta"]["result_count"] == 0:
            msg = f"It appears that there are no tweets with the hashtag {self.hashtag} in the date range provided: {self.start_time} -- {self.end_time}"
            raise ValueError(msg)

        return jsn_resp

    # analyzes the tweets and add sentiment scores
    def analyze_tweets(self):
        sentiment_df = self.tweets_df.copy()

        # not sure if this is the best way to add blank columns
        sentiment_df["sentiment_score"] = ""
        sentiment_df["sentiment_magnitude"] = ""

        for index, row in sentiment_df.iterrows():
            tweet = row["text"]
            sentiment_vals = self._analyze_tweet(index, tweet)
            row["sentiment_score"] = sentiment_vals.score
            row["sentiment_magnitude"] = sentiment_vals.magnitude

        print("------- \n \n")
        return sentiment_df

    # uses google NLP to analyze a tweet
    def _analyze_tweet(self, ind, tweet_text):
        client = language_v1.LanguageServiceClient()

        # this contains the text from a movie review
        document = language_v1.Document(
            content=tweet_text, type_=language_v1.Document.Type.PLAIN_TEXT
        )

        # this detects the sentiment of the text using google NLP
        sentiment = client.analyze_sentiment(
            request={"document": document}
        ).document_sentiment

        if self.verbose:
            print(
                f"Sentiment for the text {ind}: {sentiment.score}, {sentiment.magnitude}"
            )

        return sentiment

    def calculate_total_sentiment(self):

        all_tweet_text = ""
        all_tweets_text_only = self.tweets_df["text"]

        for tweet_text in all_tweets_text_only:
            all_tweet_text = (
                all_tweet_text + tweet_text + "."
            )  # adding a period for clarity

        if self.verbose:
            print(f"all the tweets as a single document: \n \n {all_tweet_text} \n \n ")

        return self._analyze_tweet("", all_tweet_text)


if __name__ == "__main__":

    # import the keys, check the connections
    api_conns = APIConnections(verbose=False)

    hta = HashtagAnalyzer(
        api_conns=api_conns,
        hashtag="#Salem",
        start_time="2022-10-10T00:00:00Z",
        end_time="2022-10-16T00:00:00Z",
        max_result="10",
        verbose=True,
        no_retweets=True,
    )

    # calculates the sentiment of each tweet
    sentiment_df = hta.analyze_tweets()
    print(sentiment_df)

    # calculates the total sentiment by combining the tweets into a single document
    total_sentiment = hta.calculate_total_sentiment()
    # https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values
    print(total_sentiment)
