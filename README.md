The BoxShogi Project  
Sandra Shi

1. Introduction: This project is am implemenation of an mini shogi
game between two players on an 5 * 5 board. It contains two modes:
an interactive mode, which allows the players to play the game 
interactively, and the file mode, which takes in a file containing
{board state, captures, a list of moves}, could parse the file and
return updates to the game board accordingly. 

2. Correctness: The project passes all the test cases provided.

3. Run: To run the file, uses the command provided in .command, 
as well as the test runner provide by Box. 

4. Design decisions: I decide that the game could be broken down 
into the following pieces:
a. Piece, which represents the pieces in Shogi
b. board, which represents the chess board
c. square, which represents a specific square in the board
d. player, which represents the players in game
e. game, which is the game itself

All the pieces in Shogi, no matter in its promoted or unpromoted
form, share certain similar attributes, and it makes sense to 
make all of them extend an abstract piece class. 

I also noted that any move made by the player is essentially of two
type: drop and move. For each type, we have a lot of edge cases to 
deal with, and need to be constantly mindful of the validity and 
change in game board & player capture's states. Therefore, I made
an additional move class to make passing over such information
simpler and more efficient. 

5. Time performance. The algorithm used by some of my methods
coud have a high time complexity. In particular, when attempting to 
generate all possible moves a player could do to "uncheck" himself/
herself, I iterate thorugh all the pieces captured by the player, as
well as all of the player's active pieces, then go to each of them's 
all possible moves, and attempt to drop/move a piece there to prevent 
check. Thankfully, the input size of the board is 5 * 5, and the game
runs for at most 400 iterations, so time complexity has not become
a huge burden. 

