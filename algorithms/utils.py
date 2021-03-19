import math
import heapq
import time
from elements.utils import PrintUtils

class Container(object):

    def __init__(self):
        self.list = []

    def push(self, item):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        return len(self.list) == 0


class Stack(Container):

    def __init__(self):
        super(Stack, self).__init__()

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()


class Queue(Container):

    def __init__(self):
        super(Queue, self).__init__()

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()


class PriorityQueue(Container):

    def __init__(self):
        super(PriorityQueue, self).__init__()
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.list, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.list)
        return item

    def isEmpty(self):
        return len(self.list) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.list):
            if i == item and p > priority:
                self.list[index] = (priority, c, item)
                heapq.heapify(self.list)
class SearchUtils(object):

    def executeSearch(self, fn, arg):
        start = time.time()
        solutions = fn(arg)
        end = time.time()
        return solutions, (end - start) * 1000

    def searchResult(self, obj, fn, arg):

        solutions, eslapseTime = self.executeSearch(fn, arg)
        utils = PrintUtils()
        obj.printStats()
        print("Time eslapse : " + str(eslapseTime) + " miliseconds")

        if len(solutions) == 0:
            print("No solutions")
            return 

        for solution in solutions:
            board, matrix, id, pos = solution
            print("======================================================")
            print("Place matrix at possition : " + str(pos))
            utils.print(matrix, id)
            print("Current board : ")
            board.print()
            print("======================================================")


class StatisitcUtils():

    def __init__(self):
        self._node_seen = 0
        self._node_expanded = 0
        self._memory_usage = 0

    def increaseNodeSeen(self, increase = 1):
        self._node_seen += increase

    def increaseNodeExpanded(self, increase = 1):
        self._node_expanded += increase

    def increaseMemory(self, increase):
        self._memory_usage += increase

    def statisticResult(self):
        print("Node expanded : " + str(self._node_expanded))
        print("Node seen : " + str(self._node_seen))
        print("Memory usage : " + str(self._memory_usage / 1000) + " Kbytes")

import numpy as np

def rowColHeuristic(state):

    board, shapes = state

    row, col = board.getSize()
    fullRow = np.ones((row,))
    fullCol = np.ones((col,))
    
    for i in range(row):
        for j in range(col):
            if board._board[i][j] == -1:
                fullRow[i] = 0
                fullCol[j] = 0

    return (fullRow.sum() + fullCol.sum()) / 2
                
