''' Začetek z delom na kalkulatorju '''

import math

class Vektor:

    def __init__(self, vektor):
        self.vektor = vektor
        self.stevilovrstic = len(vektor)

    def __repr__(self):
        return f'Vektor({self.vektor})'

    def __add___(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            nov_vektor = []
            for i in range(self.stevilovrstic):
                nov_vektor.append(self.vektor[i] + other.vektor[i])
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da zmnožiti")

    def __sub__(self, other):
        return self.vektor + (-1) * other.vektor

    def __eq__(self, other):
        return self.vektor == other.vektor

    def __lt__(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            for i in self.vektor:
                seznam = []
                if self.vektor[i] > other.vektor[i]:
                    seznam.append(True)
                else:
                    seznam.append(False)
            return all(seznam)
        else:
            raise Exception("Vektorjev različnih velikosti ne moremo primerjati.")

    def norma(self):
        norma = None
        for i in self.stevilovrstic:
            norma += i ** 2
        return norma
    
    def skalarni_produkt(self, other):
    # Govorimo o standardem skalarnem produktu v R^n po komponentah
        if self.stevilovrstic == other.stevilovrstic:
            produkt = None
            for i in self.stevilovrstic:
                produkt += self.vektor[i] * other.vektor[i]
            return produkt
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da.")
     
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
            return novi
        else: 
            raise Exception("Vektorski produkt je definiran le v treh dimenzijah.")

    def kot(self, other):
        return math.acos(self.skalarni_produkt(other) / (self.norma() * other.norma()))
    
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
        self.kvadratna = (self.stevilovrstic == self.stevilovrstic)

    def __repr__(self):
        return f'Matrika({self.matrika})'

    def __add__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            summation = []
            for i in range(self.stevilovrstic):
                pomozna = []
                for j in range(self.stevilostolpcev):
                    pomozna.append(self.matrika[i][j] + other.matrika[i][j])
                summation.append(pomozna)
        else:
            raise Exception("Matriki se ne da zmnožiti, saj sta različni velikosti.")

    def __sub__(self, other):
        return self.matrika + (-1) * other.matrika
    
    def __eq__(self, other):
        return self.matrika == other.matrika

    def __lt__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            for i in self.matrika:
                seznam = []
                for j in self.matrika[0]:
                    if self.matrika[i][j] > other.matrika[i][j]:
                        seznam.append(True)
                    else:
                        seznam.append(False)
                return all(seznam)
        else:
            raise Exception("Matrik različnih razsežnosti se ne da primerjati.")

    def trace(self):
        if self.kvadratna:
            trace = 0
            for i in self.stevilovrstic:
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
        return transponiranka

    def produkt_matrike_s_skalarjem(self, other):
    # Množenje matrike s skalarjem
        if isinstance(other, int) or isinstance(other, float):
            produkt = []
            for i in range(self.stevilovrstic):
                vrstica = []
                for j in range(self.stevilostolpcev):
                    vrstica.append(self.matrika[i][j] * other)
                produkt.append(vrstica)
            return Matrika(produkt)
        else:
            raise Exception("Si prepričan, da si matriko množil matriko s skalarjem?")
     
    def produkt_matrike_z_matriko(self, other):
    # Množenje matrik 
        if self.stevilostolpcev == other.vrstice:
            tansponiraj = other.transponiranje() 
            produkt = []
            for i in range(self.stevilovrstic):
                vrstica = []
                for j in range(self.stevilostolpcev):
                    vrstica.append(sum([element[0] * element[1] for element in zip(self.matrika[i], tansponiraj.matrika[j])]))
                produkt.append(vrstica)
            return produkt
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

        if not self.kvadratna:
            raise Exception("Determinanta pravokotnih matrik ni definirana.")
        elif self.stevilovrstic == 1:
            return self.matrika[0][0]
        elif self.stevilovrstic == 2:
            return self.matrika[1][1] * self.matrika[0][0] - self.matrika[1][0] * self.matrika[0][1]
        else:
            M = self.matrika
            determinanta = 0
            indeksi = list(range(M.stevilovrstic))
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
        return (-1) ** (i + j)  * ([vrstica[:j] + vrstica[j+1:] for vrstica in (self.matrika[:i] + self.matrika[i+1:])])

    def inverz(self):
        if not self.kvadratna:
            raise Exception("Matrika ni kvadratna, poskusite uporabiti funkcijo Psevdo-Inverz")
        elif self.singularnost_matrike():
            raise Exception("Matrika ni obrnljiva, torej inverz ne obstaja!")
        else:
            inverz = []
            for i in range(self.stevilovrstic):
                vrstica = []
                for j in range(self.stevilovrstic):
                    vrstica.append(self.kofaktor(j, i))
                inverz.append(vrstica)
            return  inverz * 1 / self.determinante()
    
    def psevdoinverz(self):
    # posplošitev inverza za matrike, za katere je AA^T obrnljiva matrika 
        m = self.transponiranje() * self.matrika  
        if m.singularnost_matrike():
            raise Exception("Psevdo - inverz take matrike ne znam izračunati.")
        else:
            return m.inverz() * self.transponiranje()

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
        elif k < 0 or k % 1 != 0:
            raise Exception("Število k more biti naravno število!")
        elif k == 0:
            identiteta(self.stevilostolpcev)
        else:
            M = self.matrika
            for _ in range(k - 1):
                M *= self.matrika
            return M

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
            return (identiteta(self.stevilostolpcev) + self.matrika) ** (self.stevilostolpcev - 1) > 0

    def normalnost_opratorja(self):
    # preveri normanost operatorja
        if not self.kvadratna():
            raise Exception("Normanost je definirana le za kvadratne matrike!")
        else:
            return self.matrika * self.transponiranje() == self.transponiranje() * self.matrika()
    
    def sebiadjugiranost_operatorja(self):
        if not self.normalnost_opratorja():
            return False
        else:
            return self.matrika() == self.transponiranje()

    def unitarnost_operatorja(self):
        if not self.normalnost_opratorja():
            return False
        else:
            return self.inverz() == self.transponiranje()

    def permutacijska(self):
        if not self.stohasticna_matrika():
            return False
        else:
            for vrstica in self.matrika:
                for element in vrstica:
                    if element != 0 or element != 1:
                        return False
                return True

    def cramerjevo_pravilo(self, b):
    # Naj bo A matrika, ki predstavlja sistem n enančb z n neznakami, če je A nesingularna lahko uporabimo sledeč postopek za izračun rešitve sistema
        if self.singularnost_matrike():
            raise Exception("Matrika more biti obrnljiva, sicer sistem ni enolično rešljiv")
        elif len(b) != self.stevilostolpcev:
            raise Exception("Dolžina vektorja b se mora ujemati s število vrstic oz. številom stolpcem matirike A!")
        else: 
            resitev = []
            for element in range(self.stevilostolpcev):
                M = self.transponiranje()
                M = M[:element] + [b] + M[(element + 1):]
                M = M.determinante() / self.determinante()
                resitev.append(M)

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
    return matrika


class Permutacija:

    def __init__(self, n, permutacija):
        ''' Permutacija bo predstavljala poljuben slovar, ki je permutacija (uporabnik jo natipka)
        Velikost je neodvisna od permutacije in bo omogačala, da uporabnik dobi vse permutacije
        dolžine n. Torej dobi množico Sn, za nek n element naravnih števil.'''
        self.permutacija = permutacija
        self.velikost = n
        self.jepermutacija = None
        self.dolzina = None

    def preverjanje_permutacije(self):
    # Preveri ali je seznam permutacija ! To potem shrani v vrednost slef.jepermutacija
        if set(self.permutacija.keys()) == set(range(1, len(self.permutacija.keys()) + 1)):
            if set(self.permutacija.values()) == set(self.permutacija.keys()):
                return True
            else:
                return False
        else:
            return False

    def je_permutacija(self):
        self.jepermutacija = self.preverjanje_permutacije()

    def dolzina_permutacije(self):
     # vrne dolzino permutacije
        self.dolzina = len(self.permutacija)

    def enkratna_slika_permutacije(self, k):
    # vrne m - ti elemnt permutacije 
    # Izpiše množico Sn t.j. množico vseh bijekcij {1, 2, ..., n}
        if k > self.dolzina:
            raise Exception("Število k mora biti kvečjemu število k!")
        elif k % 1 != 0 or k < 0:
            raise Exception("Število k mora biti naravno")
        else:
            return self.permutacija.get(k)

    def veckratno_slikanje_permutacije(self, k, r):
    # vrne zaporedje slik po r - kratnem slikanju k - tega elementa.
        if r > self.dolzina:
            raise Exception("Število r mora biti kvečjemu število r!")
        elif r < 0 or r % 1 != 0:
            raise Exception("Število r mora biti naravno število!")
        else:
            list_permutacij = []
            while r + 1 != 0:
                list_permutacij.append(k)
                k = self.permutacija[k]
                r -= 1 
            return list_permutacij
        
    def veckratna_slika_permutacije(self, k, r):
    # Vrne element po r - kratnem slikanju k - tega elementa
        return self.veckratno_slikanje_permutacije(k, r)[-1]

    def simetricna(self):
        if self.velikost % 1 != 0 or self.velikost < 0:
            raise Exception("VElikost mora biti naravno število !") 
        return sn(self.permutacija) 

    def cikel_v_permutaciji(self, m):
    # Vrne cikel začenši z m
        seznam = [m]
        n = self.permutacija[m]
        while n != m:
            seznam.append(n)
            n = self.permutacija[n]
        return seznam
        
    def cikli_v_permutaciji(self):
    # vrne vse cikle v permutaciji
        cikli = []
        pomozna = set()
        for x in range(1, len(self.permutacija) + 1):
            if x not in pomozna:
                cikel = self.cikel_v_permutaciji(x)
                cikli.append(cikel)
                pomozna.update(cikel)
        return cikli


    def stevilo_inverzij(self):
        inverzije = 0
        for element, sigma_element in enumerate(self.permutacija.values()):
            for _ in self.permutacija[(element + 1):]:
                if _ < sigma_element:
                    inverzije += 1
        return inverzije

    def sg(self):
        if self.stevilo_inverzij() % 2 == 0:
            return 1
        else:
            return -1

def sn(n):
# vrne množico Sn t.j. vse bijektic.
    if n == 0:
        return {()}
    else:
        sedajsne_per = sn(n - 1)
        novejse_per = set()
        for permutacija in sedajsne_per:
            for i in range(len(permutacija) + 1):
                novejse_per.add(permutacija[:i] + (n , ) + permutacija[i:])
        return novejse_per