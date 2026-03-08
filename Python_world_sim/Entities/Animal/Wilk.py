from .Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self,x,y,swiatref,logger):
        super(Wilk, self).__init__("wilk",9,5,x,y,(20,20,20),swiatref,logger,3)

    def stworz_nowy(self, x, y):
        nowyorg = Wilk(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(nowyorg)