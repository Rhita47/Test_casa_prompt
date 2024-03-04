import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

class Castillo:
    def __init__(self, nombre, coordenadas=None):
        self.nombre = nombre
        self.coordenadas = coordenadas if coordenadas is not None else (random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(0, 50))

def plot_modelo_3d(castillo, nobles, burgueses, campesinos):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Mostrar el castillo como un punto rojo
    ax.scatter(*castillo.coordenadas, color='red', label=f'{castillo.nombre} (Castillo)')

    # Mostrar a los nobles como puntos verdes
    for noble in nobles:
        ax.scatter(*noble.coordenadas, color='green', label=noble.nombre)

    # Mostrar a los burgueses como puntos azules
    for burgues in burgueses:
        ax.scatter(*burgues.coordenadas, color='blue', label=burgues.nombre)

    # Mostrar a los campesinos como puntos amarillos
    for campesino in campesinos:
        ax.scatter(*campesino.coordenadas, color='yellow', label=campesino.nombre)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.legend()
    plt.show()

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

    plot_modelo_3d(castillo, nobles, burgueses, campesinos)

if __name__ == "__main__":
    main()
