from datetime import datetime

from Objektumok.belfoldi_jarat import BelfoldiJarat
from Objektumok.legitarsasag import LegiTarsasag
from Objektumok.nemzetkozi_jarat import NemzetkoziJarat
from Szervizek.foglalas_kezelo import FoglalasKezelo


class UI:
    def __init__(self):
        self.legitarsasag: LegiTarsasag
        self.foglalasok: FoglalasKezelo
        self.first_run = True

    def start(self):
        print("\n\n--- Repülőjegy foglalási rendszer ---")
        print("\t1. Jegy foglalása")
        print("\t2. Foglalás lemondása")
        print("\t3. Foglalások listázása")
        print("\t4. Kilépés")

    def bemenet_keres(self):
        if not self.first_run:
            self.start()
        valaszt = input("Kérem válasszon a fenti opciókból: ")


        if valaszt == "1":
            self.jegy_foglalas()
        elif valaszt == "2":
            self.foglalas_lemondas()
        elif valaszt == "3":
            self.foglalasok_lista()
        elif valaszt == "4":
            self.kilep()

        input("Nyomjon le egy billentyűt a menübe való visszalépéshez!")

        self.first_run = False


    def jegy_foglalas(self):
        utas_nev=input("Adja meg az utas nevét: ")
        print("Elérhető járatok: ")
        elerheto_jaratok = self.legitarsasag.listaz_jaratok()
        foglalni_jaratszam = input("Kérem adja meg a foglalni kívánt járat számát:")
        jarat_elerheto, foglalando_jarat = self.legitarsasag.jarat_elerheto(foglalni_jaratszam)
        if jarat_elerheto:
            foglalas = self.foglalasok.foglalas(utas_nev, foglalando_jarat)
            if foglalas:
                print("Foglalás sikeresen megtörtént")
            else:
                return
        else:
            print("Helytelen járatszám")

    def foglalas_lemondas(self):
        print("Kérem adja meg a törléshez az alábbi adatokat:")
        utas_nev = input("Törlendő foglaláshoz tartozó név: ")
        torolni_jaratszam = input("Törlendő foglalás járatszáma: ")
        torles_sikeres = self.foglalasok.lemondas(utas_nev, torolni_jaratszam)
        if torles_sikeres:
            print("Foglalás törölve")
        else:
            print("Hiba! Foglalás nem törölhető mivel nem létezik")

    def foglalasok_lista(self):
        self.foglalasok.listaz_foglalasok()

    def kilep(self):
        print("Köszönjük, hogy minket választott!")
        exit(0)

    def adat_init(self):
        print("---------------------- Kezdeti adatok --------------------")
        wizzair = LegiTarsasag("WizzAir")
        foglalasok_kezelo = FoglalasKezelo()

        jarat1 = BelfoldiJarat("W62295", "Szeged", 15000, 0.5,
                               indulas_t=datetime(2025, 3, 4, 15, 30))

        jarat2 = BelfoldiJarat("W63397", "Debrecen", 18000, 0.8,
                               indulas_t=datetime(2025, 2, 3, 6, 30))

        jarat3 = NemzetkoziJarat("W69636", "Barcelona", 55000, 2.8,
                                 indulas_t=datetime(2025, 4, 8, 12, 45))

        jarat4 = NemzetkoziJarat("W61177", "Dubaj", 75000, 5.5,
                                 indulas_t=datetime(2025, 3, 10, 11, 15))

        jarat5 = NemzetkoziJarat("W63567", "Nizza", 52000, 2.2,
                                 indulas_t=datetime(2025, 1, 11, 8, 15))

        wizzair.hozzaad_jarat(jarat1)
        wizzair.hozzaad_jarat(jarat2)
        wizzair.hozzaad_jarat(jarat3)
        wizzair.hozzaad_jarat(jarat4)
        wizzair.hozzaad_jarat(jarat5)

        # Hibás járatok hozzáadásának példája.
        # A járatok hozzáadása direkt nincsen a felhasználói interfészen.
        # Ezért itt mutatom be a hibás adatok hozzáadását
        jarat_hiba_1 = NemzetkoziJarat("W63538", "Párizs", 40000, 2.2,
                                 indulas_t=datetime(2025, 11, 12, 2, 15))

        jarat_hiba_2 = BelfoldiJarat("W63538", "Nagykanizsa", 20000, 3,
                                       indulas_t=datetime(2025, 10, 1, 2, 15))

        foglalasok_kezelo.foglalas("Gipsz Jakab", jarat1)
        foglalasok_kezelo.foglalas("Gipsz Mária", jarat1)
        foglalasok_kezelo.foglalas("Katona Emília", jarat3)
        foglalasok_kezelo.foglalas("Katona Benedek", jarat3)
        foglalasok_kezelo.foglalas("Balogh Máté", jarat4)
        foglalasok_kezelo.foglalas("Baloghné Melinda", jarat4)

        self.legitarsasag= wizzair
        self.foglalasok = foglalasok_kezelo

        print("---------------------------------------------------------")

