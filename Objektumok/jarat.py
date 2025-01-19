from abc import ABC, abstractmethod
from datetime import datetime
#Járat (absztrakt osztály): Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int, utazasi_ido_h: float, indulas_t: datetime):
        self.jaratszam: str = jaratszam
        self.celallomas: str = celallomas
        self.jegyar: int = jegyar
        self.utazasi_ido_h: float = utazasi_ido_h
        self.indulasi_ido: datetime = indulas_t

    @abstractmethod
    def jarat_tipus(self):
        pass

