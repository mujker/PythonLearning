x = 50


def func(abc):
    print('x is', abc)
    abc = 2
    print('Changed local x to', abc)


func(x)
print('x is still', x)
