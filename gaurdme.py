import pyperclip
import pickle
import sys
import os

login = {}

if not os.path.exists("user.txt"):
    open("user.txt", 'w').close()

def lddict():
    try:
        with open("user.txt", 'rb') as fr:
            return pickle.load(fr)
    except EOFError:
        None
        return dict()
              
      
print("\n")
print("Please select the operation Number\n")
print("1. Save Username and Password")
print("2. Retrieve Password")
print("3. Exit\n")
choice = input("Enter your Choice: ").strip()

while True:
        if choice == "1":
            login = lddict()
            username = input("\nEnter Your username: ").strip()

            while username in login.keys():
                print("username already Exist")
                username = input("\nEnter Your Username: ").strip()
            else:
                password = input("Enter Your Password: ").strip()

            
            while username == "" or password == "":
                print("please Enter a valid Username and password:")
                username = input("Enter Your username: ").strip()
                password = input("Enter Your Password: ").strip()

            
            login[username] = password
                        
            
            fo = open("user.txt", 'wb')
            pickle.dump(login,fo)
            fo.close()

            print("\n Your Username and Password has been Saved")
            cont = input("\nDo you want to continue (y/n) ?\n").strip()
            if cont == "y" or cont == "Y":
                print("\n")
                print("Please Select the operation number")
                print("\n")
                print("1. Save Username and Password")
                print("2. retrieve Password")
                print("3.Exit")
                print("\n")
                choice = input("Enter your choice: ").strip()

            elif cont == "n" or cont == "N":
                print ("\t Thank you")
                sys.exit(0)

        elif choice == "2":
            login = lddict()
            print("\n You are about to retrieve your password \n")
            r_username = input("Enter Your username: ").strip()
                        
                        
            if r_username in login.keys():
                #print("The Passowrd is: ") ,
                #...
                #print (login.get(r_username)),  #.get() is used to retrieve password or retrieve value of key
                #r_password = login[username]
                pyperclip.copy(login.get((r_username)))
                print("Your password has been copied to clipboard")
            #f.close()
            else:
                print("username not found")
            break

        elif choice == "3":
            print("\n\tThank You\n")
            sys.exit(0)


