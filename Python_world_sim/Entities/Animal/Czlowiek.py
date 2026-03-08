from .Zwierze import Zwierze


class Czlowiek(Zwierze):
    COOLDOWN_TIME = 10
    POWER_TIME = 5

    def __init__(self, x, y, swiatref, logger):
        super(Czlowiek, self).__init__("czlowiek", 5, 4, x, y, (255, 0, 0), swiatref, logger, 1)
        self.cooldown = 0
        self.powertime = 0
        self.activespecjal = False

    def akcja(self):
        self.prevx = self.x
        self.prevy = self.y

        if self.alive:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.activespecjal:
                if self.powertime > 0:
                    self.powertime -= 1
                if self.powertime == 0:
                    self.logger.addLog("moc sie skonczyla...")
                    self.activespecjal = False
            if self.swiatref.getInput() == "w":
                self.y -= 1
            if self.swiatref.getInput() == "s":
                self.y += 1
            if self.swiatref.getInput() == "a":
                self.x -= 1
            if self.swiatref.getInput() == "d":
                self.x += 1
            if self.swiatref.getInput() == "f":
                if self.cooldown > 0 or self.powertime > 0:
                    self.logger.addLog("nie mozesz jeszcze uzyc mocy...")
                else:
                    self.logger.addLog("aktywowano moc!")
                    self.activespecjal = True
                    self.powertime = self.POWER_TIME
                    self.cooldown = self.COOLDOWN_TIME
            if self.x < 0: self.x += 1
            if self.y < 0: self.y += 1
            if self.x >= self.swiatref.getWidth(): self.x -= 1
            if self.y >= self.swiatref.getHeight(): self.y -= 1

        self.wiek += 1

    def odpornosc(self, other):
        if self.activespecjal and isinstance(other, Zwierze):
            return True
        else:
            return False

    def kolizja(self, other):
        if other.is_alive():
            if type(self) is type(other):
                self.rozmnoz()
            else:
                if not other.odpornosc(self):
                    if self.sila > other.get_sila():
                        other.die()
                    else:
                        if isinstance(other, Zwierze):
                            if self.activespecjal:
                                other.spchniecie()

    def stworz_nowy(self, x, y):
        pass

    def setCooldown(self,cooldown):
        self.cooldown=cooldown
        self.powertime=cooldown-5
        if self.powertime>0:
            self.activespecjal=True
        if self.powertime<0:
            self.powertime=0

    def rysuj(self):
        if self.activespecjal:
            self.swiatref.getGame().draw.rect(self.swiatref.getScreen(), (255,255,0), (self.x * 20, self.y * 20, 20, 20))
        else:
            self.swiatref.getGame().draw.rect(self.swiatref.getScreen(), self.kolor, (self.x*20, self.y*20, 20, 20))

