import pygame

class Komentator:
    def __init__(self, screen, width):
        self.screen = screen
        self.width = width
        self.logList = []
        self.font = pygame.font.Font(None, 16)

    def wypiszTekst(self, tekst, przesuniencie):
        text_surface = self.font.render(tekst, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.width * 20 + 50, 5 + przesuniencie * 8)
        self.screen.blit(text_surface, text_rect)

    def addLog(self, log):
        self.logList.append(log)

    def wypiszLogi(self):
        for i, log_entry in enumerate(self.logList, start=1):
            self.wypiszTekst(log_entry, i)

    def clearLogger(self):
        self.logList.clear()