''' Spletni vmesnik bo narejen s pomočjo knjižnice bottle '''

import bottle

from model import Vektor, Matrika, Permutacija, identiteta, ali_je_stohasticen, sn


def izrisi_vektor(vektor):
    v = vektor.split(' ')
    v = [float(e) for e in v]
    return Vektor(v)

def prepoznaj_matriko(matrika):
    matrika = matrika.split("\n")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [float(x) for x in vrstica]
        matrika1.append(vrstica)
    return Matrika(matrika1)


def izrise_permutacijo(permutacijia):
    v = permutacijia.split(' ')
    v = v = [float(e) for e in v]
    sl = set()
    for i in range(len(v)):
        sl.add(i)
        sl[i] = v[i]
    return sl

# Izriše začetno stran

@bottle.get("/")
def main_page():
    return bottle.template('osnovnastran.html')

@bottle.get("/sestevanjem")
def sestevanjem():
    return bottle.template("operacijem.html", operacija="/sestejm", operator="+", operiraj="SEŠTEJ")

@bottle.post("/sestejm")
def sestejm():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    vsota = matrika1 + matrika2
    return bottle.template("resitev.html", rezultat=vsota)

@bottle.get("/odstevanjem")
def odstevanjem():
    return bottle.template("operacijem.html", operacija="/odstejm", operator="-", operiraj="ODŠTEJ")

@bottle.post("/odstejm")
def odstejm():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    razlika = matrika1 - matrika2
    return bottle.template("resitev.html", rezultat=razlika)

@bottle.get("/izenacim")
def izenacim():
    return bottle.template("operacijem.html", operacija="/izenacimm", operator="=", operiraj="IZENAČI")

@bottle.post("/izenacimm")
def izenacimm():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    if matrika1 == matrika2:
        return bottle.template("enakost.html", rezultat='sta')
    else:
        return bottle.template("enakost.html", rezultat='nista')

@bottle.get("/primerjam")
def primerjam():
    return bottle.template("operacijem.html", operacija="/primerjajm", operator=">", operiraj="PRIMERJAM")

@bottle.post("/primerjajm")
def primerjajm():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    if matrika1 < matrika2:
        return bottle.template("primerjavam.html", rezultat='je večja')
    else:
        return bottle.template("primerjavam.html", rezultat='ni večja')

@bottle.get("/slede")
def sledenje():
    return bottle.template("enojnematrike.html", operacija="/sled", izracunaj="sled")

@bottle.post("/sled")
def sled():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    sled = matrika.sled()
    return bottle.template("resitev.html", rezultat=sled)

@bottle.get("/determiniranje")
def determiniranje():
    return bottle.template("enojnematrike.html", operacija="/determinanta", izracunaj="determinanta")

@bottle.post("/determinanta")
def determinanta():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    det = matrika.determinante()
    return bottle.template("resitev.html", rezultat=det)

@bottle.get("/transponiranje")
def transponiranje():
    return bottle.template("enojnematrike.html", operacija="/transponiranka", izracunaj="TRANSPONIRAJ")

@bottle.post("/transponiranka")
def transponiranka():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    rezultat = matrika.transponiranje()
    return bottle.template("resitev.html", rezultat=rezultat)

@bottle.get("/produkt")
def produkt():
    return bottle.template("operacijem.html", operacija="/produktm", operator="*", operiraj="zmnoži")

@bottle.post("/produktm")
def prouktm():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    product = matrika1 * matrika2
    return bottle.template("resitev.html", rezultat=product)

@bottle.get("/power")
def power():
    return bottle.template("eksponent.html", operacija="/potenciraj", izracunaj="potneca!")

@bottle.post("/potenciraj")
def potenciraj():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    ep = bottle.request.forms["eksponent"]
    rezultat = matrika ** ep
    return bottle.template("resitev.html", rezultat=rezultat)

@bottle.get("/inverz")
def inverz():
    return bottle.template("enojnematrike.html", operacija="/inverzm", izracunaj="inverz")

@bottle.post("/inverzm")
def inverzm():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    inverzz = matrika.inverz()
    return bottle.template("resitev.html", rezultat=inverzz)

@bottle.get("/psevdoinverz")
def psevdoinverz():
    return bottle.template("enojnematrike.html", operacija="/psevdoinverzm", izracunaj="psevdoinverz")

@bottle.post("/psevdoinverzm")
def psevdoinverzm():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    psevdoinverzz = matrika.psevdoinverz()
    return bottle.template("resitev.html", rezultat=psevdoinverzz)

@bottle.get("/sistem")
def sistem():
    return bottle.template("sistemm.html", operacija="/sistemi", operiraj="resi sitem")


@bottle.post("/sistemi")
def sistemi():
    matrika_besedilo = bottle.request.forms["matrika"]
    vektor_besedilo = bottle.request.forms["vektor"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    vektor = izrisi_vektor(vektor_besedilo)
    sol = matrika.cramerjevo_pravilo(vektor)
    return bottle.template("resitev.html", rezultat=sol)

@bottle.get("/dvojnostohasticna")
def dvojnostohasticna():
    return bottle.template("enojnematrike.html", operacija="/dvojnostohasticnam", izracunaj="dvojna stohastičnost")

@bottle.post("/dvojnostohasticnam")
def dvojnostohasticnam():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    dvojno = matrika.stohasticna_matrika()
    if dvojno:
        return bottle.template("last.html", lastnost="je dvojnosohastična")
    else:
        return bottle.template("last.html", lastnost="ni dvojnosohastična")

@bottle.get("/permutacijskaa")
def permutacijskaa():
    return bottle.template("enojnematrike.html", operacija="/permutacijskam", izracunaj="permutacija?")

@bottle.post("/permutacijskam")
def permutacijskam():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    per = matrika.permutacijska()
    if per:
        return bottle.template("last.html", lastnost="je permutacijska")
    else:
        return bottle.template("last.html", lastnost="ni permutacijska")

@bottle.get("/nenegativnost")
def nenegativnost():
    return bottle.template("enojnematrike.html", operacija="/nenegativnostm", izracunaj="nenegativna?")

@bottle.post("/nenegativnostm")
def nenegativnostm():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    neneg = matrika.nenegativna()
    if neneg:
        return bottle.template("last.html", lastnost="je nenegativna")
    else:
        return bottle.template("last.html", lastnost="ni nenegativna")

@bottle.get("/reduciabilnost")
def reduciabilnost():
    return bottle.template("enojnematrike.html", operacija="/reduciabilnostm", izracunaj="reduciabilna?")

@bottle.post("/reduciabilnostm")
def reduciabilnostm():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    red = matrika.reduciabilnost()
    if red:
        return bottle.template("last.html", lastnost="je reduciabilna")
    else:
        return bottle.template("last.html", lastnost="ni reduciabilna")

@bottle.get("/normalnost")
def normalnost():
    return bottle.template("enojnematrike.html", operacija="/normalnostm", izracunaj="unitaren?")

@bottle.post("/normalnostm")
def normalnostm():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    nor = matrika.normalnost_opratorja()
    if nor:
        return bottle.template("last.html", lastnost="je normalna")
    else:
        return bottle.template("last.html", lastnost="ni normalna")

@bottle.get("/unitarnost")
def ortogonalnost():
    return bottle.template("enojnematrike.html", operacija="/unitarnostm", izracunaj="normalna?")

@bottle.post("/unitarnostm")
def unitarnostm():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    uni = matrika.unitarnost_operatorja()
    if uni:
        return bottle.template("last.html", lastnost="je uniteran operator")
    else:
        return bottle.template("last.html", lastnost="ni uniteren operator")

@bottle.get("/sebiadjugiranost")
def sebiadjugiranost():
    return bottle.template("enojnematrike.html", operacija="/sebiadjugiranostm", izracunaj="sebiadjugiran?")

@bottle.post("/sebiadjugiranostm")
def sebiadjugiranostm():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = prepoznaj_matriko(matrika_besedilo)
    sebi = matrika.sebiadjugiranost_operatorja()
    if sebi:
        return bottle.template("last.html", lastnost="je sebiadjugiran operator")
    else:
        return bottle.template("last.html", lastnost="ni sebiadjugiran operator")

bottle.run(reloader=True, debug=True)

'''
@bottle.get("/sestevanjev")
def sestevanjev():
    return bottle.template("operacijav.html", operacija="/sestejv", operator="+", operiraj="SEŠTEJ")

@bottle.post("/sestejv")
def sestejv():
    vektor1_besedilo = bottle.request.query["vektor1"]
    vektor2_besedilo = bottle.request.query["vektor2"]
    vektor1 = izrisi_vektor(vektor1_besedilo)
    vektor2 = izrisi_vektor(vektor2_besedilo)
    vsota = vektor1 + vektor2
    return bottle.template("resitev.html", rezultat=vsota)
'''