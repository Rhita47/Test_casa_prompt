import math
import random

class Castillo:
    def __init__(self, nombre, coordenadas=None):
        self.nombre = nombre
        self.coordenadas = coordenadas if coordenadas is not None else (random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(0, 50))

    def __str__(self):
        return f"{self.nombre}: {self.coordenadas}"

    def galaxia(self):
        x, y, z = self.coordenadas
        if x >= 0 and y >= 0 and z >= 0:
            return "Galaxia A"
        elif x < 0 and y >= 0 and z >= 0:
            return "Galaxia B"
        elif x >= 0 and y < 0 and z >= 0:
            return "Galaxia C"
        elif x < 0 and y < 0 and z >= 0:
            return "Galaxia D"
        elif x >= 0 and y >= 0 and z < 0:
            return "Galaxia E"
        elif x < 0 and y >= 0 and z < 0:
            return "Galaxia F"
        elif x >= 0 and y < 0 and z < 0:
            return "Galaxia G"
        elif x < 0 and y < 0 and z < 0:
            return "Galaxia H"

    @staticmethod
    def distancia(estrella1, estrella2):
        x1, y1, z1 = estrella1.coordenadas
        x2, y2, z2 = estrella2.coordenadas
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        return distancia

def posicionar_castillo(num_nobles):
    castillo = Castillo("Castillo")

    nobles = [Castillo(f"Noble {i + 1}") for i in range(num_nobles)]
    burgueses = [Castillo(f"Burgués {i + 1}") for i in range(num_nobles) for _ in range(5)]
    campesinos = [Castillo(f"Campesino {i + 1}") for i in range(num_nobles) for _ in range(200)]

    return castillo, nobles, burgueses, campesinos

def main():
    # Puedes cambiar estos valores según tus necesidades
    num_nobles = 3

    castillo, nobles, burgueses, campesinos = posicionar_castillo(num_nobles)

    print(f"Posicionamiento en el espacio tridimensional:")
    print(castillo)
    for estrella in nobles + burgueses + campesinos:
        print(estrella)

    print(f"\nGalaxia del Castillo: {castillo.galaxia()}")

    # Calcula y muestra la distancia entre dos estrellas
    if len(nobles) >= 2:
        distancia_entre_nobles = Castillo.distancia(nobles[0], nobles[1])
        print(f"\nDistancia entre Nobles: {distancia_entre_nobles}")

if __name__ == "__main__":
    main()
