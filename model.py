import datetime
import json


class ZbirkaReceptov:
    def __init__(self, ime, datoteka):
        self.ime = ime
        self.datoteka = datoteka
        self.recepti = list()         
        self.trenutni_recept = None
        self.nalozi()
    
    def v_slovar(self):
        return {
            'recepti': [recept.v_slovar() for recept in self.recepti]
        }
    
    def iz_slovarja(self, slovar):
        self.recepti = [Recept(
            r['naslov recepta'], 
            [Sestavina(s) for s in r['seznam sestavin']], 
            r['čas priprave'], 
            r['kalorijska vrednost'], 
            r['navodila'], 
            r['indeks recepta'],
            r['glasovi'],
            [Komentar(k.split('|')[0], k.split('|')[1]) for k in r['komentarji']]
            ) for r in slovar['recepti']]

    def shrani(self):
        with open(self.datoteka, 'w', encoding="UTF-8") as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False)
    
    def nalozi(self):
        with open(self.datoteka, encoding="UTF-8") as datoteka:
            self.iz_slovarja(json.load(datoteka))

    def odpri_recept(self, indeks_recepta):
        for r in self.recepti:
            if r.indeks_recepta == indeks_recepta:
                self.trenutni_recept = r
                break
        self.shrani()

    def zapri_trenutni_recept(self):
        self.trenutni_recept = None
        self.shrani()

    def glasuj_za_recept(self, indeks_recepta):
        for r in self.recepti:
            if r.indeks_recepta == indeks_recepta:
                r.glasuj()
        self.shrani()

    def dodaj_recept(self, naslov_recepta, seznam_sestavin, cas_priprave, kalorijska_vrednost, navodila, indeks_recepta):
        self.recepti.append(Recept(naslov_recepta, seznam_sestavin, cas_priprave, kalorijska_vrednost, navodila, indeks_recepta, [], []))
        self.shrani()

    def podvoji_recept(self, indeks_recepta):
        self.recepti.append(self.recepti[indeks_recepta].podvoji())
        self.shrani()


class Recept:
    def __init__(self, naslov_recepta, seznam_sestavin, cas_priprave, kalorijska_vrednost, navodila, indeks_recepta, glasovi, komentarji):
        self.naslov_recepta = naslov_recepta
        self.seznam_sestavin = seznam_sestavin
        self.cas_priprave = cas_priprave
        self.kalorijska_vrednost = kalorijska_vrednost
        self.navodila = navodila
        self.indeks_recepta = indeks_recepta
        self.glasovi = glasovi
        self.komentarji = komentarji

    def glasuj(self):
         self.glasovi.append(datetime.datetime.now().strftime("%A, %d %b %Y"))

    def dodaj_komentar(self, ime, besedilo):
        self.komentarji.append(Komentar(ime, besedilo))
        print("OBJAVLJEN")

    def stevilo_glasov(self):
        return len(self.glasovi)

    def podvoji(self):
        return Recept(self.naslov_recepta, [sestavina.podvoji() for sestavina in self.seznam_sestavin],
        self.cas_priprave,
        self.kalorijska_vrednost,
        self.navodila,
        self.indeks_recepta,
        self.glasovi,
        self.komentarji)
    
    def v_slovar(self):
        return {
            'naslov recepta': self.naslov_recepta,
            'seznam sestavin': [x.besedilo for x in self.seznam_sestavin],
            'čas priprave': self.cas_priprave,
            'kalorijska vrednost' : self.kalorijska_vrednost,
            'navodila': self.navodila,
            'indeks recepta' : self.indeks_recepta,
            'glasovi': [g for g in self.glasovi],
            'komentarji' : [h.ime + "|" + h.besedilo for h in self.komentarji]
        }

class Sestavina:
    def __init__(self, besedilo):
        self.besedilo = besedilo

class Komentar: 
    def __init__(self, ime, besedilo):
        self.ime = ime
        self.besedilo = besedilo
