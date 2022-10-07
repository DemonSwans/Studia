import math
def czy_10():
    print("Podaj Liczbe:")
    try:
        liczba = int(input())
        if liczba > 10:
            print("Wieksze od 10")
        elif liczba<10:
            print("Mniejsze od 10")
        else:
            print("To jest 10")
    except Exception:
        czy_10()

def kwadratowa():
    try:
        a = float(input("Podaj a:"))
        if a != 0:
            b = float(input("Podaj b:"))
            c = float(input("Podaj c:"))
            delta = b**2 - 4*a*c
            if delta > 0:
                x1 = (-(b)-math.sqrt(delta))/(2*a)
                x2 = (-(b)+math.sqrt(delta))/(2*a)
                print(f"Miejsca zerowe:\nx1={x1}\nx2={x2}")
            elif delta == 0:
                x0 = (-(b))/(2*a)
                print(f"Jedno miejsce zerowe x0 = {x0}")
            else:
                print("Brak miejsc zerowych")
        else:
            kwadratowa()
    except Exception:
        kwadratowa()

kwadratowa()