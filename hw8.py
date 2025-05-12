def buy(dic):
    print('[구입]')
    obj = input('상품명? ')
    if obj == '':
        return False
    num = int(input('수량은? '))

    dic[obj] = num

    print(f'장바구니에 {obj} {num}개가 담겼습니다.')

def show(dic):
    print(f'>>> 장바구니 보기: {dic}')

def find(dic):
    print('[검색]')
    search_obj = input('장바구니에서 확인하고자 하는 상품은? ')
    if search_obj in dic:
        print(f'{search_obj}은(는) {dic[search_obj]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {search_obj}은(는) 없습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
