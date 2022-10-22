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
    "max_results": "10",
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
            "text": "Allied Universal is committed more than ever to safety. If you have a passion for being there for others, we want to hire you in #Salem, OR. Apply now! https://t.co/LXuYHMEZsr #Safety"
        },
        {
            "edit_history_tweet_ids": [
                "1583605516441649152"
            ],
            "id": "1583605516441649152",
            "text": "RT @Cosmic_Trance: Finally got around to finishing up Salem! I really dig this model. That dress 
is super cool! Let me know what ya'll thin\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583605051091996673"
            ],
            "id": "1583605051091996673",
            "text": "RT @Cosmic_Trance: Finally got around to finishing up Salem! I really dig this model. That dress 
is super cool! Let me know what ya'll thin\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583605029633552384"
            ],
            "id": "1583605029633552384",
            "text": "RT @Cosmic_Trance: Finally got around to finishing up Salem! I really dig this model. That dress 
is super cool! Let me know what ya'll thin\u2026"
        },
        {
            "edit_history_tweet_ids": [
                "1583605005151481857"
            ],
            "id": "1583605005151481857",
            "text": "Finally got around to finishing up Salem! I really dig this model. That dress is super cool! Let 
me know what ya'll think!\n\n#RWBY #Salem #NSFW #Blender3d https://t.co/iGTAyOl5OF"
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
        }
    ],
    "meta": {
        "newest_id": "1583608170685300736",
        "next_token": "b26v89c19zqg8o3fpzekpi2bdwmcth59dmevo5rm63ed9",
        "oldest_id": "1583595271044313089",
        "result_count": 10
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

  edit_history_tweet_ids                   id  ... sentiment_score sentiment_magnitude
0  [1583608120601104385]  1583608120601104385  ...             0.2                 0.2
1  [1583607250324582402]  1583607250324582402  ...             0.5                 2.2
2  [1583605005151481857]  1583605005151481857  ...             0.6                 3.1
3  [1583602581594439681]  1583602581594439681  ...             0.4                 0.4
4  [1583596744272621569]  1583596744272621569  ...            -0.1                 0.1
5  [1583595271044313089]  1583595271044313089  ...             0.0                 1.2

[6 rows x 5 columns]


 all the tweets as a single document:


 #Salem https://t.co/Csjd4gKShW.Allied Universal is committed more than ever to safety. If you have a passion for being there for others, we want to hire you in #Salem, OR. Apply now! https://t.co/LXuYHMEZsr #Safety.Finally got around think!

#RWBY #Salem #NSFW #Blender3d https://t.co/iGTAyOl5OF.This job might be a great fit for you: Driver Helper - https://t.co/7Yq7SbjuLt #Transportation #Salem, OR.we out
#Salem https://t.co/G8JhEM33RF.Nervous to apply for a job like "Island Sales Representative" at Rocket? Apply even if 
you're not a 100% match. You might be underestimating your value. Click the link in our bio for more info. #Sales #Salem, OR.




                Sentiment for the text 0:
                0.4000000059604645, 5.900000095367432

(0.4000000059604645, 5.900000095367432)
