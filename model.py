''' Popravljena verzija '''

import math


# Class Zgodovina je namenjen konsistentmem beleženju vektorev, matrik in permutacij,
# ki jih je uporabnik vpisal (vsak uporabnik ima svoj dnevnik).

class Zgodovina:

    def __init__(self):
        self.zgodovina_matrik = []
        self.zgodovina_vektorjev = []
        self.zgodovina_permutacij = []

    def dodaj_permutacijo(self, permutacija):
        return self.zgodovina_permutacij.append(permutacija)
    
    def dodaj_matriko(self, matrika):
        return self.zgodovina_matrik.append(matrika)
    
    def dodaj_vektor(self, vektor):
        return self.zgodovina_vektorjev.append(vektor)

    def zgodovinamatrik(self):
        return self.zgodovina_matrik
    
    def zgodovinapermutacij(self):
        return self.zgodovina_permutacij
    
    def zgodovinavektorjev(self):
        return self.zgodovina_vektorjev

# Class Vektor je namenjen računanju z vektorji.

class Vektor:

    def __init__(self, vektor=[]):
        self.vektor = vektor
        self.stevilovrstic = len(self.vektor)

    def __repr__(self):
        return f'Vektor({self.vektor})'

    def  __str__(self):
        return f'{list(self.vektor)}'

    def __getitem__(self, i):
        return self.vektor[i]

    def __setitem__(self, i, l):
        self.vektor[i] = l
    
    def __len__(self):
        return self.stevilovrstic
    
    def __add__(self, other):
        if len(self) == len(other):
            nov_vektor = []
            n = len(self)
            for i in range(n):
                nov_vektor.append(self[i] + other[i])
            return Vektor(nov_vektor)
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da sešteti.")

    def __sub__(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            nov_vektor = []
            n = len(self)
            for i in range(n):
                nov_vektor.append(self[i] - other[i])
            return Vektor(nov_vektor)
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da odšteti.")

    def __eq__(self, other):
        return self.vektor == other.vektor

    def __lt__(self, other):
        if len(self) == len(other):
            n = len(self)
            for i in range(n):
                seznam = []
                if self.vektor[i] > other.vektor[i]:
                    seznam.append(False)
                else:
                    seznam.append(True)
            return all(seznam)
        else:
            raise Exception("Vektorjev različnih velikosti ne moremo primerjati.")

    def norma(self):
        norma = 0
        n = len(self)
        for i in range(n):
            norma += self[i] ** 2
        return norma
    
    def skalarni_produkt(self, other):
    # Govorimo o standardem skalarnem produktu v R^n po komponentah.
        if self.stevilovrstic == other.stevilovrstic:
            produkt = 0
            n = len(self)
            for i in range(n):
                produkt += self[i] * other[i]
            return produkt
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da skalarno zmožiti.")
     
    def mnozenje_vektorja_s_skalarjem(self, skalar):
        vektor = []
        n  = len(self)
        for i in range(n):
            vektor.append(skalar * self[i])
        return Vektor(vektor)
    
    def smo_v_treh_dimenzijah(self, other):
        return len(self) == 3 and len(other) == 3

    def vektorski_produkt(self, other):
        if self.smo_v_treh_dimenzijah(other):
            s = self
            o = other
            vektor = [None, None, None]
            vektor[0] = s[1] * o[2] - o[1] * s[2]
            vektor[1] = - s[0] * o[2] + o[0] * s[2]
            vektor[2] = s[0] * o[1] - o[0] * s[1]
            return Vektor(vektor)
        else: 
            raise Exception("Vektorja morata imeti tri komponente.")

    def kot(self, other):
        if self.norma() == 0 or other.norma() == 0:
            raise Exception("Vektorja morata biti neničelna.")
        else:
            kosinus_kota = self.skalarni_produkt(other) / (self.norma() * other.norma())
            radiani = math.acos(kosinus_kota)
            stopinje = radiani * 180 / math.pi
            return stopinje
    
    def ploščina_paralelograma(self, other):
    # Izračuna ploščino, ki ga omejujeta self.vektor in other.vektor . 
        if self.smo_v_treh_dimenzijah(other):
            kot = math.sin(self.kot(other) * math.pi / 180) 
            rezultat = kot * self.norma() * other.norma()
            return rezultat
        else:
            raise Exception("Vektorski morata imeti tri komponente.")

    def volumen_paralelepipeda(self, other, tretji):
    # Izračuna volumen paraleliepipeda, ki ga omejuje trije vektorji.
        if self.smo_v_treh_dimenzijah(other) and len(tretji) == 3:
            return self.ploščina_paralelograma(other) * tretji.norma()
        else:
            raise Exception("Vektorski morata imeti tri komponente.")

    def volumen_piramide(self, other, tretji):
        if self.smo_v_treh_dimenzijah(other) and len(tretji) == 3:
            return self.volumen_paralelepipeda(other, tretji) / 6
        else:
            raise Exception("Vektorski morata imeti tri komponente.")

    def enacba_premice(self, other):
    # Ennačna premice s smernim vekotrem self, ki gre skozi točko "other".
        if self.smo_v_treh_dimenzijah(other):
            return f'(x - {other[0]}) / {self[0]} = (y - {other[1]}) / {self[1]} = (z - {other[2]}) / {self[2]}'
        else:
            raise Exception("Vektor in točka morata imate oba 3 komponente")

# Class Matrika je namenjen računajnju z matrikami.

class Matrika:

    def __init__(self, matrika=[]):
        self.matrika = matrika
        self.stevilovrstic = len(matrika)
        self.stevilostolpcev = len(matrika[0])

    def __repr__(self):
        return f'Matrika({self.matrika})'

    def __str__(self):
        mat = ""
        for vrstica in self.matrika:
            mat += str(vrstica) + '\n'
        return mat
            
    def __getitem__(self, i):
        return self.matrika[i]

    def __len__(self):
        return self.stevilovrstic

    def __setitem__(self, i, l):
        self.matrika[i] = l

    def __add__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            vsota = []
            m = self.stevilovrstic
            n = self.stevilostolpcev
            for i in range(m):
                pomozna = []
                for j in range(n):
                    pomozna.append(self[i][j] + other[i][j])
                vsota.append(pomozna)
            return Matrika(vsota)
        else:
            raise Exception("Matriki se ne da sešteti, saj sta različnih velikosti.")

    def __sub__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            razlika = []
            m = self.stevilovrstic
            n = self.stevilostolpcev
            for i in range(m):
                pomozna = []
                for j in range(n):
                    pomozna.append(self[i][j] - other[i][j])
                razlika.append(pomozna)
            return Matrika(razlika)
        else:
            raise Exception("Matriki se ne da odšteti, saj sta različnih velikosti.")    

    def __eq__(self, other):
        return self.matrika == other.matrika

    def __lt__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            m = self.stevilovrstic
            n = self.stevilostolpcev
            for i in range(m):
                seznam = []
                for j in range(n):
                    if self[i][j] > other[i][j]:
                        seznam.append(True)
                    else:
                        seznam.append(False)
                return all(seznam)
        else:
            raise Exception("Matrik se ne da primerati, saj sta različnih velikostih")

    def __mul__(self, other):
    # Množenje s skalarjem
        if isinstance(other, (int, float)):
            produkt = []
            m = self.stevilovrstic
            n = self.stevilostolpcev
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self[i][j] * other)
                produkt.append(vrstica)
            return Matrika(produkt)

    # Množenje matrik 
        elif isinstance(other, Matrika):
            if self.stevilostolpcev == other.stevilovrstic:
                return Matrika( 
                [[sum(x * y for x,y in zip(self.stevilovrstic, other.stevilostolpcev)) 
                for other.stevilostolpcev in zip(*other)] for self.stevilovrstic in self])
            else:
                raise Exception("Matrik se ne more zmnožiti.")

    def kvadratna(self):
        return self.stevilostolpcev == self.stevilovrstic 

    def sled(self):
        if self.kvadratna():
            trace = 0
            n = self.stevilostolpcev
            for i in range(n):
                trace += self[i][i]
            return trace
        else:
            raise Exception("Sled je definirana le za kvadratne matrike.")
    
    def transponiranje(self):
        transponiranka = []
        m = self.stevilovrstic
        n = self.stevilostolpcev
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self[j][i])
            transponiranka.append(vrstica)
        return Matrika(transponiranka)

    def stohasticna_matrika(self):
        if not self.kvadratna():
            return False
        else:
            for vrstica in self.matrika:
                if not ali_je_stohasticen(vrstica):
                    return False
            for vrstica in self.transponiranje():
                if not ali_je_stohasticen(vrstica):
                    return False
            return True
    
    def determinante(self):
        if not self.kvadratna():
            raise Exception("Determinanta pravokotnih matrik ni definirana.")
        elif self.stevilovrstic == 1:
            return self[0][0]
        elif self.stevilovrstic == 2:
            determinanta = self[1][1] * self[0][0] - self[1][0] * self[0][1]
            return determinanta
        else:
            M = self.matrika
            determinanta = 0
            indeksi = list(range(self.stevilovrstic))
            for stolpci in indeksi:
                M2 = M
                M2 = M2[1:]
                visina = len(M2)
                for i in range(visina): 
                    M2[i] = M2[i][0:stolpci] + M2[i][stolpci+1:] 
                signatura = (-1) ** (stolpci % 2)
                M2 = Matrika(M2)
                determinantica = M2.determinante()
                determinanta += signatura * M[0][stolpci] * determinantica
            return determinanta
    
    def singularnost_matrike(self):
        return self.determinante() == 0

    def kofaktor(self, i, j):
        return Matrika([vrstica[:j] + vrstica[j+1:] for vrstica in (self.matrika[:i] + self.matrika[i+1:])])

    def inverz(self):
        if not self.kvadratna():
            raise Exception("Matrika ni kvadratna, poskusite uporabiti funkcijo Psevdo-Inverz")
        elif self.singularnost_matrike():
            raise Exception("Matrika ni obrnljiva, torej inverz ne obstaja, poskusite uporabiti funkcijo Psevdo-Inverz!")
        else:
            inverz = []
            for i in range(self.stevilovrstic):
                vrstica = []
                for j in range(self.stevilovrstic):
                    vrstica.append((-1) ** (i + j) * self.kofaktor(i, j).determinante())
                inverz.append(vrstica)
            trs = Matrika(inverz)
            s = 1 / self.determinante()
            return trs.transponiranje() * s
    
    def psevdoinverz(self):
    # posplošitev inverza za matrike, za katere je AA^T obrnljiva matrika 
        m =  Matrika(self)  * self.transponiranje()
        if m.singularnost_matrike():
            raise Exception("Psevdo-inverz take matrike ne znam izračunati.")
        else:
            n = m.inverz() * self.transponiranje()
            return Matrika(n)

    def __pow__(self, k):
    # Matriko mnozico samo s sabo k - krat, kjer je k naravno število, sicer
    # bi morali pretvoriti v Jordanovo kanonično formo, kar je računsko zahtevno.
        if not self.kvadratna():
            raise Exception("Potenciranje je definirano le za kvadratne matrike.")
        elif float(k) < 0 or float(k) % 1 != 0:
            raise Exception("Število k more biti naravno število!")
        elif float(k) == 0:
            return identiteta(self.stevilostolpcev)
        else:
            M = Matrika(self)
            for _ in range(int(k) - 1):
                M *= self
            return Matrika(M)

    def nenegativna(self):
        for vrstica in self.matrika:
            for element in vrstica:
                if element < 0:
                    return False
        return True

    def reduciabilnost(self):
    # preveri ali je matrika reduciabilna 
        if not self.kvadratna():
            return False
        elif not self.nenegativna():
            return False
        else:
            return nicelna(self.stevilovrstic) < (identiteta(self.stevilostolpcev) + self) ** (self.stevilostolpcev - 1) 

    def normalnost_opratorja(self):
    # preveri normanost operatorja
        if not self.kvadratna():
            raise Exception("Normanost operatorja je definirana le za kvadratne matrike!")
        else:
            a = Matrika(self) * self.transponiranje()
            b = self.transponiranje() * Matrika(self)
            return a == b
    
    def sebiadjugiranost_operatorja(self):
        if not self.kvadratna():
            raise Exception("Sebiadjugiranost operatorja je definirana le za kvadratne matrike")
        else:
            return self == self.transponiranje()

    def unitarnost_operatorja(self):
        if not self.kvadratna():
            raise Exception("Unitarnost operatorja je definirana le za kvadratne matrike.")
        else:
            return self.inverz() == self.transponiranje()

    def permutacijska(self):
        if not self.stohasticna_matrika():
            return False
        else:
            for vrstica in self.matrika:
                for element in vrstica:
                    if element != 0:
                        if element != 1:
                            return False
            return True

    def cramerjevo_pravilo(self, b):
    # Naj bo A matrika, ki predstavlja sistem n enančb z n neznakami, če je A nesingularna lahko uporabimo sledeč postopek za izračun rešitve sistema.
        if self.singularnost_matrike():
            raise Exception("Matrika more biti obrnljiva, sicer sistem ni enolično rešljiv")
        elif len(b) != self.stevilovrstic:
            raise Exception("Dolžina vektorja b se mora ujemati s število vrstic oz. številom stolpcem matirike A!")
        else: 
            resitev = []
            n = self.stevilostolpcev
            for u in range(n):
                M = self.transponiranje()
                M = M[:u] + [b] + M[(u + 1):]
                M = Matrika(M)
                s = 1 / self.determinante() 
                resitev.append(M.determinante() * s)
            return resitev

# Pomožni funkciji: 

def ali_je_stohasticen(vektor):
    vsota = 0
    for i in vektor:
        if i > 1 or i < 0:
            return False
        vsota += i
    if vsota != 1:
        return False
    return True
    

def identiteta(n):
    matrika = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            if i == j:
                vrstica.append(1)
            else:
                vrstica.append(0)
        matrika.append(vrstica)
    return Matrika(matrika)

def nicelna(n):
    matrika = []
    for _ in range(n):
        vrstica = []
        for _ in range(n):
            vrstica.append(0)
        matrika.append(vrstica)
    return Matrika(matrika)

# Class Permutacija je namenjen računanju s permutacijami.

class Permutacija:

    def __init__(self, permutacija={}):
        self.permutacija = permutacija

    def __repr__(self):
        return f'Permutacija({self.permutacija})'

    def  __str__(self):
        return f'{(self.permutacija)}'

    def __len__(self):
        return len(self.permutacija)
    
    def preverjanje_permutacije(self):
    # Preveri ali je slovar permutacija.
        if set(self.permutacija.keys()) == set(range(1, len(self.permutacija.keys()) + 1)):
            if set(self.permutacija.values()) == set(self.permutacija.keys()):
                return True
            else:
                return False
        else:
            return False

    def __mul__(self, other):
        if not self.preverjanje_permutacije() or not self.preverjanje_permutacije():
            raise Exception("Vpis mora biti permutacija.")
        elif len(self) != len(other):
            raise Exception("Permutacije morata imeti enako dolžino.")
        else:
            produkt = {}
            for i in range(1, len(self) + 1):
                produkt[i] = self.permutacija.get(other.permutacija.get(i))
            return Permutacija(produkt)
        
    def enkratna_slika_permutacije(self, k):
    # Vrne m - ti elemnt permutacije. 
        if float(k) > len(self):
            raise Exception("Število k mora biti kvečjemu število k!")
        elif float(k) % 1 != 0 or float(k) < 0:
            raise Exception("Število k mora biti naravno")
        elif not self.preverjanje_permutacije():
            raise Exception("Vpis mora biti permutacija.")
        else:
            return self.permutacija.get(int(k))

    def veckratno_slikanje_permutacije(self, k, r):
    # Vrne zaporedje slik po r - kratnem slikanju k - tega elementa.
        if float(r) < 0 or float(r) % 1 != 0:
            raise Exception("Število r mora biti naravno število!")
        elif not self.preverjanje_permutacije():
            raise Exception("Vpis mora biti permutacija.")
        else:
            list_permutacij = []
            r = int(r)
            k = int(k)
            while r + 1 != 0:
                k = self.permutacija[k]
                list_permutacij.append(k)
                r -= 1 
            return list_permutacij
        
    def veckratna_slika_permutacije(self, k, r):
    # Vrne element po r - kratnem slikanju k - tega elementa
        return self.veckratno_slikanje_permutacije(k, r)[-1]

    def cikel_v_permutaciji(self, m):
    # Vrne cikel začenši z m.
        if float(m) < 0 or float(m) % 1 != 0:
            raise Exception("Število r mora biti naravno število!") 
        if float(m) > len(self):
            raise Exception("Število k mora biti kvečjemu število k!")
        elif not self.preverjanje_permutacije():
            raise Exception("Vpis mora biti permutacija.")
        seznam = [m]
        m = float(m)
        n = self.permutacija[m]
        while n != m:
            seznam.append(n)
            n = self.permutacija[n]
        return seznam
        
    def cikli_v_permutaciji(self):
    # Vrne vse cikle v permutaciji.
        if not self.preverjanje_permutacije():
            raise Exception("Vpis mora biti permutacija.")
        cikli = []
        pomozna = set()
        for x in range(1, len(self.permutacija) + 1):
            if x not in pomozna:
                cikel = self.cikel_v_permutaciji(x)
                cikli.append(cikel)
                pomozna.update(cikel)
        return cikli

    def inverz(self):
        if not self.preverjanje_permutacije:
            raise Exception("Vpis mora biti permutacija.")
        inverz = {}
        for value in self.permutacija.values():
            inverz[self.permutacija.get(value)] = value
        return Permutacija(inverz)

    def inverzije(self):
        if not self.preverjanje_permutacije:
            raise Exception("Vpis mora biti permutacija.")
        else:
            st_inverzij = 0
            for i in range(len(self)):
                for j in range(len(self)):
                    if list_kljucev(self.permutacija)[j] > list_kljucev(self.permutacija)[i]:
                        if self.permutacija.get(i + 1) > self.permutacija.get(j + 1):
                            st_inverzij += 1
        return st_inverzij

    def signatura(self):
        sg = (-1) ** (self.inverzije())
        return sg

def list_kljucev(slovar):
    return list(slovar.keys())

def množica_bijektivnih_preslikav(n):
# vrne množico Sn t.j. vse bijektic.
    if int(n) == 0:
        return {()}
    elif float(n) < 0 or float(n) % 1 != 0:
        raise Exception("Število n mora biti naravno.")
    else:
        sedajsne_per = množica_bijektivnih_preslikav(int(n) - 1)
        novejse_per = set()
        for permutacija in sedajsne_per:
            for i in range(len(permutacija) + 1):
                novejse_per.add(permutacija[:i] + (n , ) + permutacija[i:])
        return novejse_per