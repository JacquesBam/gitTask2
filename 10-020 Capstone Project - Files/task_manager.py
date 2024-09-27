# =====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

# ====Login Section====
# Stores whether the password and username are correct
validation = 0
wrong_password = 0
wrong_username = 0

# Stores the index of the comma in a line
comma_location = 0

# Stores user inputted password and username
entered_password = ""
entered_username = ""

# Stores username and password from file
password = ""
username = ""

error_msg = ""

# Loops until valid username and password are entered
while validation != 1:

    # Prompts user to enter username and password
    entered_username = input("Please enter your username: ")
    entered_password = input("Please enter your password: ")

    # Open file and iterate through
    with open("user.txt", "r") as user_file:
        for line in user_file:

            # Find the location of the comma and use it to separate
            # the username from the password
            comma_location = line.find(",")

            username = line[0:comma_location]
            password = line[comma_location + 2:len(line)].strip("\n")

            # Checks if username and password match any in file
            # Breaks loop if a match is found,
            # otherwise continues until end of file
            if entered_username == username and entered_password == password:
                validation = 1
                logged_in = username
                print("\n")
                break
            elif entered_username == username and entered_password != password:
                wrong_password = 1
            else:
                wrong_username = 1

    # Breaks while loop if username and password are correct
    # Loops again if incorrect
    if validation == 1:
        break
    elif wrong_password == 1:
        print("Password is incorrect. Please try again")
    elif wrong_username == 1:
        print("Username does not exist. Please try again")

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.

    # Menu for non-admins
    if logged_in != "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    # Admin menu that allows stats
    elif logged_in == "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - view stats
e - exit
: ''').lower()

    if menu == 'r' and logged_in == "admin":
        try_again = True
        # Loops if an already existing username is entered
        while try_again:
            in_use = 0

            # Gets new username
            new_username = input("Please enter a new username: ")

            # Opens file and iterates through
            # Checks if new username is unique
            with open("user.txt", "r") as user_file:
                for line in user_file:
                    comma_location = line.find(",")
                    old_username = line[0:comma_location]
                    if new_username == old_username:
                        in_use = 1

            # Restarts if new username is already in use
            # Continues if new username is unique
            if in_use == 1:
                print("Username is already in use. Please try again")
            else:
                try_again = False

        # Gets new password and password confirmation
        new_password = input("Please enter a new password: ")
        confirm_password = input("Please confirm your password: ")

        # Checks if password and confirmation match
        # Prints to file if they do, restarts if they don't
        if new_password == confirm_password:
            print("\nUser has been added\n")
            with open("user.txt", "a") as user_file:
                user_file.write(f"\n{new_username}, {new_password}")
        else:
            print("\nPasswords do not match. Please try again\n")

    elif menu == "r" and logged_in != "admin":
        print("--------------------------" * 3 + "\n")
        print("Only the admin is allowed to register new users\n")
        print("--------------------------" * 3)

    elif menu == 'a':

        # Stores the string that is written to the file
        task_formatted = "\n"

        # Used for while loop validation
        name_again = True
        year_again = True
        month_again = True
        day_again = True
        title_again = True
        description_again = True

        # Checks if a valid username is entered
        while name_again:
            entered_username = input("Please enter the"
                                     " user who will do the task:\n")
            does_exist = 0
            with open("user.txt", "r") as user_file:
                for line in user_file:
                    comma_location = line.find(",")
                    if entered_username == line[0:comma_location]:
                        does_exist = 1

            # Repeats if username doesn't exist, otherwise breaks loop
            if does_exist == 1:
                task_formatted += entered_username + ", "
                name_again = False
            else:
                print("\nUsername does not exist, please try again\n")

        # Gets title
        # Loops if nothing is entered. Breaks loop otherwise
        while title_again:
            task_title = input("Please enter the title of the task:\n")
            if task_title == "":
                print("You haven't entered anything."
                      " Please provide a valid title")
            else:
                task_formatted += task_title + ", "
                title_again = False

        # Gets description
        # Loops if nothing is entered. Breaks loop otherwise
        while description_again:
            task_description = input("Please enter a description"
                                     " of the task:\n")
            if task_description == "":
                print("You haven't entered anything."
                      " Please provide a valid title")
            else:
                task_formatted += task_description + ", "
                description_again = False

        # Gets year due
        # Loops if any digits aren't numeric or year is not 4 characters
        while year_again:
            due_year = str(input("Please enter the year the task is due:\n"))
            if len(due_year) == 4 and due_year.isnumeric() is True:
                year_again = False
            else:
                print("Invalid year entered. Please try again")

        # Gets month due
        while month_again:
            due_month = str(input("Please enter the month"
                                  " the task is due (mm):\n"))

            # Checks if entered value is valid
            # Loops again if it isn't
            if len(due_month) == 2 and due_month.isnumeric() is True:
                month_again = False

            # If a single digit is entered, add a zero to preserve format
            elif len(due_month) == 1 and due_month.isnumeric() is True:
                due_month = "0" + due_month
                month_again = False

            # Error message for invalid value
            else:
                print("Invalid value entered. Please try again")

        # Gets day due
        while day_again:
            due_day = str(input("Please enter the day the task is due:\n"))

            # Checks if entered value is valid
            # Loops again if it isn't
            if len(due_day) == 2 and due_day.isnumeric() is True:
                day_again = False

            # If a single digit is entered, add a zero to preserve format
            elif len(due_day) < 2 and due_day.isnumeric() is True:
                due_day = "0" + due_day
                day_again = False

            # Error message for invalid value
            else:
                print("Invalid value entered. Please try again")

        # Formats date and adds to task
        due_date = f"{due_year}-{due_month}-{due_day}"
        task_formatted += due_date + ", "

        # Gets current date, formats it and adds to task
        current_date = str(datetime.datetime.today())[0:10]
        task_formatted += current_date + ", No"

        # Appends task to file
        with open("tasks.txt", "a") as tasks_file:
            tasks_file.write(task_formatted)

    elif menu == 'va':
        tasks_assigned = 0
        with open("tasks.txt", "r") as tasks_file:

            # Loops through all tasks
            for line in tasks_file:

                # Divides task into elements and stores in list
                tasks_list = line.split(", ")

                tasks_assigned += 1

                # Prints elements in readable format
                print("--------------------------" * 3 + "\n")
                print(f"Task:\t\t\t{tasks_list[1]}")
                print(f"Assigned to:\t\t{tasks_list[0]}")
                print(f"Date assigned:\t\t{tasks_list[3]}")
                print(f"Due date:\t\t{tasks_list[4]}")
                print(f"Task complete?\t\t{tasks_list[5].strip("\n")}")
                print(f"Task description:\n {tasks_list[2]}\n")

            # If there are no tasks, prints an appropriate message
            if tasks_assigned == 0:
                print("--------------------------" * 3 + "\n")
                print("No tasks assigned\n")
            print("--------------------------" * 3)

    elif menu == 'vm':
        tasks_assigned = 0
        with open("tasks.txt", "r") as tasks_file:

            # Loops through all tasks
            for line in tasks_file:
                tasks_list = line.split(", ")

                # Checks if task name matches currently logged in user
                # If it does match, prints task in readable format
                # Otherwise skips it
                if tasks_list[0] == logged_in:
                    tasks_assigned += 1  # Used to check for no tasks
                    print("--------------------------" * 3 + "\n")
                    print(f"Task:\t\t\t{tasks_list[1]}")
                    print(f"Assigned to:\t\t{tasks_list[0]}")
                    print(f"Date assigned:\t\t{tasks_list[3]}")
                    print(f"Due date:\t\t{tasks_list[4]}")
                    print(f"Task complete?\t\t{tasks_list[5].strip("\n")}")
                    print(f"Task description:\n {tasks_list[2]}\n")

            # Prints appropriate message if no tasks are assigned
            if tasks_assigned == 0:
                print("--------------------------" * 3 + "\n")
                print("No tasks assigned to you\n")
            print("--------------------------" * 3)

    elif menu == "s" and logged_in == "admin":
        total_users = 0
        total_tasks = 0

        # Iterates through user file and gets total number of lines (users)
        with open("user.txt", "r") as user_file:
            for line in user_file:
                total_users += 1

        # Iterates through tasks file and gets total number of lines (tasks)
        with open("tasks.txt", "r") as user_file:
            for line in user_file:
                total_tasks += 1

        # Prints total users and tasks in a readable format
        print("--------------------------" * 3 + "\n")
        print(f"Total number of users:\t{total_users}")
        print(f"Total number of tasks:\t{total_tasks}\n")
        print("--------------------------" * 3)

    # Ends program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Prints error message for invalid input
    else:
        print("You have entered an invalid input. Please try again")
