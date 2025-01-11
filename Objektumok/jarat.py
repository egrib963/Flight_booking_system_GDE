from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int, utazasi_ido_h: float):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass


#jarat2=Jarat("W6120","BUD",5000)

