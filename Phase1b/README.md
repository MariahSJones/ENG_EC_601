### `movie_nlp.py`

This program takes the text of a movie review, then uses google NLP to analyse the sentiment of the text. It then returns the text of the review along with a score and a magnitude. The score ranges from -1 to 1 with positive scores indicating positive sentiment and negative scores indxicating negative sentiment. The magnitude is always positive and indicates how strong the sentiment perceived based on emotional words suchs as "hate" and "love".
```
$ python Phase1b/movie_nlp.py
Text: I really don’t understand all the low reviews this movie I think went way over most people’s head. It is 
not some redo of the first movie like many say it just feels similar because it has all the same strengths and 
many new ones. It has that perfect blend of action tension and the mix of sci fi horror with the action genera 
that made the original so stand out against every other 80s action movie. This film follows humans placed on the predator home planet and it’s clear from the start they are predators themselves from criminals to worthy warriors to fight the predator species they were all put on the planet as a test to see if these humans could use 
each of their strengths and weaknesses the right ways to overcome traps and a alien threat. Overtime many plot 
twists and secrets are revealed and the plot becomes much more than a basic predator film and it focuses much more on horror than the previous films more than the action. Also the predator civil war along with new sub species to learn about was so awesome. Also this film has so much intense violence and gore like the original it just happens with better pacing it doesn’t go from an action movie to a sci fi movie or vice versa it instead has a perfect blend of everything the predator series is amazing for and it doesn’t waste your time with one liners and corny stuff that every other predator movie seems to need so badly. I will get hate for this but predators is my favorite in the series BY FAR the only thing they could have done a little bit better is maybe pick the casting better because some characters are much better written than others and while I love the idea of the humans also being predators themselves and all of them having strengths and weaknesses some characters die off way to soon for them to be fleshed out enough for you to see them grow or show those specialties and the best characters end up staying until the end but none of that was enough to make me give this amazing effort a bad review it’s the predator movie with the best acting the best production the best violence the best tension and it does it all so well if you haven’t seen this in a while I highly suggest giving it another go not expecting anything specific and see how it goes. You won’t regret it!
Sentiment: 0.4000000059604645, 4.699999809265137
```


---
### `google_nlp.py`

This program takes the text of a movie review, then uses google NLP to analyse the sentiment of the text. Unlike the previous analyzer, this one analyzes the sentiment line by line as well as returning what it thinks the sentence is about. It then returns the text of the review along with a score and a magnitude. The score ranges from -1 to 1 with positive scores indicating positive sentiment and negative scores indxicating negative sentiment. The magnitude is always positive and indicates how strong the sentiment perceived based on emotional words suchs as "hate" and "love".
```
$ python Phase1b/google_nlp.py
Representative name for the entity: predators
Entity type: PERSON
Salience score: 0.0994439348578453
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: humans
Mention type: COMMON
Mention text: predators
Mention type: COMMON
_____
Representative name for the entity: movie     
Entity type: WORK_OF_ART
Salience score: 0.08569882065057755
Entity sentiment score: -0.4000000059604645   
Entity sentiment magnitude: 0.4000000059604645
Mention text: movie
Mention type: COMMON
_____
Representative name for the entity: reviews   
Entity type: WORK_OF_ART
Salience score: 0.0471152625977993
Entity sentiment score: -0.4000000059604645
Entity sentiment magnitude: 0.4000000059604645
Mention text: reviews
Mention type: COMMON
_____
Representative name for the entity: film
Entity type: WORK_OF_ART
Salience score: 0.0447266660630703
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 1.399999976158142
Mention text: film
Mention type: COMMON
_____
Representative name for the entity: head
Entity type: OTHER
Salience score: 0.041447192430496216
Entity sentiment score: -0.4000000059604645
Entity sentiment magnitude: 0.4000000059604645
Mention text: head
Mention type: COMMON
_____
Representative name for the entity: people
Entity type: PERSON
Salience score: 0.041447192430496216
Entity sentiment score: -0.5
Entity sentiment magnitude: 0.5
Mention text: people
Mention type: COMMON
_____
Representative name for the entity: movie
Entity type: WORK_OF_ART
Salience score: 0.03106791339814663
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: movie
Mention type: COMMON
_____
Representative name for the entity: violence
Entity type: OTHER
Salience score: 0.028327330946922302
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.699999988079071
Mention text: violence
Mention type: COMMON
_____
Representative name for the entity: none
Entity type: OTHER
Salience score: 0.026834875345230103
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.6000000238418579
Mention text: none
Mention type: COMMON
_____
Representative name for the entity: redo
Entity type: OTHER
Salience score: 0.02553834766149521
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: redo
Mention type: COMMON
_____
Representative name for the entity: strengths
Entity type: OTHER
Salience score: 0.024928055703639984
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: strengths
Mention type: COMMON
_____
Representative name for the entity: blend
Entity type: OTHER
Salience score: 0.022635946050286293
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 0.6000000238418579
Mention text: blend
Mention type: COMMON
_____
Representative name for the entity: ones
Entity type: OTHER
Salience score: 0.019994428381323814
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: ones
Mention type: COMMON
_____
Representative name for the entity: plot
Entity type: OTHER
Salience score: 0.01970694772899151
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.20000000298023224
Mention text: plot
Mention type: COMMON
_____
Representative name for the entity: action genera
Entity type: OTHER
Salience score: 0.019222714006900787
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 1.2999999523162842
Mention text: action genera
Mention type: COMMON
_____
Representative name for the entity: characters
Entity type: PERSON
Salience score: 0.018144257366657257
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.5
Mention text: characters
Mention type: COMMON
_____
Representative name for the entity: predator movie
Entity type: WORK_OF_ART
Salience score: 0.016729112714529037
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.4000000059604645
Mention text: predator movie
Mention type: COMMON
_____
Representative name for the entity: predators
Entity type: PERSON
Salience score: 0.015142607502639294
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.800000011920929
Mention text: predators
Mention type: COMMON
_____
Representative name for the entity: idea
Entity type: OTHER
Salience score: 0.014503665268421173
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.30000001192092896
Mention text: idea
Mention type: COMMON
_____
Representative name for the entity: humans
Entity type: PERSON
Salience score: 0.012171810492873192
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: humans
Mention type: COMMON
_____
Representative name for the entity: liners
Entity type: OTHER
Salience score: 0.011937814764678478
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.6000000238418579
Mention text: liners
Mention type: COMMON
_____
Representative name for the entity: action movie
Entity type: WORK_OF_ART
Salience score: 0.011748726479709148
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 0.6000000238418579
Mention text: action movie
Mention type: COMMON
_____
Representative name for the entity: many
Entity type: PERSON
Salience score: 0.008899467065930367
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: many
Mention type: COMMON
_____
Representative name for the entity: predator
Entity type: OTHER
Salience score: 0.00881274975836277
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 0.6000000238418579
Mention text: predator
Mention type: COMMON
_____
Representative name for the entity: sci fi horror
Entity type: WORK_OF_ART
Salience score: 0.008589514531195164
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 0.6000000238418579
Mention text: sci fi horror
Mention type: COMMON
_____
Representative name for the entity: action tension
Entity type: OTHER
Salience score: 0.008589514531195164
Entity sentiment score: 0.699999988079071
Entity sentiment magnitude: 0.699999988079071
Mention text: action tension
Mention type: COMMON
_____
Representative name for the entity: predator home planet
Entity type: OTHER
Salience score: 0.008559205569326878
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: predator home planet
Mention type: COMMON
_____
Representative name for the entity: original
Entity type: WORK_OF_ART
Salience score: 0.007545792497694492
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 0.6000000238418579
Mention text: original
Mention type: COMMON
_____
Representative name for the entity: mix
Entity type: OTHER
Salience score: 0.007545792497694492
Entity sentiment score: 0.5
Entity sentiment magnitude: 0.5
Mention text: mix
Mention type: COMMON
_____
Representative name for the entity: warriors
Entity type: PERSON
Salience score: 0.007519158534705639
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: warriors
Mention type: COMMON
_____
Representative name for the entity: criminals
Entity type: PERSON
Salience score: 0.007519158534705639
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: criminals
Mention type: COMMON
_____
Representative name for the entity: start
Entity type: EVENT
Salience score: 0.007519158534705639
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: start
Mention type: COMMON
_____
Representative name for the entity: predator movie
Entity type: WORK_OF_ART
Salience score: 0.007471625227481127
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: predator movie
Mention type: COMMON
_____
Representative name for the entity: sci fi movie
Entity type: WORK_OF_ART
Salience score: 0.0072901900857687
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: sci fi movie
Mention type: COMMON
_____
Representative name for the entity: action movie
Entity type: WORK_OF_ART
Salience score: 0.0072901900857687
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: action movie
Mention type: COMMON
_____
Representative name for the entity: action
Entity type: OTHER
Salience score: 0.007277363445609808
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: action
Mention type: COMMON
_____
Representative name for the entity: predator species
Entity type: OTHER
Salience score: 0.007248888723552227
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: predator species
Mention type: COMMON
_____
Representative name for the entity: films
Entity type: WORK_OF_ART
Salience score: 0.0068654208444058895
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: films
Mention type: COMMON
_____
Representative name for the entity: predator film
Entity type: WORK_OF_ART
Salience score: 0.006781537551432848
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: predator film
Mention type: COMMON
_____
Representative name for the entity: film
Entity type: WORK_OF_ART
Salience score: 0.0066350046545267105
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: film
Mention type: COMMON
_____
Representative name for the entity: predator series
Entity type: WORK_OF_ART
Salience score: 0.006407245993614197
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: predator series
Mention type: COMMON
_____
Representative name for the entity: sub species
Entity type: OTHER
Salience score: 0.006378469057381153
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 0.6000000238418579
Mention text: sub species
Mention type: COMMON
_____
Representative name for the entity: strengths
Entity type: OTHER
Salience score: 0.006332012824714184
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: strengths
Mention type: COMMON
_____
Representative name for the entity: hate
Entity type: OTHER
Salience score: 0.0059753539972007275
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: hate
Mention type: COMMON
_____
Representative name for the entity: horror
Entity type: OTHER
Salience score: 0.005831058137118816
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: horror
Mention type: COMMON
_____
Representative name for the entity: civil war
Entity type: EVENT
Salience score: 0.005779344588518143
Entity sentiment score: 0.6000000238418579
Entity sentiment magnitude: 0.6000000238418579
Mention text: civil war
Mention type: COMMON
_____
Representative name for the entity: weaknesses
Entity type: OTHER
Salience score: 0.0057756188325583935
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: weaknesses
Mention type: COMMON
_____
Representative name for the entity: planet
Entity type: LOCATION
Salience score: 0.0057756188325583935
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: planet
Mention type: COMMON
_____
Representative name for the entity: blend
Entity type: OTHER
Salience score: 0.005327993538230658
Entity sentiment score: 0.4000000059604645
Entity sentiment magnitude: 0.4000000059604645
Mention text: blend
Mention type: COMMON
_____
Representative name for the entity: predators
Entity type: PERSON
Salience score: 0.005310249514877796
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.30000001192092896
Mention text: humans
Mention type: COMMON
Mention text: predators
Mention type: COMMON
_____
Representative name for the entity: gore
Entity type: PERSON
Salience score: 0.005100862123072147
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: gore
Mention type: COMMON
_____
Representative name for the entity: original
Entity type: WORK_OF_ART
Salience score: 0.005100862123072147
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: original
Mention type: COMMON
_____
Representative name for the entity: pacing
Entity type: OTHER
Salience score: 0.005100862123072147
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: pacing
Mention type: COMMON
_____
Representative name for the entity: each
Entity type: CONSUMER_GOOD
Salience score: 0.005073307082056999
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: each
Mention type: COMMON
_____
Representative name for the entity: alien threat
Entity type: OTHER
Salience score: 0.005073307082056999
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: alien threat
Mention type: COMMON
_____
Representative name for the entity: test
Entity type: OTHER
Salience score: 0.005073307082056999
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: test
Mention type: COMMON
_____
Representative name for the entity: traps
Entity type: OTHER
Salience score: 0.005073307082056999
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: traps
Mention type: COMMON
_____
Representative name for the entity: ways
Entity type: OTHER
Salience score: 0.005073307082056999
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: ways
Mention type: COMMON
_____
Representative name for the entity: plot twists
Entity type: OTHER
Salience score: 0.005059401970356703
Entity sentiment score: 0.0
Entity sentiment magnitude: 0.0
Mention text: plot twists
Mention type: COMMON
_____
Representative name for the entity: secrets
Entity type: OTHER
Salience score: 0.005059401970356703
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: secrets
Mention type: COMMON
_____
Representative name for the entity: specialties
Entity type: OTHER
Salience score: 0.004790018312633038
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: specialties
Mention type: COMMON
_____
Representative name for the entity: vice versa
Entity type: PERSON
Salience score: 0.004680038429796696
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: vice versa
Mention type: COMMON
_____
Representative name for the entity: stuff
Entity type: OTHER
Salience score: 0.004680038429796696
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: stuff
Mention type: COMMON
_____
Representative name for the entity: everything
Entity type: OTHER
Salience score: 0.004680038429796696
Entity sentiment score: 0.30000001192092896
Entity sentiment magnitude: 0.30000001192092896
Mention text: everything
Mention type: COMMON
_____
Representative name for the entity: characters
Entity type: PERSON
Salience score: 0.004394806455820799
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: characters
Mention type: COMMON
_____
Representative name for the entity: strengths
Entity type: OTHER
Salience score: 0.004394806455820799
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: strengths
Mention type: COMMON
_____
Representative name for the entity: weaknesses
Entity type: OTHER
Salience score: 0.00400843471288681
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: weaknesses
Mention type: COMMON
_____
Representative name for the entity: effort
Entity type: OTHER
Salience score: 0.0035643817391246557
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: effort
Mention type: COMMON
_____
Representative name for the entity: end
Entity type: EVENT
Salience score: 0.0035207895562052727
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: end
Mention type: COMMON
_____
Representative name for the entity: way
Entity type: OTHER
Salience score: 0.0035207895562052727
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: way
Mention type: COMMON
_____
Representative name for the entity: best
Entity type: OTHER
Salience score: 0.0035019470378756523
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: best
Mention type: COMMON
_____
Representative name for the entity: review
Entity type: OTHER
Salience score: 0.0030577564612030983
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: review
Mention type: COMMON
_____
Representative name for the entity: violence
Entity type: OTHER
Salience score: 0.002805351512506604
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: violence
Mention type: COMMON
_____
Representative name for the entity: tension
Entity type: OTHER
Salience score: 0.002805351512506604
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: tension
Mention type: COMMON
_____
Representative name for the entity: anything
Entity type: OTHER
Salience score: 0.0026856749318540096
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: anything
Mention type: COMMON
_____
Representative name for the entity: production
Entity type: OTHER
Salience score: 0.002463961485773325
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: production
Mention type: COMMON
_____
Representative name for the entity: all
Entity type: OTHER
Salience score: 0.0021937559358775616
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: all
Mention type: COMMON
_____
Representative name for the entity: favorite
Entity type: PERSON
Salience score: 0.001974249491468072
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: favorite
Mention type: COMMON
_____
Representative name for the entity: characters
Entity type: PERSON
Salience score: 0.0018798884702846408
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: characters
Mention type: COMMON
_____
Representative name for the entity: thing
Entity type: OTHER
Salience score: 0.0018563874764367938
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: thing
Mention type: COMMON
_____
Representative name for the entity: series
Entity type: WORK_OF_ART
Salience score: 0.0017572472570464015
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: series
Mention type: COMMON
_____
Representative name for the entity: bit
Entity type: OTHER
Salience score: 0.0015433459775522351
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: bit
Mention type: COMMON
_____
Representative name for the entity: casting
Entity type: OTHER
Salience score: 0.0015433459775522351
Entity sentiment score: 0.10000000149011612
Entity sentiment magnitude: 0.10000000149011612
Mention text: casting
Mention type: COMMON
_____
Representative name for the entity: others
Entity type: PERSON
Salience score: 0.0015433459775522351
Entity sentiment score: 0.20000000298023224
Entity sentiment magnitude: 0.20000000298023224
Mention text: others
Mention type: COMMON
_____
Language of the text: en
```


---