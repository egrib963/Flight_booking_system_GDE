from abc import ABC
from datetime import datetime

from Objektumok.jarat import Jarat

#BelföldiJarat: Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.

class BelfoldiJarat(Jarat, ABC):

    MAX_UTAZASI_IDO=2
    MAX_JEGYAR=100000

    def __init__(self, jaratszam, celallomas, jegyar, utazasi_ido_h, indulas_t: datetime):
        if utazasi_ido_h > self.MAX_UTAZASI_IDO:
            print("Túl hosszú utazási idő belföldi járatnál.\nKérjük ellenőrizze a járat adatait.\n")
            return
        if jegyar > self.MAX_JEGYAR:
            print("Túl magas jegyár belföldi járatnál.\nKérjük ellenőrizze a járat adatait.\n")
            return
        super().__init__(jaratszam, celallomas, jegyar, utazasi_ido_h, indulas_t)

    def jarat_tipus(self):
        return "Belföldi járat"

