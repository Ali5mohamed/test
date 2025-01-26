import time
import os
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class User:
    def __init__(self,name , second_name , email , passwerd):
        
        self.name = name 
        self.second_name = second_name
        self.email = email
        self.passwerd = passwerd
        #self.inputs()
        
    def description(self):
        
        print (f"The first name is: {self.name}")
        print (f"The second name is: {self.second_name}")
        print (f"The email is: {self.email}")
        print (f"The passwerd is: {self.passwerd}")
         
def inputs():
    name = input("Enter the first name? ")
    second_name = input("Enter the second name? ")
    email = input("Enter the email? ")
    passwerd = int(input("Enter the paswerd? "))
    return User(name , second_name , email , passwerd)
users = []    
while True:
    print("""
          ***Welcome to the program***
          ##Choose from the following options##
          1- Add a new user
          2- View all users
          3- Delete a user
          4- Exit the program
          
          """)
    choice = input ("What is your choice [ 1 or 2 or 3 or 4 ]? ")
    if choice == "1":
        user = inputs()
        users.append(user)
       
        clear_screen()
        print("***User added successfully!***\n")
        time.sleep(2)
        
    elif choice == "2":
        clear_screen()
        
        for i in users:
            if users:
                #clear_screen()
                print(i.description())
                print("*" * 30)
            else:
                print("There are no users currently") 
    
    elif choice == "3":
        pass
    
                       
    elif choice == "4":
        print("I will leave the program.  Goodbye!")
        break
    else:
        print("Your choice is incorrect")
