import requests
import os
import json

# retrieve bearer token that is saved as local variable
bearer_token = os.environ.get("BEARER_TOKEN")

# url required for searching tweets from the past 7 days
search_url = "https://api.twitter.com/2/tweets/search/recent"


# the query contains the hashtag being searched for, the date/time range being searched,
# and the number of results that will be returned
query_params = {
    "query": "#halloween",
    "start_time": "2022-10-10T00:00:00Z",  # can only do recent tweets
    "end_time": "2022-10-14T00:00:00Z",
    "max_results": "15",
}


# authenticates using the bearer token
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    # passes the headers
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


# connects to the endpoint after authenticating with bearer token, prints exception if it fails,
# returns response in json format if it succeeds
def connect_endpoint(search_url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        print(response.status_code)
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
