import urllib.parse as us
import requests as rq
import json
moje_miasta={}

def pobierz_miasta():
    global moje_miasta
    moje_miasta=pobierz_z_pliku_slownik_miast()
    return moje_miasta

def pobierz(miasto):
    klucze=moje_miasta.keys()
    print(list(klucze))
    if miasto in list(klucze):
        return moje_miasta[miasto]
    else:
        return pobierz_lat_lon(miasto)
    
def pobierz_lat_lon(miasto):
    adres="https://nominatim.openstreetmap.org/search"
    wynik=rq.get(adres, params={"q":miasto, "format":"json"}).json()
    moje_miasta[miasto]=[float(wynik[0]["lat"]), float(wynik[0]["lon"])]  
    zapisz_do_pliku_slownik_miast()
    return [float(wynik[0]["lat"]), float(wynik[0]["lon"])]    
    # return wynik

def pobierz_z_pliku_slownik_miast():
    with open("miasta.json", "r",encoding='utf-8') as plik:
        miasta=json.load(plik)
    return miasta

def zapisz_do_pliku_slownik_miast():
    with open("miasta.json", "w", encoding='utf-8') as plik:
        json.dump(moje_miasta, plik)



# w=pobierz_lat_lon("woj. łódzkie")
# print(w)