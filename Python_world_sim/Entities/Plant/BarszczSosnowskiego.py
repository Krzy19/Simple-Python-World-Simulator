from .Roslina import Roslina
from Entities.Animal.Zwierze import Zwierze


class BarszczSosnowskiego(Roslina):
    def __init__(self,x,y,swiatref,logger):
        super(BarszczSosnowskiego, self).__init__("wilcze jagody",8,x,y,(50,0,25),swiatref,logger,11)

    def kolizja(self, other):
        if other.is_alive():
            if not other.odpornosc(self):
                other.die()


    def stworz_nowy(self, x, y):
        neworg = BarszczSosnowskiego(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(neworg)

    def polerazenia(self):
        for y in range(-1, 2):
            for x in range(-1,2):
                if(y!=0 and x!=0):
                    xd=self.x+x
                    yd=self.y+y
                    for org in self.swiatref.getOrganizmyXY(xd,yd):
                        if isinstance(org,Zwierze):
                            self.zatruj(org)



    def akcja(self):
        self.polerazenia()
        super(BarszczSosnowskiego, self).akcja()