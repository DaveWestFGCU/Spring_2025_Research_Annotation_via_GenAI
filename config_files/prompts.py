prompt = \
    {
        "emoevent_poc":
            {
                'labels':
                    """
                    <context>
                    
                    Classify the following tweet by the emotion the author intended to convey ONLY from the following list:
                    1. Anger (also includes annoyance, rage)
                    2. Disgust (also includes disinterest, dislike, loathing)
                    3. Fear (also includes apprehension, anxiety, terror)
                    4. Joy (also includes serenity, ecstasy)
                    5. Sadness (also includes pensiveness, grief)
                    6. Surprise (also includes distraction, amazement)
                    Your response should consist of only the most relevant label.
                    
                    \"<text>\"
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
                            "The UEFA Champions League (UCL): An annual club football competition organized by the Union of European Football Associations (UEFA) and contested by top-division European clubs, deciding the best team in Europe"
                    }
            },

        "emoevent_en_raw":
            {
                'text':
                    """
                    The following is a tweet portraying <original_record.labels>. 
                    \"<original_record.text>\"
                    Using this tweet, generate a tweet about the same subject and similar in style that instead portrays <target_label>. Only give the generated tweet.
                    """,

                'labels':
                    """
                    Classify the tweet \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:
                    1. Anger (also includes annoyance, rage)
                    2. Disgust (also includes disinterest, dislike, loathing)
                    3. Fear (also includes apprehension, anxiety, terror)
                    4. Joy (also includes serenity, ecstasy)
                    5. Sadness (also includes pensiveness, grief)
                    6. Surprise (also includes distraction, amazement)
                    Give only the label.
                    """
            },

        "emoevent_en_tokenized":
            {
                'text':
                    """
                    The following is a tweet with any usernames, names, hashtags, and URLs tokenized with an all-caps generalized term. 
                    \"<original_record.text>\"
                    Using this tweet, which portrays the emotion <original_record.labels>, generate a tweet about the same subject and similar in style that instead portrays <target_label>. Only give the generated tweet.
                    """,

                'text_response_start':
                    "Here is a similar tweet portraying <target_label>:\n\n\"",

                'labels':
                    """
                    Classify the tweet \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:
                    1. Anger (also includes annoyance, rage)
                    2. Disgust (also includes disinterest, dislike, loathing)
                    3. Fear (also includes apprehension, anxiety, terror)
                    4. Joy (also includes serenity, ecstasy)
                    5. Sadness (also includes pensiveness, grief)
                    6. Surprise (also includes distraction, amazement)
                    Give only the label.
                    """
            },

        "goemotions_6_single_poc":
            {
                'labels':
                    """
                    Identify the emotion most expressed by the writer of the text, given pre-defined emotion definitions (see below). 

                    Emotion Definitions:
                    anger - A strong feeling of displeasure or antagonism.
                    	Includes:
                    	annoyance - Mild anger, irritation.
                    		disapproval - Having or expressing an unfavorable opinion.
                    
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
                    	Includes:
                    	nervousness - Apprehension, worry, anxiety.
                    
                    Examples of Fear: 
                    “I want to go scuba diving so bad, but swimming in anything bigger than a pool terrifies me.”
                    “They’re honestly a cult at this point. It’s not just bad, but incredibly scary.”
                    “The Babylon Bee article makes me worry for [NAME] comic tastes.”
                    
                    joy - A feeling of pleasure and happiness.
                    	Includes:
                    admiration - Finding something impressive or worthy of respect.
                    amusement - Finding something funny or being entertained.
                    approval - Having or expressing a favorable opinion.
                    caring - Displaying kindness and concern for others.
                    desire - A strong feeling of wanting something or wishing for something to happen.
                    excitement - Feeling of great enthusiasm and eagerness.
                    gratitude - A feeling of thankfulness and appreciation.
                    love - A strong positive emotion of regard and affection.
                    optimism - Hopefulness and confidence about the future or the success of something.
                    pride - Pleasure or satisfaction due to ones own achievements or the achievements of those with whom one is closely associated.
                    relief - Reassurance and relaxation following release from anxiety or distress.
                    
                    Examples of Joy:
                    “Cool! Glad to see some cooperation.”
                    “My kitten just got very happy when Pasta scores. Such loud purrs! I was happy too.”
                    “This is most excellent news! Also, glad to know he went on to work somewhere like Google.”
                    
                    sadness - Emotional pain, sorrow.
                    	Includes:
                    disappointment - Sadness or displeasure caused by the nonfulfillment of one’s hopes or expectations.
                    embarrassment Self-consciousness, shame, or awkwardness.
                    grief - Intense sorrow, especially caused by someone’s death.
                    remorse - Regret or guilty feeling.
                    
                    Examples of Sadness:
                    “I go to a neighborhood mexican restaurant monthly for the past 2.5 years, but nobody knows my name 🙁”
                    “Sorry misunderstood you! I’m talking about viruses and bacteria that can kill you like the flu etc.”
                    “The only death that made me feel any emotion. And it wasn’t even the death itself.”
                    
                    surprise - Feeling astonished, startled by something unexpected.
                    	Includes:
                    confusion - Lack of understanding, uncertainty.
                    curiosity - A strong desire to know or learn something.
                    realization - Becoming aware of something.
                    
                    Examples of Surprise:
                    “Right, that makes sense! I wonder if the person I met in real life would acknowledge he’s more of a fence sitter than childfree, haha”
                    “Can you imagine being taken to court over a flushing loo? I can’t believe the courts are even entertaining this.”
                    “Wait, WHAT?!?!”
                    
                    neutral - Lacking in an expressed emotion.
                    
                    Examples of Neutral:
                    “[NAME] was also a vice president.”
                    “Keep us updated.”
                    “Nope. 7th grade, different state”
                    
                    Here is the Reddit comment to analyze: \"<text>\"
                    """
            },

        "enisear":
            {
                'text':
                    """
                    The following is a sentence portraying the emotion <original_record.labels>: 
                    \"<original_record.text>\"
                    Using this sentence, create a sentence about the same subject and similar in style that instead portrays <target_label>. Only give the generated sentence.
                    """,

                'labels':
                    """
                    Classify the sentence \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:"
                    1. Anger
                    2. Disgust
                    3. Fear
                    4. Guilt
                    5. Joy
                    6. Sadness
                    7. Shame
                    Give only the label.
                    """
            },

        "stackoverflow":
            {
                'text':
                    """

                    """,

                'labels':
                    """
                    Classify the Stack Overflow post \"<synthetic_text>\" by the single most represented emotion ONLY from the following list:"
                    1. ANGER
                    2. FEAR
                    3. JOY
                    4. LOVE
                    5. SADNESS
                    6. SURPRISE
                    Give only the label.
                    """
            }
    }
