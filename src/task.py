from task_manager import TaskManager

class Task():

    def action(self):

        while True:

            try:

                print("Choose your action")
                print("1. Add Task")
                print("2. View Task")
                print("3. Update Task Details")
                print("4. Delete Task")
                print("5. Exit")

                user_input = int(input("Enter your choice: "))

                match user_input:

                    case 1:

                        TaskManager.add_task(self)
                        break
                    case 2:

                        TaskManager.view_tasks()
                        break
                    case 3:

                        TaskManager.update_task_details(self)
                        break
                    case 4:

                        pass

                    case 5:

                        break

                    case _:
                        
                        print("Invalid Input!")

            except ValueError:

                print("Integer number only!")

task = Task()
task.action()