import requests
import os
import json

# retrieve bearer token that is saved as local variable
bearer_token = os.environ.get("BEARER_TOKEN")

# creates an url using the username(s) and the field(s) being searched for
def make_url():
    usernames = "usernames=keaneofficial"
    user_fields = "user.fields=description"
    url = f"https://api.twitter.com/2/users/by?{usernames}&{user_fields}"
    return url


# authenticates using the bearer token
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    # passes the headers
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"

    return r


# connects to the endpoint after authenticating with bearer token, prints exception if it fails,
# returns response in json format if it succeeds
def connect_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(f"the response status code is: {response.status_code}")
    if response.status_code != 200:
        # there is an error!
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}"
        )
    return response.json()


# this is where the main part of the program is defined
def main():
    url = make_url()
    print(f"the request url is {url}")
    json_response = connect_endpoint(url)
    # prints the returned json
    print(json.dumps(json_response, indent=4, sort_keys=True))


# this runs the main program
if __name__ == "__main__":
    main()
