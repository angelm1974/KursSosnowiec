class Pies():
    def __init__(self):
        self.dlugosc :float = 0
        self.smak :str=""
        self.rasa :str=""
        self.waga :float=0
        self.stan_skupienia :str =""
        self.kolor_siersci :str ="black"
        self.poziom_agresji :int =0
        self.poziom_zadowolenia :int =0
        self.zdjecie :str =""
        self.ilosc=0
    
    def gryz():
        pass
    
    def jedz(self, ilosc :float):
        self.waga += ilosc
    
    def szczekaj(self):
        print(30 * "Hau!!! ")
    
    def wydalaj(self, ilosc :float):
        self.waga -= ilosc      