### `username.py`

This program takes a username, then uses that to pull the twitter user's description, id, and name. It then puts this information in a json format along with the username. For testing purposes I was looking at the twitter user @keaneofficial
```
$ python Phase1a/username.py
the request url is https://api.twitter.com/2/users/by?usernames=keaneofficial&user.fields=description
the response status code is: 200
{
    "data": [
        {
            "description": "Strangeland and The Best Of Keane vinyl available to pre-order now.",
            "id": "18863720",
            "name": "Keane",
            "username": "keaneofficial"
        }
    ]
}
```


---

### `hashtags.py`

This program takes a username, the date/time range being searched for(only in the past 7 days), and the number of results that will be returned (for this example I chose to go with 15 tweets, used the hashtag #halloween, and chose a time range of 2022-10-10T00:00:00Z and 2022-10-14T00:00:00Z). It then uses that to pull a text of the tweet, the tweet's id number, and the the tweet-edit  history id (for the number of tweets specified in the paramenters) and puts it in a json format.
```

$ python Phase1a/hashtags.py
{
    "data": [
        {
            "edit_history_tweet_ids": [
                "1580709960987525120"
            ],
            "id": "1580709960987525120",
            "text": "RT @aLilBitSamantha: Come, we fly! \ud83c\udf83 Get into some witchy business with this Halloween teacher lanyard! 
https://t.co/APlK054xaQ  @Etsy #hal\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1580709959394033664"
            ],
            "id": "1580709959394033664",
            "text": "\"JUST SNACKIN' \" Men's Comfort Colors\u00ae T-Shirt\n\nhttps://t.co/Uw0SGTINc3\n\nhttps://t.co/dT3PswvVBF\n\n#halloween \ud83c\udf83\ud83e\udd87\ud83e\udddb\ud83c\udffb\u200d\u2642\ufe0f\u26b0\ufe0f\ud83c\udf1d https://t.co/H227YLwlxQ"
        },
        {
            "edit_history_tweet_ids": [
                "1580709958902898688"
            ],
            "id": "1580709958902898688",
            "text": "Vintage Alarm Clock EREVAN Factory Cream color Metal Clock USSR Made in the 50s, Home Decor, Art Deco Style Soviet 
Era https://t.co/MkYwfYhaSF #Halloween #Retro #Antiques #Backtoschool #Gifts #Vintage ##QueenElizabethII #Typewriter #AlarmClockVintage 
https://t.co/I26pUam5qt"
        },
        {
            "edit_history_tweet_ids": [
                "1580709957271715840"
            ],
            "id": "1580709957271715840",
            "text": "RT @Ramona_cool: #ThrowbackThursday #megamanx and #residentevil cross over. https://t.co/JMW4CT6N1F\n#videogame #gaming #rockman #Biohazard\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1580709956961337344"
            ],
            "id": "1580709956961337344",
            "text": "#Halloween https://t.co/mqHUIhx8XA"
        },
        {
            "edit_history_tweet_ids": [
                "1580709956696752128"
            ],
            "id": "1580709956696752128",
            "text": "RT @violett177: Rt For An Endless Summer \ud83d\udc59\ud83d\udc7b\n#Ghostface #ScaryMovie #Halloween #October \nLink In My Bio \ud83d\udda4 https://t.co/CXqRbGsGls"
        },
        {
            "edit_history_tweet_ids": [
                "1580709949243785216"
            ],
            "id": "1580709949243785216",
            "text": "RT @smolsheey: halloween ych commission for @MingraoMusic \ni still have slots for this ych! for R$30/$30! \n\n#vtuber #halloween #ychcommissi\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1580709933158629376"
            ],
            "id": "1580709933158629376",
            "text": "\ud83c\udf15 - Resident Evil 2 Remake - PS5 - Episode 9 - \ud83c\udf15 - https://t.co/ErGJphgLQH #ResidentEvil2Remake #PS5 #ResidentEvil #Remake #Halloween #Horror #Capcom #Playstation #Sony #RavenMoonX #Gaming"
        },
        {
            "edit_history_tweet_ids": [
                "1580709927714443264"
            ],
            "id": "1580709927714443264",
            "text": "Going to watch Halloween Horror Spooky and scary movies now.\n#Halloween #HalloweenMovies #HalloweenMovie #HorrorMovies #OctoberMovies #HorrorMovie #OctoberMovie"
        },
        {
            "edit_history_tweet_ids": [
                "1580709920130752512"
            ],
            "id": "1580709920130752512",
            "text": "RT @lindsayromantic: The Snow Bride (The Knight &amp; the Witch Book 1) by Lindsay Townsend \ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8https://t.co/FCXbzayXn4 via \n@amazon\n #Romanc\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1580709919665233920"
            ],
            "id": "1580709919665233920",
            "text": "RT @lindsayromantic: The Snow Bride (The Knight &amp; the Witch Book 1) by Lindsay Townsend \ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8https://t.co/FCXbzayXn4 via \n@amazon\n #Romanc\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1580709919636221952"
            ],
            "id": "1580709919636221952",
            "text": "RT @lindsayromantic: The Snow Bride (The Knight &amp; the Witch Book 1) by Lindsay Townsend \ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8https://t.co/FCXbzayXn4 via \n@amazon\n #Romanc\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1580709919438667776"
            ],
            "id": "1580709919438667776",
            "text": "RT @lindsayromantic: The Snow Bride (The Knight &amp; the Witch Book 1) by Lindsay Townsend \ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8\ud83c\uddfa\ud83c\uddf8https://t.co/FCXbzayXn4 via \n@amazon\n #Romanc\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1580709917702254593"
            ],
            "id": "1580709917702254593",
            "text": "RT @kinky_horror: ***9** Days Till #TheLastDriveIn #Halloween Special! \ud83c\udf83 https://t.co/YRm3s56hI9"       
        },
        {
            "edit_history_tweet_ids": [
                "1580709913751588864"
            ],
            "id": "1580709913751588864",
            "text": "RT @mochio_bonio: \"Rude Interruption\"\n\n(( I like to imagine this happened when Lizlily used her NP for the first time ))\n\n#FGO\n#ElizabethBa\u2026"
        }
    ],
    "meta": {
        "newest_id": "1580709960987525120",
        "next_token": "b26v89c19zqg8o3fpzejg5f8zo5ef5pjfhp1q4go7g1vh",
        "oldest_id": "1580709913751588864",
        "result_count": 15
    }
}
```


---


### `by_date.py`

This program takes a user's name, and returns the 10 most recent tweets in order from newest to oldest from the account from the past 7 days (For this example I look at tweets by @NASA or with the hashtag #NASA). The information pulled is the author id, the tweet id, tweet-edit history id, the text of the tweet, and the tweet's id number, and puts it in a json format.
```
$ python Phase1a/by_date.py
200
{
    "data": [
        {
            "author_id": "16786966",
            "edit_history_tweet_ids": [
                "1580942387849105408"
            ],
            "id": "1580942387849105408",
            "text": "#NASA #SPACEX #CREW4 - It sounds like undocking operations were stopped for a bit due to an erroneous indication of a fire in the Russian Segment of the ISS. Houston has confirmed the erroneous fire signal and undocking preps continue for a 12:05 EDT 
undock. https://t.co/vSN9zirBEW"
        },
        {
            "author_id": "4249824673",
            "edit_history_tweet_ids": [
                "1580942273952780288"
            ],
            "id": "1580942273952780288",
            "text": "\ud83d\ude80Straight outta @NASA: https://t.co/DEQz3yLU3B #space #cosmos #universe #science #astronomy #climate #NASA"
        },
        {
            "author_id": "121953044",
            "edit_history_tweet_ids": [
                "1580942194080301058"
            ],
            "id": "1580942194080301058",
            "text": "RT @HiRISE: HiPOD: Ripple Changes in Cerberus Fossae\n\nOur science goal with this observation is to test suggestions of very recent volcanis\u2026"
        },
        {
            "author_id": "1271079272204115970",
            "edit_history_tweet_ids": [
                "1580942010940211200"
            ],
            "id": "1580942010940211200",
            "text": "Enquanto as marcas buscam uma solu\u00e7\u00e3o para carregamento r\u00e1pido, a Nasa j\u00e1 t\u00e1 com o neg\u00f3cio pronto... #nasa #ev #auto #carros #carro #carregamento #bateria https://t.co/TRtnCgvrlE"
        },
        {
            "author_id": "1348345613025386496",
            "edit_history_tweet_ids": [
                "1580941812961005569"
            ],
            "id": "1580941812961005569",
            "text": "RT @pufferjworld: #alphaindustries #removebeforeflight #nasa #bomberjacket #pufferjacket #downjacket #puffercoat #downcoat #pufferfetish #d\u2026"
        },
        {
            "author_id": "1383016856810848257",
            "edit_history_tweet_ids": [
                "1580941509641138177"
            ],
            "id": "1580941509641138177",
            "text": "#Perseverance on #Mars\n\nSol: 557\n#Earth date: 2022-09-13;\n#Camera: Navigation Camera - Right\n\n#PerseveranceRover #NASAPhotos #NASA #NASAAPI #MarsPhoto #MarsPhotos #MarsMission #NASAIngenuity #Space #PerseverancePhotoBot #TwitterBot #Bot https://t.co/kThL0iKXAO"
        },
        {
            "author_id": "860601814659592192",
            "edit_history_tweet_ids": [
                "1580941498148855812"
            ],
            "id": "1580941498148855812",
            "text": "Deception Point - Dan Brown https://t.co/5G0JYqkaYr via @Etsy\n\n#OnSale - 10% Off and #FreeShipping thru 10/16\n\n#etsysale #etsycoupon #booksale #DanBrown #DeceptionPoint #mystery #NASA #arctic #aliens #bookstoread #BookWorm"
        },
        {
            "author_id": "978460662",
            "edit_history_tweet_ids": [
                "1580941424954331141"
            ],
            "id": "1580941424954331141",
            "text": "\u30b9\u30da\u30fc\u30b9X\u306e\u30af\u30eb\u30fc\u30c9\u30e9\u30b4\u30f3\u300cCrew-4\u300d\u30df\u30c3\u30b7\u30e7\u30f3\u3001\u56fd\u969b\u5b87\u5b99\u30b9\u30c6\u30fc\u30b7\u30e7\u30f3\u304b\u3089\u96e2\u8131\u3059\u308b\u751f\u4e2d\u7d99\u304c\u59cb\u307e\u3063\u305f\u3002#NASA #SpaceX #CrewDragon #Crew4\n\nhttps://t.co/fWPHutr9pg"
        },
        {
            "author_id": "4900961993",
            "edit_history_tweet_ids": [
                "1580941381903994880"
            ],
            "id": "1580941381903994880",
            "text": "'The Falcon and the Hunter's Moon' \n\nimage from the #NASA_App\n\n\ud83d\udd17https://t.co/2WgoMkPGR6\n\n#NASA #Moon #Falcon9 #spaceX #space #exploration https://t.co/stp02TPNVt"
        },
        {
            "author_id": "2330781440",
            "edit_history_tweet_ids": [
                "1580941378908934144"
            ],
            "id": "1580941378908934144",
            "text": "https://t.co/YBKq1ycat8 #NASA #Space #SpaceFlight"
        }
    ],
    "meta": {
        "newest_id": "1580942387849105408",
        "next_token": "b26v89c19zqg8o3fpzejg9pw3vbd188qizq9gqs7i07lp",
        "oldest_id": "1580941378908934144",
        "result_count": 10
    }
}
```


---
As discussed in in the quickstart overview of Botometer (https://github.com/IUNetSci/botometer-python#botometer-v4),

> **Meanings of the elements in the response:**
> * **user**: Twitter user object (from the user) plus the language inferred from majority of tweets
> * **raw scores**: bot score in the [0,1] range, both using English (all features) and Universal (language-independent) features; in each case we have the overall score and the sub-scores for each bot class (see below for subclass names and definitions)
> * **display scores**: same as raw scores, but in the [0,5] range
> * **cap**: conditional probability that accounts with a score **equal to or greater than this** are automated; based on inferred language
> 
> **Meanings of the bot type scores:**
> * `fake_follower`: bots purchased to increase follower counts 
> * `self_declared`: bots from botwiki.org
> * `astroturf`: manually labeled political bots and accounts involved in follow trains that systematically delete content
> * `spammer`: accounts labeled as spambots from several datasets
> * `financial`: bots that post using cashtags
> * `other`: miscellaneous other bots obtained from manual annotation, user feedback, etc.

### `bot_by_id.py`

This program takes the id number of a twitter account, and calls the botometer to determine if the account is a bot or not by analyzing the twitter activity of the account (for this example I used the id 18863720 that corresponds to @keaneofficial). This information is then put into a json format. The results show that it is unlikely that this account is a bot.
```
$ python Phase1a/bot_by_id.py
{
    "cap": {
        "english": 0.7287106185584935,
        "universal": 0.799570188835745
    },
    "display_scores": {
        "english": {
            "astroturf": 0.2,
            "fake_follower": 0.3,
            "financial": 0.0,
            "other": 1.4,
            "overall": 1.2,
            "self_declared": 0.2,
            "spammer": 0.0
        },
        "universal": {
            "astroturf": 0.2,
            "fake_follower": 0.2,
            "financial": 0.0,
            "other": 1.2,
            "overall": 1.8,
            "self_declared": 0.0,
            "spammer": 0.0
        }
    },
    "raw_scores": {
        "english": {
            "astroturf": 0.04,
            "fake_follower": 0.06,
            "financial": 0.0,
            "other": 0.27,
            "overall": 0.23,
            "self_declared": 0.03,
            "spammer": 0.01
        },
        "universal": {
            "astroturf": 0.03,
            "fake_follower": 0.03,
            "financial": 0.01,
            "other": 0.25,
            "overall": 0.36,
            "self_declared": 0.0,
            "spammer": 0.0
        }
    },
    "user": {
        "majority_lang": "en",
        "user_data": {
            "id_str": "18863720",
            "screen_name": "keaneofficial"
        }
    }
}
```


---


### `bot_or_not.py`

This program takes the username of a twitter account, and calls the botometer to determine if the account is a bot or not by analyzing the twitter activity of the account (for this example I look at the @lordiofficial account). This information is then put into a json format. The results show that it is unlikely that this account is a bot.
```
$ python Phase1a/bot_or_not.py
{
    "cap": {
        "english": 0.7826357858330618, 
        "universal": 0.8052176344738626
    },
    "display_scores": {
        "english": {
            "astroturf": 0.3,
            "fake_follower": 0.6,
            "financial": 0.0,
            "other": 3.2,
            "overall": 1.6,
            "self_declared": 2.6,
            "spammer": 0.1
        },
        "universal": {
            "astroturf": 0.2,
            "fake_follower": 0.7,
            "financial": 0.0,
            "other": 3.0,
            "overall": 3.2,
            "self_declared": 3.2,
            "spammer": 0.4
        }
    },
    "raw_scores": {
        "english": {
            "astroturf": 0.06,
            "fake_follower": 0.13,
            "financial": 0.0,
            "other": 0.64,
            "overall": 0.32,
            "self_declared": 0.51,
            "spammer": 0.02
        },
        "universal": {
            "astroturf": 0.03,
            "fake_follower": 0.14,
            "financial": 0.01,
            "other": 0.6,
            "overall": 0.63,
            "self_declared": 0.63,
            "spammer": 0.08
        }
    },
    "user": {
        "majority_lang": "en",
        "user_data": {
            "id_str": "115497725",
            "screen_name": "LORDIOFFICIAL"
        }
    }
}
```


---
### `bots_or_nots.py`

This program takes the usernames of multiple twitter accounts, and calls the botometer to determine if the accounts are bots or not by analyzing their twitter activity. This information is then put into a json format. For this example I looked at the  following accounts: "@NASAHubble", "@BU_Tweets", "@MBTA", "@ENGEC601". As @ENGEC601` has no tweets, the API returns a `NoTimelineError' (see below).
```
$ python Phase1a/bots_or_nots.py                                                                               
@NASAHubble {
    "cap": {
        "english": 0.7971037475964349, 
        "universal": 0.8053787930995948
    },
    "display_scores": {
        "english": {
            "astroturf": 0.5,
            "fake_follower": 0.5,      
            "financial": 0.0,
            "other": 2.0,
            "overall": 2.7,
            "self_declared": 0.2,
            "spammer": 0.0
        },
        "universal": {
            "astroturf": 0.6,
            "fake_follower": 0.6,
            "financial": 0.0,
            "other": 1.9,
            "overall": 2.5,
            "self_declared": 0.1,
            "spammer": 0.0
        }
    },
    "raw_scores": {
        "english": {
            "astroturf": 0.1,
            "fake_follower": 0.1,
            "financial": 0.0,
            "other": 0.4,
            "overall": 0.54,
            "self_declared": 0.05,
            "spammer": 0.0
        },
        "universal": {
            "astroturf": 0.13,
            "fake_follower": 0.12,
            "financial": 0.0,
            "other": 0.38,
            "overall": 0.5,
            "self_declared": 0.02,
            "spammer": 0.0
        }
    },
    "user": {
        "majority_lang": "en",
        "user_data": {
            "id_str": "14091091",
            "screen_name": "NASAHubble"
        }
    }
}
@BU_Tweets {
    "cap": {
        "english": 0.779581525363529,
        "universal": 0.7966241294741505
    },
    "display_scores": {
        "english": {
            "astroturf": 1.0,
            "fake_follower": 1.6,
            "financial": 0.0,
            "other": 2.0,
            "overall": 1.6,
            "self_declared": 0.2,
            "spammer": 0.0
        },
        "universal": {
            "astroturf": 1.2,
            "fake_follower": 1.1,
            "financial": 0.0,
            "other": 1.6,
            "overall": 1.7,
            "self_declared": 0.1,
            "spammer": 0.0
        }
    },
    "raw_scores": {
        "english": {
            "astroturf": 0.21,
            "fake_follower": 0.32,
            "financial": 0.0,
            "other": 0.4,
            "overall": 0.31,
            "self_declared": 0.03,
            "spammer": 0.0
        },
        "universal": {
            "astroturf": 0.24,
            "fake_follower": 0.22,
            "financial": 0.0,
            "other": 0.31,
            "overall": 0.34,
            "self_declared": 0.02,
            "spammer": 0.0
        }
    },
    "user": {
        "majority_lang": "en",
        "user_data": {
            "id_str": "104561488",
            "screen_name": "BU_Tweets"
        }
    }
}
@MBTA {
    "cap": {
        "english": 0.797782173166965,
        "universal": 0.8060512678410475
    },
    "display_scores": {
        "english": {
            "astroturf": 0.6,
            "fake_follower": 0.6,
            "financial": 0.0,
            "other": 3.5,
            "overall": 3.5,
            "self_declared": 1.8,
            "spammer": 0.2
        },
        "universal": {
            "astroturf": 0.7,
            "fake_follower": 0.1,
            "financial": 0.0,
            "other": 3.4,
            "overall": 3.4,
            "self_declared": 1.2,
            "spammer": 0.0
        }
    },
    "raw_scores": {
        "english": {
            "astroturf": 0.13,
            "fake_follower": 0.11,
            "financial": 0.01,
            "other": 0.7,
            "overall": 0.7,
            "self_declared": 0.35,
            "spammer": 0.04
        },
        "universal": {
            "astroturf": 0.14,
            "fake_follower": 0.02,
            "financial": 0.0,
            "other": 0.69,
            "overall": 0.69,
            "self_declared": 0.25,
            "spammer": 0.01
        }
    },
    "user": {
        "majority_lang": "en",
        "user_data": {
            "id_str": "150334831",
            "screen_name": "MBTA"
        }
    }
}
@ENGEC601 {
    "error": "NoTimelineError: "
}
```


---
