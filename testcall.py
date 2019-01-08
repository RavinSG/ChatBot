from deploy._deployment import inference
import detect_key


def call_chatbot(question):
    out = inference.inference(question)
    ans = out['answers']
    scores = out['scores']
    scores, ans = (list(t) for t in zip(*sorted(zip(scores, ans), reverse=True)))
    length = len(ans)

    for i in range(length):
        print(ans[i], ' ', scores[i])

    return ans


def call_database(question):
    return detect_key.answer_question(question)


while True:
    ques = input('Enter question: ')
    out = inference.inference(ques)
    ans = out['answers']
    scores = out['scores']
    scores, ans = (list(t) for t in zip(*sorted(zip(scores, ans), reverse=True)))
    length = len(ans)

    for i in range(length):
        count = 0
        if 'http:' not in ans[i] and scores[i] > 0:
            count += 1
            print(ans[i], ' ', scores[i])
            if count > 3:
                break

