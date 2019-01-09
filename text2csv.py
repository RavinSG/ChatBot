import csv


def convert_file(filename):
    fname = filename.split('.')[0]
    file = open('{}.txt'.format(fname), encoding='utf-8')
    out = open('{}.csv'.format(fname), 'w', newline='', encoding='utf-8')
    writer = csv.writer(out, delimiter=',')
    count = 0
    pair = []
    for row in file:
        if count % 2 == 0:
            pair = []
            pair.append(row.strip())
        else:
            pair.append(row.strip())
            print(pair)
            writer.writerow(pair)

        count += 1


convert_file('space.txt')