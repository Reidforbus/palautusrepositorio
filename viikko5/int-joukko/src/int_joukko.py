class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, koko=5, kasvatuskoko=5):
        if not isinstance(koko, int) or koko < 0:
            raise Exception("Koon on oltava positiivinen kokonaisluku")
        else:
            self.koko = koko

        if not isinstance(koko, int) or koko < 0:
            raise Exception("Kasvatuskoon on oltava positiivinen kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.koko)
        self.lukuja = 0

    def kuuluu(self, n):
        return n in self.lista

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lista[self.lukuja] = n
            self.lukuja += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.lukuja == len(self.lista):
                self.kasvata()
            return True
        return False

    def poista(self, n):
        for i in range(self.lukuja):
            if n == self.lista[i]:
                self.lista[i] = self.lista[self.lukuja - 1]
                self.lista[self.lukuja - 1] = 0
                self.lukuja -= 1
                return True
        return False

    def kasvata(self):
        uusi_lista = self._luo_lista(self.lukuja + self.kasvatuskoko)
        for i in range(self.lukuja):
            uusi_lista[i] = self.lista[i]
        self.lista = uusi_lista

    def mahtavuus(self):
        return self.lukuja

    def to_int_list(self):
        lista = self._luo_lista(self.lukuja)
        for i in range(self.lukuja):
            lista[i] = self.lista[i]
        return lista

    @staticmethod
    def yhdiste(a_joukko, b_joukko):
        yhdistejoukko = IntJoukko()
        a_taulu = a_joukko.to_int_list()
        b_taulu = b_joukko.to_int_list()

        for i in range(len(a_taulu)):
            yhdistejoukko.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            yhdistejoukko.lisaa(b_taulu[i])

        return yhdistejoukko

    @staticmethod
    def leikkaus(a_joukko, b_joukko):
        leikkausjoukko = IntJoukko()
        a_taulu = a_joukko.to_int_list()
        b_taulu = b_joukko.to_int_list()

        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkausjoukko.lisaa(b_taulu[j])

        return leikkausjoukko

    @staticmethod
    def erotus(a_joukko, b_joukko):
        erotusjoukko = IntJoukko()
        a_taulu = a_joukko.to_int_list()
        b_taulu = b_joukko.to_int_list()

        for i in range(len(a_taulu)):
            erotusjoukko.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            erotusjoukko.poista(b_taulu[i])

        return erotusjoukko

    def __str__(self):
        luvut = [str(x) for x in self.lista[:self.lukuja]]
        return "{" + ", ".join(luvut) + "}"
