prompt = \
    {
        "emoevent":
            {
                'labels':
"""
You are given a tweet. Your task is to identify the primary emotion the author intended to convey in the tweet and classify it using one of the following labels: anger, disgust, fear, joy, sadness, surprise or others.

Mapping Guidelines:
If the tweet conveys a secondary emotion similar to annoyance or rage, classify it as anger.
If the tweet conveys a secondary emotion similar to disinterest, dislike, or loathing, classify it as disgust.
If the tweet conveys a secondary emotion similar to apprehension, anxiety, or terror, classify it as fear.
If the tweet conveys a secondary emotion similar to serenity or ecstasy, classify it as joy.
If the tweet conveys a secondary emotion similar to pensiveness or grief, classify it as sadness.
If the tweet conveys a secondary emotion similar to distraction or amazement, classify it as surprise.
If the tweet conveys no emotion, there are multiple emotions with no dominant one expressed, or more context is needed to determine the emotion, classify it as others.

Your response must ONLY consist of one word: the chosen emotion label from the list: anger, disgust, fear, joy, sadness, surprise, or others. Do not include any explanation, reasoning, or additional text. Output NOTHING but that one label.

Context: <context>

Tweet: \"<text>\"
""",
                'context':
                    {
                        'NotreDame':
                            "The Notre Dame Cathedral Fire: On 15 April 2019, a structure fire broke out beneath the roof of Notre-Dame Cathedral in Paris.",

                        'GretaThunberg':
                            "Greta Thunberg: Founder of the movement \"Fridays for Future\". It refers to how she strikes every Friday to protest the lack of effective climate legislation on a governmental level. Students throughout Europe regularly held strikes on Fridays.",

                        'WorldBookDay':
                            "World book day or International Day of the Book: An annual event organized by the United Nations Educational, Scientific and Cultural Organization (UNESCO) to promote reading, publishing, and copyright.",

                        'Venezuela':
                            "Venezuela's presidential crisis: A crisis concerning who is the legitimate President of Venezuela had been underway since January 10th of 2019, with the nation and the world divided in support for Nicolas Maduro or Juan Guaido.",

                        'GameOfThrones':
                            "Game of Thrones: An American fantasy drama television series. It was one of the most popular series in the world today. The last season premiered in April 2019.",

                        'LaLiga':
                            "Campeonato Nacional de Liga de Primera Division (La Liga): The men’s top professional football division of the Spanish football league system.",

                        'ChampionsLeague':
                            "The UEFA Champions League (UCL): An annual club football competition organized by the Union of European Football Associations (UEFA) and contested by top-division European clubs, deciding the best team in Europe",

                        'SpainElection':
                            "The 2019 Spanish general election was held on Sunday, April 2018, to elect the 13th Cortes Generales of the president of Spain."
                    }
            },


        "goemotions_ekman_single":
            {
                'labels':
                    """Identify the emotion most people will feel the speaker may be feeling given a sentence or a short text snipped uttered by the speaker.
                    
                    Choose the emotion from following choices [anger, disgust, fear, joy, sadness, surprise, neutral] given the emotion category definitions below. 

                    Emotion Definitions:
                    anger - A strong feeling of displeasure or antagonism.
                    	Anger includes annoyance and disapproval.
                        Examples of Anger:
                            “I don’t like [NAME] in the slightest but I hate [NAME] even more. Get her Belcalis”
                            “Are you daft ... ? That is and always has been the proposal. [NAME] don't listen and don't care though. Fucking dumbass.”
                            “You are oddly defensive about a random chef. Did you come to /r/wewantplates just to insult people and build up this chef? [NAME]”
                    
                    disgust - Revulsion or strong disapproval aroused by something unpleasant or offensive.
                        Examples of Disgust:
                            “Those floors with *that* paneling? Ugh!”
                            “That’s such a selfish mentality to have.”
                            “This is the worst thing I’ve ever seen. Take my upvote.”
                    
                    fear - Being afraid or worried.
                    	Fear includes nervousness and anxiety.
                        Examples of Fear: 
                        “I want to go scuba diving so bad, but swimming in anything bigger than a pool terrifies me.”
                        “They’re honestly a cult at this point. It’s not just bad, but incredibly scary.”
                        “The Babylon Bee article makes me worry for [NAME] comic tastes.”
                    
                    joy - A feeling of pleasure and happiness.
                    	Joy includes admiration, amusement, approval, caring, desire, excitement, gratitude, love, optimism, pride, and relief.
                        Examples of Joy:
                            “Cool! Glad to see some cooperation.”
                            “My kitten just got very happy when Pasta scores. Such loud purrs! I was happy too.”
                            “This is most excellent news! Also, glad to know he went on to work somewhere like Google.”
                    
                    sadness - Emotional pain, sorrow.
                    	Sadness includes disappointment, embarrassment, grief, and remorse.
                        Examples of Sadness:
                            “I go to a neighborhood mexican restaurant monthly for the past 2.5 years, but nobody knows my name 🙁”
                            “Sorry misunderstood you! I’m talking about viruses and bacteria that can kill you like the flu etc.”
                            “The only death that made me feel any emotion. And it wasn’t even the death itself.”
                    
                    surprise - Feeling astonished, startled by something unexpected.
                    	Surprise includes confusion, curiosity and realization.
                        Examples of Surprise:
                            “Right, that makes sense! I wonder if the person I met in real life would acknowledge he’s more of a fence sitter than childfree, haha”
                            “Can you imagine being taken to court over a flushing loo? I can’t believe the courts are even entertaining this.”
                            “Wait, WHAT?!?!”
                    
                    neutral - Lacking in an expressed emotion.
                        Examples of Neutral:
                            “[NAME] was also a vice president.”
                            “Keep us updated.”
                            “Nope. 7th grade, different state”
                    
                    <response instructions>
                    Use ONLY the emotion categories [anger, disgust, fear, joy, sadness, surprise, neutral].
                    
                    Here is the speaker's Reddit comment (made in response to a post or another commenter) to analyze: \"<text>\"
                    """,

                'with considerations': "Your response should consist of important points to consider given the text, followed by the one most relevant emotion label within two asterisks (i.e. **emotion**).",
                'only label': "Your response should consist of only the one most relevant emotion label within two asterisks (i.e. **emotion**)."
            }
    }
