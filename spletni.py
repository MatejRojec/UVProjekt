''' Spletni vmesnik bo narejen s pomočjo knjižnice bottle '''

import bottle

from model import Vektor, Matrika, Permutacija, identiteta, ali_je_stohasticen, sn


def izrisi_vektor(vektor):
    v = vektor.split(' ')
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
    v = permutacijia.split(' ')
    v = v = [float(e) for e in v]
    sl = {}
    for i in range(1, int(len(v) + 1)):
        sl[i] = v[(i - 1)]
    return Permutacija(sl)

@bottle.get("/")
def main_page():
    return bottle.template('osnovnastran.html')

# MATRIKE

@bottle.get("/sestevanjem")
def sestevanjem():
    return bottle.template("operacijem.html", operacija="/sestejm", operator="+", operiraj="SEŠTEJ")

@bottle.post("/sestejm")
def sestejm():
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    vsota = matrika1 + matrika2
    return bottle.template("resitev.html", besedilo="Vsota matrik" , rezultat=vsota)

@bottle.get("/odstevanjem")
def odstevanjem():
    return bottle.template("operacijem.html", operacija="/odstejm", operator="-", operiraj="ODŠTEJ")

@bottle.post("/odstejm")
def odstejm():
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    razlika = matrika1 - matrika2
    return bottle.template("resitev.html", besedilo="Razlika matrik", rezultat=razlika)

@bottle.get("/izenacim")
def izenacim():
    return bottle.template("operacijem.html", operacija="/izenacimm", operator="=", operiraj="IZENAČI")

@bottle.post("/izenacimm")
def izenacimm():
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    if matrika1 == matrika2:
        return bottle.template("resitev.html",  besedilo="Matriki", rezultat='sta enaki')
    else:
        return bottle.template("resitev.html", besedilo="Matriki", rezultat='nista enaki')

@bottle.get("/primerjam")
def primerjam():
    return bottle.template("operacijem.html", operacija="/primerjajm", operator=">", operiraj="PRIMERJAM")

@bottle.post("/primerjajm")
def primerjajm():
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    if matrika1 < matrika2:
        return bottle.template("resitev.html",  besedilo="Prva matrika", rezultat='je večja od druge matrike')
    else:
        return bottle.template("resitev.html",  besedilo="Prva matrika", rezultat='ni večja od druge matrike')

@bottle.get("/slede")
def sledenje():
    return bottle.template("enojnematrike.html", operacija="/sled", izracunaj="sled")

@bottle.post("/sled")
def sled():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    sled = matrika.sled()
    return bottle.template("resitev.html", besedilo="Sled:", rezultat=sled)

@bottle.get("/determiniranje")
def determiniranje():
    return bottle.template("enojnematrike.html", operacija="/determinanta", izracunaj="determinanta")

@bottle.post("/determinanta")
def determinanta():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    det = matrika.determinante()
    return bottle.template("resitev.html", besedilo="Determinanta:", rezultat=det)

@bottle.get("/transponiranje")
def transponiranje():
    return bottle.template("enojnematrike.html", operacija="/transponiranka", izracunaj="TRANSPONIRAJ")

@bottle.post("/transponiranka")
def transponiranka():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    rezultat = matrika.transponiranje()
    return bottle.template("resitev.html", besedilo="Transponirana matrika:", rezultat=rezultat)

@bottle.get("/produkt")
def produkt():
    return bottle.template("operacijem.html", operacija="/produktm", operator="*", operiraj="zmnoži")

@bottle.post("/produktm")
def prouktm():
    matrika1r = bottle.request.forms["matrika1"]
    matrika2r = bottle.request.forms["matrika2"]
    matrika1 = izrisi_matriko(matrika1r)
    matrika2 = izrisi_matriko(matrika2r)
    product = matrika1 * matrika2
    return bottle.template("resitev.html", besedilo="Produkt matrik:", rezultat=product)

@bottle.get("/power")
def power():
    return bottle.template("eksponent.html", objekt="eksponent", operacija="/potenciraj", izracunaj="potneca!")

@bottle.post("/potenciraj")
def potenciraj():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    ep = bottle.request.forms["eksponent"]
    rezultat = matrika ** ep
    return bottle.template("resitev.html", besedilo="Potencirana matrika:", rezultat=rezultat)

@bottle.get("/inverz")
def inverz():
    return bottle.template("enojnematrike.html", operacija="/inverzm", izracunaj="inverz")

@bottle.post("/inverzm")
def inverzm():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    inverzz = matrika.inverz()
    return bottle.template("resitev.html", besedilo="Inverz matrike:", rezultat=inverzz)

@bottle.get("/psevdoinverz")
def psevdoinverz():
    return bottle.template("enojnematrike.html", operacija="/psevdoinverzm", izracunaj="psevdoinverz")

@bottle.post("/psevdoinverzm")
def psevdoinverzm():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    psevdoinverzz = matrika.psevdoinverz()
    return bottle.template("resitev.html", besedilo="Psevdoinverz matrike:", rezultat=psevdoinverzz)

@bottle.get("/sistem")
def sistem():
    return bottle.template("eksponent.html", objekt="vektor prostih členov", operacija="/sistemi", operiraj="resi sitem", izracunaj="reši")


@bottle.post("/sistemi")
def sistemi():
    matrikar = bottle.request.forms["matrika"]
    vektorr = bottle.request.forms["eksponent"]
    matrika = izrisi_matriko(matrikar)
    vektor = izrisi_vektor(vektorr)
    sol = matrika.cramerjevo_pravilo(vektor)
    return bottle.template("resitev.html", besedilo="Rešitev sistema", rezultat=sol)

@bottle.get("/dvojnostohasticna")
def dvojnostohasticna():
    return bottle.template("enojnematrike.html", operacija="/dvojnostohasticnam", izracunaj="dvojnastohastičnost")

@bottle.post("/dvojnostohasticnam")
def dvojnostohasticnam():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    dvojno = matrika.stohasticna_matrika()
    if dvojno:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je dvojnostohastična.')
    else:
        return bottle.template("last.html", lastnost="ni dvojnosohastična")

@bottle.get("/permutacijskaa")
def permutacijskaa():
    return bottle.template("enojnematrike.html", operacija="/permutacijskam", izracunaj="permutacija?")

@bottle.post("/permutacijskam")
def permutacijskam():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    per = matrika.permutacijska()
    if per:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je permutacijska.')
    else:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='ni permutacijska.')

@bottle.get("/nenegativnost")
def nenegativnost():
    return bottle.template("enojnematrike.html", operacija="/nenegativnostm", izracunaj="nenegativna?")

@bottle.post("/nenegativnostm")
def nenegativnostm():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    neneg = matrika.nenegativna()
    if neneg:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je nenegativna.')
    else:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='ni nenegativna.')

@bottle.get("/reduciabilnost")
def reduciabilnost():
    return bottle.template("enojnematrike.html", operacija="/reduciabilnostm", izracunaj="reduciabilna?")

@bottle.post("/reduciabilnostm")
def reduciabilnostm():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    red = matrika.reduciabilnost()
    if red:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='je reduciabilna..')
    else:
        return bottle.template("resitev.html",  besedilo="Matrika", rezultat='ni reduciabilna.')

@bottle.get("/normalnost")
def normalnost():
    return bottle.template("enojnematrike.html", operacija="/normalnostm", izracunaj="normalen?")

@bottle.post("/normalnostm")
def normalnostm():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    nor = matrika.normalnost_opratorja()
    if nor:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='je normalnen.')
    else:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='ni normalnen.')

@bottle.get("/unitarnost")
def ortogonalnost():
    return bottle.template("enojnematrike.html", operacija="/unitarnostm", izracunaj="normalna?")

@bottle.post("/unitarnostm")
def unitarnostm():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    uni = matrika.unitarnost_operatorja()
    if uni:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='je unitaren.')
    else:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='ni unitaren.')

@bottle.get("/sebiadjugiranost")
def sebiadjugiranost():
    return bottle.template("enojnematrike.html", operacija="/sebiadjugiranostm", izracunaj="sebiadjugiran?")

@bottle.post("/sebiadjugiranostm")
def sebiadjugiranostm():
    matrikar = bottle.request.forms["matrika"]
    matrika = izrisi_matriko(matrikar)
    sebi = matrika.sebiadjugiranost_operatorja()
    if sebi:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='je sebiadjugiran.')
    else:
        return bottle.template("resitev.html",  besedilo="Operator", rezultat='ni sebiadjugiran.')

# VEKTORJI

@bottle.get("/sestevanjev")
def sestevanjev():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/sestejv", operator="+", operiraj="SEŠTEJ")

@bottle.post("/sestejv")
def sestejv():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    vsota = vektor1 + vektor2
    return bottle.template("resitev.html", besedilo="Vsota vektorjev:", rezultat=vsota)

@bottle.get("/odstevanjev")
def odstevanjev():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/odstevanjevv", operator="-", operiraj="odstej")

@bottle.post("/odstevanjevv")
def odstevanjevv():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    razlika = vektor1 - vektor2
    return bottle.template("resitev.html", besedilo="Razlika matrik", rezultat=razlika)

@bottle.get("/izenaciv")
def izenaciv():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/izenacivv", operator="=", operiraj="izenači")

@bottle.post("/izenacivv")
def izenacivv():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    if vektor1 == vektor2:
        return bottle.template("resitev.html", besedilo="Vektorja", rezultat="sta enaka!")
    else:
        return bottle.template("resitev.html", besedilo="Vektorja", rezultat="nista enaka")

@bottle.get("/primerjajv")
def primerjajv():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/primerjajvv", operator=">", operiraj="primerjaj")

@bottle.post("/primerjajvv")
def primerjajvv():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    if vektor1 > vektor2:
        return bottle.template("resitev.html", besedilo="Prvi vektor", rezultat="je večji od drugega vektorja")
    else:
        return bottle.template("resitev.html", besedilo="Razlika matrik", rezultat="ni večji od drugega vektorja")

@bottle.get("/norm")
def norm():
    return bottle.template("enojnivektor.html", ime="vektor", operacija="/normm", izracunaj="norma")

@bottle.post("/normm")
def normm():
    vektorr = bottle.request.forms["vektor"]
    vektor = izrisi_vektor(vektorr)
    normaa = vektor.norma()
    return bottle.template("resitev.html", besedilo="Norma:", rezultat=normaa)

@bottle.get("/skalarniprodukt")
def skalarniprodukt():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/skalarniproduktv", operator="*", operiraj="skalarno zmnoži")

@bottle.post("/skalarniproduktv")
def skalarniproduktv():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    sp = vektor1.skalarni_produkt(vektor2)
    return bottle.template("resitev.html", besedilo="Skalarni produkt:", rezultat=sp) 

@bottle.get("/kot")
def kot():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/kotv", operator="", operiraj="izračunaj kot")

@bottle.post("/kotv")
def kotv():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    k = vektor1.kot(vektor2)
    return bottle.template("resitev.html", besedilo="Kot:", rezultat=k)

@bottle.get("/vektorskiprodukt")
def vektorskiprodukt():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/vektorskiproduktv", operator="", operiraj="vektorsko množi")

@bottle.post("/vektorskiproduktv")
def vektorskiproduktv():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    vp = vektor1.vektorski_produkt(vektor2)
    return bottle.template("resitev.html", besedilo="Vektorski produkt:", rezultat=vp)

@bottle.get("/ploscinaparlalograma")
def ploscinaparlalograma():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/ploscinaparlalogramav", operator="", operiraj="ploscina paralelograma")

@bottle.post("/ploscinaparlalogramav")
def ploscinaparlalogramav():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    pp = abs(vektor1.ploščina_paralelograma(vektor2))
    return bottle.template("resitev.html", besedilo="Ploščina paralelograma:", rezultat=pp)

@bottle.get("/volumenparalelopipeda")
def volumenparalelopipeda():
    return bottle.template("trivektorji.html", objekt1="prvi vektor", objekt2="drugi vektor", objekt3="tretji vektor", operacija="/volumenparalelopipedav", operator="", operiraj="volumen paralelopipeda")

@bottle.post("/volumenparalelopipedav")
def volumenparalelopipedav():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor3r = bottle.request.forms["vektor3"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    vektor3 = izrisi_vektor(vektor3r)
    vop = abs(vektor1.volumen_paralelepipeda(vektor2, vektor3))
    return bottle.template("resitev.html", besedilo="Velumen paralelopipeda:", rezultat=vop) 

@bottle.get("/volumenpiramide")
def volumenpiramide():
    return bottle.template("trivektorji.html", objekt1="prvi vektor", objekt2="drugi vektor", objekt3="tretji vektor", operacija="/volumenpiramidev", operator="", operiraj="volumen piramide")

@bottle.post("/volumenpiramidev")
def volumenpiramidev():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor3r = bottle.request.forms["vektor3"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    vektor3 = izrisi_vektor(vektor3r)
    volp = vektor1.volumen_piramide(vektor2, vektor3)
    return bottle.template("resitev.html", besedilo="Volumen piramide:", rezultat=volp) 

@bottle.get("/enacbapremice")
def enacbapremice():
    return bottle.template("operacijav.html", prvi="prvi vektor" , drugi="drugi vektor", operacija="/enacbapremicev", operator="", operiraj="Enačba:")

@bottle.post("/enacbapremicev")
def enacbapremicev():
    vektor1r = bottle.request.forms["vektor1"]
    vektor2r = bottle.request.forms["vektor2"]
    vektor1 = izrisi_vektor(vektor1r)
    vektor2 = izrisi_vektor(vektor2r)
    ep = vektor1.enacba_premice(vektor2)
    return bottle.template("resitev.html", besedilo="Enačba premice:", rezultat=ep) 

# PERMUTACIJE

@bottle.get("/preverjanjepermutacije")
def preverjanjepermutacije():
    return bottle.template("enojnivektor.html", ime="permutacijo", operacija="/preverjanjepermutacijep", izracunaj="permutacija?")

@bottle.post("/preverjanjepermutacijep")
def preverjanjepermutacijep():
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    lx = permutacija.preverjanje_permutacije()
    if lx:
        return bottle.template("resitev.html", besedilo="Zapis je", rezultat="permutacija.")
    else:
        return bottle.template("resitev.html", besedilo="Zapis ni", rezultat="permutacija")

@bottle.get("/enkratnaslikapermutacije")
def enkratnaslikapermutacije():
    return bottle.template("operacijav.html", prvi="permutacijo" , drugi="element, ki ga slikamo:", operator="", operacija="/enkratnaslikapermutacijep", operiraj="slika")

@bottle.post("/enkratnaslikapermutacijep")
def enkratnaslikapermutacijep():
    permutacijar = bottle.request.forms["vektor1"]
    epb = bottle.request.forms["vektor2"]
    permutacija = izrisi_permutacijo(permutacijar)
    el = permutacija.enkratna_slika_permutacije(epb)
    return bottle.template("resitev.html", besedilo="Slika elementa:", rezultat=el)

@bottle.get("/veckratnaslikapermutacije")
def veckratnaslikapermutacije():
    return bottle.template("trivektorji.html", objekt1="prvo permutacijo", objekt2="element, ki ga slikamo", 
            objekt3="kolikokrat slikamo element", operacija="/veckratnaslikapermutacijep", operator="", operiraj="slikanje")

@bottle.post("/veckratnaslikapermutacijep")
def veckratnaslikapermutacijep():
    permutacijar = bottle.request.forms["vektor1"]
    epb = bottle.request.forms["vektor2"]
    vb = bottle.request.forms["vektor3"]
    permutacija = izrisi_permutacijo(permutacijar)
    el = permutacija.veckratno_slikanje_permutacije(epb, vb)
    return bottle.template("resitev.html", besedilo="Slike elementov:", rezultat=el)

@bottle.get("/elemntpoveckrantenemslikanjupermutacije")
def elemntpoveckrantenemslikanjupermutacije():
    return bottle.template("trivektorji.html", objekt1="prvo permutacijo", objekt2="element, ki ga slikamo", 
            objekt3="kolikokrat slikamo element", operacija="/elemntpoveckrantenemslikanjupermutacijep", operator="", operiraj="slikaj")

@bottle.post("/elemntpoveckrantenemslikanjupermutacijep")
def elemntpoveckrantenemslikanjupermutacijep():
    permutacijar = bottle.request.forms["vektor1"]
    epb = bottle.request.forms["vektor2"]
    vb = bottle.request.forms["vektor3"]
    permutacija = izrisi_permutacijo(permutacijar)
    el = permutacija.veckratna_slika_permutacije(epb, vb)
    return bottle.template("resitev.html", besedilo="Element po večkratnem slikanju:", rezultat=el)

@bottle.get("/snn")
def snn():
    return bottle.template("enojnivektor.html", ime="naravno število, za katero želiš množico bijektivnih preslikav", operacija="/snp", izracunaj="Bijekcije")

@bottle.post("/snp")
def snp():
    vb = bottle.request.forms["vektor"]
    el = sn(vb)
    return bottle.template("resitev.html", besedilo="Množica bijektivnih preslikav", rezultat=el)

@bottle.get("/cikel")
def cikel():
    return bottle.template("operacijav.html", prvi="permutacijo" , drugi="element, s katerim se cikel začne", operator="", operacija="/cikelp", operiraj="Cikel")

@bottle.post("/cikelp")
def cikelp():
    permutacijar = bottle.request.forms["vektor1"]
    epb = bottle.request.forms["vektor2"]
    permutacija = izrisi_permutacijo(permutacijar)
    el = permutacija.cikel_v_permutaciji(epb)
    return bottle.template("resitev.html", besedilo="Cikel:", rezultat=el)

@bottle.get("/cikli")
def cikli():
    return bottle.template("enojnivektor.html", ime="Vpiši permutacijo", operacija="/ciklip", izracunaj="Cikli")


@bottle.post("/ciklip")
def ciklip():
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    el = permutacija.cikli_v_permutaciji()
    return bottle.template("resitev.html", besedilo="Cikli:", rezultat=el)

@bottle.get("/inverzz")
def inverzz():
    return bottle.template("enojnivektor.html", ime="Vpiši permutacijo", operacija="/inverzp", izracunaj="Inverz")


@bottle.post("/inverzp")
def inverzp():
    permutacijar = bottle.request.forms["vektor"]
    permutacija = izrisi_permutacijo(permutacijar)
    el = permutacija.inverz()
    return bottle.template("resitev.html", besedilo="Inverz:", rezultat=el)

@bottle.get("/produktp")
def produktp():
    return bottle.template("operacijav.html", prvi="permutacijo" , drugi="permutacijo", operator="*", operacija="/produktpp", operiraj="Produkt")

@bottle.post("/produktpp")
def produktpp():
    permutacijar1 = bottle.request.forms["vektor1"]
    permutacijar2 = bottle.request.forms["vektor2"]
    permutacija1 = izrisi_permutacijo(permutacijar1)
    permutacija2 = izrisi_permutacijo(permutacijar2)
    pr = permutacija1 * permutacija2
    return bottle.template("resitev.html", besedilo="Produkt", rezultat=pr)


bottle.run(reloader=True, debug=True)

