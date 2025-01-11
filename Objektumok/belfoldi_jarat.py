from abc import ABC

from Objektumok.jarat import Jarat

#BelföldiJarat: Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.

class BelfoldiJarat(Jarat, ABC):

    MAX_UTAZASI_IDO=2
    MAX_JEGYAR=100000

    def __init__(self, jaratszam, celallomas, jegyar, utazasi_ido_h):
        if utazasi_ido_h > self.MAX_UTAZASI_IDO:
            print("Túl hosszú utazási idő belföldi járatnál.")
            return
        if jegyar > self.MAX_JEGYAR:
            print("Túl magas jegyár belföldi járatnál.")
            return
        super().__init__(jaratszam, celallomas, jegyar, utazasi_ido_h)

