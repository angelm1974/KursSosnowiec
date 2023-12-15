import requests as rq
import folium as fl
from folium.plugins import HeatMap
import lokacje as lk
adres="https://danepubliczne.imgw.pl/api/data/synop/"

pobrane=rq.get(adres)
pobrane.encoding="utf-8"
lista=pobrane.json()

lk.pobierz_miasta()
m = fl.Map(location=(51.75, 19.45), zoom_start=6, title="Polska")
for wiersz in lista:
    temp=float(wiersz["temperatura"])
    
        
    dane=lk.pobierz(wiersz["stacja"])

    # fl.Marker(
    #     location=dane,
    #     tooltip="Pokaż!",
    #     popup=f"miasto: {wiersz["stacja"]}, temperatura:  {wiersz["temperatura"]} ",
    #     icon=fl.Icon(color="blue"),
    # ).add_to(m)
HeatMap(lk.pobierz_miasta().values()).add_to(m)
m.show_in_browser()