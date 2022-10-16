### `analyzer_nlp.py`

This program searches through tweets for up to the past 7 days for a specified number of results about a particular hashtag, and returns sentiment scores for them. For this example I chose #Salem, a date/time range of 2022-10-10T00:00:00Z to 2022-10-16T00:00:00Z, and a maximum of 10 results. When the program is run it firsts checks to see if the file exists and is readable, and alerts the user if it is or not. In this case it was, so it says "The file exists, and is readable!" before running through the program.

The analyzer uses some of the APIs in phase 1 of the project, most notably the hashtags.py for the ability to search by hashtag, and the movie_nlp for analyzing the sentiment of the tweets.

```
The file exists, and is readable! 

query parameters: {
    "end_time": "2022-10-16T00:00:00Z", 
    "max_results": "10",
    "query": "#Salem",
    "start_time": "2022-10-10T00:00:00Z"
}
self.tweets_data: 

 {
    "data": [
        {
            "edit_history_tweet_ids": [
                "1581434627595505664"  
            ],
            "id": "1581434627595505664",
            "text": "RT @ThouPodcast: Available Now: Episode 0, Salem - Ballet Des Moines, an interview with artistic director Tom Mattingly and creative direct\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1581433510912724993"
            ],
            "id": "1581433510912724993",
            "text": "Available Now: Episode 0, Salem - Ballet Des Moines, an interview with artistic director Tom Mattingly and creative director Jami Milne.\nListen at https://t.co/UAsGHJtzoX  or with your favorite podcast app.\n#salem #desmoines #salemwitchtrials #ballet https://t.co/ksckdL35Rk"
        },
        {
            "edit_history_tweet_ids": [
                "1581433060943286272"
            ],
            "id": "1581433060943286272",
            "text": "I would be in #Salem while the town is trending on Twitter right now \ud83d\ude02\ud83e\udee0"
        },
        {
            "edit_history_tweet_ids": [
                "1581432273827557377"
            ],
            "id": "1581432273827557377",
            "text": "Road bikes to Salem, got art. Road home in the dark!\n#Salem #hauntedhappenings #halloween #happyhalloween #art https://t.co/qd6SEeDMlt"
        },
        {
            "edit_history_tweet_ids": [
                "1581431914245738496"
            ],
            "id": "1581431914245738496",
            "text": "RT @baelfleur: F\u0338i\u0335n\u0337i\u0336s\u0334h\u0336 \u0336t\u0337h\u0334e\u0335m\u0336 \u0338o\u0334r\u0335 \u0336y\u0338o\u0336u\u0334'\u0334r\u0335e\u0338 \u0334n\u0338e\u0334x\u0334t\u0337\n\n#RWBY  #RWBYfanart #Salem #RWBYSalem https://t.co/OW2dJDMDlc"
        },
        {
            "edit_history_tweet_ids": [
                "1581431667574525954"
            ],
            "id": "1581431667574525954",
            "text": "Anyone need grave yard dirt ? #Salem #salemma #cemetary #graveyard #spells #spellwork #witch #malewitch https://t.co/Xfj5UA5O8Y"
        },
        {
            "edit_history_tweet_ids": [
                "1581429703722008576"
            ],
            "id": "1581429703722008576",
            "text": "I do miss living in #Salem during October.  \n\nAll the tourist. All the people watching."        },
        {
            "edit_history_tweet_ids": [
                "1581427125147832320"
            ],
            "id": "1581427125147832320",
            "text": "RT @vile_individual: day 10- age gap! #kinktober #kinktober2022 #agegap #shota #underage #priest #OC #salem https://t.co/dBrojqWqut"
        },
        {
            "edit_history_tweet_ids": [
                "1581425544784027648"
            ],
            "id": "1581425544784027648",
            "text": "#NuevaFotoDePerfil #witch #Halloween #bruja #salem #trans #ilovehalloween https://t.co/af1VEAJNXA"
        },
        {
            "edit_history_tweet_ids": [
                "1581425292765036545"
            ],
            "id": "1581425292765036545",
            "text": "RT @baelfleur: F\u0338i\u0335n\u0337i\u0336s\u0334h\u0336 \u0336t\u0337h\u0334e\u0335m\u0336 \u0338o\u0334r\u0335 \u0336y\u0338o\u0336u\u0334'\u0334r\u0335e\u0338 \u0334n\u0338e\u0334x\u0334t\u0337\n\n#RWBY  #RWBYfanart #Salem #RWBYSalem https://t.co/OW2dJDMDlc"
        }
    ],
    "meta": {
        "newest_id": "1581434627595505664",
        "next_token": "b26v89c19zqg8o3fpzejv4nlvh1eofohfcfihzfrz8q65",
        "oldest_id": "1581425292765036545",
        "result_count": 10
    }
}
 -------


self.tweets_df:

   edit_history_tweet_ids                   id                                               text
0  [1581433510912724993]  1581433510912724993  Available Now: Episode 0, Salem - Ballet Des M...
1  [1581433060943286272]  1581433060943286272  I would be in #Salem while the town is trendin...
2  [1581432273827557377]  1581432273827557377  Road bikes to Salem, got art. Road home in the...
3  [1581431667574525954]  1581431667574525954  Anyone need grave yard dirt ? #Salem #salemma ...
4  [1581429703722008576]  1581429703722008576  I do miss living in #Salem during October.  \n...
5  [1581425544784027648]  1581425544784027648  #NuevaFotoDePerfil #witch #Halloween #bruja #s...
 -------


Sentiment for the text 0: 0.30000001192092896, 1.100000023841858
Sentiment for the text 1: 0.0, 0.0
Sentiment for the text 2: 0.30000001192092896, 0.8999999761581421
Sentiment for the text 3: -0.10000000149011612, 0.5
Sentiment for the text 4: 0.0, 0.699999988079071
Sentiment for the text 5: 0.0, 0.0
------- 


  edit_history_tweet_ids                   id  ... sentiment_score sentiment_magnitude
0  [1581433510912724993]  1581433510912724993  ...             0.3                 1.1
1  [1581433060943286272]  1581433060943286272  ...             0.0                 0.0
2  [1581432273827557377]  1581432273827557377  ...             0.3                 0.9
3  [1581431667574525954]  1581431667574525954  ...            -0.1                 0.5
4  [1581429703722008576]  1581429703722008576  ...             0.0                 0.7
5  [1581425544784027648]  1581425544784027648  ...             0.0                 0.0

[6 rows x 5 columns]
all the tweets as a single document:

 Available Now: Episode 0, Salem - Ballet Des Moines, an interview with artistic director Tom Mattingly and creative director Jami Milne.
Listen at https://t.co/UAsGHJtzoX  or with your favorite podcast app.
#salem #desmoines #salemwitchtrials #ballet https://t.co/ksckdL35Rk.I would be in #Salem while the town is trending on Twitter right now 😂🫠.Road bikes to Salem, got art. Road home in the dark!
#Salem #hauntedhappenings #halloween #happyhalloween #art https://t.co/qd6SEeDMlt.Anyone need grave yard dirt ? #Salem #salemma #cemetary #graveyard #spells #spellwork #witch #malewitch https://t.co/Xfj5UA5O8Y.I do miss living in #Salem during October.

All the tourist. All the people watching..#NuevaFotoDePerfil #witch #Halloween #bruja #salem #trans #ilovehalloween https://t.co/af1VEAJNXA.


Sentiment for the text : 0.0, 2.299999952316284
magnitude: 2.3

```


---
