from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["M3"]

    def createCollections(self):
        self.db["units"].insert_many([
            {
                "name": "Unit 1",
                "location": "Base location",
                "status": "None",
                "messages": []
            },
            {
                "name": "Unit 2",
                "location": "Base location",
                "status": "None",
                "messages": []
            },
            {
                "name": "Unit 3",
                "location": "Base location",
                "status": "None",
                "messages": []
            }
        ])
        
        self.db["areas"].insert_many([
            {"area_id": i, "status": "Not Explored", "found": False, "needs_assistance": True}
            for i in range(1, 6)
        ])
        
        self.db["messages"].insert_many([
            {"unit_name": "Unit 1", "message": "Ready for deployment", "area_id": None},
            {"unit_name": "Unit 2", "message": "Looking for a victim", "area_id": None},
            {"unit_name": "Unit 3", "message": "Heading to area 1", "area_id": 1}
        ])

    def get_area(self, area_id):
        return self.db["areas"].find_one({"area_id": area_id})

    def get_unexplored_areas(self):
        return list(self.db["areas"].find({"found": False, "needs_assistance": True, "status": "Not Explored"}))

    def update_area(self, area_id, update_data):
        self.db["areas"].update_one({"area_id": area_id}, {"$set": update_data})

    def update_unit_status(self, unit_name, status):
        self.db["units"].update_one({"name": unit_name}, {"$set": {"status": status}})

    def add_message(self, unit_name, message, area_id=None):
        self.db["messages"].insert_one({
            "unit_name": unit_name,
            "message": message,
            "area_id": area_id
        })

    def get_messages(self):
        return list(self.db["messages"].find())