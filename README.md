## Project 2

Welcome to the main readme for project 2!

For more information on this project please visit the wiki: https://github.com/MariahSJones/ENG_EC_601/wiki

### Phase 1
For phase 1 you will need the following:
```
conda create -n phase1 python==3.8
conda activate phase1
pip install -r requirements.txt
```

For this code to work, you will need a number of environment variables. In the `~/.bashrc` add the following:

```
export 'GOOGLE_APPLICATION_CREDENTIALS'='<path_to_google_application_json>'

export 'CONSUMER_KEY'='<your_consumer_key>'
export 'CONSUMER_SECRET'='<your_consumer_secret>'
export 'BEARER_TOKEN'='<your_bearer_token>'
export 'ACCESS_TOKEN'='<your_access_token>'
export 'ACCESS_SECRET'='<your_access_secret>'
export 'RAPIDAPI_KEY'='<your_rapidAPI_key>'
```


### Phase 2

In addition to the environment variables that were used in phase 1 you will also need the following:
```
conda create -n hashtag_analyzer python==3.8
conda activate hashtag_analyzer
pip install -r requirements.txt
```


#### Two main ways to use the API
```
##### Use the `hta.analyze_tweets` code to analyze each tweet individually
sentiment_df = hta.analyze_tweets()
print(sentiment_df)

##### Use `hta.calculate_total_sentiment` to calculate total sentiment by combining tweets into a single document
total_sentiment = hta.calculate_total_sentiment()
##### https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values
print(total_sentiment)
```

---
