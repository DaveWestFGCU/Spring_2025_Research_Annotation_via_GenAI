prompt = \
    {
        "poc_subset":
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
