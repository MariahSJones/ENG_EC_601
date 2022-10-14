import requests
import json
import os

# this imports the Google Cloud client library
from google.cloud import language_v1

# this instantiates a client
client = language_v1.LanguageServiceClient()

# this contains the text from a movie review from the nightmare before christmas
review = "I really don’t understand all the low reviews this movie I think went way over most people’s head. It is not some redo of the first movie like many say it just feels similar because it has all the same strengths and many new ones. It has that perfect blend of action tension and the mix of sci fi horror with the action genera that made the original so stand out against every other 80s action movie. This film follows humans placed on the predator home planet and it’s clear from the start they are predators themselves from criminals to worthy warriors to fight the predator species they were all put on the planet as a test to see if these humans could use each of their strengths and weaknesses the right ways to overcome traps and a alien threat. Overtime many plot twists and secrets are revealed and the plot becomes much more than a basic predator film and it focuses much more on horror than the previous films more than the action. Also the predator civil war along with new sub species to learn about was so awesome. Also this film has so much intense violence and gore like the original it just happens with better pacing it doesn’t go from an action movie to a sci fi movie or vice versa it instead has a perfect blend of everything the predator series is amazing for and it doesn’t waste your time with one liners and corny stuff that every other predator movie seems to need so badly. I will get hate for this but predators is my favorite in the series BY FAR the only thing they could have done a little bit better is maybe pick the casting better because some characters are much better written than others and while I love the idea of the humans also being predators themselves and all of them having strengths and weaknesses some characters die off way to soon for them to be fleshed out enough for you to see them grow or show those specialties and the best characters end up staying until the end but none of that was enough to make me give this amazing effort a bad review it’s the predator movie with the best acting the best production the best violence the best tension and it does it all so well if you haven’t seen this in a while I highly suggest giving it another go not expecting anything specific and see how it goes. You won’t regret it!"
document = language_v1.Document(
    content=review, type_=language_v1.Document.Type.PLAIN_TEXT
)

# this detects the sentiment of the text using google NLP
sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment

# prints the text of the review, whether the review was positive or negative, and how strong the sentiment was
print(f"Text: {review}")
print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")
