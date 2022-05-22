import CsvReader

import sklearn.feature_extraction.text
from TextPreparation import prepared_text


file = CsvReader.read_csv("alexa_reviews.csv")


def visual() -> None:
    vectorizer = sklearn.feature_extraction.text.CountVectorizer(tokenizer=prepared_text)