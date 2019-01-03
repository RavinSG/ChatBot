import sqlite3

sqlite_file = 'user_data.sqlite'
username = 'Ravin'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


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


def add_entry(question, answer):
    c.execute('INSERT INTO Ravin VALUES (?, ?)',
              (question, answer))
    conn.commit()
    return None


create_user(username)

add_entry('df', '123')
