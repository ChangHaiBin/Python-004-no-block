
x = 0

while x < 100:
    print(f"Your current score is {x}.")
    print("How many points did you get?")
    input1 = input()

    try:
        score = int(input1)
        x = x + score
    except:
        print("Invalid input. Please try again")

    print()




print("You reach 100 points. You win!")


input("Press Enter to continue:")

