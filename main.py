from elements.utils import PrintUtils
from game.board import Board
from game.game import BoardFulFilGame as Game
from algorithms.utils import *
from algorithms.global_search import GlobalSearch as Search 
from elements.all_elements import allElements



utils = PrintUtils()

w = int(input("Board width : "))
h = int(input("Board height : "))

gameBoard = Board(w, h, debug = False)

game = Game(gameBoard, allElements)

search = Search()

searchUtils = SearchUtils()

# searchUtils.searchResult(search, search.iterativeDeepeningSearch, game)

searchUtils.searchResult(search, search.depthFirstSearch, game)
