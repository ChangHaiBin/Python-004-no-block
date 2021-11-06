
x = 0
userQuit = False

while (x < 100) and (userQuit == False):
    print(f"Your current score is {x}.")
    print("How many points did you get?")
    input1 = input()

    if input1 == "QUIT":
        userQuit = True
        print("You have quit the game.")
    else:
        try:
            score = int(input1)
            x = x + score
        except:
            print("Invalid input. Please try again")

    print()



if x < 100:
    print("You quit before you reach 100 points. You lose!")
else:
    print("You reach 100 points. You win!")



