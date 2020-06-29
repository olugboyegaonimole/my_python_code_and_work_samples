print ('made by gboyega onimole')

lose = ("the computer wins")
win = ("you win")
lives = 5
score = 0
draws = 0
computer_lives = 5
password_list = []


def you_lose(computer, lives, score, computer_lives):
    print("\n" * 3)
    print("the computer chose ", computer)
    print(" ")
    print("you lose this turn")
    print(" ")
    lives -=1
    print("your score is ", score)
    print(" ")
    print("you have ", lives, " lives left")
    print(" ")
    print("the computer has ", computer_lives, " lives left")
    print("\n" * 3)
    return lives

def you_win(computer, lives, score, computer_lives):
    print("\n" * 3)
    print("the computer chose ", computer)
    print(" ")
    print("you win this turn")
    print(" ")
    score = score + 1
    computer_lives = computer_lives - 1
    print("your score is ", score)
    print(" ")
    print("you have ", lives, " lives left")
    print(" ")
    print("the computer has ", computer_lives, " lives left")
    print("\n" * 3)
    return score, computer_lives

def you_draw(draws, computer, lives, score, computer_lives):
    print("\n" * 3)
    print("the computer chose ", computer)
    print(" ")
    print("draw")
    print(" ")
    draws +=1
    print("your score is ", score)
    print(" ")
    print("you have ", lives, " lives left")
    print(" ")
    print("the computer has ", computer_lives, " lives left")
    print("\n" * 3)
    return draws


while True:
    
    print("WELCOME TO ROCK PAPER SCISSORS!!")
    print("to begin, fill in the below information")
    username = input("please enter your username: ")
    password = input("please enter your password: ")

    searchfile = open("accounts.txt", "r")
    #print(searchfile.read())
    #break
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            
            import time
            time.sleep(1)
            print("loading...")
            time.sleep(1)
            print("loading...")            
            time.sleep(1)
            print("loading...")
            
            montage = """
            access granted!
            -------------------------
            ROCK! PAPER! SCISSORS!
            -------------------------
            rules:
            you start with 5 lives
            if you win you get an extra life
            if you lose you lose a life
            if you draw the lives stay the same
            -------------------------
            -------------------------
            to see a list of rules type rules
            -------------------------
            to see the number of lives you have type lives
            -------------------------
            to see the number of computer lives type computer_lives
            -------------------------
            to see the number of draws type draws
            -------------------------
            to see your score type score
            -------------------------
            to restart type restart
            -------------------------
            at any point type exit to leave the game
            -------------------------
            the computer has lives as well
            can you beat the computer???
            good luck!!!
            -------------------------
            """
            print(montage)

            while True:

                userinput = input("rock, paper, scissors?    ")
                userinput = userinput.lower()

                import random 
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)

                #rock if statements
                if userinput == "rock" and computer == "paper":
                    lives = you_lose(computer, lives, score, computer_lives)
                if userinput == "rock" and computer == "scissors":
                    score, computer_lives = you_win(computer, lives, score, computer_lives)

                #paper if statements
                if userinput == "paper" and computer == "rock":
                    score, computer_lives = you_win(computer, lives, score, computer_lives)
                if userinput == "paper" and computer == "scissors":
                    lives = you_lose(computer, lives, score, computer_lives)

                #scissors if statements
                if userinput == "scissors" and computer == "paper":
                    score, computer_lives = you_win(computer, lives, score, computer_lives)
                if userinput == "scissors" and computer == "rock":
                    lives = you_lose(computer, lives, score, computer_lives)

                #duplicates
                if userinput == "scissors" and computer == "scissors":
                    draws = you_draw(draws, computer, lives, score, computer_lives)

                if userinput == "paper" and computer == "paper":
                    draws = you_draw(draws, computer, lives, score, computer_lives)

                if userinput == "rock" and computer == "rock":
                    draws = you_draw(draws, computer, lives, score, computer_lives)

                #system
                if userinput == "rules":
                    print("\n" * 3)
                    print("RULES")
                    print("rock beats scissors")
                    print("rock loses against paper")
                    print("scissors beats paper")
                    print("scissors loses against rock")
                    print("paper beats rock")
                    print("paper loses against scissors")
                    print("\n" * 3)
                if userinput == "lives":
                    print("\n" * 3)
                    print(lives)
                    print("\n" * 3)
                if userinput == "computer_lives":
                    print("\n" * 3)
                    print(computer_lives)
                    print("\n" * 3)
                if userinput == "score":
                    print("\n" * 3)
                    print(score)
                    print("\n" * 3)
                if userinput == "draws":
                    print("\n" * 3)
                    print(draws)
                    print("\n" * 3)

                #exit
                if lives == 0:
                    print("thanks for playing")
                    print("you've run out of lives")
                    print("you beat the computer ", score, " times")
                    print("you drew ", draws, " times")
                    stop = input("press enter to exit")
                    exit()

                if userinput == "exit":
                    print("thanks for playing")
                    print("you beat the computer", score, "times")
                    print("you drew", draws, "times")
                    stop = input("press enter to exit")
                    exit()

                if computer_lives == 0:
                    print("thanks for playing")
                    print("the computer lost all its lives, you win the game")
                    print("you beat the computer ", score, " times")
                    print("you drew ", draws, " times")
                    stop = input("press enter to exit")
                    exit()

                if userinput == "restart":
                    break
        else:
            print("your username or password is incorrect")
            print("--------------------")
