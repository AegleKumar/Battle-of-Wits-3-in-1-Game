# Battle-of-Wits-3-in-1-Game
This Python game combines Hangman, Tic-Tac-Toe, and Rock-Paper-Scissors (RPS). Players guess letters for Hangman—correct guesses allow a Tic-Tac-Toe move, while wrong guesses trigger an RPS match to save their turn. The game ends when Tic-Tac-Toe is won or the Hangman word is fully guessed, creating a fun and strategic experience.

## How It Works  
1. **Hangman Phase**   
   - Players take turns guessing letters in a hidden word.  
   - A correct guess allows them to place an **X or O** on the Tic-Tac-Toe board.  
   - A wrong guess triggers an **RPS match** against the computer.  

2. **Rock-Paper-Scissors (RPS) Phase** 
   - If they win, they **keep their turn** and place their Tic-Tac-Toe mark.  
   - If they lose, their **turn is skipped**.  

3. **Tic-Tac-Toe Phase**   
   - The game continues until **a player wins Tic-Tac-Toe** or **the Hangman word is fully guessed**.  
   - If the board fills up without a winner, it's a draw.  

## 🔧 Features  
✅ Random word selection for Hangman  
✅ Turn-based play (X & O)  
✅ Simple text-based Tic-Tac-Toe board  
✅ RPS as a turn-saving mechanic  
✅ Input validation for a smooth experience  

## 🏆 Win Conditions  
- **Tic-Tac-Toe Win:** A player forms a row, column, or diagonal of 3 Xs or Os.  
- **Hangman Win:** The word is fully guessed before Tic-Tac-Toe ends.  
- **Draw:** If neither game is won, it's a tie.

