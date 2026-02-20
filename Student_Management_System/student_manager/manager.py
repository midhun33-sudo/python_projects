from student_manager.storage import StorageManager
storage = StorageManager()

class StudentManager:
    def __init__(self, storage):
        self.storage = storage
        self.data = self.storage.load()
    
    def add(self, name, roll, marks):
        if roll in self.data:
            return "Roll number already exists"
            
        if not (0 <= marks <= 25):
            return "Please check the marks entered (should be between 0–25)"
            
        self.data[roll] = {
            "Name": name,
            "Marks": marks
        }
        self.storage.save(self.data)
        return "Student added successfully"

    def view(self):
        lis = []
        for roll,n_m in self.data.items():
            lis.append((roll,n_m["Name"],n_m["Marks"]))
        return lis

    def search(self,roll):
        if roll in self.data:
            return (roll,self.data[roll]["Name"],self.data[roll]["Marks"])
        else:return None

    def update(self, roll, marks):
        if roll not in self.data:
            return None
        
        if not (0 <= marks <= 25):
            return None
        
        self.data[roll]["Marks"] = marks
        self.storage.save(self.data)
        return (roll,self.data[roll]["Name"],self.data[roll]["Marks"])

    def delete(self, roll):
        if roll not in self.data:
            return None
            
        del self.data[roll]
        self.storage.save(self.data)
        return True
