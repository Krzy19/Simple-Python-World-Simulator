from .Roslina import Roslina


class Trawa(Roslina):
    def __init__(self,x,y,swiatref,logger):
        super(Trawa, self).__init__("trawa",0,x,y,(0,200,0),swiatref,logger,7)

    def stworz_nowy(self, x, y):
        neworg = Trawa(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(neworg)