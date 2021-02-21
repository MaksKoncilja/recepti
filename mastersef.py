import bottle
from datetime import datetime
from model import ZbirkaReceptov, Recept, Sestavina

zbirka_receptov = ZbirkaReceptov(ime='Mastersef', datoteka='recepti.json')

@bottle.get('/')
def osnovna_stran():
    recept = zbirka_receptov.trenutni_recept
    return bottle.template('osnovna_stran.tpl', recept=recept)

@bottle.post('/glasuj/')
def glasuj():
    indeks_recepta = int(bottle.request.forms['indeks_recepta'])
    zbirka_receptov.glasuj_za_recept(indeks_recepta)
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)

