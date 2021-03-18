from elements.utils import PrintUtils
from game.board import Board
from game.game import BoardFulFilGame as Game
from algorithms.utils import SearchUtils
from algorithms.global_search import GlobalSearch as Search 
from elements.all_elements import allElements



utils = PrintUtils()

gameBoard = Board(11, 5, debug = False)

game = Game(gameBoard, allElements)

search = Search()

searchUtils = SearchUtils()

searchUtils.searchResult(search.breadthFirstSearch, game)
