naglowek="a;b;c;d;e;g"
liczby=list(range(1,7))

with open("plik.csv","w") as plik:
    plik.write(naglowek+"\n")
    for liczba in liczby:
        plik.write(str(liczba)+";"+str(liczba*2)+";"+str(liczba*3)+";"+str(liczba*4)+";"+str(liczba*5)+";"+str(liczba*6)+"\n")