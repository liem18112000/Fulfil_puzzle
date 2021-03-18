class PrintUtils(object):

    def getShape(self, element, rot):
        return self.getMatrix(element.getMatrix(rot), element._id)
        

    def getMatrix(self, matrix, id):
        row, column = matrix.shape

        result = ""
        for i in range(row):
            for j in range(column):
                if matrix[i, j] == id:
                    if 0 <= id <= 9 :
                        result += '[0' + str(id) + ']'
                    elif id > 9:
                        result += '[' + str(id) + ']'
                else:
                    result += '    '
            result += '\n'

        return result


    def printElement(self, element, rot):
        print(self.getShape(element, rot))

    def print(self, matrix, id):
        print(self.getMatrix(matrix, id))
