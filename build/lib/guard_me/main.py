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

def menu():
    print("\n")
    print("\t\t MENU")
    print("\t\t==================================\n")
    print("\t\tPLEASE SELECT THE OPERATION NUMBER\n")
    print("\t\t1. Save Username and Password")
    print("\t\t2. Retrieve Password")
    print("\t\t3. Exit\n")
    print("\t\t==================================\n")
    choice = input("Enter your Choice: ").strip()

    while True:
            if choice == "1":
                login = lddict()
                username = input("\nEnter Your username: ").strip()
                while username in login.keys():
                    print("\t\tusername already Exist")
                    username = input("\nEnter Your Username: ").strip()

                while username == "":
                    print("\n\t\tPlease Enter a valid Username\n")
                    username = input("Enter Your username: ").strip()

                password = input("Enter Your Password: ").strip()
                while password == "":
                    print("\n\t\tPleaser Enter a valid Password\n")
                    password = input("Enter Your Password: ").strip()

                login[username] = password

                fo = open("user.txt", 'wb')
                pickle.dump(login,fo)
                fo.close()

                print("\n Your Username and Password has been Saved")
                cont = input("\nDo you want to continue (y/n) ?\n").strip()
                if cont == "y" or cont == "Y":
                    menu()

                elif cont == "n" or cont == "N":
                    print ("\t Good Bye\n")
                    sys.exit(0)

            elif choice == "2":
                login = lddict()
                print("\n\n\t\tYou Are About To Retrieve Your PASSWORD \n")
                r_username = input("Enter Your username: ").strip()
                            
                            
                if r_username in login.keys():
                    pyperclip.copy(login.get((r_username)))
                    print("\n\t\tYour PASSWORD Has Been Copied To Clipboard\n\t Use Ctrl + V And Paste Your Password To Your Desired Location.\n")
                else:
                    print("username not found")

                cont1 = input("\nDo you want to continue (y/n) ?\n").strip()
                if cont1 == "y" or cont1 == "Y":
                    menu()

                elif cont1 == "n" or cont == "N":
                    print ("\t Good Bye\n")
                    sys.exit(0)

            elif choice == "3":
                print("\n\tGood Bye\n")
                sys.exit(0)

            elif choice == "": #and choice >= "4":
                print("\n\n\t\tPLEASE ENTER A VALID CHOICE NUMBER\n")
                menu()

            elif choice >= "4":
                print("\n\n\t\tPLEASE ENTER A VALID CHOICE NUMBER\n")
                menu()

def main():
    menu()


if __name__=='__main__':
    main()