import requests
import os
import json

# retrieve bearer token that is saved as local variable
bearer_token = os.environ.get("BEARER_TOKEN")

# url required for searching tweets from the past 7 days
search_url = "http://api.twitter.com/2/tweets/search/recent"

# parameters used for searching (this is where the user's name being searched for is specified)
query_params = {
    "query": "(from:NASA -is:retweet) OR #NASA",
    "tweet.fields": "author_id",
}

# authenticates using the bearer token
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    # passes the headers
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


# connects to the endpoint after authenticating with bearer token, prints exception if it fails,
# returns response in json format if it succeeds
def connect_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# this is where the main part of the program is defined
def main():
    json_response = connect_endpoint(search_url, query_params)
    # prints the returned json
    print(json.dumps(json_response, indent=4, sort_keys=True))


# this runs the main program
if __name__ == "__main__":
    main()
