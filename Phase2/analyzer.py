import json
import os
import requests

from google.cloud import language_v1
import pandas as pd

# imports the contents of utils folder
from utils.utils import (
    check_empty_str_in_dict,
    json_check,
    masked_dict_vals,
)


class APIConnections:
    """
    This class uses the bearer token for authentication, and checks the connections to both the twitter API and the Google NLP API.    
    """

    def __init__(
        self,
        twitter_bearer_token=os.environ.get("BEARER_TOKEN"),
        google_application_credentials=os.environ.get(
            "GOOGLE_APPLICATION_CREDENTIALS"
        ),  # noqa: E501
        verbose=False,
    ) -> None:

        # set the keys into dictionaries corresponding to
        # twitter and google

        self.verbose = verbose

        self.twitter_keys = {
            "bearer_token": str(twitter_bearer_token),
        }
        # ensure there are not empty strings for values
        check_empty_str_in_dict(self.twitter_keys)

        # checks the connection
        self.check_twitter_connection()

        self.google_application_credentials = {
            "GOOGLE_APPLICATION_CREDENTIALS": str(
                google_application_credentials
            )  # noqa: E501
        }
        # ensures there are not empty strings for values
        check_empty_str_in_dict(self.google_application_credentials)

        # checks the the json exists
        json_check(
            self.google_application_credentials[
                "GOOGLE_APPLICATION_CREDENTIALS"
            ],  # noqa: E501
            verbose=self.verbose,
        )
        # checks the connection
        self.check_google_connection()

        if self.verbose:
            print("The (masked) API keys: \n")
            print(json.dumps(masked_dict_vals(self.twitter_keys), indent=4))
            print(
                json.dumps(
                    masked_dict_vals(self.google_application_credentials),
                    indent=4,  # noqa: E501
                )
            )
            print("\n")

    def check_google_connection(self):
        """
        This checks the endpoints for connecting to the Google NLP API.
        """

        # Instantiates a client
        client = language_v1.LanguageServiceClient()

        # Detects the sentiment of the text
        _ = client.analyze_sentiment(
            request={
                "document": language_v1.Document(
                    content="Hello, world!",
                    type_=language_v1.Document.Type.PLAIN_TEXT,  # noqa: E501
                )
            }
        ).document_sentiment

    # checks the connection to the twitter API
    def check_twitter_connection(self):
        """
        The method checks the endpoints. If it can't connect it raisesan an exception.
        """
        _ = requests.request(
            "GET",
            "https://api.twitter.com/2/tweets/search/recent",
            auth=self._bearer_oauth,
            params={"query": "#Twitter"},
        )

        if _.status_code != 200:
            raise Exception(_.status_code, _.text)

    def _bearer_oauth(self, r):
        """
         This uses the bearer token for authorization to use the twitter API.
        """
        # passes the headers
        r.headers[
            "Authorization"
        ] = f"""
        Bearer {self.twitter_keys['bearer_token']}
        """
        r.headers["User-Agent"] = "v2FullArchiveSearchPython"

        return r


class HashtagAnalyzer:
    """
    This class searches for tweets containing the specified hashtag within a specified range of time (not greater than the past 7 days)   
    """

    def __init__(
        self,
        api_conns=None,
        hashtag="#Salem",
        start_time="2022-10-16T00:00:00Z",
        end_time="2022-10-22T00:00:00Z",
        max_result="15",
        no_retweets=False,
        verbose=False,
    ) -> None:

        # setting the variables
        self.api_conns = api_conns
        self.search_url = "https://api.twitter.com/2/tweets/search/recent"
        self.hashtag = hashtag
        self.start_time = start_time
        self.end_time = end_time
        self.max_result = max_result
        self.no_retweets = no_retweets
        self.verbose = verbose

        # gets the tweets
        self.tweets_data = self._get_tweets()

        if self.verbose:
            print(
                "self.tweets_data: \n \n",
                json.dumps(self.tweets_data, indent=4, sort_keys=True),
                "\n ------- \n \n",
            )

        # creates a dataframe from self.tweets_data
        self.tweets_df = self._generate_df()

        if self.verbose:
            print("self.tweets_df: \n \n", self.tweets_df, "\n ------- \n \n")

    def _bearer_oauth(self, r):
        """
        This uses the bearer token for authorization to use the twitter API.
        """
        # passes the headers
        r.headers[
            "Authorization"
        ] = f"Bearer {self.api_conns.twitter_keys['bearer_token']}"
        r.headers["User-Agent"] = "v2FullArchiveSearchPython"

        return r

    # conncts to endpoint after authenticating, or prints exception if it fails
    def _connect_endpoint(self, search_url, params):
        """
        This method connects to the endpoints.
        """
        response = requests.request(
            "GET", search_url, auth=self._bearer_oauth, params=params
        )
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def _generate_df(self):
        """
        This method creates a pd.DataFrame from a twitter API JSON.
        """
        tweet_df = pd.json_normalize(self.tweets_data["data"])

        if self.no_retweets:
            return tweet_df[
                ~tweet_df["text"].astype(str).str.startswith("RT ")
            ].reset_index(drop=True)

        return tweet_df

    # gets tweets using hashtag
    def _get_tweets(self):
        """
        Gets the tweets with the previously specified hashtag.
        """
        query_params = {
            "query": self.hashtag,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "max_results": self.max_result,
        }

        if self.verbose:
            print(
                "query parameters:",
                json.dumps(query_params, indent=4, sort_keys=True,),
            )

        jsn_resp = self._connect_endpoint(self.search_url, query_params,)

        # check if tweets are returned
        if jsn_resp["meta"]["result_count"] == 0:
            msg = f"""
            It appears that there are no tweets with the hashtag {self.hashtag}
            in the date range provided: {self.start_time} -- {self.end_time}
            """
            raise ValueError(msg)

        return jsn_resp

    # analyzes the tweets and add sentiment scores
    def analyze_tweets(self):
        """
        This analyze the tweets one-by-one, adds sentiment and magnitusde scores, and returns them.
        -------
        sentiment_df: pd.DataFrame
            dataframe with the tweet text, and sentiment score/magnitude
        """

        sentiment_df = self.tweets_df.copy()

        # adds blank columns
        sentiment_df["sentiment_score"] = ""
        sentiment_df["sentiment_magnitude"] = ""

        for index, row in sentiment_df.iterrows():
            tweet = row["text"]
            sentiment_vals = self._analyze_tweet(index, tweet)
            row["sentiment_score"] = sentiment_vals.score
            row["sentiment_magnitude"] = sentiment_vals.magnitude

        return sentiment_df

    # uses google NLP to analyze a tweet
    def _analyze_tweet(self, ind, tweet_text):
        """
        This method analyzes a tweet using Google NLP and returns a sentiment score and a magnitude score for each sentence in the tweet.
        """
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
                f"""
                Sentiment for the text {ind}:
                {sentiment.score}, {sentiment.magnitude}
                """
            )

        return sentiment

    def calculate_total_sentiment(self):
        """
        As the sentiment scores cannot be summed, this function takes all
        tweets, creates a single document and calculates a single sentiment
        score
        See:
        https://cloud.google.com/natural-language/docs/basics
        https://stackoverflow.com/questions/47998973/google-natural-language-sentiment-analysis-aggregate-scores # noqa: E501
        """

        all_tweet_text = ""
        all_tweets_text_only = self.tweets_df["text"]

        for tweet_text in all_tweets_text_only:
            all_tweet_text = (
                all_tweet_text + tweet_text + "."
            )  # adding a period for clarity

        if self.verbose:
            print(
                f"""
                \n all the tweets as a single document:
                \n \n {all_tweet_text} \n \n
                """
            )

        s = self._analyze_tweet(0, all_tweet_text)

        return (s.score, s.magnitude)


if __name__ == "__main__":

    # import the keys, check the connections
    api_c = APIConnections(verbose=True)

    hta = HashtagAnalyzer(
        api_conns=api_c,
        hashtag="#Salem",
        start_time="2022-10-16T00:00:00Z",
        end_time="2022-10-22T00:00:00Z",
        max_result="15",
        verbose=True,
        no_retweets=True,
    )

    # calculates the sentiment of each tweet
    hta_sentiment = hta.analyze_tweets()
    print(hta_sentiment)

    # calculates the total sentiment by combining
    # the tweet into a single document
    hta_total_sentiment = hta.calculate_total_sentiment()
    # https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values # noqa: E501
    print(hta_total_sentiment)
