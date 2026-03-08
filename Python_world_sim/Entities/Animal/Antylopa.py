import random

from .Zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, x, y, swiatref, logger):
        super(Antylopa, self).__init__("antylopa", 4, 4, x, y, (255, 204, 102), swiatref, logger, 5)

    def stworz_nowy(self, x, y):
        nowyorg = Antylopa(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(nowyorg)

    def ruch(self):
        newx = self.randomize_num(self.x, 2)
        newy = self.randomize_num(self.y, 2)

        while newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight():
            newx = self.randomize_num(self.x, 2)
            newy = self.randomize_num(self.y, 2)

        self.x = newx
        self.y = newy

    def odpornosc(self, other):
        if random.random() < 0.5:
            self.logger.addLog(self.nazwa + " odparla atak")
            return True
        else:
            return False

    def kolizja(self, other):
        if other.is_alive():
            if type(self) is type(other):
                self.rozmnoz()
            else:
                if not other.odpornosc(self):
                    if self.sila > other.get_sila():
                        other.die()
                    else:
                        newx = self.randomize_num(self.x, 1)
                        newy = self.randomize_num(self.y, 1)

                        zablokowane = False

                        if self.swiatref.czyZajete(newx, newy):
                            zablokowane = True

                        max_proby=99

                        while newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight() or zablokowane:

                            zablokowane = False

                            newx = self.randomize_num(self.x, 1)
                            newy = self.randomize_num(self.y, 1)

                            organizmy = self.swiatref.getOrganizmyXY(newx,newy)
                            for organizm in organizmy:
                                if organizm.x == newx and organizm.y == newy and isinstance(organizm, Zwierze.Zwierze):
                                    zablokowane = True
                                    break
                            max_proby-=1
                            if max_proby<=0:
                                break

                        self.x = newx
                        self.y = newy
                        self.logger.addLog(self.nazwa + " poszedl do: " + str(self.x) + " , " + str(self.y))
