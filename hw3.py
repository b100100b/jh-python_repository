def get_fixed_price(disper, dispri):
    original_price = (dispri / (1 - (disper/100)))
    return original_price

discount = float(input('할인율입력(숫자만):'))
dispri1 = int(input('A상품 할인가 입력:'))
dispri2 = int(input('B상품 할인가 입력:'))

print('A 상품의 정가는', get_fixed_price(discount, dispri1), '원')
print('B 상품의 정가는', get_fixed_price(discount, dispri2), '원')

