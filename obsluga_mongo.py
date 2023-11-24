import pymongo as pm

serwer_adres="mongodb+srv://student:HOdg80lm7WqGGG92@cluster0.cddpk.mongodb.net/?retryWrites=true&w=majority"
baza_danych="pierwsza_baza"
kolekcja="kolarze"

serwer=pm.MongoClient(serwer_adres)
baza=serwer.get_database(baza_danych)

def dodaj_kolarza(dane):
    kolekcja_kolarze=baza.get_collection("kolarze")
    kolekcja_kolarze.insert_one(dane)

def pobierz_kolarzy():
    kolekcja_kolarze=baza.get_collection("kolarze")
    kolarze=kolekcja_kolarze.find()
    return kolarze


kolarz={
    "imie":"Jan",
    "nazwisko":"Kowalski",
    "waga":80,
}

kolarze=pobierz_kolarzy()
for kolarz in kolarze:
    print(kolarz)
# dodaj_kolarza(kolarz)