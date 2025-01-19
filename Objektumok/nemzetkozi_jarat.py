from abc import ABC
from datetime import datetime

from Objektumok.jarat import Jarat

#NemzetkoziJarat: Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.

class NemzetkoziJarat(Jarat, ABC):

    MIN_UTAZASI_IDO=1
    MIN_JEGYAR=50000

    def __init__(self, jaratszam, celallomas, jegyar,utazasi_ido_h, indulas_t: datetime):
        if utazasi_ido_h < self.MIN_UTAZASI_IDO:
            print("Túl rövid utazási idő nemzetközi járatnál.\nKérjük ellenőrizze a járat adatait.\n")
            return
        if jegyar < self.MIN_JEGYAR:
            print("Túl alacsony jegyár nemzetközi járatnál.\nKérjük ellenőrizze a járat adatait.\n")
            return
        super().__init__(jaratszam, celallomas, jegyar,utazasi_ido_h, indulas_t)

    def jarat_tipus(self):
        return "Nemzetközi járat"