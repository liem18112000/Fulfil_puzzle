import numpy as np
from copy import deepcopy
class Board(object):

    def __init__(self, widht, height, debug = False):
        self._board = np.zeros((widht, height), dtype=int)
        self._board[:,:] = -1
        self._debug = debug

    def getSize(self):
        return self._board.shape

    def isBoardFull(self):
        row, col = self._board.shape
        for i in range(row):
            for j in range(col):
                if self._board[i, j] == -1:
                    return False
        return True

    def isShapeArrangable(self, matrix, startPos):
        row, col = matrix.shape
        startRow, startCol = startPos
        endRow, endCol = startRow + row, startCol + col
        maxRow, maxCol = self._board.shape
        flag = True
        if endRow > maxRow:
            if self._debug:
                print("Row of matrix is out of bounds")
            flag = False

        if endCol > maxCol:
            if self._debug:
                print("Col of matrix is out of bounds")
            flag = False

        if not flag:
            return flag

        temp = deepcopy(self._board[startRow:endRow, startCol:endCol])
        for i in range(row):
            for j in range(col):
                if temp[i, j] >= 0 and matrix[i, j] >= 0:
                    if self._debug:
                        print("Collision at position (" + str(startRow + i), ", " + str(startCol + j) + ")")
                    del temp 
                    return False
        del temp
        return True

    def arrangeShapeAtPos(self, matrix, startPos):
        if self.isShapeArrangable(matrix, startPos):
            row, col = matrix.shape
            startRow, startCol = startPos
            for i in range(row):
                for j in range(col):
                    if self._board[startRow + i, startCol + j] == -1:
                        self._board[startRow + i, startCol + j] = matrix[i, j]
            return True
        return False

    def getBoard(self):
        row, column = self._board.shape

        result = ""
        for i in range(-1, row + 1):
            if i != -1 and i != row:
                result += "|"
            else:
                result += "+"
            for j in range(0, column):
                if i == -1 or i == row:
                    result += "----"
                elif self._board[i, j] >= 0:
                    if self._board[i, j] > 9:
                        result += '[' + str(self._board[i, j]) + ']'
                    else:
                        result += '[0' + str(self._board[i, j]) + ']'
                else:
                    result += '    '
            if i != -1 and i != row:
                result += '|\n'
            else:
                result += '+\n'

        return result

    def print(self):
        print(self.getBoard())
