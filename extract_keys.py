import csv
from sklearn.feature_extraction.text import  TfidfVectorizer


def extract_keys(file_name):
    with open('in.csv', newline='', encoding='utf-8') as file:
        a = csv.reader(file)
        questions = []
        for row in a:
            questions.append(row[0])

    vectorizer = TfidfVectorizer()
    response = vectorizer.fit_transform(questions)
    return vectorizer.get_feature_names()


