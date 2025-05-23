import os
import pickle

scores = []

filepath = 'score.bin'
filepath2= 'sums.txt'

def input_scores():
    print('[점수 입력]')
    lis = []
    n = 1
    while True:
        sco = int(input(f'#{n}? '))

        if sco < 0:
                  break

        lis.append(sco)
        n += 1

    return lis

def get_average(lis):
    return (sum(lis) / len(lis))

def show_scores(lis):
    for i in lis:
        print(i, end = ' ')

if os.path.exists(filepath):
    with open(filepath2, mode = 'r', encoding = 'utf-8') as file:
        lenth = int(file.read())
    print('[파일 읽기]')
    print()
    print('[점수 출력]')
    print('개인 점수: ', end = '')

    with open(filepath, mode = 'rb') as file:
        for i in range(lenth):
            scores.append(pickle.load(file))

        show_scores(scores)
        print()
        ave = get_average(scores)
        print(f'평균: {ave:.1f}')
else :
    scores = input_scores()

    print('[점수 출력]')
    print('개인 점수: ', end = '')
    show_scores(scores)
    print()
    ave = get_average(scores)
    print(f'평균: {ave:.1f}')

    with open(filepath, mode = 'wb') as file:
        for i in scores:
            pickle.dump(i, file)

    with open(filepath2, mode = 'w', encoding = 'utf-8') as file:
        file.write(f'{len(scores)}')
            


