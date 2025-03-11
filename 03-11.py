def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(r):
    s = 3.14*r*r
    return s

input_r = get_radius('원의 반지름을 입력해주세요.')
print('반지름', input_r, '인 원의 넓이 = 3.14 x', input_r, 'x', input_r, '=', get_circle_area(input_r))
