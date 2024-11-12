class Robot:
    def __init__(self, id_robot, pizarra):
        self.id_robot = id_robot 
        self.pizarra = pizarra 
        self.tarea_actual = None

    def solicitar_tarea(self):
        """Solicita una tarea pendiente a la pizarra."""
        tarea = self.pizarra.obtener_tarea(self.id_robot)
        if tarea:
            self.tarea_actual = tarea
            print(f"Robot {self.id_robot} ha recibido la tarea: {tarea['id_tarea']} en {tarea['ubicacion']}")
        else:
            print(f"No hay tareas disponibles para el robot {self.id_robot}.")

    def actualizar_estado(self, estado):
        """Actualiza el estado de la tarea en la pizarra central."""
        if self.tarea_actual:
            self.pizarra.actualizar_estado_robot(self.tarea_actual["id_tarea"], estado)
        else:
            print(f"Robot {self.id_robot} no tiene tarea asignada.")
