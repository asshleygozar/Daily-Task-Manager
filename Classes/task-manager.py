import csv
import time


class TaskManager:

    def __init__(self,task_name,description,due_date,priority,status):

        self.file_path = "Database\\task-records.csv"
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.load_file = TaskManager.load_tasks()

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

        task_data = [["Task", "Task-Description", "Task-Due-Date", "Task-Priority", "Task-Status"]]

        try:
            with open(self.file_path, mode="w") as file:
                
                csv_writer = csv.DictWriter(file)

        except FileNotFoundError:
            print("File not found error!")
            csv_writer = []
    

    def view_tasks(self):
        pass

    def update_tasks_status():
        pass

    def filter_by_due_date():
        pass

    def filter_by_priority():
        pass
