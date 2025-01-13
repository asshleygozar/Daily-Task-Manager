from datetime import time
from datetime import datetime
from plyer import notification
from time import sleep
import csv
import sys
import os


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

    def date_time(input_time):
        strip_time = input_time.strip("/")
        hours = int(f"{strip_time[0]}{strip_time[1]}")
        minute = int(f"{strip_time[3]}{strip_time[4]}")
    
        formatted_time = str(time(hours,minute))
        return str(formatted_time)
    
    def task_notification(task_title,task_description):
         notification.notify(
             title = task_title,
             message = task_description,
             app_name ="My Daily Task Manager",
             timeout = 10
         )

    def notification_timer():

        now = datetime.now()
        try:
            with open(TaskManager.data_file_path(), "r") as read_dates:
                date_reader = csv.DictReader(read_dates)
                rows = list(date_reader)
                for date in rows:
                    check_hour, check_minute,check_second = map(int,date["Deadline"].split(":"))
                    target_time = now.replace(hour=check_hour,minute=check_minute,second=check_second,microsecond=0)
                    if target_time >= now:
                        TaskManager.task_notification(date["Task"],date["Description"])
                        break
                    
                    sleep(1)

        except FileNotFoundError:
            print("File not found!")

    def add_task(self):

        self.task = input("Enter task name: ")
        self.description = input("Enter task description: ")
        self.priority = input("Enter task priority level: ")
        self.status = input("Enter status: ")
        self.deadline = input("Enter task time deadline (HH/MM): ")

        formatted_deadline = TaskManager.date_time(self.deadline)
        
        task_data = {   
                     "Task":self.task,
                     "Description":self.description,
                     "Priority":self.priority,
                     "Status":self.status,
                     "Deadline":formatted_deadline
                        }

        with open(TaskManager.data_file_path(), mode='a', newline='') as file:
            field_names = ["Task","Description","Priority","Status", "Deadline"] 
            file_exists = os.path.isfile(TaskManager.data_file_path())
            writer = csv.DictWriter(file,fieldnames=field_names)
            
            if not file_exists or os.stat(TaskManager.data_file_path()).st_size == 0:
                writer.writeheader()
            writer.writerow(task_data)
        TaskManager.task_notification(self.task, self.description)
        print("Task added successfully!")

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
                checker = list(csv_reader)
                for task in checker:
                    if task["Task"] != task_name:
                        print("Task does not exists")
                        sys.exit(0)
                    else:
                       updated_description = input("Updated description: ")
                       updated_priority = input("Updated priority: ")
                       updated_status = input("Updated status: ")
                       updated_deadline = input("Updated deadline: ")
                       TaskManager.update_row(self,task_name,updated_description,updated_priority,updated_status,updated_deadline)   

        except FileNotFoundError:
            print("File not found!")

    def delete_task():

        task_name = input("Enter task here: ")

        try:
            with open(TaskManager.data_file_path(),mode="r") as read_file:
                read_file = csv.DictReader(read_file)
                rows = list(read_file)
                filter_rows = [row for row in rows if row["Task"] != task_name]

                for task in rows:
                    if task["Task"] == task_name:
                        with open(TaskManager.data_file_path(), mode='w') as write_update:
                            field_names = ["Task","Description","Priority","Status", "Deadline"]
                            csv_delete = csv.DictWriter(write_update,fieldnames=field_names)
                            csv_delete.writeheader()
                            csv_delete.writerows(filter_rows)

                        print("Task deleted successfully")
                        break
                    if task["Task"] != task_name:
                        print("Task does not exists!")
                        break
                
        except FileNotFoundError:
            print("File not found!")

    if __name__ == "__main__":
        notification_timer()







            




