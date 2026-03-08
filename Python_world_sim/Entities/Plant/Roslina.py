import random

from Entities.Organizm import Organizm


class Roslina(Organizm):

    def __init__(self, nazwa, sila, x, y, kolor, swiatref, logger, ID):
        super(Roslina, self).__init__(nazwa, sila, 0, x, y, kolor, swiatref, logger, ID)
        self.prevx = x
        self.prevy = y
        self.rozmnozony = True

    def kolizja(self, other):
        if other.is_alive():
            if not other.odpornosc(self):
                if self.sila > other.get_sila():
                    self.logger.addLog(self.nazwa + " ponkonal " + other.get_nazwa())
                    other.die()

    def rozsiej(self):
        if self.swiatref.czyMaxOrganizmow() and not self.rozmnozony:
            newx = self.randomize_num(self.x, 1)
            newy = self.randomize_num(self.y, 1)

            while newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight() and \
                    newx != self.x and newy != self.y:
                newx = self.randomize_num(self.x, 1)
                newy = self.randomize_num(self.y, 1)

            if not self.swiatref.czyZajete(newx, newy):
                self.logger.addLog(self.nazwa + " rozsial sie: " + str(newx) + " , " + str(newy))
                self.stworz_nowy(newx, newy)

    def akcja(self):
        self.prevx = self.x
        self.prevy = self.y
        if random.random() < 0.5:
            self.rozsiej()
        self.rozmnozony = False
        self.wiek += 1

    def rysuj(self):
        self.swiatref.getGame().draw.circle(self.swiatref.getScreen(), self.kolor, (self.x * 20 + 10, self.y * 20 + 10),
                                            10)
