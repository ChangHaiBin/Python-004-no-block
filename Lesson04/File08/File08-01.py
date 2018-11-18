
x = 1
y = 2

while x < 1000:
    print(f"x and y are currently {x} and {y} respectively")
    input("Press ENTER to continue")
    
    z = x + y
    print(f"z is the sum of x and y. z is now {z}")
    input("Press ENTER to continue")

    x = y
    print(f"x has been replaced with the value of y. x is now {x}")
    input("Press ENTER to continue")

    y = z
    print(f"y has been replaced with the value of z (which is the sum of the previous x and y). y is now {y}")
    input("Press ENTER to continue")





print("Fibonacci sequence ended.")

input("Press Enter to continue:")

