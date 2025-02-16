import random
print("WELCOME TO THE GAME")
# Hangman Word List 
words = ["python", "developer", "program", "algorithm", "variable"]
secret_word = words[random.randint(0, len(words) - 1)]  # Select a random word
guessed_letters = set()

# Tic-Tac-Toe Board 
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Rock-Paper-Scissors Choices
rps_choices = ["rock", "paper", "scissors"]

turn = "X"

def display_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def display_word():
    displayed = []
    for letter in secret_word:
        if letter in guessed_letters:
            displayed.append(letter)
        else:
            displayed.append("_")
    print("Word: " + " ".join(displayed))

def check_tic_tac_toe_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_word_complete():
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def play_rps():
    print("Rock, Paper, or Scissors? ")
    player_choice = input().lower()
    
    while player_choice not in rps_choices:
        print("Invalid choice! Choose Rock, Paper, or Scissors: ")
        player_choice = input().lower()

    # Select RPS for computer manually
    computer_index = random.randint(0, 2)  # Get a random index
    computer_choice = rps_choices[computer_index]  # Picks RPS move from list
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie! You get another chance.")
        return True

    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "scissors" and computer_choice == "paper") or \
       (player_choice == "paper" and computer_choice == "rock"):
        print("You win RPS! You still get to place your mark.")
        return True
    else:
        print("You lost RPS! Turn skipped.")
        return False

while True:
    display_board()
    display_word()

    print("Player", turn, "'s turn!")
    letter = input("Guess a letter: ").lower()

    if letter in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.add(letter)

    if letter in secret_word:
        print("Correct guess!")
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                if board[row][col] == " ":
                    board[row][col] = turn
                    break
                else:
                    print("Cell already occupied!")
            except:
                print("Invalid input! Enter numbers between 0 and 2.")
    else:
        print("Wrong guess! But you can save your turn by winning Rock-Paper-Scissors!")
        if play_rps():  # If the player wins RPS, they still get to place a mark
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))

                    if board[row][col] == " ":
                        board[row][col] = turn
                        break
                    else:
                        print("Cell already occupied!")
                except:
                    print("Invalid input! Enter numbers between 0 and 2.")

    winner = check_tic_tac_toe_winner()
    if winner:
        display_board()
        print("Player", winner, "wins the Tic-Tac-Toe game!")
        break

    if is_word_complete():
        display_word()
        print("The word was guessed completely! It's a draw!")
        break

    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print("Tic-Tac-Toe board is full! It's a draw!")
        break

    turn = "O" if turn == "X" else "X"
