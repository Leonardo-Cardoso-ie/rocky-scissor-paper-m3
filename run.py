import random 

"""Create two variables"""

user_points = 0
computer_points = 0


options = ["r", "s", "p"] #rock, scissor, papers

"""Start a loop and use the lower function"""
while True:

    """Use lower() - all characters typed will become lowercase"""

    user_choice = input("Choose R(Rock)/S(Scissor)/P(Paper) ou Q to quit.").lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    """Give some skill to the computer"""

    cpu_choice = random.randint(0, 2)
    # 0 : R, 1 : T, 2 : P
    cpu_option = options[computer_choice]






