''' Verzija nlizu koncu '''

import math

class Vektor:

    def __init__(self, vektor):
        self.vektor = vektor
        self.stevilovrstic = len(self.vektor)

    def __repr__(self):
        return f'Vektor({self.vektor})'

    def  __str__(self):
        return f'{tuple(self.vektor)}'

    def __getitem__(self, i):
        return self.vektor[i]

    def __setitem__(self, i, l):
        self.vektor[i] = l
    
    def __len__(self):
        return self.stevilovrstic
    
    def __add__(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            nov_vektor = []
            for i in range(self.stevilovrstic):
                nov_vektor.append(self.vektor[i] + other.vektor[i])
            return Vektor(nov_vektor)
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da sešteti.")

    def __sub__(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            nov_vektor = []
            for i in range(self.stevilovrstic):
                nov_vektor.append(self.vektor[i] - other.vektor[i])
            return Vektor(nov_vektor)
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da odšteti.")


    def __eq__(self, other):
        return self.vektor == other.vektor

    def __lt__(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            for i in range(len(self.vektor)):
                seznam = []
                if self.vektor[i] > other.vektor[i]:
                    seznam.append(True)
                else:
                    seznam.append(False)
            return all(seznam)
        else:
            raise Exception("Vektorjev različnih velikosti ne moremo primerjati.")

    def norma(self):
        norma = 0
        for i in range(self.stevilovrstic):
            norma += self[i] ** 2
        return norma
    
    def skalarni_produkt(self, other):
    # Govorimo o standardem skalarnem produktu v R^n po komponentah
        if self.stevilovrstic == other.stevilovrstic:
            produkt = 0
            for i in range(self.stevilovrstic):
                produkt += self[i] * other[i]
            return produkt
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da skalarno zmožiti.")
     
    def mnozenje_vektorja_s_skalarjem(self, skalar):
        novi = []
        for i in range(self.stevilovrstic):
            novi.append(skalar * self.vektor[i])
        return novi
    
    def vektorski_produkt(self, other):
        if self.stevilovrstic == 3 and other.stevilovrstic == 3:
            s = self.vektor
            o = other.vektor
            novi = [None, None, None]
            novi[0] = s[1] * o[2] - o[1] * s[2]
            novi[1] = - s[0] * o[2] + o[0] * s[2]
            novi[2] = s[0] * o[1] - o[0] * s[1]
            return Vektor(novi)
        else: 
            raise Exception("Vektorski produkt je definiran le v treh dimenzijah.")

    def kot(self, other):
        if self.norma() == 0 or other.norma() == 0:
            raise Exception("VEktorja morata biti neničelna.")
        radiani = math.acos(self.skalarni_produkt(other) / (self.norma() * other.norma()))
        return 180 / radiani
    
    def ploščina_paralelograma(self, other):
    # izračuna ploščino, ki ga omejujeta vektorja self in other 
        return math.sin(self.kot(other)) * self.norma() * other.norma()

    def volumen_paralelepipeda(self, other, tretji):
    # izračuna volumen paraleliepipeda, ki ga omejuje trije vektorji
        return self.ploščina_paralelograma(other) * tretji.norma()
    
    def volumen_piramide(self, other, tretji):
        return self.volumen_paralelepipeda(other, tretji) / 6

    def enacba_premice(self, tocka):
    # enačba premice s smernim vekotrem self, ki gre skozi točko "tocka"
        if self.stevilovrstic == 3 and len(tocka) == 3:
            return f'(x - {tocka[0]}) / {self.vektor[0]} = (y - {tocka[1]}) / {self.vektor[1]} = (z - {tocka[2]}) / {self.vektor[2]}'
        else:
            raise Exception("Vektorj in točma morata imate oba 3 komponente")


class Matrika:

    def __init__(self, matrika):
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

    def kvadratna(self):
        return self.stevilostolpcev == self.stevilovrstic 

    def __add__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            vsota = []
            for i in range(self.stevilovrstic):
                pomozna = []
                for j in range(self.stevilostolpcev):
                    pomozna.append(self.matrika[i][j] + other.matrika[i][j])
                vsota.append(pomozna)
            return Matrika(vsota)
        else:
            raise Exception("Matriki se ne da sešteti, saj sta različni velikosti.")

    def __sub__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            razlika = []
            for i in range(self.stevilovrstic):
                pomozna = []
                for j in range(self.stevilostolpcev):
                    pomozna.append(self.matrika[i][j] - other.matrika[i][j])
                razlika.append(pomozna)
            return Matrika(razlika)
        else:
            raise Exception("Matriki se ne da odšteti, saj sta različni velikosti.")    

    def __eq__(self, other):
        return self.matrika == other.matrika

    def __lt__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            for i in range(len(self.matrika)):
                seznam = []
                for j in range(len(self.matrika[0])):
                    if self.matrika[i][j] > other.matrika[i][j]:
                        seznam.append(True)
                    else:
                        seznam.append(False)
                return all(seznam)
        else:
            raise Exception("Matrik različnih razsežnosti se ne da primerjati.")

    def sled(self):
        if self.kvadratna():
            trace = 0
            for i in range(self.stevilovrstic):
                trace += self.matrika[i][i]
            return trace
        else:
            raise Exception("Sled je definirana le za kvadratne matrike.")
    
    def transponiranje(self):
        transponiranka = []
        for i in range(self.stevilostolpcev):
            vrstica = []
            for j in range(self.stevilovrstic):
                vrstica.append(self.matrika[j][i])
            transponiranka.append(vrstica)
        return Matrika(transponiranka)
     
    def __mul__(self, other):
    # Množenje s skalarjem
        if isinstance(other, (int, float)):
            zmnozek = []
            m = self.stevilovrstic
            n = self.stevilovrstic
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self.matrika[i][j] * other)
                zmnozek.append(vrstica)
            return Matrika(zmnozek)

    # Množenje matrik 
        elif isinstance(other, Matrika):
            if self.stevilostolpcev == other.stevilovrstic:
                return Matrika( 
                [[sum(x * y for x,y in zip(self.stevilovrstic, other.stevilostolpcev)) 
                for other.stevilostolpcev in zip(*other)] for self.stevilovrstic in self])
        else:
            raise Exception("Matrik se ne more zmnožiti.")

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
    # Determinanto bomo izračunali s pomočjo razvoja 
    # Za to uporabimo rekurzivno zvezo

        if not self.kvadratna():
            raise Exception("Determinanta pravokotnih matrik ni definirana.")
        elif self.stevilovrstic == 1:
            return self.matrika[0][0]
        elif self.stevilovrstic == 2:
            return self.matrika[1][1] * self.matrika[0][0] - self.matrika[1][0] * self.matrika[0][1]
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
            raise Exception("Matrika ni obrnljiva, torej inverz ne obstaja!")
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
        m =  Matrika(self.matrika)  * self.transponiranje()
        if m.singularnost_matrike():
            raise Exception("Psevdo - inverz take matrike ne znam izračunati.")
        else:
            n = m.inverz() * self.transponiranje()
            return Matrika(n)

    def metoda_najmanjsih_kvadratov(self, b , y):
    # izračuna neko rešitev sistema po metodi najmanjših kvadratov
    # Sistem Ax = b, kjer je AA^T obrnljiva matrika
        if self.singularnost_matrike():
            return Exception("Takega sistema ne znam rešiti.")
        elif len(b) != self.stevilovrstic:
            raise Exception("Dolžine se ne ujemajo")
        elif len(y) != self.stevilostolpcev:
            raise Exception("Dolžine se ne ujemajo. ")
        else:
            return self.psevdoinverz() * b + (identiteta(self.stevilovrstic) - self.psevdoinverz() * self.matrika) * y

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
            raise Exception("Normanost je definirana le za kvadratne matrike!")
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
    # Naj bo A matrika, ki predstavlja sistem n enančb z n neznakami, če je A nesingularna lahko uporabimo sledeč postopek za izračun rešitve sistema
        if self.singularnost_matrike():
            raise Exception("Matrika more biti obrnljiva, sicer sistem ni enolično rešljiv")
        elif len(b) != self.stevilovrstic:
            raise Exception("Dolžina vektorja b se mora ujemati s število vrstic oz. številom stolpcem matirike A!")
        else: 
            resitev = []
            for u in range(self.stevilostolpcev):
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

class Permutacija:

    def __init__(self, permutacija):
        ''' Permutacija bo predstavljala poljuben slovar, ki je permutacija (uporabnik jo natipka)
        Velikost je neodvisna od permutacije in bo omogačala, da uporabnik dobi vse permutacije
        dolžine n. Torej dobi množico Sn, za nek n element naravnih števil.'''
        self.permutacija = permutacija

    def __repr__(self):
        return f'Permutacija({self.permutacija})'

    def  __str__(self):
        return f'{(self.permutacija)}'

    def __len__(self):
     # vrne dolzino permutacije
        return len(self.permutacija)
    
    def preverjanje_permutacije(self):
    # Preveri ali je seznam permutacija ! To potem shrani v vrednost slef.jepermutacija
        if set(self.permutacija.keys()) == set(range(1, len(self.permutacija.keys()) + 1)):
            if set(self.permutacija.values()) == set(self.permutacija.keys()):
                return True
            else:
                return False
        else:
            return False

    def enkratna_slika_permutacije(self, k):
    # vrne m - ti elemnt permutacije 
    # Izpiše množico Sn t.j. množico vseh bijekcij {1, 2, ..., n}
        if float(k) > len(self):
            raise Exception("Število k mora biti kvečjemu število k!")
        elif float(k) % 1 != 0 or float(k) < 0:
            raise Exception("Število k mora biti naravno")
        elif not self.preverjanje_permutacije():
            raise Exception("Vpis mora biti permutacija.")
        else:
            return self.permutacija.get(int(k))

    def veckratno_slikanje_permutacije(self, k, r):
    # vrne zaporedje slik po r - kratnem slikanju k - tega elementa.
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
    # Vrne cikel začenši z m
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
    # vrne vse cikle v permutaciji
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

def sn(n):
# vrne množico Sn t.j. vse bijektic.
    if int(n) == 0:
        return {()}
    elif float(n) < 0 or float(n) % 1 != 0:
        raise Exception("Število n mora biti naravno.")
    else:
        sedajsne_per = sn(int(n) - 1)
        novejse_per = set()
        for permutacija in sedajsne_per:
            for i in range(len(permutacija) + 1):
                novejse_per.add(permutacija[:i] + (n , ) + permutacija[i:])
        return novejse_per