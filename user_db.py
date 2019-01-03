import sqlite3
import json

sqlite_file = 'user_data.sqlite'
username = 'Ravin'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

stop_words = json.load(open('stopwords-en.json', 'r', encoding='utf-8'))


def create_user(new_user):
    global username
    username = new_user
    field1 = 'question'
    field2 = 'answer'
    field_type = 'STRING'
    names = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(
        table_name=username)).fetchall()

    if len(names) == 0:
        c.execute('CREATE TABLE {tn} ('
                  '{f1} {ft1}, '
                  '{f2} {ft2}'
                  ')'.format(tn=username, f1=field1, ft1=field_type, f2=field2, ft2=field_type))

    return names


def remove_stop_words(phrase):
    keys = []
    phrase = phrase.lower().strip('?').split(' ')
    for word in phrase:
        if word not in stop_words:
            keys.append(word)
    return ' '.join(keys)


def add_entry(answer):
    question = remove_stop_words(answer)
    c.execute('INSERT INTO Ravin VALUES (?, ?)',
              (question, answer))
    conn.commit()
    return None


def change_pronouns(phrase):
    source = ['i', 'am', 'i\'m', 'my']
    target = ['you', 'are', 'you\'re', 'your']
    phrase = phrase.lower().split(' ')
    for i in range(len(phrase)):
        if phrase[i] in source:
            phrase[i] = target[source.index(phrase[i])]
    return ' '.join(phrase)


def answer_question(question):
    keys = remove_stop_words(question).split(' ')
    max_score = 0
    answer = c.execute('SELECT * from {tn}'.format(tn =username)).fetchall()
    reply = ''
    for ans in answer:
        score = 0
        q_keys = ans[0].split(' ')
        for key in keys:
            if key in q_keys:
                score += 1
        if score >= max_score:
            max_score = score
            reply = ans[1]
    print(change_pronouns(reply))

answer_question('Where do i study?')
