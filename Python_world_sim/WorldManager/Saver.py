from Entities.Animal.Antylopa import Antylopa
from Entities.Plant.BarszczSosnowskiego import BarszczSosnowskiego
from Entities.Animal.CyberOwca import CyberOwca
from Entities.Animal.Czlowiek import Czlowiek
from Entities.Plant.Guarana import Guarana
from Entities.Animal.Lis import Lis
from Entities.Plant.Mlecz import Mlecz
from Entities.Animal.Owca import Owca
from Entities.Plant.Trawa import Trawa
from Entities.Plant.WilczeJagody import WilczeJagody
from Entities.Animal.Wilk import Wilk
from Entities.Animal.Zolw import Zolw
from .swiat import Swiat

class Saver:
    def __init__(self, swiat):
        self.swiat = swiat

    def savestate(self):
        try:
            with open('./plik.txt', 'w') as file:
                file.write(str(self.swiat.getTura()) + '\n')
                file.write(str(self.swiat.getHeight()) + '\n')
                file.write(str(self.swiat.getWidth()) + '\n')
                organizmy = self.swiat.getAllOrganizmy()
                for org in organizmy:
                    if isinstance(org, Czlowiek):
                        file.write(f"{org.get_ID()},{org.get_x()},{org.get_y()},{org.get_sila()},{org.get_wiek()},{org.cooldown}\n")
                    else:
                        file.write(f"{org.get_ID()},{org.get_x()},{org.get_y()},{org.get_sila()},{org.get_wiek()}\n")
        except:
            self.swiat.logger.addLog("Failed to save")
        else:
            self.swiat.logger.addLog("Saved!")

    def loadstate(self):
        try:
            with open('./plik.txt', 'r') as file:
                lines = file.readlines()
                tura = int(lines[0].strip())
                height = int(lines[1].strip())
                width = int(lines[2].strip())

                screen = self.swiat.getScreen()
                logger = self.swiat.logger
                pygame = self.swiat.getGame()

                nowy_swiat = Swiat(width, height, screen, logger, pygame)
                nowy_swiat.tura = tura

                organizmy_data = lines[3:]
                for line in organizmy_data:
                    parts = list(map(int, line.strip().split(',')))
                    id, x, y, sila, wiek = parts[:5]
                    cooldown = parts[5] if id == 1 and len(parts) > 5 else None
                    self.dodaj_organizm_z_id(id, x, y, sila, wiek, nowy_swiat, cooldown)

                self.swiat = nowy_swiat
        except:
            self.swiat.logger.addLog("Failed to load")
        else:
            self.swiat.logger.addLog("Loaded!")
    def dodaj_organizm_z_id(self, id, x, y, sila, wiek, swiat, cooldown=None):
        id_to_animal = {
            1: Czlowiek,
            2: Owca,
            3: Wilk,
            4: Lis,
            5: Antylopa,
            6: Zolw,
            7: Trawa,
            8: Mlecz,
            9: WilczeJagody,
            10: Guarana,
            11: BarszczSosnowskiego,
            12: CyberOwca
        }
        if id in id_to_animal:
            zwierze_klasa = id_to_animal[id]
            zwierze = zwierze_klasa(x, y, swiat, swiat.logger)
            zwierze.set_sila(sila)
            zwierze.set_wiek(wiek)
            if isinstance(zwierze, Czlowiek) and cooldown is not None:
                zwierze.setCooldown(cooldown)
            swiat.dodaj_organizm(zwierze)

    def get_swiat(self):
        return self.swiat