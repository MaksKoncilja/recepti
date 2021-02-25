import bottle
from bottle import request
from datetime import datetime
from model import ZbirkaReceptov, Recept, Sestavina

zbirka_receptov = ZbirkaReceptov(ime='Mastersef', datoteka='data/recepti.json')

@bottle.get('/')
def osnovna_stran():
    seznam_receptov = zbirka_receptov.recepti
    return bottle.template('views/prva.tpl', seznam_receptov=seznam_receptov)


@bottle.get('/recept/<id>')
def recept_stran(id):
    zbirka_receptov.odpri_recept(id)
    recept = zbirka_receptov.trenutni_recept
    return bottle.template('views/recept.tpl', recept=recept)


@bottle.post('/glasuj/<id>')
def glasuj(id):
    zbirka_receptov.glasuj_za_recept(id)
    bottle.redirect('/recept/' + id)


@bottle.get('/dodaj')
def dodaj_stran():
    return bottle.template('views/nov_recept.tpl')


@bottle.post('/dodaj/')
def nov_recept():
    naslov_recepta = request.forms.get('naslov_recepta')
    print(naslov_recepta)
    #zbirka_receptov.dodaj_recept(res['naslov_recepta'])



bottle.run(debug=True, reloader=True)

