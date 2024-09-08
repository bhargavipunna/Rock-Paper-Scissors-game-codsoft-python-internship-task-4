import random


# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


# Function to display results
def display_result(user_choice, computer_choice, winner):
    print(f"\nUser choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")


# Main game function
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to stop playing): ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, winner)
        print(f"Scores - User: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\n--- Final Scores ---")
    print(f"User: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")


# Start the game
play_game()
