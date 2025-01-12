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
        
    def __str__(self):
        return f"{self.task} | {self.description} | {self.priority} | {self.deadline}"
    
    def add_task(self):
        self.task = input("Enter task name: ")
        self.description = input("Enter task description")
        self.priority = input("Enter task priority level: ")
        self.deadline = input("Enter task deadline (MM/DD/YYYY): ")
        
        task_number = self.number =+ 1
        task_data = [{task_number:
                       {"Task":self.task,
                        "Description":self.description,
                        "Priority":self.priority,
                        "Deadline":self.deadline
                        }}]

        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.write(file)




