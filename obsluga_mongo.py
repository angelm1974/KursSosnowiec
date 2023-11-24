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

def update_kolarza(kolarz):
    kolekcja_kolarze=baza.get_collection("kolarze")
    kolekcja_kolarze.update_one({"_id":kolarz.get("_id")}, {"$set":kolarz})

def wyszukaj_po_nr_startowym(nr_startowy):
    kolekcja_kolarze=baza.get_collection("kolarze")
    kolarz=kolekcja_kolarze.find_one({"numer_startowy":nr_startowy})
    return kolarz

# def dodaj_numer_startowy_inkrementacyjnie():
#     nr=1
#     kolekcja_kolarze=baza.get_collection("kolarze")
#     kolarze=kolekcja_kolarze.find()
#     for kolarz in kolarze:
#         kolarz["numer_startowy"]=nr
#         nr += 1
#         update_kolarza(kolarz)

kolarz={
    "imie":"Jan",
    "nazwisko":"Kowalski",
    "waga":80,
}
# dodaj_numer_startowy_inkrementacyjnie()
# kolarze=pobierz_kolarzy()
# for kolarz in kolarze:
#     print("parametry: ",kolarz.get("imię"), kolarz.get("nazwisko"), kolarz.get("waga")  )
# dodaj_kolarza(kolarz)
print(wyszukaj_po_nr_startowym(1))