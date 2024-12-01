class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._loki = []

    def miinus(self, operandi):
        self._loki.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._loki.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._loki.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        self._arvo = self._loki.pop()


class KomentoSuoritin:
    def __init__(self, logiikka, lukija):
        self._logiikka = logiikka
        self._lukija = lukija
        self._luku = 0

    def suorita(self):
        self._luku = int(self._lukija())
        self.laske()

    def laske(self):
        return 0


class Nollaus(KomentoSuoritin):
    def __init__(self, logiikka, lukija):
        super().__init__(logiikka, lukija)

    def suorita(self):
        self._logiikka.nollaa()


class Summa(KomentoSuoritin):
    def __init__(self, logiikka, lukija):
        super().__init__(logiikka, lukija)

    def laske(self):
        self._logiikka.plus(self._luku)


class Erotus(KomentoSuoritin):
    def __init__(self, logiikka, lukija):
        super().__init__(logiikka, lukija)

    def laske(self):
        self._logiikka.miinus(self._luku)


class Kumoa(KomentoSuoritin):
    def __init__(self, logiikka, lukija):
        super().__init__(logiikka, lukija)

    def suorita(self):
        self._logiikka.kumoa()
