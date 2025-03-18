def exchange(money):
    n500 = money//500
    money %= 500
    n100 = money//100
    money %= 100
    n50 = money//50
    money %= 50
    n10 = money//10
    print('500원:', n500, '개', '100원:', n100, '개', '50원:', n50, '개', '10원:', n10, '개')

def get_integer(prompt):
    num = int(input(prompt))
    return num

exchange(get_integer('동전으로 교환하고자 하는 금액은?'))


