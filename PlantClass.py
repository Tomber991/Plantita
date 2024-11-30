import pygame
import config
import utils

pygame.init()

class Plant:
    def __init__(self):
        # Inicializar valores predeterminados
        self.estage_main = 0
        self.life_time = 0
        self.atributes = {
            "agua": 100,
            "luz": 100,
            "nutrientes": 100
        }

        # Intentar cargar el estado guardado
        try:
            utils.load_state(self)
        except FileNotFoundError:
            print("No se encontró un estado guardado, iniciando nueva planta.")
        except Exception as e:
            print(f"Error al cargar estado: {e}")

        self.grafics = [
            pygame.image.load("images/semilla.png"),
            pygame.image.load("images/brote.png"),
            pygame.image.load("images/planta_pequena.png"),
            pygame.image.load("images/planta_grande.png")
        ]
        self.time = pygame.time.Clock()

    def update(self):
        self.life_time += self.time.tick(30) / 1000  # Tiempo en segundos

        # Reducir los atributos lentamente
        self.atributes["agua"] = max(0, self.atributes["agua"] - 0.02)
        self.atributes["luz"] = max(0, self.atributes["luz"] - 0.01)
        self.atributes["nutrientes"] = max(0, self.atributes["nutrientes"] - 0.005)

        # Crecimiento por etapas
        if self.life_time >= (self.estage_main + 1) * 30 and self.estage_main < len(self.grafics) - 1:
            self.estage_main += 1

        # Condición de muerte
        if any(attr <= 0 for attr in self.atributes.values()):
            print("¡Tu plantita murió por falta de cuidado! 😢")
            config.Running = False

    def draw(self, pantalla):
        pantalla.fill(config.BLANCO)

        try:
            plant_ins = self.grafics[self.estage_main]
            pantalla.blit(plant_ins, (10, 5))
        except IndexError:
            print("Error al dibujar planta: índice fuera de rango.")
            return

        # Mostrar los atributos
        texto_tiempo = config.fuente.render(f"Tiempo de vida: {int(self.life_time)}s", True, config.NEGRO)
        pantalla.blit(texto_tiempo, (200, 5))

        texto_agua = config.fuente.render(f"Agua: {int(self.atributes['agua'])}%", True, config.AZUL)
        pantalla.blit(texto_agua, (200, 25))

        texto_luz = config.fuente.render(f"Luz: {int(self.atributes['luz'])}%", True, config.VERDE)
        pantalla.blit(texto_luz, (200, 45))

        texto_nutrientes = config.fuente.render(f"Nutrientes: {int(self.atributes['nutrientes'])}%", True, config.NEGRO)
        pantalla.blit(texto_nutrientes, (200, 65))

        pygame.display.flip()
