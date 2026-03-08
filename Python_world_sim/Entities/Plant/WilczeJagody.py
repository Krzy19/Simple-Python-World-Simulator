from .Roslina import Roslina


class WilczeJagody(Roslina):
    def __init__(self,x,y,swiatref,logger):
        super(WilczeJagody, self).__init__("wilcze jagody",99,x,y,(30,0,100),swiatref,logger,9)

    def kolizja(self, other):
        if other.is_alive():
            if not other.odpornosc(self):
                other.die()


    def stworz_nowy(self, x, y):
        neworg = WilczeJagody(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(neworg)