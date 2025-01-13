import csv
import os
import time

class TaskManager():

    def __init__(self, task="Not Provided", description="None", priority="Low",status="Not Started", deadline="Now"):
        self.task = task
        self.description = description
        self.priority = priority
        self.status = status
        self.deadline = deadline
    
    def data_file_path():
        __file_path = "G:\\Daily-Task-Manager\\Database\\task-records.csv"
        return __file_path
    
    def add_task(self):

        self.task = input("Enter task name: ")
        self.description = input("Enter task description: ")
        self.priority = input("Enter task priority level: ")
        self.status = input("Enter status: ")
        self.deadline = input("Enter task deadline (MM/DD/YYYY): ")
        
        task_data = {   
                     "Task":self.task,
                     "Description":self.description,
                     "Priority":self.priority,
                     "Status":self.status,
                     "Deadline":self.deadline
                        }

        with open(TaskManager.data_file_path(), mode='a', newline='') as file:
            field_names = ["Task","Description","Priority","Status", "Deadline"] 
            file_exists = os.path.isfile(TaskManager.data_file_path())
            writer = csv.DictWriter(file,fieldnames=field_names)
            
            if not file_exists or os.stat(TaskManager.data_file_path()).st_size == 0:
                writer.writeheader()
            writer.writerow(task_data)

    def view_tasks():
        try:
            with open(TaskManager.data_file_path(),mode="r") as read:
                csv_reader = csv.reader(read)
                for row in csv_reader:
                    print(row)
        except FileNotFoundError:
            print("File not found!")

    def update_row(self,task_name, description,priority,status_update, deadline):
     
        updated_details = {"Task":task_name,"Description":description,"Priority":priority,"Status":status_update,"Deadline":deadline}
        try:
            with open(TaskManager.data_file_path(),mode="r") as read_task:
                csv_reader = csv.DictReader(read_task)
                rows = list(csv_reader)
        
            filter_rows = [row for row in rows if row["Task"] != task_name]
            filter_rows.append(updated_details)

            with open(TaskManager.data_file_path(), mode='w') as write_update:
                field_names = ["Task","Description","Priority","Status", "Deadline"]
                csv_status = csv.DictWriter(write_update,fieldnames=field_names)
                csv_status.writeheader()
                csv_status.writerows(filter_rows)

        except FileNotFoundError:
            print("File not found!")

        print("Updated successful!")
        

    def update_task_details(self):
        task_name = input("Enter task here: ")

        try:
            with open(TaskManager.data_file_path(),mode="r") as read_task:
                csv_reader = csv.DictReader(read_task)
                for task in csv_reader:
                    if task["Task"] != task_name:
                        print("Task does not exists")

            updated_description = input("Updated description: ")
            updated_priority = input("Updated priority: ")
            updated_status = input("Updated status: ")
            updated_deadline = input("Updated deadline: ")
            TaskManager.update_row(self,task_name,updated_description,updated_priority,updated_status,updated_deadline)

        except FileNotFoundError:
            print("File not found!")







            




