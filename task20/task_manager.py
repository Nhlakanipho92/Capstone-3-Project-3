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
    for line in open("user.txt", "r").readlines():
        line = line.strip()
        login_user = line.split(", ")
        if username == login_user[0] and password == login_user[1]:
            login = True
    print("Welcome", username)
else:
    if login == False:
       print("Incorrect credentials.")

# Verify user to access the different menu.
options = input("Verify username:    ")
if options == "admin":
# If user is admin then display admin_menu. 
# Request input from user.   
    admin_menu = input('''
    Welcom to the Admin menu.
    Please select one of the following options:
    r\t  - \t register user
    a\t  - \t add task
    va\t - \t view all tasks
    vm\t - \t view my tasks
    s\t  - \t statistics
    e\t  - \t exit
    ''')

# If users selects r  then request new user information.
# Declare register as false
# Loop through register and request confirmion information.
# If confirmion information equals user information.
# Append user information to user.txt file and break.
    if options == "admin" and admin_menu == "r":
            reg_username = input("Enter new username:                     \t")
            reg_password = input("Enter new password:                     \t")
            register = False
            while register == False:
               confirm_username = input("Enter username to confirm username:   \t")
               confirm_password = input("Enter username to confirm password:   \t")
               if confirm_username == reg_username and confirm_password == reg_password:
                   print()
                   print("Registration successful")
                   user_file = open("user.txt", "a")
                   user_file.write("\n")
                   user_file.write(reg_username)
                   user_file.write(", ")
                   user_file.write(reg_password)
                   user_file.close()
                   break
            else:
                print("username or password doesn't match")

# If users selects 'a'.
# Open tasks_file and append user information.
# Request input from user.
# close taske_file.
    if admin_menu == "a":
        tasks_file = open("tasks.txt", "a+")

        user = input("Enter username                                \t")
        title = input("Enter title of the task:                     \t")
        description = input("Enter description of the task:         \t")
        due_date = input("Enter due date:                           \t")
        current_date = input("Enter current date                    \t")
        is_complete = "No"
        tasks_file.write(f"{user}, {title}, {description}, {due_date}, {current_date}, {is_complete}\n")
        tasks_file.close()

# If users selects 'va'.
# open taske_file and read user information.
# Loop through text file and get  all information.
#  close file.
    elif admin_menu == "va":
        tasks_file = open("tasks.txt", "r")

        for line in tasks_file:
            line = line.strip()
            user, title, description, due_date, current_date, is_complete = line.split(", ")
            print(f'''
            Username :         \t\t{user}
            The title :        \t\t{title}
            Description :      \t\t{description}
            End date :         \t\t{due_date}
            Start date :       \t\t{current_date}
            Is task complete : \t\t{is_complete}
            ''')
        tasks_file.close()

# If users selects 'vm'.
# open taske_file and read user information.
# Loop through text file and get  useers information.
# close file.
    elif admin_menu == "vm":
        tasks_file = open("tasks.txt", "r")

        for line in tasks_file:
            line = line.strip()
            user, title, description, due_date, current_date, is_complete = line.split(", ")
            if username == user:
                print(f'''
                Username :         \t\t{user}
                The title :        \t\t{title}
                Description :      \t\t{description}
                End date :         \t\t{due_date}
                Start date :       \t\t{current_date}
                Is task complete : \t\t{is_complete}
                ''')
        tasks_file.close

# If users selects 's'.
# Open user_file and read user information line by line.
# Sum up all lines.
# Display output.
    elif admin_menu == "s":
        user_file = open("user.txt", "r").readlines()
        sum_users = 0
        for i in user_file:
            sum_users += 1
        print(f"There are {sum_users} users")
# Open tasks_file and read user information line by line.
# Sum up all lines.
# Display output.
        tasks_file = open("tasks.txt", "r").readlines()
        sum_tasks = 0
        for i in tasks_file:
            sum_tasks += 1
        print(f"There are {sum_tasks} tasks")
# If user selects 'e'.
# Print  message and exit.
    if admin_menu == "e":
        print("Good bye")

# If user is not admin display menu.
# Request user information.
if options != "admin":
    user_menu = input('''
    Welcome to the menu:
    Please select one of the following options:
    r\t - \t register user
    a\t - \t add task
    va\t -\t view all tasks
    vm\t -\t view my tasks
    e\t - \t exit
    ''')
    
# If user selects 'r'
# Compare option input and check if input is admin and r.
    if options == "admin" and user_menu == "r":
# If check is admin request new information.
# And confirm username and password.
# if confirmion information is equal to new user information.
# Display message and append new user information to user_file.
# close user_file.
        register_admin = False 
        while register_admin == False:
            new_username = input("Enter new users username:                \t")
            new_password = input("Enter new users password:             \t")

            confirm_username = input("Enter username to confirm username: \t")
            confirm_password = input("Enter username to confirm password: \t")
            if confirm_username == new_username and confirm_password == new_password:
                print("Registration successful")
                user_file = open("user.txt", "a")
                user_file.write("\n")
                user_file.write(new_username)
                user_file.write(", ")
                user_file.write(new_password)
                break
            else:
                print("username or password doesn't match")
    else:
        print("Only admin users are allowed to register")

# If users selects 'a'.
# Open tasks_file and append user information.
# Request input from user.
# close taske_file.         
    if user_menu == "a":
        tasks_file = open("tasks.txt", "a+")

        user = input("Enter username                               \t")
        title = input("Enter title of the task:                    \t")
        description = input("Enter description of the task:        \t")
        due_date = input("Enter due date:                          \t")
        current_date = input("Enter current date                   \t")
        is_complete = "No"
        tasks_file.write(f"\n{user}, {title}, {description}, {due_date}, {current_date}, {is_complete}")

        tasks_file.close()
    
# If users selects 'va'.
# open taske_file and read user information.
# Loop through text file and get  all information.
#  close file.
    elif user_menu == "va":
        tasks_file = open("tasks.txt", "r")

        for line in tasks_file:
            line = line.strip()
            user, title, description, due_date, current_date, is_complete = line.split(", ")
            print(f'''
            Username :         \t\t{user}
            The title :        \t\t{title}
            Description :      \t\t{description}
            End date :         \t\t{due_date}
            Start date :       \t\t{current_date}
            Is task complete : \t\t{is_complete}
            ''')
        tasks_file.close

# If users selects 'vm'.
# open taske_file and read user information.
# Loop through text file and get  useers information.
# close file.
    elif user_menu == "vm":
        tasks_file = open("tasks.txt", "r")

        for line in tasks_file:
            line = line.strip()
            user, title, description, due_date, current_date, is_complete = line.split(", ")
            if username == user:
                print(f'''
                Username :         \t\t{user}
                The title :        \t\t{title}
                Description :      \t\t{description}
                End date :         \t\t{due_date}
                Start date :       \t\t{current_date}
                Is task complete : \t\t{is_complete}
                ''')
        tasks_file.close

# If user selects 'e'.
# Print  message and exit.
    else:
        user_menu == "e"
        print("Good bye")

# Done by Nhlakanipho Hlophe
# nhlakaniphohlophe@gmail.com

