from .Zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, x, y, swiatref, logger):
        super(Lis, self).__init__("lis", 3, 7, x, y, (255, 60, 0), swiatref, logger, 4)

    def stworz_nowy(self, x, y):
        nowyorg = Lis(x, y, self.swiatref, self.logger)
        self.swiatref.dodaj_organizm(nowyorg)

    def ruch(self):

        newx = self.randomize_num(self.x, 1)
        newy = self.randomize_num(self.y, 1)

        zablokowane = False

        organizmy = self.swiatref.getOrganizmyXY(newx,newy)
        for organizm in organizmy:
            if organizm.x == newx and organizm.y == newy and organizm.sila > self.sila:
                zablokowane = True
                break

        while newx < 0 or newx >= self.swiatref.getWidth() or newy < 0 or newy >= self.swiatref.getHeight() or zablokowane:

            zablokowane = False

            newx = self.randomize_num(self.x, 1)
            newy = self.randomize_num(self.y, 1)

            organizmy = self.swiatref.getOrganizmyXY(newx,newy)
            for organizm in organizmy:
                if organizm.x == newx and organizm.y == newy and organizm.sila > self.sila:
                    zablokowane = True
                    break

        self.x = newx
        self.y = newy
        self.logger.addLog(self.nazwa + " poszedl do: " + str(self.x) + " , " + str(self.y))
