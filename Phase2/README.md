## Phase 2

```
conda create -n phase2 python==3.8
conda activate phase2
pip install -r requirements.txt

# For flake8 & black
pre-commit install
pre-commit run --all

Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Check JSON...........................................(no files to check)Skipped
Check for added large files..............................................Passed
Check Toml...........................................(no files to check)Skipped
Check docstring is first.................................................Passed
Check for case conflicts.................................................Passed
Check for merge conflicts................................................Passed
Debug Statements (Python)................................................Passed
flake8...................................................................Passed
black....................................................................Passed

```

### `analyzer.py`

`analyzer.py` includes two classes, the `APIConnections` and the `HashtagAnalyzer` classes.

#### `APIConnections` class

A user should first instantiate the `APIConnections` class. When called with no arguments, e.g. `APIConnections()`, it attempts to read the required keys from the environment variables. i.e. in `bash` the keys have been exported, e.g. `export 'BEARER_TOKEN'='<your_key_value>'`. Alternatively, the user can provide these as input parameters, e.g.:

```
Python 3.8.0 | packaged by conda-forge | (default, Nov 22 2019, 19:11:19)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from analyzer import APIConnections

# the user can provide the keys as variables
In [2]: APIConnections(
   ...:     twitter_bearer_token='************', # key masked for security
   ...:     google_application_credentials='gcp.json',
   ...:     verbose=False,
   ...:     )
Out[2]: <analyzer.APIConnections at 0x7f8580af59d0>

# or alternatively, let them be obtained from the environment variables
In [3]: APIConnections(verbose=False)
Out[3]: <analyzer.APIConnections at 0x7f85908eac10>
```

On instantiation, the class sets these keys into dictionaries corresponding to twitter, and google. Once these are set, the `utils.utils.check_empty_str_in_dict` function ensures that the values of the key-value pairs are not empty strings or `None`. Further, each dictionary has a corresponding function to check that the API can be hit. E.g. for the Google NLP keys, `check_google_connection` sends a test message of `Hello World!`.

The idea here is that any connection issues to the APIs will be caught in this initial class. To demonstrate this, we can pass an invalid `twitter bearer token` would raise an exception:

```
In [2]: APIConnections(twitter_bearer_token='this_is_an_invalid_key', verbose=False)

Exception: (401, '{\n  "title": "Unauthorized",\n  "type": "about:blank",\n  "status": 401,\n  "detail": "Unauthorized"\n}')
```

#### `HashtagAnalyzer` class

The `HashtagAnalyzer` class is the main class of this work. The user should provide the previously instantiated `APIConnections` as the variable `api_conns`, and the program allows the user to define the `hashtag`, `start_time`, `end_time`, `max_results`, and if retweets should be ignored (`no_retweets`).






#### Running the main code

One can either work with the previous classes or run `analyzer.py` directly (and this will run with `verbose=True`).

This program searches through tweets for up to the past 7 days for a specified number of results about a particular hashtag, and returns sentiment scores for them. For this example I chose #Salem, a date/time range of 2022-10-16T00:00:00Z to 2022-10-22T00:00:00Z, and a maximum of 15 results.

The analyzer uses some of the APIs in phase 1 of the project, most notably the hashtags.py for the ability to search by hashtag, and the movie_nlp for analyzing the sentiment of the tweets.

##### Running in `iPython`

```
Python 3.8.0 | packaged by conda-forge | (default, Nov 22 2019, 19:11:19)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from analyzer import APIConnections, HashtagAnalyzer

In [2]: api_c = APIConnections(verbose=False)

In [3]: hta = HashtagAnalyzer(
   ...:     api_conns=api_c,
   ...:     hashtag="#Salem",
   ...:     start_time="2022-10-16T00:00:00Z",
   ...:     end_time="2022-10-22T00:00:00Z",
   ...:     max_result="15",
   ...:     verbose=False,
   ...:     no_retweets=True,
   ...: )
query parameters: {
    "end_time": "2022-10-22T00:00:00Z",
    "max_results": "15",
    "query": "#Salem",
    "start_time": "2022-10-16T00:00:00Z"
}

In [4]: hta.analyze_tweets()
Out[4]:
  edit_history_tweet_ids                   id                                               text sentiment_score sentiment_magnitude
0  [1581433510912724993]  1581433510912724993  Available Now: Episode 0, Salem - Ballet Des M...             0.3                 1.1
1  [1581433060943286272]  1581433060943286272  I would be in #Salem while the town is trendin...             0.0                 0.0
2  [1581432273827557377]  1581432273827557377  Road bikes to Salem, got art. Road home in the...             0.3                 0.9
3  [1581431667574525954]  1581431667574525954  Anyone need grave yard dirt ? #Salem #salemma ...            -0.1                 0.5
4  [1581429703722008576]  1581429703722008576  I do miss living in #Salem during October.  \n...             0.0                 0.7
5  [1581425544784027648]  1581425544784027648  #NuevaFotoDePerfil #witch #Halloween #bruja #s...             0.0                 0.0

In [5]: hta.calculate_total_sentiment()
Out[5]: (0.0, 2.299999952316284)
```

and you can go back and check what the hashtag was, for example:

```
In [6]: hta.hashtag
Out[6]: '#Salem'
```

#### Running `analyzer.py` directly

the output for the code run through `python analyzer.py` is the following:

```
$ Python Phase2/analyzer.py
The intrepid-flight-365523-a3a81b2e13fe.json exists, and is readable! 

The (masked) API keys: 

{
    "bearer_token": "****************************************************************************************************************"
}
{
    "GOOGLE_APPLICATION_CREDENTIALS": "*********************************************************************"
}


query parameters: {
    "end_time": "2022-10-22T00:00:00Z",
    "max_results": "15",
    "query": "#Salem",
    "start_time": "2022-10-16T00:00:00Z"
}
self.tweets_data: 

 {
    "data": [
        {
            "edit_history_tweet_ids": [
                "1583608170685300736"
            ],
            "id": "1583608170685300736",
            "text": "RT @trsights: Hocus Pocus \ud83c\udf41\ud83c\udf42\ud83c\udf83 #trickortreat #ghoul #halloweennights #fallseason #autumnseason #salem #pumpkinspice #autumnpeople #fallpeopl\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583608120601104385"
            ],
            "id": "1583608120601104385",
            "text": "#Salem https://t.co/Csjd4gKShW"
        },
        {
            "edit_history_tweet_ids": [
                "1583607250324582402"
            ],
            "id": "1583607250324582402",
            "text": "Allied Universal is committed more than ever to safety. If you have a passion for being there for 
others, we want to hire you in #Salem, OR. Apply now! https://t.co/LXuYHMEZsr #Safety"
        },
        {
            "edit_history_tweet_ids": [
                "1583605516441649152"
            ],
            "id": "1583605516441649152",
            "text": "RT @Cosmic_Trance: Finally got around to finishing up Salem! I really dig this model. That dress is super cool! Let me know what ya'll thin\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583605051091996673"
            ],
            "id": "1583605051091996673",
            "text": "RT @Cosmic_Trance: Finally got around to finishing up Salem! I really dig this model. That dress is super cool! Let me know what ya'll thin\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583605029633552384"
            ],
            "id": "1583605029633552384",
            "text": "RT @Cosmic_Trance: Finally got around to finishing up Salem! I really dig this model. That dress is super cool! Let me know what ya'll thin\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583605005151481857"
            ],
            "id": "1583605005151481857",
            "text": "Finally got around to finishing up Salem! I really dig this model. That dress is super cool! Let me know what ya'll think!\n\n#RWBY #Salem #NSFW #Blender3d https://t.co/iGTAyOl5OF"
        },
        {
            "edit_history_tweet_ids": [
                "1583602581594439681"
            ],
            "id": "1583602581594439681",
            "text": "This job might be a great fit for you: Driver Helper - https://t.co/7Yq7SbjuLt #Transportation #Salem, OR"
        },
        {
            "edit_history_tweet_ids": [
                "1583596744272621569"
            ],
            "id": "1583596744272621569",
            "text": "we out \n#Salem https://t.co/G8JhEM33RF"
        },
        {
            "edit_history_tweet_ids": [
                "1583595271044313089"
            ],
            "id": "1583595271044313089",
            "text": "Nervous to apply for a job like \"Island Sales Representative\" at Rocket? Apply even if you're not a 100% match. You might be underestimating your value. Click the link in our bio for more info. #Sales #Salem, OR"   
        },
        {
            "edit_history_tweet_ids": [
                "1583594102733803520"
            ],
            "id": "1583594102733803520",
            "text": "#Salem is still spooky in the daytime! Our 60 minute mid-day #ghosttour runs daily at 2:30pm.  https://t.co/JDbep3KvbW"
        },
        {
            "edit_history_tweet_ids": [
                "1583594063827468288"
            ],
            "id": "1583594063827468288",
            "text": "RT @DLGenealogist: If you missed my lecture today on \"Verifying Descent from Salem's Accused Witches\" you can view it online for #FREE and\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583592366673272832"
            ],
            "id": "1583592366673272832",
            "text": "RT @NyxxZeiss: Salem joined the group!\n#RWBY #Salem #CinderFall #Koikatsu #KoikatuParty\nwould you like to help me? https://t.co/xWzgnbOcSW\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583590175648940033"
            ],
            "id": "1583590175648940033",
            "text": "Massachusetts, too many pics to choose from, you were a dream. #boston #capecod #salem #plymoth @ 
Massachusetts https://t.co/W6phU8nygA"
        },
        {
            "edit_history_tweet_ids": [
                "1583584646532861952"
            ],
            "id": "1583584646532861952",
            "text": "RT @cottage_green: Massachusetts Historic House Plaque Circa Date Signs by https://t.co/qOU0YmaF2O #CapeAnn #Salem #Boston #CircaPlaque #Gl\u2026"
        }
    ],
    "meta": {
        "newest_id": "1583608170685300736",
        "next_token": "b26v89c19zqg8o3fpzekpi20jzh32h6tudqp8004doiv1",
        "oldest_id": "1583584646532861952",
        "result_count": 15
    }
} 
 -------


self.tweets_df:

   edit_history_tweet_ids                   id                                               text
0  [1583608120601104385]  1583608120601104385                     #Salem https://t.co/Csjd4gKShW
1  [1583607250324582402]  1583607250324582402  Allied Universal is committed more than ever t...
2  [1583605005151481857]  1583605005151481857  Finally got around to finishing up Salem! I re...
3  [1583602581594439681]  1583602581594439681  This job might be a great fit for you: Driver ...
4  [1583596744272621569]  1583596744272621569            we out \n#Salem https://t.co/G8JhEM33RF
5  [1583595271044313089]  1583595271044313089  Nervous to apply for a job like "Island Sales ...
6  [1583594102733803520]  1583594102733803520  #Salem is still spooky in the daytime! Our 60 ...
7  [1583590175648940033]  1583590175648940033  Massachusetts, too many pics to choose from, y...
 -------



                Sentiment for the text 0:
                0.20000000298023224, 0.20000000298023224


                Sentiment for the text 1:
                0.5, 2.200000047683716


                Sentiment for the text 2:
                0.6000000238418579, 3.0999999046325684


                Sentiment for the text 3:
                0.4000000059604645, 0.4000000059604645


                Sentiment for the text 4:
                -0.10000000149011612, 0.10000000149011612


                Sentiment for the text 5:
                0.0, 1.2000000476837158


                Sentiment for the text 6:
                0.10000000149011612, 0.5


                Sentiment for the text 7:
                0.4000000059604645, 0.8999999761581421

  edit_history_tweet_ids                   id  ... sentiment_score sentiment_magnitude
0  [1583608120601104385]  1583608120601104385  ...             0.2                 0.2
1  [1583607250324582402]  1583607250324582402  ...             0.5                 2.2
2  [1583605005151481857]  1583605005151481857  ...             0.6                 3.1
3  [1583602581594439681]  1583602581594439681  ...             0.4                 0.4
4  [1583596744272621569]  1583596744272621569  ...            -0.1                 0.1
5  [1583595271044313089]  1583595271044313089  ...             0.0                 1.2
6  [1583594102733803520]  1583594102733803520  ...             0.1                 0.5
7  [1583590175648940033]  1583590175648940033  ...             0.4                 0.9

[8 rows x 5 columns]


 all the tweets as a single document:


 #Salem https://t.co/Csjd4gKShW.Allied Universal is committed more than ever to safety. If you have a passion for being there for others, we want to hire you in #Salem, OR. Apply now! https://t.co/LXuYHMEZsr #Safety.Finally got around to 
finishing up Salem! I really dig this model. That dress is super cool! Let me know what ya'll think!

#RWBY #Salem #NSFW #Blender3d https://t.co/iGTAyOl5OF.This job might be a great fit for you: Driver Helper - https://t.co/7Yq7SbjuLt #Transportation #Salem, OR.we out
#Salem https://t.co/G8JhEM33RF.Nervous to apply for a job like "Island Sales Representative" at Rocket? Apply even if you're not a 100% match. You might be underestimating your value. Click the link in our bio for more info. #Sales #Salem, OR.#Salem is still spooky in the daytime! Our 60 minute mid-day #ghosttour runs daily at 2:30pm.  https://t.co/JDbep3KvbW.Massachusetts, too many pics to choose from, you were a dream. #boston #capecod #salem #plymoth @ Massachusetts https://t.co/W6phU8nygA.




                Sentiment for the text 0:
                0.4000000059604645, 7.099999904632568

(0.4000000059604645, 7.099999904632568)

```

#### User Story MVP

This code meets the MVP because a user is able to search for hashtags of a city's name (in this case Salem), see a number of recent tweets about Salem, and get two different estimates of how people felt about the city. This project also provides a partial solution to the other user stories; a business owner could search for tweets that have his business name as a hashtag, or an influencer can search for tweets with her handle as a hashtag, or a researcher can collect the sentiment of a number of people on topics tagged with a specific hashtag.
