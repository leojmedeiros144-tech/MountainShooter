from tkinter import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            pass

            # CHeck for all events
            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.quit()  # Close Window
               #     quit()  # End pygame
