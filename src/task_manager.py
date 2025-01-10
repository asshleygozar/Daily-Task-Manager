import csv
import os
import time


class TaskManager:

    def __init__(self,task_name="",description="None",due_date="Today",priority="Priority 4",status="Not Started"):

        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.load_file = TaskManager.load_tasks(self)
   
    def database():

        __file_path = "Database\\task-records.csv"

        return __file_path
        

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
    

    def view_tasks(self):

        print("Task | Task-Description | Task-Due-Date | Task-Priority | Task-Status")
        
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

        updated_data = []
        try:
            with open(TaskManager.database(), mode='r') as fileReader:

                csv_reader = csv.DictReader(fileReader)

            for task in csv_reader:

                if task["Task"] != task_name:
                    updated_data.append(task)

                if task["Task"] == task_name:
                    temporary_data = [{"Task":task["Task"], "Task-Description":task["Task-Description"], "Task-Due-Date":task["Task-Due-Date"], "Task-Priority":task["Task-Priority"], "Task-Status":task_name}]
                    updated_data.append(temporary_data)

        except FileNotFoundError:

            print("File not found error!")
            csv_reader = []

        try:
            with open(TaskManager.database(), mode="a", newline='') as file:

                field_names = ["Task", "Task-Description", "Task-Due-Date", "Task-Priority", "Task-Status"]
                file_header_exists = os.path.isfile(TaskManager.database())

                csv_writer = csv.DictWriter(file, fieldnames = field_names)
                
                if not file_header_exists or os.stat(TaskManager.database()).st_size == 0:

                    csv_writer.writeheader()

                csv_writer.writerows(updated_data)

        except FileNotFoundError:
            
            print("File not found error!")
            csv_writer = []

    def filter_by_due_date():
        pass

    def filter_by_priority():
        pass

