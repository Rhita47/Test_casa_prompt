import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

class Castillo:
    def __init__(self, nombre, coordenadas=(0, 0, 0)):
        self.nombre = nombre
        self.coordenadas = coordenadas

def plot_modelo_3d(castillo, nobles, burgueses, campesinos):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Mostrar el castillo como un punto rojo
    ax.scatter(*castillo.coordenadas, color='red', label=f'{castillo.nombre} (Castillo)')

    # Mostrar a los nobles como puntos verdes más cercanos al castillo
    for noble in nobles:
        ax.scatter(*noble.coordenadas, color='green', label=noble.nombre)

    # Mostrar a los burgueses como puntos azules, lejos de los nobles pero cerca del castillo
    for burgues in burgueses:
        ax.scatter(*burgues.coordenadas, color='blue', label=burgues.nombre)

    # Mostrar a los campesinos como puntos amarillos, a una distancia fija de los burgueses
    for campesino in campesinos:
        ax.scatter(*campesino.coordenadas, color='yellow', label=campesino.nombre)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.legend()
    plt.show()

def posicionar_castillo(num_nobles):
    castillo = Castillo("Castillo")

    # Coordenadas del castillo
    x_castillo, y_castillo, z_castillo = castillo.coordenadas

    # Nobles más cercanos al castillo
    nobles = [Castillo(f"Noble {i + 1}", (x_castillo + random.uniform(-5, 5), y_castillo + random.uniform(-5, 5), z_castillo + random.uniform(0, 5))) for i in range(num_nobles)]

    # Burgueses lejos de los nobles pero cerca del castillo
    burgueses = [Castillo(f"Burgués {i + 1}", (x_castillo + random.uniform(-10, 10), y_castillo + random.uniform(-10, 10), z_castillo + random.uniform(15, 25))) for i in range(num_nobles) for _ in range(5)]

    # Campesinos a una distancia fija de los burgueses
    distancia_fija = 10
    campesinos = [Castillo(f"Campesino {i + 1}", (burgues.coordenadas[0] + random.uniform(-distancia_fija, distancia_fija),
                                                      burgues.coordenadas[1] + random.uniform(-distancia_fija, distancia_fija),
                                                      burgues.coordenadas[2] + random.uniform(-distancia_fija, distancia_fija)))
                  for i in range(num_nobles) for burgues in burgueses for _ in range(40)]

    return castillo, nobles, burgueses, campesinos

def main():
    # Puedes cambiar estos valores según tus necesidades
    num_nobles = 3

    castillo, nobles, burgueses, campesinos = posicionar_castillo(num_nobles)

    plot_modelo_3d(castillo, nobles, burgueses, campesinos)

if __name__ == "__main__":
    main()

