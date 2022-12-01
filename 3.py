def liczby(numer1, *args):
    '''
    :param args:
    :return:
    '''
    print(*args)
    a = numer1

    for m in args:
        if m > a:
            a = m
    return a

print(liczby(1, 2, 3, -5, 3.14, -56))
#print(liczby())