import urllib.parse as us
import requests as rq
import json

def pobierz_lat_lon(miasto):
    adres="https://nominatim.openstreetmap.org/search"
    wynik=rq.get(adres, params={"q":miasto, "format":"json"}).json()

    return [float(wynik[0]["lat"]), float(wynik[0]["lon"])]    



