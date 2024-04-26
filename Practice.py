# stone paper scissor game using def function
import random


def welcome():
    print("Welcome to the stone paper scissor game ")
    name = input("What is your name? :")


def game():
    user_score = 0
    computer_score = 0
    choice = ['rock', 'paper', 'scissors']
    choice2 = [1,2,3]
    # random_choice = random.choice(choice)
    no_of_round = int(input("How many rounds would you like to play :"))
    count_of_rounds = 0
    print('''For rock press no 1 
    For paper press no 2 
    For scissors press no 3 
    For exit press no 4
    For quit press no 5''')
    print()
    while count_of_rounds < no_of_round:
        count_of_rounds += 1
        random_choice = random.choice(choice)
        user_choice = int(input("Your choice in integer value :"))
        if user_choice == 4:
            break
        if user_choice not in choice2:
            count_of_rounds -= 1
            continue
        elif user_choice  == 1 and random_choice == 'paper':
            print("Tie")
        elif user_choice == 2 and random_choice == 'rock':
             print("TIE")
        elif user_choice == 3 and random_choice == 'scissor':
            print("TIE")
        elif user_choice == 2 and random_choice == "rock":
            user_score += 1
            print("YOU wins!")
        elif user_choice == 1 and random_choice == "scissors":
            user_score += 1
            print("YOU wins!")
        elif user_choice == 3 and random_choice == "paper":
            user_score += 1
            print("YOU win")
        else:
            computer_score += 1
            print("YOU LOSE ")

    print("The total score is below ")
    print()
    if user_score > computer_score:
        print("YOU WIN  WTITH THE POINT OF {}".format(user_score))
    else:
        if user_score == computer_score:
            print("TIE")
            play_again()
        else:
            print("YOU LOSE WTITH THE POINT OF {}".format(computer_score))


def play_again():
    game()

welcome()
game()
print()
print("Thank you for playing!")
print("IF you want to play again press 10 ")
user = int(input("Enter your choice: "))
if user == 10:
    play_again()
else:
    print("Thank you for playing!")