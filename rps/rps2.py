
draws=0
lives=5
computerlives=5
score=0
passlist=[]

def win(computer, draws, score, lives, computerlives):
    print("\n" *3)
    print("you win")
    print("the computer chose", computer)
    score+=1
    computerlives-=1
    print("your score is", score)
    print("you have", lives, "lives left")
    print("the computer has", computerlives, "lives left")
    print("\n" *3)
    return score, computerlives

def lose(computer, draws, score, lives, computerlives):
    print("\n" *3)
    print("you lose")
    print("the computer chose", computer)
    lives-=1
    print("your score is", score)
    print("you have", lives, "lives left")
    print("the computer has", computerlives, "lives left")
    print("\n" *3)
    return lives

def draw(computer, draws, score, lives, computerlives):
    print("\n" *3)
    print("draw")
    print("the computer chose", computer)
    draws+=1
    print("your score is", score)
    print("you have", lives, "lives left")
    print("the computer has", computerlives, "lives left")
    print("\n" *3)
    return draws

while True:

    username=input("enter username: ")
    password=input("enter password: ")

    file_object = open("accounts.txt", "r")

    for item in file_object:
        passlist.append(item.strip())

    if username and password in passlist:

        rules = """
        ------------------------------
        RULES:
        ------------------------------
        rock beats scissors
        paper beats rock
        scissors beats paper
        ------------------------------
        """

        commands="""
        ------------------------------
        COMMANDS:
        ------------------------------
        to see how many lives you have left type lives
        ------------------------------
        to see your score type score
        ------------------------------
        to see how many lives the computer has left type computerlives
        ------------------------------
        to see how many times you've drawn type draws
        ------------------------------
        """

        print("")
        print("    WELCOME TO ROCK PAPER SCISSORS!!!")
        print("")
        print(rules)
        print("")
        print(commands)


        while True:

            userinput=input("rock, paper, scissors? ")
            userinput=userinput.lower()

            import random
            computer = ("rock", "paper", "scissors")
            computer = random.choice(computer)


            #rock 
            if userinput=="rock" and computer=="rock":
                draws=draw(computer, draws, score, lives, computerlives)

            if userinput=="rock" and computer=="paper":
                lives=lose(computer, draws, score, lives, computerlives)

            if userinput=="rock" and computer=="scissors":
                score, computerlives=win(computer, draws, score, lives, computerlives)


            #paper 
            if userinput=="paper" and computer=="paper":
                draws=draw(computer, draws, score, lives, computerlives)

            if userinput=="paper" and computer=="scissors":
                lives=lose(computer, draws, score, lives, computerlives)

            if userinput=="paper" and computer=="rock":
                score, computerlives=win(computer, draws, score, lives, computerlives)


            #scissors 
            if userinput=="scissors" and computer=="scissors":
                draws=draw(computer, draws, score, lives, computerlives)

            if userinput=="scissors" and computer=="rock":
                lives=lose(computer, draws, score, lives, computerlives)

            if userinput=="scissors" and computer=="paper":
                score, computerlives=win(computer, draws, score, lives, computerlives)



            if lives==0:
                print("you have run out of lives")
                print("thanks for playing")
                print("your score is", score)
                print("you have", lives, "lives left")
                print("the computer has", computerlives, "lives left")
                stop=input("press enter to exit")
                exit()
                
            if computerlives==0:
                print("you win!")
                print("thanks for playing")
                print("your score is", score)
                print("you drew", draws,"times")
                print("you have", lives, "lives left")
                print("the computer has", computerlives, "lives left")
                stop=input("press enter to exit")
                exit()

            if userinput=="exit":
                print("your score is", score)
                print("you have", lives, "lives left")
                print("the computer has", computerlives, "lives left")
                stop=input("press enter to exit")
                exit()

            if userinput=="restart":
                break


            if userinput=="rules":
                print("")
                print(rules)
                print("")

            if userinput=="commands":
                print("")
                print(commands)
                print("")

            if userinput=="lives":
                print("")
                print("you have", lives, "lives left")
                print("")

            if userinput=="computerlives":
                print("")
                print("the computer has", computerlives,"lives left")
                print("")

            if userinput=="score":
                print("")
                print("your score is", score)
                print("")

            if userinput=="draws":
                print("")
                print("the number of draws is", draws)
                print("")
    else:
        print("username and/or password incorrect")
