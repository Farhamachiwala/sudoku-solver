# Sudoku Solver by Farha Machiwala

from fourByFourBoard import displayBoard1, solveBoard1
from nineByNineBoard import displayBoard2, solveBoard2

def main():
   # each row is a list
   # 0 indicates a blank
   board = [
      [0, 0, 2, 8, 0, 0, 3, 0, 0],
      [0, 0, 0, 0, 0, 9, 0, 2, 0],
      [4, 3, 7, 2, 5, 6, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 4],
      [3, 0, 4, 0, 1, 0, 6, 0, 7],
      [5, 0, 6, 4, 0, 7, 0, 1, 0],
      [6, 0, 8, 1, 0, 2, 4, 7, 9],
      [0, 0, 3, 5, 0, 0, 0, 6, 0],
      [0, 9, 0, 7, 0, 4, 0, 3, 8]
   ]

   # board = [
   #    [0, 3, 4, 0],
   #    [4, 0, 0, 2],
   #    [1, 0, 0, 3],
   #    [0, 2, 1, 0]
   # ]

   numOfRows = len(board)
   numOfColumns = len(board[0])

   # replacing all the 0's on the board with *'s for easy readability for the user
   for rowIndex in range(len(board)):
      for columnIndex in range(len(board[0])):
         if board[rowIndex][columnIndex] == 0:
            board[rowIndex][columnIndex] = "*"

   if numOfColumns == numOfRows == 4:
      print("\nInitial Board")
      displayBoard1(board)

      validBoard = solveBoard1(board)
      print("-" * 40)
      # displays the appropiate output whether the board is valid or not
      if validBoard == False:
         print("\nEntered board is invalid!\nA solution for the board could not be found.")
      else:
         print("\nThe Solution of the Board")
         displayBoard1(board)
   
   elif numOfColumns == numOfRows == 9:
      print("\nInitial Board")
      displayBoard2(board)

      validBoard = solveBoard2(board)
      print("-" * 40)
      # displays the appropiate output whether the board is valid or not
      if validBoard == False:
         print("\nEntered board is invalid!\nA solution for the board could not be found.")
      else:
         print("\nThe Solution of the Board")
         displayBoard2(board)

   else:
      print("Cannot solve this board!")

main()