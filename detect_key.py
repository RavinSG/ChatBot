import csv
import json
import os
import extract_keys


def create_dict(file_name):
    name = file_name.split('.csv')[0]
    exists = os.path.isfile('{}.json'.format(name))
    if exists:
        return json.load(open('{}.json'.format(name), 'r'))
    else:
        with open(file_name, newline='', encoding='utf-8') as file:
            key_words = extract_keys.extract_keys(file_name)
            length = len(key_words)
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
        vectors['key_words'] = key_words
        with open('{}.json'.format(name), 'w') as output:
            json.dump(vectors, output)
        return vectors


def answer_question(key_words, answer_dict):
    while True:
        questions = input("Enter question: ")
        questions = questions.lower().strip().replace('?', '').split(' ')
        q_vector = [0] * len(key_words)
        for i in questions:
            if i in key_words:
                index = key_words.index(i)
                q_vector[index] = 1
        q_vector = ''.join(map(str, q_vector))
        try:
            print(answer_dict[q_vector])
        except:
            print('Sorry I don\'t know the answer to that question :(')



answer_dict = create_dict('in.csv')
answer_question(answer_dict['key_words'], answer_dict)

