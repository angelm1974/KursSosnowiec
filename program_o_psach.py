import pies
import customtkinter

jamnik=pies.Pies()
jamnik.dlugosc=40.5
jamnik.smak="słodko kwaśny"
jamnik.rasa="Jamnik krótkowłosy"
jamnik.waga=1.10
jamnik.stan_skupienia="stały"
jamnik.kolor_siersci="rudy"
jamnik.poziom_agresji=3
jamnik.poziom_zadowolenia=6
jamnik.zdjecie="images/jamnik.jpg"

# jamnik.jedz(2)
# jamnik.wydalaj(1)
# print(jamnik.waga)
# jamnik.szczekaj()



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app=customtkinter.CTk()
app.geometry("500x300")
label = customtkinter.CTkLabel(app, text="CTkLabel", fg_color="transparent")
label.pack(padx=20,pady=40)

def klikniecie():
    label.configure(text=f"kliknieto - {jamnik.ilosc} razy")
    jamnik.ilosc+=1
    
button= customtkinter.CTkButton(app,text="Przycisk1",command=klikniecie)
button.pack(padx=20,pady=30)
tekst=customtkinter.CTkEntry(app,placeholder_text="Podaj smak psa")
tekst.pack(padx=20,pady=30)

app.mainloop()


