import botometer
import os
import json

# retrieve the keys that are stored as environment variables
rapidapi_key = os.environ.get("RAPIDAPI_KEY")
twitter_app_auth = {
    "consumer_key": os.environ.get("CONSUMER_KEY"),
    "consumer_secret": os.environ.get("CONSUMER_SECRET"),
    "access_token": os.environ.get("ACCESS_TOKEN"),
    "access_token_secret": os.environ.get("ACCESS_SECRET"),
}

# calls the botometer
bom = botometer.Botometer(
    wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth
)

# checks a sequence of accounts
accounts = ["@NASAHubble", "@BU_Tweets", "@MBTA", "@ENGEC601"]
for screen_name, result in bom.check_accounts_in(accounts):

    # prints the output json
    print(screen_name, json.dumps(result, indent=4, sort_keys=True))
