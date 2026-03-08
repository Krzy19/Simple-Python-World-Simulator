from .Roslina import Roslina


class Guarana(Roslina):
    def __init__(self,x,y,swiatref,logger):
        super(Guarana, self).__init__("guarana",0,x,y,(0,100,50),swiatref,logger,10)

    def kolizja(self, other):
        if other.is_alive():

            other.set_sila(other.get_sila()+5)
            self.logger.addLog(self.nazwa + " zwiekszyl sile " + other.get_nazwa() + " do " +str(other.get_sila()))
            if not other.odpornosc(self):
                if self.sila > other.get_sila():
                    other.die()


    def stworz_nowy(self, x, y):
        neworg = Guarana(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(neworg)