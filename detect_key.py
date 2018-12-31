import csv
import extract_keys

key_words = extract_keys.extract_keys('in.csv')
length = len(key_words)

with open('in.csv', newline='', encoding='utf-8') as file:
    a = csv.reader(file)
    vectors = {}
    v_lis = []
    for row in a:
        question = row[0].lower()
        question = question.strip().replace('?', '').split(' ')
        answer = row[1]
        vector = [0] * length
        for i in range(length):
            if key_words[i] in question:
                vector[i] = 1
        vector = ''.join(map(str, vector))
        v_lis.append(vector)
        vectors[vector] = answer


def answer_question(questions):
    questions = questions.lower().strip().replace('?', '').split(' ')
    q_vector = [0] * length
    for i in questions:
        if i in key_words:
            index = key_words.index(i)
            q_vector[index] = 1
    q_vector = ''.join(map(str, q_vector))
    print(vectors[q_vector])


while True:
    question = input("Enter question: ")
    try:
        answer_question(question)
    except:
        print('Sorry I don\'t know the answer to that question :(')
