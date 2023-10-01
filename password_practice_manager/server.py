from cryptography.fernet import Fernet

#this function is for getting the master key..
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

#this function is for adding a user and the users password..
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write( name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#this function is for viewing the user and the users password..
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: ", user, ", Password: ", fer.decrypt(password.encode()).decode())

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? If you want to quit please press q. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid")