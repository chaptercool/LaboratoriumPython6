def document(imie, wiek):
    ''' Funkcja wykonywa wypisywanie imie oraz wiek.
    :param imie:
    :param wiek:
    :return:
    '''
    print(imie, wiek)

document("Karolina", 20)
document("Patryk", 98)
document(wiek=72, imie="Karolina")
print(document.__doc__)

print(help(document))
document("Karolina")