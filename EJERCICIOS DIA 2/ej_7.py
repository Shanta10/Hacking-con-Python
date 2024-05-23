def mostrar_colaboradores():
    with open("colaboradores.txt", "r") as archivo:
        colaboradores = archivo.readlines()
        if not colaboradores:
            print("No hay colaboradores registrados.")
        else:
            print("Colaboradores:")
            for i, colaborador in enumerate(colaboradores[:5], start=1):
                print(f"{i}. {colaborador.strip()}")

def agregar_colaborador(nombre):
    with open("colaboradores.txt", "r+") as archivo:
        colaboradores = archivo.readlines()
        if len(colaboradores) >= 15:
            print("No se pueden agregar más colaboradores. Se ha alcanzado el límite de 15.")
            return
        archivo.write(nombre + "\n")
        print(f"Colaborador '{nombre}' agregado correctamente.")

def main():
    print("Bienvenido al programa de gestión de colaboradores.")
    while True:
        print("\n1. Mostrar colaboradores")
        print("2. Agregar colaborador")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            mostrar_colaboradores()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del nuevo colaborador: ")
            agregar_colaborador(nombre)
        elif opcion == "3":
            print("Gracias por usar el programa de gestión de colaboradores. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
