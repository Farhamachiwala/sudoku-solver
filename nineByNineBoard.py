def displayBoard2(board):
   '''
   Displays the board to the screen
   Input: board (list of lists) - the board that needs to be displayed
   Returns: None
   '''
   print()
   for row in range(len(board)):
      # for every third row, it prints the dashes
      if row % 3 == 0:
         print("- " * 19)

      for col in range(len(board[0])):
         # leaves a space between each number
         if board[0] and col != 0:
            print(" ", end="")
         # for every third column, it prints the border
         if col % 3 == 0:
            print("|  ", end="")

         # if it is the eighth column, it prints the number as well as the border
         if col == 8:
            print(str(board[row][col]) + "  |")
         else:
            print(str(board[row][col]) + " ", end="")
   
   print("- " * 19)
   print()

def findEmpty(board):
   '''
   Find the coordinates of an empty space
   Input: board (list of lists) - the board that needs to be solved
   Returns: a tuple with the location of the empty space, else returns None (by default)
   '''
   for rowIndex in range(len(board)):
      for colIndex in range(len(board[0])):
         if board[rowIndex][colIndex] == "*":
            return (rowIndex, colIndex) # returns a tuple with the location of the empty space

def validBoard(board, num, position):
   '''
   Checks if the given board is valid or not
   Input: board (list of lists) - the board that needs to be solved
          num (int) - the number to be inserted in the board
          position (tuple) - the rows are represented by the first element and the column by the second
   Returns: True if the number entered in the position is valid and unique for each row, column and box, False otherwise
   '''
   # checks the row
   for i in range(len(board[0])):
      # checks each element in the row and sees if it is equal to the number we just put in and if it is the position we just inserted, then we ignore it
      if board[position[0]][i] == num and position[1] != i:
         return False
   
   # checks the column
   for i in range(len(board)):
      # checks each element in the column and sees if it is equal to the number we just put in and if it is the position we just inserted, then we ignore it
      if board[i][position[1]] == num and position[0] != i:
         return False

   # checks the box
   # gives values in terms of 0, 1 or 2
   # (0, 0) is the box on the top left
   boxX = position[1] // 3
   boxY = position[0] // 3

   # we multiple by 3 to get the appropiate index
   for rowIndex in range(boxY * 3, boxY * 3 + 3):
      for colIndex in range(boxX * 3, boxX * 3 + 3):
         # loop through the box and check if any other element is same as the box and not check the position we just inserted
         if board[rowIndex][colIndex] == num and (rowIndex, colIndex) != position:
            return False
   return True

def solveBoard2(board):
   '''
   Solves the board recursively and with the help of backtracking
   Input: board (list of lists) - the board that needs to be solved
   Returns: True if the solution of the board has been found, else False
   '''
   emptyLocation = findEmpty(board)
   # Base case is when the board is full
   if not emptyLocation:   # if it returned None 
      return True
   else:
      row, column = emptyLocation
   
   # if the solution cannot be found with the value added, we need to try a different value and repeat the process again recursively
   for i in range(1, 10):
      # checks if the value added is valid
      if validBoard(board, i, (row, column)):
         board[row][column] = i

         # calls the board recursively on the board with the new value added
         if solveBoard2(board):
            return True

         # if the value is not valid
         board[row][column] = "*"

   return False