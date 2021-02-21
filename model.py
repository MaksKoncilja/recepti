import datetime
import json


class ZbirkaReceptov:
    def __init__(self, ime, datoteka):
        self.ime = ime
        self.datoteka = datoteka
        self.recepti = [
            Recept('Čokoladna torta', [
                Sestavina('mleko'),
                Sestavina('sol'),
                Sestavina('sladkor'),
            ],
            "3h", '150kal', 'zmešajte, počakaj, speci'),
            Recept('Palačinke' , [
                Sestavina('moka'),
                Sestavina('jajca'),
            ],
             "1h", '100kal', 'zmešaj, počakaj, speci'),
        ]            
        self.trenutni_recept = self.recepti[0]
        self.nalozi()
    
    def v_slovar(self):
        return {
            'recepti': [recept.v_slovar() for recept in self.recepti]
        }
    
    def iz_slovarja(self, slovar):
        pass

    def shrani(self):
        with open(self.datoteka, 'w', encoding='utf-8') as datoteka:
            json.dump(self.v_slovar(), datoteka)
    
    def nalozi(self):
        with open(self.datoteka, encoding='utf-8') as datoteka:
            self.iz_slovarja(json.load(datoteka))

    def odpri_recept(self, indeks_recepta):
        self.trenutni_recept = self.recepti[indeks_recepta]
        self.shrani()

    def zapri_trenutni_recept(self):
        self.trenutni_recept = None
        self.shrani()

    def glasuj_za_recept(self):
        self.trenutni_recept.glasuj()
        self.shrani()

    def dodaj_recept(self, naslov_recepta, seznam_sestavin, cas_priprave, kalorijska_vrednost, navodila):
        self.recepti.append(Recept(naslov_recepta, [Sestavina(odgovor) for odgovor in seznam_sestavin], cas_priprave, kalorijska_vrednost, navodila))
        self.shrani()

    def podvoji_recept(self, indeks_recepta):
        self.recepti.append(self.recepti[indeks_recepta].podvoji())
        self.shrani()


class Recept:
    def __init__(self, naslov_recepta, seznam_sestavin, cas_priprave, kalorijska_vrednost, navodila):
        self.naslov_recepta = naslov_recepta
        self.seznam_sestavin = seznam_sestavin
        self.cas_priprave = cas_priprave
        self.kalorijska_vrednost = kalorijska_vrednost
        self.navodila = navodila
        self.glasovi = []

    def glasuj(self):
         self.glasovi.append(Glas())

    def stevilo_glasov(self):
        return len(self.glasovi)

    def podvoji(self):
        return Recept(self.naslov_recepta, [sestavina.podvoji() for sestavina in self.seznam_sestavin],
        self.cas_priprave,
        self.kalorijska_vrednost,
        self.navodila)
    
    def v_slovar(self):
        return {
            'naslov recepta': self.naslov_recepta,
            'seznam sestavin': ['bla bla bla'],
            'čas priprave': self.cas_priprave,
            'kalorijska vrednost' : self.kalorijska_vrednost,
            'navodila': self.navodila
        }

class Sestavina:
    def __init__(self, besedilo):
        self.besedilo = besedilo

class Glas:
    def __init__(self):
        self.cas = datetime.datetime.now()