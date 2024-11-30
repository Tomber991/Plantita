import pygame
import config

pygame.init()

class Plant:
    def __init__(self):
        try:
            self.grafics = [
                pygame.image.load("images/semilla.png"),
                pygame.image.load("images/brote.png"),
                pygame.image.load("images/planta_pequena.png"),
                pygame.image.load("images/planta_grande.png")
            ]
        except pygame.error as e:
            print(f"Error al cargar las imágenes: {e}")
            sys.exit()

        self.estage_main = 0
        self.life_time = 0
        self.atributes = {
            "agua": 100,
            "luz": 100,
            "nutrientes": 100
        }
        self.time = pygame.time.Clock()

    def update(self):
        self.life_time += self.time.tick(30) / 1000  # Tiempo en segundos
        self.atributes["agua"] = max(0, self.atributes["agua"] - 0.1)
        self.atributes["luz"] = max(0, self.atributes["luz"] - 0.05)
        self.atributes["nutrientes"] = max(0, self.atributes["nutrientes"] - 0.03)

        if self.life_time >= (self.estage_main + 1) * 10 and self.estage_main < len(self.grafics) - 1:
            self.estage_main += 1        

        if self.atributes["agua"] <= 0 or self.atributes["luz"] <= 0 or self.atributes["nutrientes"] <= 0:
            print("¡Tu plantita murió por falta de cuidado! 😢")
            config.Running = False

    def draw(self, pantalla):
        pantalla.fill(config.BLANCO)

        plant_ins = self.grafics[self.estage_main]
        pantalla.blit(plant_ins, (100, 200))

        texto_tiempo = config.fuente.render(f"Tiempo de vida: {self.life_time:.2f}s", True, config.NEGRO)
        pantalla.blit(texto_tiempo, (400, 50))

        texto_agua = config.fuente.render(f"Agua: {self.atributes['agua']}%", True, config.AZUL)
        pantalla.blit(texto_agua, (400, 100))

        texto_luz = config.fuente.render(f"Luz: {self.atributes['luz']}%", True, config.VERDE)
        pantalla.blit(texto_luz, (400, 150))

        texto_nutrientes = config.fuente.render(f"Nutrientes: {self.atributes['nutrientes']}%", True, config.NEGRO)
        pantalla.blit(texto_nutrientes, (400, 200))
        
        pygame.display.flip()
