import random
import tkinter
from tkinter import simpledialog

import pygame

from WorldManager.Saver import Saver
from Entities.Animal.Wilk import Wilk

from Entities.Animal.CyberOwca import CyberOwca
from Entities.Animal.Antylopa import Antylopa
from Entities.Plant.BarszczSosnowskiego import BarszczSosnowskiego
from Entities.Animal.Czlowiek import Czlowiek
from Entities.Plant.Guarana import Guarana
from WorldManager.Initializer import Initializer
from Entities.Animal.Lis import Lis
from Entities.Animal.Owca import Owca
from Entities.Plant.Trawa import Trawa
from Entities.Plant.Mlecz import Mlecz
from Entities.Plant.WilczeJagody import WilczeJagody
from Entities.Animal.Zolw import Zolw
from WorldManager.swiat import Swiat
from Entities.Komentator import Komentator

def wyswietlSwiat():
    swiat.rysujSwiat()
    wypiszTekst("Tura: " + str(swiat.getTura()), 0)
    logger.wypiszLogi()
    logger.clearLogger()
    pygame.display.flip()

def wypiszTekst(tekst,przesuniencie):
    text_surface = font.render(tekst, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.center = (width*20+50, 5+przesuniencie*5)
    screen.blit(text_surface, text_rect)

def dodaj_zwierze(id, x, y, swiat, logger):
    id_to_animal = {
        1: Czlowiek,
        2: Owca,
        3: Wilk,
        4: Lis,
        5: Antylopa,
        6: Zolw,
        7: Trawa,
        8: Mlecz,
        9: WilczeJagody,
        10: Guarana,
        11: BarszczSosnowskiego,
        12: CyberOwca
    }
    if id in id_to_animal:
        zwierze_klasa = id_to_animal[id]
        zwierze = zwierze_klasa(x, y, swiat, logger)
        swiat.dodaj_organizm(zwierze)



dialog = Initializer()
values = dialog.get_initial_values()

width = values['width']
height = values['height']

pygame.init()
screen = pygame.display.set_mode((width * 20 + 150, height * 20))
clock = pygame.time.Clock()
pygame.display.set_caption('World simulation')
running = True



logger = Komentator(screen,width)
swiat = Swiat(width, height, screen, logger, pygame)
saver=Saver(swiat)

def dodaj_losowe_zwierzeta(id, ile, swiat, logger):
    for _ in range(ile):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        dodaj_zwierze(id, x, y, swiat, logger)

if values['ileczlowiek']:
    dodaj_losowe_zwierzeta(1, values['ileczlowiek'], swiat, logger)
dodaj_losowe_zwierzeta(2, values['ileowca'], swiat, logger)
dodaj_losowe_zwierzeta(3, values['ilewilk'], swiat, logger)
dodaj_losowe_zwierzeta(4, values['ilelis'], swiat, logger)
dodaj_losowe_zwierzeta(5, values['ileantylopa'], swiat, logger)
dodaj_losowe_zwierzeta(6, values['ilezolw'], swiat, logger)
dodaj_losowe_zwierzeta(7, values['iletrawa'], swiat, logger)
dodaj_losowe_zwierzeta(8, values['ilemlecz'], swiat, logger)
dodaj_losowe_zwierzeta(9, values['ilewilcze'], swiat, logger)
dodaj_losowe_zwierzeta(10, values['ileguarana'], swiat, logger)
dodaj_losowe_zwierzeta(11, values['ilebarszcz'], swiat, logger)
dodaj_losowe_zwierzeta(12, values['ilecyberowca'], swiat, logger)

def open_context_menu(x, y):
    root = tkinter.Tk()
    root.withdraw()

    options = {
        "Człowiek": 1,
        "Owca": 2,
        "Wilk": 3,
        "Lis": 4,
        "Antylopa": 5,
        "Żółw": 6,
        "Trawa": 7,
        "Mlecz": 8,
        "Wilcze Jagody": 9,
        "Guarana": 10,
        "Barszcz Sosnowskiego": 11,
        "Cyber Owca": 12
    }

    animal = simpledialog.askstring("Dodaj zwierzę", "Wybierz zwierzę:\n" + "\n".join(options.keys()))
    if animal in options:
        if not swiat.czyZajete(x,y):
            dodaj_zwierze(options[animal], x, y, swiat, logger)

    root.destroy()

font = pygame.font.Font(None, 16)
inputpassed=False

#pierwsza pętla
swiat.rysujSwiat()
wypiszTekst("Tura: "+str(swiat.getTura()),0)
pygame.display.flip()
clock.tick(60)

while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            inputpassed = True
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                swiat.setInput("w")
            elif event.key == pygame.K_DOWN:
                swiat.setInput("s")
            elif event.key == pygame.K_LEFT:
                swiat.setInput("a")
            elif event.key == pygame.K_RIGHT:
                swiat.setInput("d")
            elif event.key == pygame.K_f:
                swiat.setInput("f")
            elif event.key == pygame.K_s:
                inputpassed = False
                saver.savestate()
                wyswietlSwiat()

            elif event.key == pygame.K_l:
                saver.loadstate()
                swiat=saver.get_swiat()
                screen = pygame.display.set_mode((swiat.getWidth() * 20 + 150, swiat.getHeight() * 20))
                inputpassed = False
                wyswietlSwiat()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                inputpassed=False
                mouse_x, mouse_y = event.pos
                grid_x = mouse_x // 20
                grid_y = mouse_y // 20
                print(str(grid_x)+","+str(grid_y))
                if grid_x > 0 and grid_y >0 and grid_x < width and grid_y < height:
                    open_context_menu(grid_x, grid_y)
                    swiat.rysujSwiat()
                    pygame.display.flip()
    if(inputpassed):
        swiat.wykonajTure()
        wyswietlSwiat()
        clock.tick(60)
        inputpassed=False


pygame.quit()