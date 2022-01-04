import os
import datetime
import sys

#Path of parent directory
#Navigate to Strings directory
absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
parentDirectory = os.path.dirname(fileDirectory)
newPath = os.path.join(parentDirectory,"task25") 
print(newPath)  

# Reg_user function if register function = to false
# Request new user name then checks against the user file.
# For loops through the user_file.
# Turns the user information to a list.
def reg_user():
        register = False
        while register == False:
            reg_username = input("Enter new username:                     \t")
            user_file = open("user1.txt", "r+")
            check_username = []
            for line in user_file:
                line = line.strip().strip("\n")
                login_user = line.split(", ")
                if reg_username == login_user[0]:
                    check_username.append(login_user[0])

# Checks new usernames in check_username.
# Prints error messages.
# Closes file.
# Else register  new users and write to the file.
# If all conditions are not a match print error.               
            if reg_username in check_username:
                print("User already exists try a different username")
                user_file.close()
            else:
                reg_password = input("Enter new password:                     \t")
                confirm_username = input("Enter username to confirm username:   \t")
                confirm_password = input("Enter username to confirm password:   \t")
                if confirm_username == reg_username and confirm_password == reg_password:
                    print()
                    print("Registration successful")
                    user_file = open("user1.txt", "a")
                    user_file.write("\n")
                    user_file.write(reg_username)
                    user_file.write(", ")
                    user_file.write(reg_password)
                    user_file.close()
                    break
                else:
                    print("username or password doesn't match")
                return register

# Open tasks_file and append user information.
# Request input from user.
# close taske_file.  
def add_task():
        tasks_file = open("tasks.txt", "a+")
        user = input("Enter username                                \t")
        title = input("Enter title of the task:                     \t")
        description = input("Enter description of the task:         \t")
        due_date = input("Enter due date:                           \t")
        current_date = input("Enter current date                    \t")
        is_complete = "No"
        tasks_file.write(f"{user}, {title}, {description}, {due_date}, {current_date}, {is_complete}\n")
        tasks_file.close()

# open taske_file and read user information.
# Loop through text file and get  all information.
#  close file.        
def view_all_tasks():
        tasks_file = open("tasks.txt", "r")
        for line in tasks_file:
            line = line.strip()
            line = line.split(", ")
            print(
            "\nUsername:    \t\t" + line[0] +
                "\nThe title:    \t\t" + line[1] +
                "\nDescription: \t\t" + line[2]+
                "\nDue Date:    \t\t" + line[3] +
                "\nStart date:    \t\t" + line[4] +
                "\nCompleted:   \t\t " + line[5] +
                "\n")
        tasks_file.close()

# Opens the tasks_file and reads through the file.
# For loop through strips file and strip the file
# Adds the number to each tasks_file.
# If username is = the user index acceess user file.
# Print output users tasks.
def view_mine():
        num_task = 0
        with open("tasks.txt", "r") as tasks_file:
            view_mine = tasks_file.readlines()
            for line in view_mine:
                line = line.strip().split(", ")
                num_task += 1
                if username == line[0]:
                    print(
                "\nTask Number: \t\t "+ str(num_task) + 
                "\nUsername:    \t\t" + line[0] +
                "\nThe title:    \t\t" + line[1] +
                "\nDescription: \t\t" + line[2]+
                "\nDue Date:    \t\t" + line[3] +
                "\nStart date:    \t\t" + line[4] +
                "\nCompleted:   \t\t " + line[5] +
                "\n")
        
# Request input to detemine the users wants to edits tasks or exist.
        edit_task = input("Select (Edit) to edit a task or (-1) to return to menu:       ")
        edit_task = edit_task.lower()
# If user selects edit request change file user wants to edit.
# Open file read through file and print selects file.
        if edit_task == "edit":
            num_task = int(input("Please enter the number of tasks:     "))
            num_task = num_task - 1
            with open("tasks.txt", "r") as file:
                tasks_file = file.readlines()
            for line in tasks_file:
                print(line[num_task] + "\n")
                break

# Request input if user has completed tasks.
# If yes strip and split information the replace perivous with new state.
# Open file and write new to task_file.
            task_completed = input(" Is task completed ?  yes | no :              ") 
            if task_completed == "yes": 
                userTask = tasks_file[num_task].strip().split(", ")
                new_state = tasks_file[num_task].strip().replace(userTask[5], task_completed)
                print(new_state)
                with open("tasks.txt", "r+") as tasks_file:
                    tasks_file.seek(0)
                    tasks_file.write(new_state)

# Request input if user has completed tasks.
# If yes strip and split information the replace perivous with new state.
# Open file and write new to task_file.   
            if task_completed == "no":
                userTask = tasks_file[num_task].strip().split(", ")
                new_state = tasks_file[num_task].strip().replace(userTask[5], task_completed)
                print(new_state)
                with open("tasks.txt", "r") as tasks_file:
                    tasks_file.write(new_state)
                
# Elif user selects -1 exit programe and return menu.
        if  edit_task == "-1" and username == "admin":
            return admin_menu()
        elif edit_task == "-1" and username != "admin":
            return user_name()
    
# Counts the tasks in the file and adds any new tasks to the count.
def count_all():
    tasks_file = open("tasks.txt", "r").read()
    all_tasks = tasks_file.count(tasks_file)
    all_tasks += 1
    return all_tasks

# Opens and reads the file.
# Counts the number of files 
# Counts the number fo completed_tasks and incompleted files.
def gen_report():
        tasks_file = open("tasks.txt", "r").read()
        all_tasks = tasks_file.count(tasks_file)
        all_tasks += 1
        completed_tasks = tasks_file.count('Yes')
        
        incompleted_tasks = tasks_file.count('No')
        

# opens the file and reads through the file.
# declares datetime of the currents day.
# For loops through the tasks_file and checks the dates
# And compares if the tasks over due and adds a count.   
        with open("tasks.txt", "r")as tasks_file:
            today = datetime.datetime.today()
            overdue_tasks = 0
            for line in tasks_file:
                if not line.startswith('Due Date'): continue
                field, value = line.split(':')
                if field == 'Due Date':
                    if datetime.datetime.strptime(value.strip(), '%d %m %Y') < today:
                        overdue_tasks = overdue_tasks =+ 1

# Displays the overdue_tasks or incomplete_tasks.
# Calcutales the overdue_tasks divided by   all_tasks time 100 to get percentage.
# Calcutales the incomplete_tasks divided by   all_tasks time 100 to get percentage.
            incompleted_overdue_tasks = overdue_tasks or incompleted_tasks
            percentage_overdue = (overdue_tasks/all_tasks)*100
            percentage_incomplete = (incompleted_tasks/all_tasks)*100

# Creates and file and writs the calcutales the the created file.            
        with open ("task_overview.txt", "w") as task_overview:
            task_overview.write(f"Total number of tasks generated using Task Manager: {all_tasks}\n")
            task_overview.write(f"Total number of tasks completed:  {completed_tasks}")
            task_overview.write(f"\nTotal number of tasks uncompleted:  {incompleted_tasks}")
            task_overview.write(f"\nTotal number of tasks uncompleted or overdue :  {incompleted_overdue_tasks}")
            task_overview.write(f"\nPercentage of tasks incompleted:  {percentage_incomplete:.0f}%")
            task_overview.write(f"\nPercentage of tasks overdue:  {percentage_overdue:.0f}%")

# Opens the file and reads through the file.
# Checks if username and opens users file.
# Counts  the users tasks and adds on.
# count all the yes and no tasks. 
# And compares if the tasks  and adds a count. 
        tasks_file = open("tasks.txt", "r").readlines()
        user_tasks = tasks_file.count(tasks_file)
        check =  input(" Please enter username:  ")
        successful = print(" The report has been successful generated open display_stats")
        for i in tasks_file:
            user_tasks = i.count(i)
            user_tasks += 1
            if username == check:
                completed_tasks = i.count('Yes')
                completed_tasks += 1
                incompleted_tasks = i.count('No')
                incompleted_tasks += 1

# opens the file and reads through the file.
# declares datetime of the currents day.
# For loops through the tasks_file and checks the dates
# And compares if the tasks over due and adds a count. 
            tasks_file = open("tasks.txt", "r").readlines()
            today = datetime.datetime.today()
            overdue_tasks = 0
            for line in tasks_file:
                if not line.startswith('Due Date'): continue
                field, value = line.split(':')
                if field == 'Due Date':
                    if datetime.datetime.strptime(value.strip(), '%d %m %Y') < today:
                        overdue_tasks = overdue_tasks =+ 1 

# Displays the overdue_tasks or incomplete_tasks and gets the percentages.
# Calculates the overdue_tasks divided by   user_tasks time 100 to get percentage.
# Calculates the incomplete_tasks divided by   user_tasks time 100 to get percentage. 
# Calculates  the user_tasks divid by the count function.
            incompleted_overdue_tasks = (overdue_tasks or incompleted_tasks/user_tasks)*100
            percentage_overdue = (overdue_tasks/user_tasks)*100
            percentage_incomplete = (incompleted_tasks/user_tasks)*100
            completed_ontime = (completed_tasks / user_tasks)*100

# Creates and file and writs the calcutales the the created file.
        with open ("user_overview.txt", "w") as user_overview: 
            user_overview.write(f"Generating report for  {username}.\n")
            user_overview.write(f"\nTotal number of tasks assigned:  {user_tasks}.")
            total_user_tasks = (user_tasks / count_all())*100
            user_overview.write(f"\nPercentage of total number of tasks assigned to user:  {total_user_tasks:.0f}%.")
            user_overview.write(f"\nPercentage of tasks assigned completed:  {completed_ontime:.0f}%.")
            user_overview.write(f"\nPercentage of tasks not completed:  {percentage_incomplete:.0f}%.")
            user_overview.write(f"\nPercentage of tasks not completed and overdue :  {incompleted_overdue_tasks:.0f}%.")

# The function checks if task_overview and user_overview file exists.
# If not a report is generated.
# Then open and print report.
def display_stats():
        if not os.path.exists("task_overview.txt") and not os.path.exists("user_overview.txt"):
            gen_report()

        with open("task_overview.txt", "r") as tasks_file:
            print("\nTASK OVERVIEW STATS:\n")
            for line in tasks_file:
                print(line.strip())
        
        with open("user_overview.txt", "r") as tasks_file:
            print('\nUSER OVERVIEW STATS:\n')
            for line in tasks_file:
                print(line.strip())

def exist():
        print("Good bye")

# While loop through and request login input.
# For loop through user.text file and read file line by line.
# Strip whitespace in file.
# Split file to  witha , and space.
# If username and password are equal to enters to text files.
# If login is True output message.
# Else if login is False output message. 
login = False
while login == False:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for line in open("user1.txt", "r").readlines():
        line = line.strip()
        login_user = line.split(", ")
        if username == login_user[0] and password == login_user[1]:
            login = True
        else:
            if login == False:
                print("Incorrect credentials.")

# If user is admin then display admin_me
def admin_menu():
    if username == "admin":
        ad_menu = input('''
    Welcome to the Admin menu.
    Please select one of the following options:
    r\t  - \t register user
    a\t  - \t add task
    va\t - \t view all tasks
    vm\t - \t view my tasks
    gr\t - \t generate report
    ds\t - \t display statistics
    e\t  - \t exit
    ''')
        if  ad_menu == "r":
            reg_user()
        elif ad_menu == "a":
            add_task()
        elif ad_menu == "va":
            view_all_tasks()
        elif ad_menu == "vm":
            view_mine()
        elif ad_menu == "gr": 
            gen_report()
        elif ad_menu == "ds": 
            display_stats()
        elif ad_menu == "e":
            exit()

# If user is not admin display menu.
# Request user information.
def user_name():
    if not username == "admin":  
        user_menu = input('''
    Welcome to the menu:
    Please select one of the following options:
    r\t - \t register user
    a\t - \t add task
    va\t -\t view all tasks
    vm\t -\t view my tasks
    e\t - \t exit
    ''')
        if user_menu == "r":
            print("you are not admin")
            exit()
        if user_menu == "a":
            add_task()
        if user_menu == "va":
            view_all_tasks()
        if user_menu == "vm":
            view_mine()
        if user_menu == "e":
            exit()

# Call user menu functions
def main():
    admin_menu()
    user_name()
main()






