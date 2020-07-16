''' Spletni vmesnik je narejen s pomočjo knjižnice bottle '''

import bottle
import random
from model import Zgodovina, Vektor, Matrika, Permutacija, identiteta, nicelna, ali_je_stohasticen, množica_bijektivnih_preslikav, list_kljucev

def izrisi_vektor(vektor):
    v = vektor.split()
    v = [float(e) for e in v]
    return Vektor(v)

def izrisi_matriko(matrika):
    matrika = matrika.split("\n")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [float(x) for x in vrstica]
        matrika1.append(vrstica)
    return Matrika(matrika1)


def izrisi_permutacijo(permutacijia):
    v = permutacijia.split()
    v = v = [float(e) for e in v]
    sl = {}
    for i in range(1, int(len(v) + 1)):
        sl[i] = v[(i - 1)]
    return Permutacija(sl)

zgodovine = {}

def zgodovina_uporabnika():
    st_uporabnika = bottle.request.get_cookie('st_uporabnika')
    if st_uporabnika is None:
        st_uporabnika = str(random.randint(0, 3 ** 140))
        zgodovine[st_uporabnika] = Zgodovina()
        bottle.response.set_cookie("st_uporabnika",  str(st_uporabnika), path='/')
    return zgodovine[st_uporabnika]


@bottle.get("/")
def main_page():
    return bottle.template('osnovnastran.html')

# VEKTORJI

@bottle.get("/sestevanjev")
def sestevanjev():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", 
            operacija="/sestejv", operator="+", operiraj="seštej")

@bottle.post("/sestejv")
def sestejv():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    vsota = vektor1 + vektor2
    return bottle.template("resitev.html", besedilo="Vsota vektorjev", rezultat=vsota)

@bottle.get("/odstevanjev")
def odstevanjev():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", 
            operacija="/odstevanjevv", operator="-", operiraj="odštej")

@bottle.post("/odstevanjevv")
def odstevanjevv():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    razlika = vektor1 - vektor2
    return bottle.template("resitev.html", besedilo="Razlika vektorjev", rezultat=razlika)

@bottle.get("/izenaciv")
def izenaciv():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", 
            operacija="/izenacivv", operator="=", operiraj="izenači")

@bottle.post("/izenacivv")
def izenacivv():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    if vektor1 == vektor2:
        return bottle.template("resitev.html", besedilo="Vektorja", rezultat="sta enaka!")
    else:
        return bottle.template("resitev.html", besedilo="Vektorja", rezultat="nista enaka!")

@bottle.get("/primerjajv")
def primerjajv():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", 
            operacija="/primerjajvv", operator=">", operiraj="primerjaj")

@bottle.post("/primerjajvv")
def primerjajvv():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    if vektor1 < vektor2:
        return bottle.template("resitev.html", besedilo="Prvi vektor", rezultat="ni večji od drugega vektorja!")
    else:
        return bottle.template("resitev.html", besedilo="Prvi vektor", rezultat="je večji od drugega vektorja!")

@bottle.get("/norm")
def norm():
    return bottle.template("enojnivektor.html", ime="vektor", operacija="/normm", izracunaj="dolžina")

@bottle.post("/normm")
def normm():
    zgodovina = zgodovina_uporabnika()
    vektorr = bottle.request.forms["vektor"]
    vektor = izrisi_vektor(vektorr)
    zgodovina.dodaj_vektor(vektor)
    normaa = vektor.norma()
    return bottle.template("resitev.html", besedilo="Norma:", rezultat=normaa)

@bottle.get("/skalarniprodukt")
def skalarniprodukt():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", 
            operacija="/skalarniproduktv", operator="*", operiraj="zmnoži")

@bottle.post("/skalarniproduktv")
def skalarniproduktv():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    sp = vektor1.skalarni_produkt(vektor2)
    return bottle.template("resitev.html", besedilo="Skalarni produkt:", rezultat=sp) 

@bottle.get("/kot")
def kot():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", 
            operacija="/kotv", operator="", operiraj="kot")

@bottle.post("/kotv")
def kotv():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    k = vektor1.kot(vektor2)
    return bottle.template("resitev.html", besedilo="Kot v stopinjah:", rezultat=k)

@bottle.get("/vektorskiprodukt")
def vektorskiprodukt():
    return bottle.template("operacijav.html", prvi="prvi vektor s tremi komponentami" , 
            drugi="drugi vektor s tremi komponentami", operacija="/vektorskiproduktv", operator="", operiraj="vektorsko")

@bottle.post("/vektorskiproduktv")
def vektorskiproduktv():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    vp = vektor1.vektorski_produkt(vektor2)
    return bottle.template("resitev.html", besedilo="Vektorski produkt", rezultat=vp)

@bottle.get("/ploscinaparlalograma")
def ploscinaparlalograma():
    return bottle.template("operacijav.html", prvi="prvi vektor s tremi komponentami" , drugi="drugi vektor s tremi komponentami", 
            operacija="/ploscinaparlalogramav", operator="", operiraj="ploščina")

@bottle.post("/ploscinaparlalogramav")
def ploscinaparlalogramav():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    pp = vektor1.ploščina_paralelograma(vektor2)
    return bottle.template("resitev.html", besedilo="Ploščina paralelograma:", rezultat=pp)

@bottle.get("/volumenparalelopipeda")
def volumenparalelopipeda():
    return bottle.template("trivektorji.html", objekt1="prvi vektor s tremi komponentami", objekt2="drugi vektor s tremi komponentami", 
            objekt3="tretji vektor s tremi komponentami", operacija="/volumenparalelopipedav", operator="", operiraj="volumen paralelopipeda")

@bottle.post("/volumenparalelopipedav")
def volumenparalelopipedav():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor3r = bottle.request.forms["vektor3"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    vektor3 = izrisi_vektor(vektor3r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    zgodovina.dodaj_vektor(vektor3)
    vop = vektor1.volumen_paralelepipeda(vektor2, vektor3)
    return bottle.template("resitev.html", besedilo="Volumen paralelopipeda:", rezultat=vop) 

@bottle.get("/volumenpiramide")
def volumenpiramide():
    return bottle.template("trivektorji.html", objekt1="prvi vektor s tremi komponentami", objekt2="drugi vektor s tremi komponentami", 
            objekt3="tretji vektor s tremi komponentami", operacija="/volumenpiramidev", operator="", operiraj="volumen piramide")

@bottle.post("/volumenpiramidev")
def volumenpiramidev():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor3r = bottle.request.forms["vektor3"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    vektor3 = izrisi_vektor(vektor3r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    zgodovina.dodaj_vektor(vektor3)
    volp = vektor1.volumen_piramide(vektor2, vektor3)
    return bottle.template("resitev.html", besedilo="Volumen piramide:", rezultat=volp) 

@bottle.get("/enacbapremice")
def enacbapremice():
    return bottle.template("operacijav.html", prvi="vektor s tremi komponentami" , 
            drugi="točko s tremi komponentami", operacija="/enacbapremicev", operator="", operiraj="enačba")

@bottle.post("/enacbapremicev")
def enacbapremicev():
    zgodovina = zgodovina_uporabnika()
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    zgodovina.dodaj_vektor(vektor1)
    zgodovina.dodaj_vektor(vektor2)
    ep = vektor1.enacba_premice(vektor2)
    return bottle.template("resitev.html", besedilo="Enačba premice:", rezultat=ep) 

# MATRIKE

@bottle.get("/sestevanjem")
def sestevanjem():
    return bottle.template("operacijem.html", operacija="/sestejm", operator="+", operiraj="seštej")

@bottle.post("/sestejm")
def sestejm():
    zgodovina = zgodovina_uporabnika()
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    zgodovina.dodaj_matriko(matrika1)
    zgodovina.dodaj_matriko(matrika2)
    vsota = matrika1 + matrika2
    return bottle.template("resitev.html", besedilo="Vsota matrik" , rezultat=vsota)

@bottle.get("/odstevanjem")
def odstevanjem():
    return bottle.template("operacijem.html", operacija="/odstejm", operator="-", operiraj="odštej")

@bottle.post("/odstejm")
def odstejm():
    zgodovina = zgodovina_uporabnika()
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    zgodovina.dodaj_matriko(matrika1)
    zgodovina.dodaj_matriko(matrika2)
    razlika = matrika1 - matrika2
    return bottle.template("resitev.html", besedilo="Razlika matrik", rezultat=razlika)

@bottle.get("/izenacim")
def izenacim():
    return bottle.template("operacijem.html", operacija="/izenacimm", operator="=", operiraj="izenači")

@bottle.post("/izenacimm")
def izenacimm():
    zgodovina = zgodovina_uporabnika()
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    zgodovina.dodaj_matriko(matrika1)
    zgodovina.dodaj_matriko(matrika2)
    if matrika1 == matrika2:
        return bottle.template("resitev.html",  besedilo="Matriki", rezultat="sta enaki")
    else:
        return bottle.template("resitev.html", besedilo="Matriki", rezultat="nista enaki")

@bottle.get("/primerjam")
def primerjam():
    return bottle.template("operacijem.html", operacija="/primerjajm", operator=">", operiraj="primerjaj")

@bottle.post("/primerjajm")
def primerjajm():
    zgodovina = zgodovina_uporabnika()
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    zgodovina.dodaj_matriko(matrika1)
    zgodovina.dodaj_matriko(matrika2)
    if matrika1 < matrika2:
        return bottle.template("resitev.html",  besedilo="Prva matrika", rezultat='je večja od druge matrike')
    else:
        return bottle.template("resitev.html",  besedilo="Prva matrika", rezultat='ni večja od druge matrike')

@bottle.get("/slede")
def sledenje():
    return bottle.template("enojnematrike.html", operacija="/sled", izracunaj="sled")

@bottle.post("/sled")
def sled():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    sled = matrika.sled()
    return bottle.template("resitev.html", besedilo="Sled:", rezultat=sled)

@bottle.get("/determiniranje")
def determiniranje():
    return bottle.template("enojnematrike.html", operacija="/determinanta", izracunaj="determinanta")

@bottle.post("/determinanta")
def determinanta():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    det = matrika.determinante()
    return bottle.template("resitev.html", besedilo="Determinanta:", rezultat=det)

@bottle.get("/transponiranje")
def transponiranje():
    return bottle.template("enojnematrike.html", operacija="/transponiranka", izracunaj="transponiraj")

@bottle.post("/transponiranka")
def transponiranka():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    rezultat = matrika.transponiranje()
    return bottle.template("resitev.html", besedilo="Transponirana matrika:", rezultat=rezultat)

@bottle.get("/produkt")
def produkt():
    return bottle.template("operacijem.html", operacija="/produktm", operator="*", operiraj="zmnoži")

@bottle.post("/produktm")
def prouktm():
    zgodovina = zgodovina_uporabnika()
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    zgodovina.dodaj_matriko(matrika1)
    zgodovina.dodaj_matriko(matrika2)
    product = matrika1 * matrika2
    return bottle.template("resitev.html", besedilo="Produkt matrik:", rezultat=product)

@bottle.get("/power")
def power():
    return bottle.template("eksponent.html", objekt="eksponent", operacija="/potenciraj", izracunaj="potneca")

@bottle.post("/potenciraj")
def potenciraj():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    ep = bottle.request.forms["eksponent"]
    rezultat = matrika ** ep
    return bottle.template("resitev.html", besedilo="Potencirana matrika:", rezultat=rezultat)

@bottle.get("/inverz")
def inverz():
    return bottle.template("enojnematrike.html", operacija="/inverzm", izracunaj="inverz")

@bottle.post("/inverzm")
def inverzm():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    inverzz = matrika.inverz()
    return bottle.template("resitev.html", besedilo="Inverz matrike:", rezultat=inverzz)

@bottle.get("/psevdoinverz")
def psevdoinverz():
    return bottle.template("enojnematrike.html", operacija="/psevdoinverzm", izracunaj="psevdoinverz")

@bottle.post("/psevdoinverzm")
def psevdoinverzm():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    psevdoinverzz = matrika.psevdoinverz()
    return bottle.template("resitev.html", besedilo="Psevdoinverz matrike:", rezultat=psevdoinverzz)

@bottle.get("/sistem")
def sistem():
    return bottle.template("eksponent.html", objekt="vektor prostih členov", 
            operacija="/sistemi", operiraj="resi sitem", izracunaj="reši")


@bottle.post("/sistemi")
def sistemi():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    vektorr = bottle.request.forms["eksponent"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    vektor = izrisi_vektor(vektorr)
    sol = matrika.cramerjevo_pravilo(vektor)
    return bottle.template("resitev.html", besedilo="Rešitev sistema", rezultat=sol)

@bottle.get("/dvojnostohasticna")
def dvojnostohasticna():
    return bottle.template("enojnematrike.html", operacija="/dvojnostohasticnam", izracunaj="dvojnastohastičnost")

@bottle.post("/dvojnostohasticnam")
def dvojnostohasticnam():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    dvojno = matrika.stohasticna_matrika()
    if dvojno:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je dvojnostohastična.')
    else:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='ni dvojnostohastična.')

@bottle.get("/permutacijskaa")
def permutacijskaa():
    return bottle.template("enojnematrike.html", operacija="/permutacijskam", izracunaj="permutacijska")

@bottle.post("/permutacijskam")
def permutacijskam():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    per = matrika.permutacijska()
    if per:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je permutacijska.')
    else:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='ni permutacijska.')

@bottle.get("/nenegativnost")
def nenegativnost():
    return bottle.template("enojnematrike.html", operacija="/nenegativnostm", izracunaj="nenegativna")

@bottle.post("/nenegativnostm")
def nenegativnostm():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    neneg = matrika.nenegativna()
    if neneg:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je nenegativna.')
    else:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='ni nenegativna.')

@bottle.get("/reduciabilnost")
def reduciabilnost():
    return bottle.template("enojnematrike.html", operacija="/reduciabilnostm", izracunaj="reduciabilna")

@bottle.post("/reduciabilnostm")
def reduciabilnostm():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    red = matrika.reduciabilnost()
    if red:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je reduciabilna..')
    else:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='ni reduciabilna.')

@bottle.get("/normalnost")
def normalnost():
    return bottle.template("enojnematrike.html", operacija="/normalnostm", izracunaj="normalen")

@bottle.post("/normalnostm")
def normalnostm():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    nor = matrika.normalnost_opratorja()
    if nor:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='je normalnen.')
    else:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='ni normalnen.')

@bottle.get("/unitarnost")
def unitarnost():
    return bottle.template("enojnematrike.html", operacija="/unitarnostm", izracunaj="unitaren")

@bottle.post("/unitarnostm")
def unitarnostm():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    uni = matrika.unitarnost_operatorja()
    if uni:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='je unitaren.')
    else:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='ni unitaren.')

@bottle.get("/sebiadjugiranost")
def sebiadjugiranost():
    return bottle.template("enojnematrike.html", operacija="/sebiadjugiranostm", izracunaj="sebiadjugiran")

@bottle.post("/sebiadjugiranostm")
def sebiadjugiranostm():
    zgodovina = zgodovina_uporabnika()
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    zgodovina.dodaj_matriko(matrika)
    sebi = matrika.sebiadjugiranost_operatorja()
    if sebi:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='je sebiadjugiran.')
    else:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='ni sebiadjugiran.')

# PERMUTACIJE

@bottle.get("/preverjanjepermutacije")
def preverjanjepermutacije():
    return bottle.template("enojnivektor.html", ime="permutacijo", 
            operacija="/preverjanjepermutacijep", izracunaj="permutacija?")

@bottle.post("/preverjanjepermutacijep")
def preverjanjepermutacijep():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    lx = permutacija.preverjanje_permutacije()
    if lx:
        return bottle.template("resitev.html", besedilo="Zapis je", rezultat="permutacija.")
    else:
        return bottle.template("resitev.html", besedilo="Zapis ni", rezultat="permutacija")

@bottle.get("/enkratnaslikapermutacije")
def enkratnaslikapermutacije():
    return bottle.template("operacijav.html", prvi="permutacijo" , drugi="element, ki ga slikamo:", 
            operator="", operacija="/enkratnaslikapermutacijep", operiraj="slika")

@bottle.post("/enkratnaslikapermutacijep")
def enkratnaslikapermutacijep():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor1"]
    epb = bottle.request.forms["vektor2"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    sl = permutacija.enkratna_slika_permutacije(epb)
    return bottle.template("resitev.html", besedilo="Slika elementa:", rezultat=sl)

@bottle.get("/elemntpoveckrantenemslikanjupermutacije")
def elemntpoveckrantenemslikanjupermutacije():
    return bottle.template("trivektorji.html", objekt1="prvo permutacijo", objekt2="element, ki ga slikamo", 
            objekt3="kolikokrat slikamo element", operacija="/elemntpoveckrantenemslikanjupermutacijep", operator="", operiraj="slika")

@bottle.post("/elemntpoveckrantenemslikanjupermutacijep")
def elemntpoveckrantenemslikanjupermutacijep():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor1"]
    epb = bottle.request.forms["vektor2"]
    vb = bottle.request.forms["vektor3"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    vsl = permutacija.veckratna_slika_permutacije(epb, vb)
    return bottle.template("resitev.html", besedilo="Element po večkratnem slikanju:", rezultat=vsl)

@bottle.get("/snn")
def snn():
    return bottle.template("enojnivektor.html", ime="naravno število, za katero želiš množico bijektivnih preslikav", 
            operacija="/snp", izracunaj="bijekcije")

@bottle.post("/snp")
def snp():
    v = bottle.request.forms["vektor"]
    mn = množica_bijektivnih_preslikav(v)
    return bottle.template("resitev.html", besedilo="Množica bijektivnih preslikav", rezultat=mn)

@bottle.get("/cikel")
def cikel():
    return bottle.template("operacijav.html", prvi="permutacijo" , drugi="element, s katerim se cikel začne", 
            operator="", operacija="/cikelp", operiraj="Cikel")

@bottle.post("/cikelp")
def cikelp():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor1"]
    epb = bottle.request.forms["vektor2"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    cik = permutacija.cikel_v_permutaciji(epb)
    return bottle.template("resitev.html", besedilo="Cikel:", rezultat=cik)

@bottle.get("/cikli")
def cikli():
    return bottle.template("enojnivektor.html", ime="Vpiši permutacijo", operacija="/ciklip", izracunaj="Cikli")


@bottle.post("/ciklip")
def ciklip():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    cikl = permutacija.cikli_v_permutaciji()
    return bottle.template("resitev.html", besedilo="Cikli:", rezultat=cikl)

@bottle.get("/inverzz")
def inverzz():
    return bottle.template("enojnivektor.html", ime="permutacijo", operacija="/inverzp", izracunaj="Inverz")

@bottle.post("/inverzp")
def inverzp():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    inv = permutacija.inverz()
    return bottle.template("resitev.html", besedilo="Inverz:", rezultat=inv)

@bottle.get("/produktp")
def produktp():
    return bottle.template("operacijav.html", prvi="permutacijo" , drugi="permutacijo", 
            operator="*", operacija="/produktpp", operiraj="Produkt")

@bottle.post("/produktpp")
def produktpp():
    zgodovina = zgodovina_uporabnika()
    permutacijar1 = bottle.request.forms["vektor1"]
    permutacijar2 = bottle.request.forms["vektor2"]
    permutacija1 = izrisi_permutacijo(permutacijar1)
    permutacija2 = izrisi_permutacijo(permutacijar2)
    zgodovina.dodaj_permutacijo(permutacija1)
    zgodovina.dodaj_permutacijo(permutacija2)
    pr = permutacija1 * permutacija2
    return bottle.template("resitev.html", besedilo="Produkt", rezultat=pr)

@bottle.get("/inverzije")
def inverzije():
    return bottle.template("enojnivektor.html", ime="Vpiši permutacijo", 
            operacija="/inverzijep", izracunaj="Inverzije")

@bottle.post("/inverzijep")
def inverzijep():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    stinverz = permutacija.inverzije()
    return bottle.template("resitev.html", besedilo="Inverzije:", rezultat=stinverz)

@bottle.get("/signatura")
def signatura():
    return bottle.template("enojnivektor.html", ime="Vpiši permutacijo", 
            operacija="/signaturap", izracunaj="signatura")

@bottle.post("/signaturap")
def signaturap():
    zgodovina = zgodovina_uporabnika()
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    zgodovina.dodaj_permutacijo(permutacija)
    sg = permutacija.signatura()
    return bottle.template("resitev.html", besedilo="Signatura:", rezultat=sg)

#ZGODOVINA

@bottle.get("/zgodovinamat")
def zgodovinamat():
    zgodovina = zgodovina_uporabnika()
    zgodovinamatrik = zgodovina.zgodovinamatrik()
    if len(zgodovinamatrik) == 0:
        return bottle.template("resitev.html", besedilo="Niste vpisali še nobene matrike", rezultat="")
    else:
        return bottle.template("resitev.html", besedilo="Zgodovina matrik:", rezultat=zgodovinamatrik)

@bottle.get("/zgodovinavek")
def zgodovinavek():
    zgodovina = zgodovina_uporabnika()
    zgodovinavek = zgodovina.zgodovinavektorjev()
    if len(zgodovinavek) == 0:
        return bottle.template("resitev.html", besedilo="Niste vpisali še nobenega vektorja", rezultat="")
    else:
        return bottle.template("resitev.html", besedilo="Zgodovina vektorjev:", rezultat=zgodovinavek)
    
@bottle.get("/zgodovinaper")
def zgodovinaper():
    zgodovina = zgodovina_uporabnika()
    zgodovinaper = zgodovina.zgodovinapermutacij()
    if len(zgodovinaper) == 0:
        return bottle.template("resitev.html", besedilo="Niste vpisali še nobene permutacije", rezultat="")
    else:
        return bottle.template("resitev.html", besedilo="Zgodovina permutacij:", rezultat=zgodovinaper)

bottle.run(reloader=True, debug=True)

