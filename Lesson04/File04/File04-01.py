
x = 1

subtotal = 0

while x < 100:

    if (x % 2 == 1):
        subtotal = subtotal + x
        print(f"{x} added to subtotal")
    else:
        print(f"{x} is NOT added to subtotal")

    print(f"The current subtotal is {subtotal}")
    input("Press Enter to continue:")
    x = x + 1



print(f"The sum of all odd numbers from 1 to 99 is {subtotal}")



