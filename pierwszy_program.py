lista_kolarzy=[]

kolarz = {
    'imie': '-',
    'nazwisko': '-',
    'numer_startowy': -1,
    'klub': '-',
    'wiek': -1,
    'kraj': '-',
    'rank': -1
}

def create_kolarz():
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    numer_startowy = int(input("Podaj numer startowy: "))
    klub = input("Podaj klub: ")
    wiek = int(input("Podaj wiek: "))
    kraj = input("Podaj kraj: ")
    rank = int(input("Podaj rank: "))

    kolarz = {
        'imie': imie,
        'nazwisko': nazwisko,
        'numer_startowy': numer_startowy,
        'klub': klub,
        'wiek': wiek,
        'kraj': kraj,
        'rank': rank
    }
    
    lista_kolarzy.append(kolarz)

def print_kolarz(kolarz):
    print("-"*20)
    print(f"|Imię: {kolarz['imie']}")
    print(f"|Nazwisko: {kolarz['nazwisko']}")
    print(f"|Numer startowy: {kolarz['numer_startowy']}")
    print(f"|Klub: {kolarz['klub']}")
    print(f"|Wiek: {kolarz['wiek']}")
    print(f"|Kraj: {kolarz['kraj']}")
    print(f"|Rank: {kolarz['rank']}")
    print("-"*20)
    
def print_kolarz2(kolarz):
    print(f"Mój kolarz ma imię: {kolarz['imie']}",end=", ")
    print(f"oraz nazywa się: {kolarz['nazwisko']}")
    
def read_kolarze():
    for wybrany_kolarz in lista_kolarzy:
        print_kolarz2(wybrany_kolarz)

def update(kolarz : dict)->dict:
    imie = input(f"Podaj imię ({kolarz["imie"]}): ")
    nazwisko = input(f"Podaj nazwisko ({kolarz["nazwisko"]}): ")
    klub = input(f"Podaj klub ({kolarz["klub"]}): ")
    wiek = int(input(f"Podaj wiek ({kolarz["wiek"]}): "))
    kraj = input(f"Podaj kraj ({kolarz["kraj"]}): ")
    rank = int(input(f"Podaj rank ({kolarz["rank"]}): "))

    if len(imie) > 0:
        kolarz['imie'] = imie
    if len(nazwisko) > 0:
        kolarz['nazwisko'] = nazwisko
    if len(klub) > 0:
        kolarz['klub'] = klub
    if wiek > 0:
        kolarz['wiek'] = wiek
    if len(kraj) > 0:
        kolarz['kraj'] = kraj
    if rank > 0: 
        kolarz['rank'] = rank
    return kolarz

def delete_kolarz(nr):
    lista_kolarzy.pop(nr)
    return lista_kolarzy

# nr = int(input(f"Podaj numer startowy: "))
# lista_kolarzy[nr]=update(lista_kolarzy[nr])
# print_kolarz(lista_kolarzy[nr])
# delete_kolarz(nr)