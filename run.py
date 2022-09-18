import random 

"""Create two variables"""

user_points = 0
computer_points = 0


options = ["r", "s", "p"]  #rock, scissor, papers list

"""Start a loop and use the lower function"""
while True:

    """Use lower() - all characters typed will become lowercase"""

    user_choice = input("Choose R(Rock)/S(Scissor)/P(Paper) or Q to Quit :").lower()


    if user_choice == 'q':  #Quit the game
        break

    if user_choice not in options:
        continue

    """Give some skill to the computer"""

    cpu_choice = random.randint(0, 2)
    cpu_option = options[cpu_choice]

    print("Computer chose " + cpu_option)  # 0 : R, 1 : T, 2 : P

    if user_choice == cpu_option:
        print("Tie!\n")

    elif user_choice == "r" and cpu_option == "s":
        print("You win!\n")
        user_points = user_points + 1

    elif user_choice == "p" and cpu_option == "r":
        print("You win!\n")
        user_points = user_points + 1

    elif user_choice == "S" and cpu_option == "p":
        print("You win!\n")
        user_points = user_points + 1

    """if all conditions are false the user loses the game"""

 
print("Your score: " + str(user_points))
print("Computer score: " + str(computer_points))

if computer_points > user_points:
    print("You Loose!!!!\n")
elif computer_points == user_points:
    print("Tie \n")
else:
    print("You are the Champion!\n")










