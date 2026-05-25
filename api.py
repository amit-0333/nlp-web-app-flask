# APPROACH:
# Sentiment → VADER (rule-based, fast)
# Emotion → NRCLex (lexicon-based)
# NER → spaCy (pretrained NLP pipeline)


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy


class API:

    def __init__(self):
        # Initialize models once
        self.sentiment_model = SentimentIntensityAnalyzer()
        self.nlp = spacy.load("en_core_web_sm")

    # ---------------- SENTIMENT ----------------
    def sentiment_analysis(self, text):

        scores = self.sentiment_model.polarity_scores(text)

        result = (
            f"Positive : {scores['pos']}\n"
            f"Neutral  : {scores['neu']}\n"
            f"Negative : {scores['neg']}\n"
            f"Compound : {scores['compound']}"
        )

        return result

    # ---------------- EMOTION ----------------
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    def emotion_analysis(self, text):

        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)
        c = score["compound"]

        if c >= 0.85:
            return "Extremely Happy 🤩"
        elif c >= 0.7:
            return "Very Happy 😄"
        elif c >= 0.55:
            return "Happy 😊"
        elif c >= 0.4:
            return "Positive 🙂"
        elif c >= 0.2:
            return "Slightly Positive 😌"
        elif -0.2 < c < 0.2:
            return "Neutral 😐"
        elif c <= -0.2 and c > -0.4:
            return "Slightly Sad 😕"
        elif c <= -0.4 and c > -0.55:
            return "Sad 😔"
        elif c <= -0.55 and c > -0.7:
            return "Angry 😡"
        elif c <= -0.7 and c > -0.85:
            return "Very Angry 🤬"
        elif c <= -0.85:
            return "Extremely Angry 💀"
        else:
            return "Unknown"
    # ---------------- NER ----------------
    def ner(self, text):

        doc = self.nlp(text)

        if not doc.ents:
            return "No entities found"

        result = ""
        for ent in doc.ents:
            result += f"Name : {ent.text} | Category : {ent.label_}\n\n"

        return result