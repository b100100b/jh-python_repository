def rep_char(c, n):
    print(c * n)

def draw_line_string(stri):
    msg1 = f'Welcome {stri}'
    msg2 = 'Welcome to Seoul.'

    nstr = len(msg1)

    if nstr > len(msg2):
        rep_char('-', nstr)
        print(msg1)
        print(msg2)
        rep_char('-', nstr)

    else:
        rep_char('-', len(msg2))
        print(msg1)
        print(msg2)
        rep_char('-', len(msg2))

name = input('input name:')

draw_line_string(name)
