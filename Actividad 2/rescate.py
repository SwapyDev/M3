import random
from database import Database

class RescueOperations:
    def __init__(self):
        self.db = Database()

    def explore_area(self, unit_name, area_id):
        area = self.db.get_area(area_id)
        if area and not area["found"]:
            # Simular que la unidad encontró a la persona
            self.db.update_area(area_id, {"status": "Explored", "found": True})
            
            # Actualizar el estado de la unidad
            self.db.db["units"].update_one(
                {"name": unit_name},
                {"$set": {"status": "Found person in area {}".format(area_id)}}
            )
            
            # Enviar un mensaje a las otras unidades sobre el hallazgo
            message = f"Unit {unit_name} found the person in area {area_id}."
            self.db.add_message(unit_name, message, area_id)
            
            # Actualizar la pizarra de situación
            print(f"Updated situation board: {message}")
        else:
            print(f"Area {area_id} has already been explored or person was found.")

    def assign_area(self, unit_name):
        unassigned_areas = self.db.get_areas()
        area = random.choice(list(unassigned_areas)) if unassigned_areas else None
        
        if area:
            self.db.db["units"].update_one(
                {"name": unit_name},
                {"$set": {"status": f"Assigned to area {area['area_id']}"}} 
            )
            return area["area_id"]
        return None

    def read_messages(self):
        messages = self.db.db["messages"].find()
        for message in messages:
            print(f"{message['unit_name']} says: {message['message']}")

# Ejemplo de uso
if __name__ == "__main__":
    operations = RescueOperations()
    
    # Crear colecciones
    operations.db.createCollections()
    
    # Asignar áreas y simular exploración
    operations.assign_area("Unit 1")
    operations.explore_area("Unit 1", 1)  # Unidad 1 explora el área 1
    operations.explore_area("Unit 2", 1)  # Unidad 2 intenta explorar el área 1, pero ya fue explorada
    operations.explore_area("Unit 3", 2)  # Unidad 3 explora el área 2
    
    # Leer los mensajes
    operations.read_messages()
