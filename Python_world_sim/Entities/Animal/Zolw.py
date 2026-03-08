import random

from .Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, x, y, swiatref, logger):
        super(Zolw, self).__init__("zolw", 2, 1, x, y, (100, 255, 100), swiatref, logger, 6)

    def stworz_nowy(self, x, y):
        nowyorg = Zolw(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(nowyorg)

    def kolizja(self, other):
        if other.is_alive():
            if type(self) is type(other):
                self.rozmnoz()
            else:
                if not other.odpornosc(self):
                    if self.sila > other.get_sila():
                        self.logger.addLog(self.nazwa + " ponkonal " + other.get_nazwa())
                        other.die()
                    else:
                        if other.get_sila()<5 and isinstance(other,Zwierze):
                            other.cofnijRuch()

    def akcja(self):
        self.prevx = self.x
        self.prevy = self.y
        self.rozmnozony = False
        if random.random() < 0.25:
            self.ruch()
        self.wiek += 1

    def odpornosc(self, other):
        if other.get_sila()<5:
            if isinstance(other,Zwierze):
                self.logger.addLog(self.nazwa + " odparl atak " + other.get_nazwa())
            return True
        else:
            return False

