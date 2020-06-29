''' Začetek z delom na kalkulatorju '''

class Vektorji:

    def __init__(self, vektor):
        self.vektor = vektor
        self.stevilovrstic = len(vektor)

    def __add___(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            nov_vektor = []
            for i in range(self.stevilovrstic):
                nov_vektor.append(self.vektor[i] + other.vektor[i])
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da zmnožiti")
    
    def __repr__(self):
        return f'Vektor({self.vektor})'

    def __sub__(self, other):
        return self.vektor + (-1) * other.vektor

    def __eq__(self, other):
        return self.vektor == other.vektor

    def norma(self):
        norma = None
        for i in self.stevilovrstic:
            norma += i ** 2
        return norma
    
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
        return
    
    def ploščina_paralelograma(self, other):
        pass

    def ploščina_paralelepipeda(self, other, tretji):
        pass
    
    def volumen_piramide(self, other, tretji):
        pass

    def enacba_premice(self, tocka):
    # enačba premice s smernim vekotrem self, ki gre skozi točko ''tocka''
        pass

    def razdalja_tocke_do_premice(self, tocka1, tocka2 ):
    # self je smerni vektor premice, tocka1 je tocka ki je na premice, tocka2 pa tocka, katere razdalja do premice nas zanima
        pass

class Matrika:

    def __init__(self, matrika):
        self.matrika = matrika
        self.stevilovrstic = len(matrika)
        self.stevilostolpcev = len(matrika[0])
        self.kvadratna = (self.stevilovrstic == self.stevilovrstic)

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
    
    def __repr__(self):
        return f'Matrika({self.matrika})'

    def __sub__(self, other):
        return self.matrika + (-1) * other.matrika
    
    def __eq__(self, other):
        return self.matrika == other.matrika

    def trace(self):
        if self.kvadratna:
            trace = 0
            for i in self.stevilovrstic:
                trace += self.matrika[i][i]
            return trace
        else:
            raise Exception("Sled je definirana le za kvadratne matrike.")

    def produkt(self, other):
        pass

    def transponiranje(self):
        transponiranka = []
        for i in range(self.stevilostolpcev):
            vrstica = []
            for j in range(self.stevilovrstic):
                vrstica.append(self.matrika[j][i])
            transponiranka.append(vrstica)
        return transponiranka

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
