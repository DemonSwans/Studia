a = "11111111"
wynik = 0
index = len(a)-1
for i in a:
    wynik += int(i)*2**index
    index -= 1
print(wynik)
def dec_2_bin(a):
    a = int(a)
    wyniki = []
    wynik = ""
    while int(a) != 1:
        wyniki.append(int(a%2))
        a = (a-(a%2))/2
        if a == 1 :
            wyniki.append(1)
    wyniki.reverse()
    for i in wyniki:
        wynik += str(i)
    return wynik

def dec_2_bin_point(liczba):
    liczba = liczba.replace(",",".")
    bylu = []
    pierwsza=dec_2_bin(liczba[:liczba.find(".")])
    druga = float("0"+liczba[liczba.find("."):])
    wynik = ""
    while druga != 1:
        print(druga)
        if not str(druga)[str(druga).find(".")+1:] in bylu:
            if str(druga)[0] == "1":
                wynik += "1"
                druga = float("0"+str(druga)[str(druga).find("."):])
            else:
                wynik += "0"
            bylu.append(str(druga)[str(druga).find(".")+1:])
            druga = druga*2
        else:
            break
    print(str(pierwsza)+"."+str(wynik)[1:len(wynik)-1])




dec_2_bin_point("133,345")