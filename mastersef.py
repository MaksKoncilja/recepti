import bottle
from datetime import datetime
from model import ZbirkaReceptov, Recept, Sestavina, Glas

zbirka_receptov = ZbirkaReceptov(ime='UVP 2018/19', datoteka='recepti.json')

@bottle.get('/')
def osnovna_stran():
    recept = zbirka_receptov.trenutni_recept
    return bottle.template('osnovna_stran.tpl', recept=recept)

@bottle.post('/glasuj/')
def glasuj():
    indeks_recepta = int(bottle.request.forms['indeks_recepta'])
    zbirka_receptov.glasuj(indeks_recepta)
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)

