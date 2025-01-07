import csv
import time


class TaskManager:

    def __init__(self,task_name="",description="None",due_date="Today",priority="Priority 4",status="Not Started"):

        self.file_path = "Database\\task-records.csv"
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.load_file = TaskManager.load_tasks(self)
   

    def load_tasks(self):

        try:
            with open(self.file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                
        except FileNotFoundError:
            print("File not found error!")
            csv_reader = []

        return csv_reader
            
    def add_tasks(self):

        task_name = input("Task name: ")
        task_description = input("Task Description: ")
        task_due_date = input("Task due date (mm/dd/yyyy): ")
        task_priority = input("Task priority: ")
        task_status = input("Task status: ")

        self.task_name = task_name
        self.description = task_description
        self.due_date = task_due_date
        self.priority = task_priority
        self.status = task_status

        tasks_data = [{"Task":self.task_name, "Task-Description":self.description, "Task-Due-Date":self.due_date, "Task-Priority":self.priority, "Task-Status":self.status}]

        try:
            with open("Database\\task-records.csv", mode="a", newline='') as file:

                csv_writer = csv.DictWriter(file)

                csv_writer.writeheader()
                csv_writer.writerows(tasks_data)

        except FileNotFoundError:
            print("File not found error!")
            csv_writer = []
    

    def view_tasks(self):

        try:
            with open("Database\\task-records.csv", mode='r') as file:

                csv_reader = csv.DictReader(file)
                for task in csv_reader:
                    print(task)

        except FileNotFoundError:

            print("File not found error!")
            csv_reader = []
    

    def update_tasks_status():
        pass

    def filter_by_due_date():
        pass

    def filter_by_priority():
        pass

task = TaskManager()

task.view_tasks()