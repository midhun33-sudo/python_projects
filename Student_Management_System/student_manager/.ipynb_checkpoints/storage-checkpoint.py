import json
import os
class StorageManager:
    def load(self):
        if "Student_data.json" in os.listdir("../data/"):
            with open("../data/Student_data.json", "r") as file:
                self.data = json.load(file)
                file.close()
    
    def save(self,data):
        self.data = data 
        with open("../data/Student_data.json","w") as file:
            json.dump(self.data,file)
            file.close()


# File: Student_Management_System/student_manger/storage.py