
def read_single_digit(n):
    if n == '1':
        print('일', end = '')
    elif n == '2':
        print('이', end = '')
    elif n == '3':
        print('삼', end = '')
    elif n == '4':
        print('사', end = '')
    elif n == '5':
        print('오', end = '')
    elif n == '6':
        print('육', end = '')
    elif n == '7':
        print('칠', end = '')
    elif n == '8':
        print('팔', end = '')
    elif n == '9':
        print('구', end = '')
    elif n == '0':
        print('영', end = '')
    else :
        print('', end = '')

def read_number(num):
    num = str(num)
    read_single_digit(num[0])
    if len(num) > 1:
        read_single_digit(num[1])
    else :
        print('', end = '')
    if len(num) > 2:
        read_single_digit(num[2])
    else :
        print('', end = '') 

number = int(input('정수입력:'))

read_number(number)
