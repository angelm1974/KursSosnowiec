import requests as rq
import folium as fl
import lokacje as lk
adres="https://danepubliczne.imgw.pl/api/data/synop/"

pobrane=rq.get(adres)
pobrane.encoding="utf-8"
lista=pobrane.json()


m = fl.Map(location=(51.75, 19.45), zoom_start=6, title="Polska")
for wiersz in lista:
    temp=float(wiersz["temperatura"])
    if temp<0:
        
        dane=lk.pobierz_lat_lon(wiersz["stacja"])

        fl.Marker(
            location=dane,
            tooltip="Pokaż!",
            popup=f"miasto: {wiersz["stacja"]}, temperatura:  {wiersz["temperatura"]} ",
            icon=fl.Icon(color="blue"),
        ).add_to(m)

m.show_in_browser()