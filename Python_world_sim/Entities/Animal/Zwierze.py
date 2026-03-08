from Entities.Organizm import Organizm


class Zwierze(Organizm):

    def __init__(self, nazwa, sila, inicjatywa, x, y, kolor, swiatref, logger, ID):
        super(Zwierze, self).__init__(nazwa, sila, inicjatywa, x, y, kolor, swiatref, logger, ID)
        self.prevx = x
        self.prevy = y

    def rozmnoz(self):
        if not self.rozmnozony and self.swiatref.czyMaxOrganizmow():
            newx = self.randomize_num(self.x, 1)
            newy = self.randomize_num(self.y, 1)

            while newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight() or (
                    newx == self.x or newy == self.y):
                newx = self.randomize_num(self.x, 1)
                newy = self.randomize_num(self.y, 1)

            self.stworz_nowy(newx, newy)
            self.logger.addLog(self.nazwa + " sie rozmnozyl: " + str(newx) + " , " + str(newy))

            self.rozmnozony = True

    def kolizja(self, other):
        if other.is_alive():
            if type(self) is type(other):
                self.rozmnoz()
            else:
                if not other.odpornosc(self):
                    if self.sila > other.get_sila():
                        self.logger.addLog(self.nazwa + " ponkonal " + other.get_nazwa())
                        other.die()

    def ruch(self):
        newx = self.randomize_num(self.x, 1)
        newy = self.randomize_num(self.y, 1)

        while newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight():
            newx = self.randomize_num(self.x, 1)
            newy = self.randomize_num(self.y, 1)

        self.x = newx
        self.y = newy
        self.logger.addLog(self.nazwa + " poszedl do: " + str(self.x) + " , " + str(self.y))

    def cofnijRuch(self):
        self.x = self.prevx
        self.y = self.prevy

    def akcja(self):
        self.prevx = self.x
        self.prevy = self.y
        self.rozmnozony = False
        self.ruch()
        self.wiek += 1

    def spchniecie(self):
        newx = self.randomize_num(self.x, 1)
        newy = self.randomize_num(self.y, 1)

        while (newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight()) and(newx!=self.x and newy!=self.y):
            newx = self.randomize_num(self.x, 1)
            newy = self.randomize_num(self.y, 1)

        self.x = newx
        self.y = newy
        self.logger.addLog(self.nazwa + "zostal spchniety: "+str(newx)+" , "+str(newy))

    def cofnijRuch(self):
        self.x=self.prevx
        self.y=self.prevy
