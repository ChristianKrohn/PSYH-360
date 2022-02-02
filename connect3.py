# The number of rows on the board
NROW = 7
# The number of columns on the board
NCOL = 6
# The number of connected pieces needed to win
NWIN = 4

# Used to end the game once winner is true.
winner = False

# Empty array that will hold the entire game board and pieces
board = []
# Empty array that will hold the player's pieces
pieces = []

# The current player's character that will appear on the board, starts as X
activePlayer = "X"


# Resets variables and arrays so the game can be played again
def reset_game():
    # Makes the global winner variable be used in the function
    global winner
    # Resets winner to false so the game won't end instantly
    winner = False

    # Makes the global activePlayer variable be used in the function
    global activePlayer
    # Resets activePlayer to X for the new game
    activePlayer = "X"

    # Makes the global pieces array be used in the function
    global pieces
    # Empties the pieces array for the new game
    pieces = []

    # Makes the global board array be used in the function
    global board
    # Empties the board array for the new game
    board = []
    # Prints out the game board for the needed number of rows
    for i in range(NROW + 1):
        # If i isn't at the end of the range
        if i != NROW:
            # Adds the empty row with its proper number to the array
            board.append(f"{NROW-i}|   |   |   |   |   |   |")
        else:
            # Adds the numbers below the board, for each column, into the array
            board.append(f"   1   2   3   4   5   6")
        # Prints out the current value (line) of the game board
        print(board[i], "\n")

    # Empty array used to make pieces have the proper number of elements
    columns = []
    # For each of the columns on the board, and each row position in that column
    for i in range(NCOL):
        for j in range(NROW):
            # Add a " " to each element in the array
            columns.append(" ")
        # Adds the column of " " into the pieces array 
        pieces.append(columns)
        # Resets the columns array for the next iteration of the for loop
        columns = []


# Prints out the game board
def print_board():
     # Makes the global board array be used in the function
    global board
    # For the number of rows on the board, plus the numbered row on the bottom
    for i in range(NROW + 1):
        # If i isn't at the end of the range
        if i <= 6:
            # Changes the current row of board[] to be formatted and contain the current pieces.
            board[i] = (f"{NROW-i}| {pieces[0][i]} | {pieces[1][i]} | {pieces[2][i]} | {pieces[3][i]} | {pieces[4][i]} | {pieces[5][i]} |")
        # Prints the current row in the terminal
        print(board[i], "\n")


# Handles the placement of player pieces.
# @Column = The column the current player wants to place a piece
# @Player = The current player
# @return: Returns None if the piece placement was valid, else returns 1
def place_piece(Column, Player):
    # Turn the value of Column into a useable int 
    Column = int(Column)
    # For the number of rows in each column.
    for i in range(NROW):
        # If the lowest spot of the column is available.
        if pieces[Column-1][6-i] != "X" and pieces[Column-1][6-i] != "O":
            # Insert the current players character into the pieces array.
            pieces[Column-1][6-i] = Player
            # Piece was placed
            return None
    # Piece couldn't be placed
    return 1


# Checks if a player has won the game
# @Player = The activePlayer's character
# @return: Returns True if a player has one, else returns the value of draw_check() 
def win_check(Player):
    # For the number of columns, and number of rows that need to be examined, on the board. 
    for i in range(NCOL):
        for j in range(NROW - 3):
            # Checks if the activePlayer has won vertically
            if pieces[i][j] == Player and pieces[i][j+1] == Player and pieces[i][j+2] == Player\
                 and pieces[i][j+3] == Player:
                return True
    # For the number of rows and columns on the board that need to be examined
    for i in range(NCOL - 3):
        for j in range(NROW - 3):
            # Checks if the activePlayer has won in a diagonal line to the right
            if pieces[i][j] == Player and pieces[i+1][j+1] == Player and pieces[i+2][j+2] == Player\
                and pieces[i+3][j+3] == Player:
                return True
            # Checks if the activePlayer has won in a diagonal line to the left
            elif pieces[i][j+3] == Player and pieces[i+1][j+2] == Player and pieces[i+2][j+1] == Player\
                and pieces[i+3][j] == Player:
                return True
    # For the number of columns that need to be examined, and the number of rows, on the board
    for i in range(NCOL - 3):
        for j in range(NROW):
            # Checks if the player has won horizontally
            if pieces[i][j] == Player and pieces[i+1][j] == Player and pieces[i+2][j] == Player\
                and pieces[i+3][j] == Player:
                return True
    # Returns the result of draw_check to see if the game is a tie
    return draw_check()


# Checks if the game has ended in a draw
# @return: Returns false if there is a valid spot to be played in, else return true
def draw_check():
    # For the number of columns and rows the player can place a piece in
    for i in range(NCOL):
        for j in range(NROW):
            # Checks if the current place on the board has been played in.
            if pieces[i][j] == " ":
                # The game board is not full
                return False
    # The game board is full
    print("The game has ended in a tie, nobody wins.")
    return True


# Handles the sequence of the activePlayer's turn
# @Player = the activePlayer
def player_turn(Player):
    # Used to make sure the player makes a valid move.
    valid = False

    # While the player hasn't made a valid move
    while valid == False:
        # Stores the activePlayer's inputted column
        Column = input(f"Player {Player}, pick a column to drop a piece in: ")

        # Checks if the player inputted an invalid column
        if Column != "1" and Column != "2" and Column != "3" and Column != "4" and Column != "5" and Column != "6":
            print("Invalid column, please try again. \n")
        else:
            # Used to store whether or not the activePlayer placed a piece
            placement = place_piece(Column, Player)
            # If a piece was placed in the place_piece function
            if placement == None:
                # Ends the players turn
                valid = True
            else:
                print(f"Invalid placement, column {Column} is full, please try again. \n")
    # Prints out the board for the players to see.
    print_board()


# Handles the main gameplay loop
def play_game():
    # Call to reset the game 
    reset_game()
    # Makes the global winner variable be used in the function
    global winner

    # While the game isn't over yet
    while winner != True:
        # Makes the activePlayer variable be used in the function
        global activePlayer
        # Swaps the activePlayer's character with the opposite character
        if activePlayer == "X":
            activePlayer = "O"
        else:
            activePlayer = "X"

        # Starts the activePlayer's turn
        player_turn(activePlayer)
        # Used to end the game when a player wins
        winner = win_check(activePlayer)

    print(f"Player {activePlayer} is the winner! \n")
    # Stores the player's choice to replay or not
    replay = input("Would you like to play again? Type Y to replay: ")

    # Restarts the game is the players wish to play again
    if replay == "Y":
        play_game()
    else:
        print("Goodbye!")

# Launches the game once the program is run.
play_game()