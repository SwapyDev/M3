from pizarra_central import PizarraCentral
from robot import Robot

def main():
    pizarra = PizarraCentral()

    pizarra.agregar_tarea(1, "Pasillo A")
    pizarra.agregar_tarea(2, "Pasillo B")
    pizarra.agregar_tarea(3, "Pasillo C")

    robot1 = Robot(1, pizarra)
    robot2 = Robot(2, pizarra)

    robot1.solicitar_tarea()
    robot2.solicitar_tarea()

    robot1.actualizar_estado("en progreso")
    robot2.actualizar_estado("completada")

if __name__ == "__main__":
    main()
