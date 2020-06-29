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
    
    def __sub__(self, other):
        return self.matrika + (-1) * other.matrika
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
    
    def __sub__(self, other):
        return self.vektor + (-1) * other.vektor