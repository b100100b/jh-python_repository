def rep_char(c, n):
    print(c * n)

def draw_line_string(stri):
    msg1 = f' Welcome {stri}, '
    msg2 = ' Welcome to Seoul. '

    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    rep_char('-', nstr)
    print(msg1)
    print(msg2)
    rep_char('-', nstr)

name = input('input name:')

draw_line_string(name)

