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
            raise Exception("Vektorj in točma morata imate oba le 3 komponente")


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
            raise Exception("Matriki se ne da zmnožiti, saj sta sešteti velikosti.")

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
            return self.matrika[1][1] * self.matrika[0][1] - self.matrika[1][0] * self.matrika[0][1]
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
    
    def psevdo_inverz(self):
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
            return self.psevdo_inverz() * b + (identiteta(self.stevilovrstic) - self.psevdo_inverz() * self.matrika) * y

    def potenciaranje(self):
        pass

    def reduciabilnost(self):
        pass

    def normalnost_opratorja(self):
        pass
    
    def sebiadjugiranost_operatorja(self):
        pass

    def unitarnost_operatorja(self):
        pass

    def permutacijska(self):
        pass
    

def permutacije(n):
    pass

def signatura(permutacija):
    pass

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