first_name = input("What is your name? ")

while first_name == "":
    first_name = input("You have to enter your name: ")


username = input("Enter your username: ");

while username == "":
    username = input("Username cannot be empty. Please enter a username: ")

password = input(f"Enter password of username {username}: ")    

while password == "":
    password = input("Password cannot be empty. Please enter a password: ")

print(f"########## ########## ##### {first_name}! ##### ########## ##########")
print(f"            {username}, you are currently logged in")    
print(f"            {first_name}, welcome to your dashboard")
print(f"########## ########## ##### {first_name}! ##### ########## ##########")