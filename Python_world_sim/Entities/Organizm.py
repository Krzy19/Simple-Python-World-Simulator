from abc import ABC, abstractmethod
import random

class Organizm(ABC):
    def __init__(self, nazwa, sila, inicjatywa, x, y, kolor, swiatref, logger, ID):
        self.nazwa = nazwa
        self.alive = True
        self.rozmnozony = True
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.x = x
        self.y = y
        self.wiek = 0
        self.kolor = kolor
        self.swiatref = swiatref
        self.logger = logger
        self.ID = ID

    def akcja(self):
        self.wiek += 1

    def kolizja(self, other):
        if type(self) != type(other) and other.is_alive():
            if self.sila > other.get_sila():
                self.logger.addLog(self.nazwa + " ponkonal " + other.get_nazwa())
                other.die()

    def rysuj(self):
        self.swiatref.getGame().draw.rect(self.swiatref.getScreen(), self.kolor, (self.x*20, self.y*20, 20, 20))

    def die(self):
        self.alive = False
        self.logger.addLog(self.nazwa + "zginal")

    @abstractmethod
    def stworz_nowy(self, x, y):
        pass

    def randomize_num(self, num, range_):
        return num + random.randint(-range_, range_)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_sila(self):
        return self.sila

    def get_inicjatywa(self):
        return self.inicjatywa

    def get_wiek(self):
        return self.wiek

    def set_sila(self, new_sila):
        self.sila = new_sila

    def get_nazwa(self):
        return self.nazwa

    def get_ID(self):
        return self.ID

    def odpornosc(self, other):
        return False

    def zatruj(self,other):
        if not other.odpornosc(self):
            other.die()


    def is_alive(self):
        return self.alive

    def is_rozmnozony(self):
        return self.rozmnozony

    def set_wiek(self, wiek):
        self.wiek = wiek
