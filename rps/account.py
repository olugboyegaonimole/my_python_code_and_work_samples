print("rock paper scissors account setup")
while True:
    username = input("pick a username: " )
    password = input("pick a password: " )
    password_confirm = input("please confirm your password: ")
    if password != password_confirm:
        print("your passwords don;t match, please try again")

    if password == password_confirm:
        print("your account has been set up")

        #text_file = open("accounts.txt", "r")
        #filelen = sum(1 for line in text_file)

        text_file = open("accounts.txt", "a")

        #if filelen != 0:
        #    text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.write("\n")
        text_file.close()
        break