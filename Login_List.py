usernames = ["hbrown", "peter299", "claire50", "thepythoncoder", "marymelendez", "abhishek01", "robin.deacon", "drakevaldez", "amira80", "naturewalker"]
passwords = ["Aw-M8a", "v5Z*d<", "happy", "codingiscool", "'nfY4#", "aljdssd", "Js.-2#", "ckS7Nq", "vRK6yw", "treeflowers"]

while True:
    print("Welcome. Please choose from the following options:")
    print("1: Register")
    print("2: Login")
    print("3: Exit")
    number = int(input("Please enter a number: "))

    if number == 1:
        print("Please register below.")
        usernamereg = input("Enter the username you would like to use: ")
        passwordreg = input("Enter the password you would like to use: ")
        usernames.append(usernamereg)
        passwords.append(passwordreg)
        print("Registration successful.")

    elif number == 2:
        username_login = input("Enter your username: ")
        password_login = input("Enter your password: ")
        while username_login not in usernames:
            print(input("Username wrong, please enter again: "))
        position = usernames.index(username_login)
        while password_login != passwords[position]:
            print("Password incorrect.")
            password_login = input("Enter your password: ")
        print("Welcome. Access granted.")
        break

    elif number == 3:
        print("Thanks for visting. Goodbye.")
        break
