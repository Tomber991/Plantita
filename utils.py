import json
import time

def save_state(plant):
    state = {
        "estage_main": plant.estage_main,
        "life_time": plant.life_time,
        "atributes": plant.atributes,
        "last_saved_time": time.time()  # Guardar el tiempo actual en segundos
    }
    with open("plant_state.json", "w") as file:
        json.dump(state, file)
    print("Estado guardado.")

def load_state(plant):
    with open("plant_state.json", "r") as file:
        state = json.load(file)

    plant.estage_main = state["estage_main"]
    plant.life_time = state["life_time"]
    plant.atributes = state["atributes"]

    # Calcular el tiempo transcurrido desde el último guardado
    last_saved_time = state["last_saved_time"]
    elapsed_time = time.time() - last_saved_time

    print(f"Tiempo transcurrido desde el cierre: {int(elapsed_time)} segundos.")

    # Aplicar el impacto del tiempo transcurrido a los atributos y al tiempo de vida
    plant.life_time += elapsed_time
    plant.atributes["agua"] = max(0, plant.atributes["agua"] - elapsed_time * 0.02)
    plant.atributes["luz"] = max(0, plant.atributes["luz"] - elapsed_time * 0.01)
    plant.atributes["nutrientes"] = max(0, plant.atributes["nutrientes"] - elapsed_time * 0.005)
