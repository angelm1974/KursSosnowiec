# moj_tekst = 'jestem "dobry" z polskiego'
# i_to_jest_zmienna = 'To jest zmienna'

# duzy_tekst = '''
# Po pozytywnej rekomendacji Komisji nad sprawą
# pochylą się jeszcze unijni ministrowie, którzy
# ostatecznie muszą zaakceptować plan na Radzie
# 8 grudnia, ale i tu dyplomaci nie przewidują
# już trudności i pierwsze środki powinny
# pojawić się na polskim koncie na początku
# przyszłego roku — informował w poniedziałek TVN24.
# '''
# print(i_to_jest_zmienna)
# import datetime

# dzisiaj=datetime.datetime.now().strftime("%Y-%m-%d")
# zmienna=5
# sciezka=f"D:\\Dane\\{dzisiaj}"
# print(sciezka)
# l1 = 4
# l2 = 4
# wynik = l1 // l2
# print(wynik)

# tu_mieszka_henio=12,44,"Henio"

# x,y,nazwa=tu_mieszka_henio
# print(tu_mieszka_henio)

# PI=3.14
# PI=PI+2
# print(PI)
# pudelko=input("Podaj no swoje imię: ")
# pudelko1=input("Podaj no swoje nazwisko: ")
# try:
#     pudelko2=int(input("Podaj no swój wiek: "))
# except:
#     print("Wiek musi być liczbą palancie")
#     exit("Koniec programu")


# print(f"Nazywam się {pudelko} {pudelko1} i do 100 lat brakuje mi {100 - pudelko2}" )


# print(1,2,3,4,5,6,7,8,9,10,sep="; ",end=";\n")
# print(1,2,3,4,5,6,7,8,9,10,sep="; ",end="; ")

# print(4**2)

# zdanie = "Ola"
# zd2 = "ola"
# print(zd2  >  zdanie)
# lista_burakow=["Tomek"]
# lista_burakow.append("Tomek")
# lista_burakow.append("Kasia")
# lista_burakow[1]="Ola"
# lista_burakow.remove("Tomek")
# print(lista_burakow)
# first_list=[ 2, 3]
# second_list=[ 5, 6,2]
# full_list=["opel","fiat","bmw","mazda"]
# full_list.sort(key=len)
# full_list.copy()
# print(full_list)

# nowalista=full_list[0:2].copy()
# print(full_list)

# animals=["tygrys","lew","kot","pies","krowa","kura"]
# for bania in animals:

#     if bania=="tygrys":
#         print("To jest tygrys i jest niebezpieczny")
#     else:
#         print(bania)

import os
while True:
    os.system("cls")
    print(f'''Moje menu
          Wybierz opcję:
          1. Dodaj kolarza
          2. Wyświetl kolarzy
          3. Wyjdź z programu''')
    input_user = input("Wybierz opcję: ")
    
    if input_user == "1":
        print("Dodaję kolarza")
    elif input_user == "2":
        print("Wyświetlam kolarzy")
    elif input_user == "3":
        print("Wychodzę z programu")
        break
    input("Naciśnij enter aby kontynuować")