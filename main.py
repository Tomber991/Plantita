import pygame
import sys
import config
import utils
from PlantClass import Plant

class App:
    def __init__(self):
        pygame.init()
        config.Running = True
        config.pantalla = pygame.display.set_mode((400, 200))
        pygame.display.set_caption("Cuidado de Plantas")

        self.plant = Plant()
        self.Time = pygame.time.Clock()

    def draw(self):
        self.plant.draw(config.pantalla)

    def update(self):
        while config.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    utils.save_state(self.plant)
                    config.Running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        utils.save_state(self.plant)
                        config.Running = False
                        pygame.quit()
                        sys.exit()

                    # Controlar los atributos con teclas
                    if event.key == pygame.K_r:
                        self.plant.atributes["agua"] = min(100, self.plant.atributes["agua"] + 20)
                    if event.key == pygame.K_l:
                        self.plant.atributes["luz"] = min(100, self.plant.atributes["luz"] + 20)
                    if event.key == pygame.K_n:
                        self.plant.atributes["nutrientes"] = min(100, self.plant.atributes["nutrientes"] + 20)

            self.plant.update()
            self.draw()
            self.Time.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = App()
    app.update()
