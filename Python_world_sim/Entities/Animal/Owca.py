from .Zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self,x,y,swiatref,logger):
        super(Owca, self).__init__("owca",4,4,x,y,(60,60,60),swiatref,logger,2)

    def stworz_nowy(self, x, y):
        nowa_owca = Owca(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(nowa_owca)