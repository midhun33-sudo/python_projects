from student_manager.manager import StudentManager
from student_manager.storage import StorageManager

if __name__ == "__main__":
    storage = StorageManager()
    sm = StudentManager(storage)
    while True:
        print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Update Student Marks\n5. Delete Student\n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            marks = int(input("Enter marks (0-25): "))
            print(sm.add(name, roll, marks))
        
        elif choice == '2':
            students = sm.view()
            for student in students:
                print(f"Roll: {student[0]}, Name: {student[1]}, Marks: {student[2]}")
        
        elif choice == '3':
            roll = input("Enter roll number to search: ")
            result = sm.search(roll)
            if result:
                print(f"Roll: {result[0]}, Name: {result[1]}, Marks: {result[2]}")
            else:
                print("Student not found")
        
        elif choice == '4':
            roll = input("Enter roll number to update: ")
            marks = int(input("Enter new marks (0-25): "))
            result = sm.update(roll, marks)
            if result:
                print(f"Updated - Roll: {result[0]}, Name: {result[1]}, Marks: {result[2]}")
            else:
                print("Update failed. Check roll number and marks.")
        
        elif choice == '5':
            roll = input("Enter roll number to delete: ")
            if sm.delete(roll):
                print("Student deleted successfully")
            else:
                print("Student not found")
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")