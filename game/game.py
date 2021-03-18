class GameInterface(object):

    def isGoalState(self, state):
        pass

    def getStartState(self):
        pass

    def getSuccessors(self, state):
        pass

from copy import deepcopy
class BoardFulFilGame(GameInterface):

    def __init__(self, board, listOfAvailableShape):
        self._startState = (board, listOfAvailableShape)

    def getStartState(self):
        return self._startState

    def isGoalState(self, state):
        return state[0].isBoardFull()

    def isFailState(self, state):
        return len(state[1]) <= 0

    def getSuccessors(self, state):
        successors = []
        board, shapes = state
        boardRow, boardCol = board.getSize()
        for shape in shapes:
            for r in range(4):
                matrix = shape.getMatrix(rot=r)
                id = shape._id
                shapeRow, shapeCol = matrix.shape
                row, col = boardRow - shapeRow, boardCol - shapeCol

                for i in range(row + 1):
                    for j in range(col + 1):
                        if board.isShapeArrangable(matrix, (i, j)):
                            newBoard = deepcopy(board)
                            newBoard.arrangeShapeAtPos(matrix, (i, j))
                            for removed_shape in shapes:
                                if removed_shape._id == id:
                                    shapes.remove(removed_shape)
                                    break
                            cur_shapes = deepcopy(shapes)
                            successors.append(((newBoard, cur_shapes), (newBoard, matrix, id, (i, j))))
        return successors
