import json

class Covek:
    def __init__(self, ime, prezime):
        self.ime =ime
        self.prezime = prezime


    def predstavi_se(self):
        print(f"Zdrav, ja sam {self.ime} {self.prezime}.")


class Profesor(Covek):
    def __init__(self, ime, prezime, predmet):
        super().__init__(ime, prezime)
        self.predmet = predmet



    def predstavi_se(self):
        print(f"Dobar dan. Ja sam profesor {self.ime} {self.prezime} i predavacu predmet {self.predmet}.")



        

class Ucenik(Covek):
    def __init__(self, ime, prezime, ocena):
        super().__init__(ime, prezime)
        self.ocena = ocena


    def predstavi_se(self):
        print(f"Zdrava, ja sam ucenik {self.ime} {self.prezime} i moja ocena je {self.ocena}.")


    def da_li_je_ucenik_odlican(self):
        if self.ocena == 5:
            print(f"Ucenik {self.ime} {self.prezime} je odlican.")
        else:
            print(f"Ucenik {self.ime} {self.prezime} nije odlican.")


class Dnevnik:
    def __init__(self):
        self.lista_ucenika = []


    def dodaj_ucenika(self, ucenik_objekat):
        self.lista_ucenika.append(ucenik_objekat)
        print(f"Ucenik {ucenik_objekat.ime} {ucenik_objekat.prezime} je dodat u Dnevnik.")


    def prikazi_sve(self):
        print("\n--- SVI UČENICI U DNEVNIKU ---")
        for djak in self.lista_ucenika:
            djak.predstavi_se()


    def izracunaj_prosek(self):
        if not self.lista_ucenika:
            print("Dnevnik je prazan")
            return
            
        suma = 0
        for djak in self.lista_ucenika:
            suma += djak.ocena
        prosek = suma / len(self.lista_ucenika)
        print(f"Prosek odelenja je {prosek}") 


    def sacuvaj_u_fajl(self, class_ucenik="dnevnik.json"):
        # 1. Pretvaramo listu objekata u listu običnih rečnika
        podaci_za_cuvanje = []
        for djak in self.lista_ucenika:
            podaci_za_cuvanje.append({
                "ime": djak.ime,
                "prezime": djak.prezime,
                "ocena": djak.ocena
            })
        
        # 2. Upisujemo tu listu rečnika u fajl u JSON formatu
        with open("C:/Users/Marko/Desktop/class_ucenik.txt", "w", encoding="utf-8") as f:
            json.dump(podaci_za_cuvanje, f, indent=4, ensure_ascii=False)
        print(f"\nPodaci su uspešno sačuvani u fajl '{class_ucenik}'.")

    def ucitaj_iz_fajla(self, class_ucenik="dnevnik.json"):
        try:
            # 1. Otvaramo fajl i čitamo sirove podatke (rečnike)
            with open("C:/Users/Marko/Desktop/class_ucenik.txt", "r", encoding="utf-8") as f:
                podaci = json.load(f)
            
            # 2. Resetujemo trenutnu listu i ponovo pravimo prave OOP objekte
            self.lista_ucenika = []
            for djak_podaci in podaci:
                novi_djak = Ucenik(djak_podaci["ime"], djak_podaci["prezime"], djak_podaci["ocena"])
                self.lista_ucenika.append(novi_djak)
            print(f"Uspešno učitani podaci iz fajla. Broj učenika: {len(self.lista_ucenika)}")
            
        except FileNotFoundError:
            # Ako fajl još uvek ne postoji (prvo pokretanje), ne radimo ništa
            print("Fajl sa podacima nije pronađen. Kreće se od praznog dnevnika.")
   
            
             
             
moj_dnevnik = Dnevnik()

moj_dnevnik.ucitaj_iz_fajla()

print("-----Dobrodosli u skolski sistem-----")

while True:
    ime = input(f"Unesite ime ucenika (ili 'stop' za kraj): ")
    if ime.lower() == 'stop':
            break
    prezime = input(f"Unesite prezime ucenika: ")
    
    
    try:
        ocena = int(input(f"Unesite ocenu za ucenika {ime} {prezime}: "))
    except ValueError:
        print("Greska! Ocena mora biti broj. Pokusajte ponovo.") 
        continue
    if ocena < 1 or ocena > 5:
        print("Ocena mora biti izmedju 1 i 5.")
        continue
    novi_ucenik = Ucenik(ime,prezime, ocena)
    moj_dnevnik.dodaj_ucenika(novi_ucenik)


        

moj_dnevnik.prikazi_sve()
moj_dnevnik.izracunaj_prosek()
moj_dnevnik.sacuvaj_u_fajl()

print("\n-----Testiranje Polimorfizma-----")
profesor_matematike = Profesor("Dragan", "Petrovic", "Matematika")
obican_prolaznik = Covek("Nikola", "Simic")
if moj_dnevnik.lista_ucenika:
    test_ucenik = moj_dnevnik.lista_ucenika[0]
else:
    test_ucenik = Ucenik("Jelena", "Jankovic", 5)

skolski_kolektiv = [test_ucenik, profesor_matematike, obican_prolaznik]
for osoba in skolski_kolektiv:
    osoba.predstavi_se()    
