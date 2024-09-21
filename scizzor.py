rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game = True
while game:
    user_choice = int(input("Enter 0 for 'rock',1 for 'paper',2 for 'scissors'"))
    if user_choice == 0:
        print("You choose 'rock'")
        print(rock)
    elif user_choice == 1:
        print("You choose 'paper'")
        print(paper)
    elif user_choice == 2:
        print("You choose 'scissors'")
        print(scissors)
    else:
        print("You chose something wrong!")
    comp_choice = random.randint(0, 3)
    if comp_choice == 0:
        print("Computer choose 'rock'")
        print(rock)
    elif comp_choice == 1:
        print("Computer choose 'paper'")
        print(paper)
    elif comp_choice == 2:
        print("Computer choose 'scissors'")
        print(scissors)
    else:
        print("Nothing is wrong")
#COMPARING BOTH USER AND COMPUTER INPUTS
    if user_choice == comp_choice:
        print("It's a tie")
    elif user_choice == 1 and comp_choice == 0:
        print("You won!")
    elif user_choice == 0 and comp_choice == 1:
        print("Computer won!")
    elif user_choice == 2 and comp_choice == 1:
        print("You won!")
    elif user_choice == 1 and comp_choice == 2:
        print("Computer won!")
    elif user_choice == 0 and comp_choice == 2:
        print("You won!")
    elif user_choice == 2 and comp_choice == 0:
        print("Computer won!")
    else:
        print("Something is wrong")
    cntnu = input("Do you want to play another game?'yes' or 'no'").lower()
    if cntnu == "no":
        game = False
        print("Thanks for playing this game with me!")
    else:
        game = True