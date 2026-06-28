import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Score variables
user_score = 0
computer_score = 0

# Game loop
while True:

    # User-friendly interface
    print("\n==============================")
    print(" ROCK PAPER SCISSORS GAME")
    print("==============================")
    print("Choose: Rock, Paper, or Scissors")

    # User input
    user_choice = input("Enter your choice: ").lower()

    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Computer selection
    computer_choice = random.choice(choices)

    # Display choices
    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game Logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):

        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    # Display scores
    print("\n===== SCORE BOARD =====")
    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Scores")
        print("Your Score     :", user_score)
        print("Computer Score :", computer_score)
        print("Thanks for playing!")
        break