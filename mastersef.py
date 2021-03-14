import bottle
from datetime import datetime
from model import ZbirkaReceptov, Recept, Sestavina, Komentar

zbirka_receptov = ZbirkaReceptov(ime='Mastersef', datoteka='data/recepti.json')


@bottle.get('/')
def osnovna_stran():
    seznam_receptov = zbirka_receptov.recepti
    return bottle.template('views/prva.tpl', seznam_receptov=seznam_receptov)


@bottle.get('/recept/<st>')
def recept_stran(st):
    zbirka_receptov.odpri_recept(st)
    recept = zbirka_receptov.trenutni_recept
    return bottle.template('views/recept.tpl', recept=recept)


@bottle.post('/glasuj/<st>')
def glasuj(st):
    zbirka_receptov.glasuj_za_recept(st)
    bottle.redirect('/recept/' + st)


@bottle.get('/dodaj')
def dodaj_stran():
    napaka = 0
    return bottle.template('views/nov_recept.tpl', napaka=napaka)


@bottle.post('/dodaj/')
def nov_recept():
    naslov_recepta = bottle.request.forms.getunicode('naslov_recepta')
    seznam_sestavin = list()
    for sestavina in bottle.request.forms.getunicode('seznam_sestavin').split('\n'):
        seznam_sestavin.append(Sestavina(sestavina.rstrip()))
    cas_priprave = bottle.request.forms.getunicode('cas_priprave')
    kalorijska_vrednost = 0
    pogoj_kalorijski = bottle.request.forms.getunicode('kalorijska_vrednost')
    if pogoj_kalorijski and pogoj_kalorijski.isdigit():
        kalorijska_vrednost = int(pogoj_kalorijski)
    navodila = bottle.request.forms.getunicode('navodila')
    povezava_slike = bottle.request.forms.get('povezava_slike')
    indeks_recepta = 0
    for recept in zbirka_receptov.recepti:
        if int(recept.indeks_recepta) > indeks_recepta:
            indeks_recepta = int(recept.indeks_recepta)
    indeks_recepta += 1
    zbirka_receptov.dodaj_recept(naslov_recepta, seznam_sestavin,
                                 cas_priprave, kalorijska_vrednost, navodila, str(indeks_recepta), povezava_slike)
    bottle.redirect('/')


@bottle.get('/<key>')
def sortirano(key):
    seznam_receptov = zbirka_receptov.recepti
    if key == 'h':
        seznam_receptov = sorted(
            zbirka_receptov.recepti, key=lambda x: x.cas_priprave, reverse=True)
    elif key == 'k':
        seznam_receptov = sorted(
            zbirka_receptov.recepti, key=lambda x: x.kalorijska_vrednost, reverse=False)
    elif key == 'g':
        seznam_receptov = sorted(
            zbirka_receptov.recepti, key=lambda x: len(x.glasovi), reverse=True)
    return bottle.template('views/prva.tpl', seznam_receptov=seznam_receptov)


@bottle.post('/recept')
def objavi_komentar():
    ime = bottle.request.forms.getunicode('komentator')
    besedilo = bottle.request.forms.getunicode('komentar')
    zbirka_receptov.trenutni_recept.dodaj_komentar(ime, besedilo)
    bottle.redirect(
        '/recept/' + zbirka_receptov.trenutni_recept.indeks_recepta)


bottle.run(debug=True, reloader=True)

