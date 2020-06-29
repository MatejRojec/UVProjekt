''' Začetek z delom na kalkulatorju '''

class Matrika:

    def __init__(self, matrika):
        self.matrika = matrika
        self.stevilovrstic = len(matrika)
        self.stevilostolpcev = len(matrika[0])

    def __add__(self, other):
        if self.stevilostolpcev == other.stevilostolpcev and self.stevilovrstic == other.stevilovrstic:
            summation = []
            for i in range(self.stevilovrstic):
                pomozna = []
                for j in range(self.stevilostolpcev):
                    pomozna.append(self.matrika[i][j] + other.matrika[i][j])
                summation.append(pomozna)
        else:
            raise Exception("Matriki se ne da zmnožiti, saj sta sešteti velikosti")
     def __repr__(self):
        return f'Matrika({self.matrika})'

    def __sub__(self, other):
        return self.matrika + (-1) * other.matrika
    
    def __eq__(self, other):
        return self.matrika == other.matrika
    
    def produkt(self, other):


class Vektorji:

    def __init__(self, vektor):
        self.vektor = vektor
        self.stevilovrstic = len(vektor)

    def __add___(self, other):
        if self.stevilovrstic == other.stevilovrstic:
            nov_vektor = []
            for i in range(self.stevilovrstic):
                nov_vektor.append(self.vektor[i] + other.vektor[j])
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da")
    
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
    
    def skalarni_produkt(self, other):
    # Govorimo o standardem skalarnem produktu v R^n po komponentah
        if self.stevilovrstic == other.stevilovrstic:
            produkt = None
            for i in self.stevilovrstic:
                produkt += self.vektor[i] * other.vektor[i]
            return produkt
        else:
            raise Exception("Vektorja imata različno število vrstic, zatorej se ju ne da")
     
     def vektorski_produkt(self, other):
        pass

     def kot(self, other):
        pass
    
    def ploščina_paralelograma(self, other):
        pass

    def ploščina_paralelepipeda(self, other, drugi):
        pass
    
    def volumen_piramide(self, other, drugi):
        pass

    def enacba_premice(self, tocka):
        pass

    def razdalja_tocke_do_premice(self, tocka1, tocka2  ):
    # self je smerni vektor premice, tocka1 je tocka ki je na premice, tocka2 pa tocka, katere razdalja do premice nas zanima
        pass