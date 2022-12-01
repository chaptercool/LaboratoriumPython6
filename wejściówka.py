cyfry = []
x = 6

for i in range(x):
    a = int(input("Podaj liczbę: "))
    cyfry.append(a)

print(cyfry)

a = cyfry[0]%2
b = cyfry[1]%2
c = cyfry[2]%2
d = cyfry[3]%2
e = cyfry[4]%2
f = cyfry[5]%2
parz = []

if a == 0:
    parz.append(cyfry[0])

