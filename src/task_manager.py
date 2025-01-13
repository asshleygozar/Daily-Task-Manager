import csv
import os
import time

class TaskManager():

    def __init__(self, task="Not Provided", description="None", priority="Low", deadline="Now"):
        self.task = task
        self.description = description
        self.priority = priority
        self.deadline = deadline
    
    def data_file_path():
        __file_path = "G:\\Daily-Task-Manager\\Database\\task-records.csv"
        return __file_path
    
    def add_task(self):

        self.task = input("Enter task name: ")
        self.description = input("Enter task description: ")
        self.priority = input("Enter task priority level: ")
        self.deadline = input("Enter task deadline (MM/DD/YYYY): ")
        
        task_data = {   
                     "Task":self.task,
                     "Description":self.description,
                     "Priority":self.priority,
                     "Deadline":self.deadline
                        }

        with open(TaskManager.data_file_path(), mode='a', newline='') as file:
            field_names = ["Task","Description","Priority","Deadline"] 
            writer = csv.DictWriter(file,fieldnames=field_names)

            writer.writeheader()
            writer.writerow(task_data)

    def view_tasks(self):
        try:
            with open(TaskManager.data_file_path(),mode="r") as read:
                csv_reader = csv.reader(read)
                for row in csv_reader:
                    print(row)
        except FileNotFoundError:
            print("File not found!")




            




