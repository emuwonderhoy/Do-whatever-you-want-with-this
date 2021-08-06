#This is a normal program, so, try convert this to something bigger, this is your code.
username = input("Enter your username: ")
password = input(f"Enter your password: ")
password2 = input(f"re-enter your pasword: ")
if password == password2:
    print("$Welcome, dear ", username)
else:
    print("Please, re-start the program and write correctly your password, else, you never going to register.")
