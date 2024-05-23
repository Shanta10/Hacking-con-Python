def agregar(tasks, task):
    tasks.append(task)

def remove(tasks, task):
    if task in tasks:
        tasks.remove(task)

def show(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"task {i}: {task}")

def main():
    tasks = []

    while True:
        print("\n---- Gestor de tareas ----")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tarea")
        print("4. Salir")

        sel = input("Ingrese el número de la opción que desea realizar: ")

        if sel == "1":
            task = input("Ingrese la tareas que desea agregar: ")
            agregar(tasks, task)
        elif sel == "2":
            task = input("Ingrese el número de la tareas que desea eliminar: ")
            remove(tasks, task)
        elif sel == "3":
            print("\nLista de tareas:")
            show(tasks)
        elif sel == "4":
            print("Gracias por usar el Gestor de tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()