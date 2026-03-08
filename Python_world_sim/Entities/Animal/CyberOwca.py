from Entities.Plant.BarszczSosnowskiego import BarszczSosnowskiego
from .Zwierze import Zwierze


class CyberOwca(Zwierze):
    def __init__(self,x,y,swiatref,logger):
        super(CyberOwca, self).__init__("cyber owca",11,4,x,y,(100,100,120),swiatref,logger,12)

    def stworz_nowy(self, x, y):
        nowa_owca = CyberOwca(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(nowa_owca)

    def znajdz_najblizszego_barszcz(self):
        najblizszy_barszcz = None
        najmniejsza_odleglosc = float('inf')

        for organizm in self.swiatref.organizmy:
            if isinstance(organizm, BarszczSosnowskiego):
                odleglosc = abs(self.x - organizm.get_x()) + abs(self.y - organizm.get_y())
                if odleglosc < najmniejsza_odleglosc:
                    najmniejsza_odleglosc = odleglosc
                    najblizszy_barszcz = organizm

        return najblizszy_barszcz

    def zbierz_sie_do(self, cel_x, cel_y):
        nowy_x = self.x
        nowy_y = self.y

        if cel_x > nowy_x:
            nowy_x += 1
        elif cel_x < nowy_x:
            nowy_x -= 1

        if cel_y > nowy_y:
            nowy_y += 1
        elif cel_y < nowy_y:
            nowy_y -= 1

        return nowy_x, nowy_y

    def ruch(self):
        najblizszy_barszcz = self.znajdz_najblizszego_barszcz()
        if najblizszy_barszcz:
            self.logger.addLog(self.nazwa + " znalazla barszcz ")
            self.x, self.y = self.zbierz_sie_do(najblizszy_barszcz.get_x(), najblizszy_barszcz.get_y())
            self.logger.addLog(self.nazwa + " zbliża się do BarszczuSosnowskiego: " + str(self.x) + " , " + str(self.y))
        else:
            self.normalruch()

    def normalruch(self):
        newx = self.randomize_num(self.x, 1)
        newy = self.randomize_num(self.y, 1)

        while newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight():
            newx = self.randomize_num(self.x, 1)
            newy = self.randomize_num(self.y, 1)

        self.x = newx
        self.y = newy
        self.logger.addLog(self.nazwa + " poszedl do: " + str(self.x) + " , " + str(self.y))

    def kolizja(self, other):
        if other.is_alive():
            if type(self) is type(other):
                self.rozmnoz()
            else:
                if not other.odpornosc(self):
                    if isinstance(other,BarszczSosnowskiego):
                        self.logger.addLog(self.nazwa + " ponkonal " + other.get_nazwa())
                        other.die()
                    else:
                        if 4 > other.get_sila():
                            self.logger.addLog(self.nazwa + " ponkonal " + other.get_nazwa())
                            other.die()


    def odpornosc(self, other):
        if isinstance(other,BarszczSosnowskiego):
            return True
        else:
            return False