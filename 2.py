def oblicz(par1, par2):
    suma = par1 + par2
    roznica = par1 - par2
    return suma, roznica
print(oblicz(int(input("Podaj liczbę nr. 1: ")), int(input("Podaj liczbę nr. 2: "))))

x, y = oblicz(3, 2)
print(f"Suma równa się {x}, a różnica {y}")