from pymongo import MongoClient

class PizarraCentral:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["almacen_db"] 
        self.tareas = self.db["tareas"]  

    def agregar_tarea(self, id_tarea, ubicacion):
        """Agrega una tarea a la base de datos."""
        tarea = {"id_tarea": id_tarea, "ubicacion": ubicacion, "estado": "pendiente"}
        self.tareas.insert_one(tarea)
        print(f"Tarea {id_tarea} agregada en la ubicación {ubicacion}.")

    def obtener_tarea(self, id_robot):
        """Obtiene una tarea pendiente por id_robot."""
        return self.tareas.find_one({"id_tarea": id_robot, "estado": "pendiente"})

    def actualizar_estado_robot(self, id_robot, estado):
        """Actualiza el estado de una tarea asociada a un robot."""
        resultado = self.tareas.update_one(
            {"id_tarea": id_robot}, 
            {"$set": {"estado": estado}}  
        )
        if resultado.modified_count > 0:
            print(f"Tarea {id_robot} actualizada a {estado}.")
        else:
            print(f"No se encontró la tarea {id_robot} para actualizar.")
