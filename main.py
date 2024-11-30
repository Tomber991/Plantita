import pygame
import time
import config
import sys
import PlantClass

class App:
    def __init__(self):
        pygame.init()
        config.Running = True
        config.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cuidado de Plantas")

        self.plant = PlantClass.Plant()
        self.time = pygame.time.Clock()

    def draw(self):
        self.plant.draw(config.pantalla)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    config.Running = False
                elif event.key == pygame.K_r:
                    self.plant.atributes["agua"] = min(100, self.plant.atributes["agua"] + 20)
                elif event.key == pygame.K_l:
                    self.plant.atributes["luz"] = min(100, self.plant.atributes["luz"] + 20)
                elif event.key == pygame.K_n:
                    self.plant.atributes["nutrientes"] = min(100, self.plant.atributes["nutrientes"] + 20)

    def update(self):
        while config.Running:
            self.handle_events()
            self.plant.update()
            self.draw()
            self.time.tick(30)  # Limitar a 30 FPS

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = App()
    app.update()
