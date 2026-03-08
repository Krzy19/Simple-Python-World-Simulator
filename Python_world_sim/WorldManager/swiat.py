from Entities.Plant.Roslina import Roslina


class Swiat:
    def __init__(self,width,heigh,screen,logger,pygame):
        self.width=width
        self.height=heigh
        self.tura=0
        self.screen=screen
        self.input=""
        self.organizmy=[]
        self.logger=logger
        self.pygame=pygame


    def dodaj_organizm(self, organizm):
        self.organizmy.append(organizm)

    def rysujSwiat(self):
        self.screen.fill((200,200,200))
        for org in self.organizmy:
            org.rysuj()


    def wykonajTure(self):
        self.wykonajAkcje()
        self.wykonajKolizje()
        self.usunMartwe()
        self.input=""
        self.tura+=1

    def wykonajAkcje(self):
        self.organizmy.sort(key=lambda organizm: (organizm.get_inicjatywa(), organizm.get_wiek()), reverse=True)
        for org in self.organizmy:
            org.akcja()

    def wykonajKolizje(self):
        for y in range(self.height):
            for x in range(self.width):
                kolejka = [org for org in self.organizmy if org.get_x() == x and org.get_y() == y]

                if len(kolejka) > 1:
                    kolejka.sort(key=lambda organizm: (organizm.get_inicjatywa(), organizm.get_wiek()), reverse=True)

                    for org in kolejka:
                        for other in kolejka:
                            if org is not other and org.is_alive() and other.is_alive():
                                org.kolizja(other)
                                if isinstance(other, Roslina):
                                    other.kolizja(org)




    def usunMartwe(self):
        self.organizmy = [organizm for organizm in self.organizmy if organizm.is_alive()]

    def setInput(self,newinput):
        self.input=newinput

    def getInput(self):
        return self.input

    def getTura(self):
        return self.tura

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    def getScreen(self):
        return self.screen

    def getGame(self):
        return self.pygame

    def czyMaxOrganizmow(self):
        return len(self.organizmy) < 1000

    def czyZajete(self,x,y):
        for organizm in self.organizmy:
            if organizm.get_x() == x and organizm.get_y() == y:
                return True
        return False

    def getOrganizmyXY(self,x,y):
        return [organizm for organizm in self.organizmy if organizm.get_x() == x and organizm.get_y() == y]

    def getAllOrganizmy(self):
        return self.organizmy


