Age=22
counter=0
for i in range(10):
    if counter < 3:
        guess_number=int(input("Plese input your guess number:\n"))
        if guess_number == Age:
            print("You got the number, congratulations!")
            break
        elif guess_number > Age:
            print("The number you guessed is too big, guess a smaller one\n")
        else:
            print("The number you guessed is too small, guess a bigger one\n")
        counter += 1
    elif counter == 3:
        continue_flag=input("Do you want to continue? Please type Y to continue or N to quit:\n ")
        if continue_flag == "Y":
            counter = 0
        else:
            print("Bye")
            break
    else:
        print("You've tried too many times.")
