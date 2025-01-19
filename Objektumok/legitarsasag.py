from traceback import print_tb
from typing import List

from Objektumok.jarat import Jarat
#LégiTársaság: Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.

class LegiTarsasag:

    def __init__(self, nev):
        self.nev = nev
        self.jaratok: List[Jarat] = []

    def hozzaad_jarat(self, jarat: Jarat):
        for jarat_a_listaban in self.jaratok:
            if jarat.jaratszam == jarat_a_listaban.jaratszam and jarat.celallomas == jarat_a_listaban.celallomas:
                print("Járat már létezik a %s légitársaságnál: %s - %s" %  (self.nev, jarat.jaratszam,jarat.celallomas))
                return
        self.jaratok.append(jarat)
        print("Járat hozzáadva a %s légitársasághoz: %s - %s" % (self.nev, jarat.jaratszam, jarat.celallomas))

    def torol_jarat(self, jarat: Jarat):
        for jarat_a_listaban in self.jaratok:
            if jarat.jaratszam == jarat_a_listaban.jaratszam and jarat.celallomas == jarat_a_listaban.celallomas:
                self.jaratok.remove(jarat)
                print("Járat törölve a %s légitársaságból: %s - %s" %  (self.nev, jarat.jaratszam,jarat.celallomas))
                return
        print("Járat nem létezik a %s légitársaságnál: %s - %s" % (self.nev, jarat.jaratszam, jarat.celallomas))

    def listaz_jaratok(self):
        print("A %s légitársaság járatai:" % self.nev)
        for jarat in self.jaratok:
            print("\t%s - %s. Ár: %d Indulás: %s" % (jarat.jaratszam, jarat.celallomas, jarat.jegyar, str(jarat.indulasi_ido)))

        return self.jaratok

    def jarat_elerheto(self, jaratszam: str):
        jarat_letezik = False
        elerheto_jarat = None
        for jarat_a_listaban in self.jaratok:
            if jaratszam == jarat_a_listaban.jaratszam:
                elerheto_jarat = jarat_a_listaban
                jarat_letezik = True

        if jarat_letezik:
            print("Járat létezik.")
        else:
            print("Járat nem létezik.")

        return jarat_letezik, elerheto_jarat

