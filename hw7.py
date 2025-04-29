shopping_bag = {}

while True:
    item = input('상품명?')
    if item == '' or item == ' ':
        break
    stock = int(input('수량은?'))
    shopping_bag[item] = stock
    print(f'장바구니에 {item} {stock}개가 담겼습니다.')

print('장바구니 보기:', shopping_bag)

print('[검색]')
search = input('장바구니에서 확인하고자 하는 상품은?')
num = shopping_bag.get(search)
print(f'{search}은(는) {num}개 담겨 있습니다.')
