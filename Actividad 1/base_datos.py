# base_datos.py
from pymongo import MongoClient

class BaseDatos:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["almacen_robot"]
        self.tareas = self.db["tareas"]
        self.estados_robots = self.db["estados_robots"]

    def inicializar_datos(self):
        self.tareas.delete_many({})
        self.estados_robots.delete_many({})

        self.tareas.insert_many([
            {"id": 1, "ubicacion": (2, 3), "estado": "pendiente"},
            {"id": 2, "ubicacion": (4, 2), "estado": "pendiente"},
            {"id": 3, "ubicacion": (1, 5), "estado": "pendiente"}
        ])

    def obtener_tarea(self):
        tarea = self.tareas.find_one({"estado": "pendiente"})
        if tarea:
            self.tareas.update_one({"id": tarea["id"]}, {"$set": {"estado": "en progreso"}})
            return tarea
        return None

    def completar_tarea(self, id_tarea):
        self.tareas.update_one({"id": id_tarea}, {"$set": {"estado": "completada"}})

    def actualizar_estado_robot(self, id_robot, estado):
        self.estados_robots.update_one(
            {"id_robot": id_robot},
            {"$set": estado},
            upsert=True
        )
