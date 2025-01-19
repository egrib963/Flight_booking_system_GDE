from Objektumok.jegyfoglalas import JegyFoglalas
from datetime import datetime


#Funkciók:
#Jegy foglalása: A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
#Foglalás lemondása: A felhasználó lemondhatja a meglévő foglalást.
#Foglalások listázása: Az összes aktuális foglalás listázása.

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, utas_nev, jarat):
        # Idő validáció
        jelenlegi_ido = datetime.now()
        mai_datum = jelenlegi_ido.strftime("%Y-%m-%d")
        if mai_datum == jarat.indulasi_ido.strftime("%Y-%m-%d"):
            print("Nem foglalható járat mai indulással")
            return False
        if mai_datum > jarat.indulasi_ido.strftime("%Y-%m-%d"):
            print("A foglalás egy múltban lévő járatra mutat. Foglalás nem lehetséges")
            return False

        #Foglalás
        foglalas = JegyFoglalas(utas_nev, jarat)
        self.foglalasok.append(foglalas)
        return foglalas

    def lemondas(self, utas_nev, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def listaz_foglalasok(self):
        print("Foglalások: ")
        for foglalas in self.foglalasok:
            print("\t%s - %s" % (foglalas.utas_nev, foglalas.jarat.jaratszam))
