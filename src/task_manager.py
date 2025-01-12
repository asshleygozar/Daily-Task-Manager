import csv
import time

class TaskManager():

    def __init__(self, task, description="None", priority="Low", deadline="Now"):
        self.task = task
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.number = 0
        self.file_path = "G:\\Daily-Task-Manager\\Database\\task-records.csv"
        
<<<<<<< HEAD

    def load_tasks(self):

        try:

            with open(TaskManager.database(), mode='r') as file:
                csv_reader = csv.DictReader(file)
                
        except FileNotFoundError:
            print("File not found error!")
            csv_reader = []

        return csv_reader
            
    def add_tasks(self):

        self.task_name = input("Task name: ")
        self.description = input("Task Description: ")
        self.due_date = input("Task due date (mm/dd/yyyy): ")
        self.priority = input("Task priority: ")
        self.status = input("Task status: ")

        tasks_data = [{"Task":self.task_name, "Task-Description":self.description, "Task-Due-Date":self.due_date, "Task-Priority":self.priority, "Task-Status":self.status}]

        try:
            with open(TaskManager.database(), mode="a", newline='') as file:

                field_names = ["Task", "Task-Description", "Task-Due-Date", "Task-Priority", "Task-Status"]
                file_header_exists = os.path.isfile(TaskManager.database())

                csv_writer = csv.DictWriter(file, fieldnames = field_names)
                
                if not file_header_exists or os.stat(TaskManager.database()).st_size == 0:

                    csv_writer.writeheader()

                csv_writer.writerows(tasks_data)

        except FileNotFoundError:
            
            print("File not found error!")
            csv_writer = []
=======
    def __str__(self):
        return f"{self.task} | {self.description} | {self.priority} | {self.deadline}"
>>>>>>> testing-branch
    
    def add_task(self):
        self.task = input("Enter task name: ")
        self.description = input("Enter task description")
        self.priority = input("Enter task priority level: ")
        self.deadline = input("Enter task deadline (MM/DD/YYYY): ")
        
<<<<<<< HEAD
        try:
            with open(TaskManager.database(), mode='r') as file:
                csv_reader = csv.DictReader(file)

                for task in csv_reader:
                    print(f"{task["Task"]} | {task["Task-Description"]} | {task["Task-Due-Date"]} | {task["Task-Priority"]} | {task["Task-Status"]}")

        except FileNotFoundError:

            print("File not found error!")
            csv_reader = []
    

    def update_tasks_status():
            
        task_name = input("Enter task name: ")

        try:
            with open(TaskManager.database(), mode='r') as fileReader:
                csv_reader = csv.DictReader(fileReader)

                for task in csv_reader:

                    if task_name != task["Task"]:
                        print("Task name does not exists!")

                    else:

                        user_status_update = input("Enter updated status: ")
                        tasks_data = [{"Task": task["Task"], "Task-Description":task["Task-Description"], "Task-Due-Date":task["Task-Due-Date"], "Task-Priority":task["Task-Priority"], "Task-Status":user_status_update}]
                        updated_data = []
                        updated_data.append(tasks_data)

                        try:

                            with open(TaskManager.database(), mode='r') as read:
                                csv_read = csv.DictReader(read)

                                for row in csv_read:

                                    if row["Task"] == task_name:

                                        row["Task"] = ""

                                    updated_data.append(row)     

                        except FileNotFoundError:
                            print("File not found error!")
                            csv_read = []

                        try:
                            with open(TaskManager.database(), mode="a", newline='') as fileWriter:

                                field_names = ["Task", "Task-Description", "Task-Due-Date", "Task-Priority", "Task-Status"]
                                file_header_exists = os.path.isfile(TaskManager.database())
                                csv_writer = csv.DictWriter(fileWriter, fieldnames = field_names)
                                
                                if not file_header_exists or os.stat(TaskManager.database()).st_size == 0:
                                    csv_writer.writeheader()

                                csv_writer.writerows(updated_data)

                        except FileNotFoundError:

                            print("File not found error!")
                            csv_reader = []

                    break

        except FileNotFoundError:

            print("File not found!")

            csv_reader = []
         

    def filter_by_due_date():
        pass

    def filter_by_priority():
        pass
=======
        task_number = self.number =+ 1
        task_data = [{task_number:
                       {"Task":self.task,
                        "Description":self.description,
                        "Priority":self.priority,
                        "Deadline":self.deadline
                        }}]

        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.write(file)



>>>>>>> testing-branch

