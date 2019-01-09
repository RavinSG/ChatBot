from deploy._deployment import inference
import detect_key
import user_db


def call_chatbot(question):
    out = inference.inference(question)
    ans = out['answers']
    scores = out['scores']
    scores, ans = (list(t) for t in zip(*sorted(zip(scores, ans), reverse=True)))
    length = len(ans)
    count = 0
    for i in range(length):
        count += 1
        if count > 3:
            break
        if 'http:' not in ans[i] and scores[i] > 0:
            print(ans[i], ' ', scores[i])

    return ans


def call_cricket_database(question):
    return detect_key.answer_question(question)


def call_user_database(question):
    return user_db.answer_question(question)


def call_user_change(username):
    user_db.change_user(username)


modes = ['Cricket Questions', 'Private Conversation', 'Learning Mode', 'Neural Translation', 'Change User', 'Change Answer File']
current_mode = 0
prompts = ['Enter question', 'What should I tell about you? ', 'Tell me about yourself', 'Ask the Neural Network']
while True:
    ques = input('{}: '.format(prompts[current_mode]))
    if ques == 'ESC':
        print('Username:',user_db.get_user())
        for mode in range(len(modes)):
            if mode == current_mode:
                print('{}) '.format(mode + 1), modes[mode], '<--- current mode')
            else:
                print('{}) '.format(mode + 1), modes[mode])

        while True:
            try:
                entered_mode = int(input('Please select a mode from the above list: ')) - 1
                if entered_mode > (len(modes) - 1) or entered_mode < 0:
                    print('Enter a valid number')
                else:
                    current_mode = entered_mode
                    if current_mode == 4:
                        user = input('Please enter your name: ')
                        call_user_change(user)
                        current_mode = 1
                    elif current_mode == 5:
                        while True:
                            try:
                                file = input('Please enter the file name:')
                                detect_key.change_answer_dict(file)
                                current_mode = 0
                                break
                            except:
                                print('Please enter a valid file path!')
                    break
            except:
                print('Enter a valid number')
    else:
        if current_mode == 3:
            call_chatbot(ques)
        elif current_mode == 0:
            call_cricket_database(ques)
        elif current_mode == 1:
            call_user_database(ques)
        elif current_mode == 2:
            user_db.add_entry(ques)

