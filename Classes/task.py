
class Task():

    def action():

        while True:

            try:

                print("Choose your action")
                print("1. Add Task")
                print("2. View Task")
                print("3. Update Task")
                print("4. Delete Task")
                print("5. Exit")

                user_input = int(input("Enter your choice: "))

                match user_input:

                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case _:
                        print("Invalid Input!")

            except ValueError:

                print("Integer number only!")

    