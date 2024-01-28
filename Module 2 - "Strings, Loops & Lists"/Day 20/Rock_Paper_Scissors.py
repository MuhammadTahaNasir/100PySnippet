import random

def display_welcome():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Options: 1. Rock, 2. Paper, 3. Scissors")

def get_user_choice():
    return int(input("Enter your choice (1-3): "))

def display_result(user_action, computer_action):
    print(f"\nYou chose {'Rock' if user_action == 1 else 'Paper' if user_action == 2 else 'Scissors'},"
          f" computer chose {'Rock' if computer_action == 1 else 'Paper' if computer_action == 2 else 'Scissors'}.")

    if user_action == computer_action:
        print("It's a tie!")
    elif (
        (user_action == 1 and computer_action == 3) or
        (user_action == 2 and computer_action == 1) or
        (user_action == 3 and computer_action == 2)
    ):
        print(f"You win!")
    else:
        print("You lose!")

def play_game():
    display_welcome()
    user_choice = get_user_choice()
    computer_choice = random.randint(1, 3)
    display_result(user_choice, computer_choice)

if __name__ == "__main__":
    play_game()
