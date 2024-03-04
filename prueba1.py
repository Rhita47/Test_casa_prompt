def obtener_integrantes(num_nobles):
    num_burgueses = num_nobles * 5
    num_campesinos = num_burgueses * 40

    return num_nobles, num_burgueses, num_campesinos

def main():
    # Puedes cambiar estos valores según tus necesidades
    num_nobles = 7

    nobles, burgueses, campesinos = obtener_integrantes(num_nobles)

    print(f"Total de nobles: {nobles}")
    print(f"Total de burgueses: {burgueses}")
    print(f"Total de campesinos: {campesinos}")

if __name__ == "__main__":
    main()
