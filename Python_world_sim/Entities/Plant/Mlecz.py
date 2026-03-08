import random

from .Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self,x,y,swiatref,logger):
        super(Mlecz, self).__init__("mlecz",0,x,y,(150,200,0),swiatref,logger,8)

    def stworz_nowy(self, x, y):
        neworg = Mlecz(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(neworg)

    def akcja(self):
        self.prevx = self.x
        self.prevy = self.y
        if random.random() < 0.5:
            self.rozsiej()
        if random.random() < 0.5:
            self.rozsiej()
        if random.random() < 0.5:
             self.rozsiej()
        self.rozmnozony = False
        self.wiek += 1