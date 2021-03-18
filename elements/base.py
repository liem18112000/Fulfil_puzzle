import numpy as np

class Element:

    def __init__(self, id):
        self._children = []
        self._id = id

    def addElement(self, pos):

        if pos in self._children:
            return False

        self._children.append(pos)
        return True

    def addElements(self, listOfPos):
        for elem in listOfPos:
            self.addElement(elem)

    def countElement(self):
        return len(self._children)

    def getMatrix(self, rot):
        maxRow, maxCol = self._findMaxRowColumn()

        matrix = np.zeros((maxRow, maxCol), dtype=int)

        for i in range(maxRow):
            for j in range(maxCol):
                if (i, j) in self._children:
                    matrix[i, j] = self._id
                else:
                    matrix[i, j] = -1

        matrix = np.rot90(matrix, k = rot)

        return matrix


    def _findMaxRowColumn(self):
        maxCol = 0
        maxRow = 0

        for row, col in self._children:
            if row > maxRow:
                maxRow = row

            if col > maxCol:
                maxCol = col

        return maxRow + 1, maxCol + 1
                    


        
