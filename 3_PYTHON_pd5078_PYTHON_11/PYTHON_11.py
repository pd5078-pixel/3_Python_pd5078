class Organizm:     
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
    def opisz(self):
        print(f"\nNazwa organizmu to {self.nazwa}.\nRodzaj organizmu to {self.rodzaj}.")
    @staticmethod
    def transkrybuj(sekwencja):
        return sekwencja.replace("T", "U")

class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, ksztalt):
        super().__init__(nazwa, rodzaj)
        self.ksztalt = ksztalt
    def opisz(self):
        super().opisz()
        print(f"Kształt organizmu to {self.ksztalt}.")


e_coli = Bakteria("Escherichia coli", "Enterobacteriaceae", "pałeczka")
e_coli.opisz()

s_pyogenes = Bakteria("Streptococcus pyogenes", "Streptococcus", "kula (ziarenkowce)")
s_pyogenes.opisz()

b_subtilis = Bakteria("Bacillus subtilis", "Bacillus", "pałeczka")
b_subtilis.opisz()

s_pyogenes.transkrybuj("ATTGCAAGGACCATGATT")
print(s_pyogenes.transkrybuj("ATTGCAAGGACCATGATT"))