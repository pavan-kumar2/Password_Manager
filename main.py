import random
import string

passwords = {}

try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website]=pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits+"!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Check Result")
    print("4. Exist")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("enter website: ")
        pwd =input("enter password: ")

        passwords[site] = pwd


        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!")

    elif choice =="2":
        if not passwords:
            print("No data")

        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)

    elif choice =="3":
        print("generated Password", generate_password())

    elif choice =="4":
        print("ok bye..")

    else: 
        print("In-valid input")
    