
#JegyFoglalás: A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

class JegyFoglalas:
    def __init__(self, utas_nev, jarat):
        self.jarat=jarat
        self.utas_nev = utas_nev
        print("Foglalás történt: %s - %s" % (self.utas_nev, self.jarat.jaratszam))
