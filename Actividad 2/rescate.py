import random
from database import Database
import threading
from concurrent.futures import ThreadPoolExecutor

class RescueOperations:
    def __init__(self):
        self.db = Database()
        self.lock = threading.Lock()

    def explore_area(self, unit_name, area_id):
        # Update area status to "Explored" and set "found" to True
        with self.lock:
            area = self.db.get_area(area_id)
            if area and area["status"] == "Not Explored":
                self.db.update_area(area_id, {"status": "Explored", "found": True})
                self.db.update_unit_status(unit_name, f"Found person in area {area_id}")
                
                message = f"{unit_name} found a person in area {area_id}."
                self.db.add_message(unit_name, message, area_id)
                
                print(f"[Update] {message}")
            else:
                print(f"[Info] Area {area_id} already explored by another unit.")

    def assign_and_explore(self, unit_name):
        # Assign unit to an unexplored area
        unexplored_areas = self.db.get_unexplored_areas()
        if unexplored_areas:
            area = random.choice(unexplored_areas)
            area_id = area["area_id"]
            
            self.db.update_unit_status(unit_name, f"Assigned to area {area_id}")
            print(f"{unit_name} assigned to area {area_id}")
            
            self.explore_area(unit_name, area_id)
        else:
            print(f"{unit_name}: No unexplored areas left.")
    # Read messages from the database
    def read_messages(self):
        messages = self.db.get_messages()
        for message in messages:
            print(f"{message['unit_name']} says: {message['message']}")

if __name__ == "__main__":
    operations = RescueOperations()
    operations.db.createCollections()
    
    # Assign and explore areas concurrently
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(operations.assign_and_explore, ["Unit 1", "Unit 2", "Unit 3"])
    
    # Read messages from the database
    operations.read_messages()