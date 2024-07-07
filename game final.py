import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

choices = ['rock', 'paper', 'scissors']

while True:
    print("\nLet's play Rock-Paper-Scissors!")
    print("Choose one: rock, paper, or scissors.")
    user_choice = input("Your choice: ").lower()

    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()

    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
