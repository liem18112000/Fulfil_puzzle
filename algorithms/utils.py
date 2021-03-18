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


def manhattanDistance(xy1, xy2):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def euclidianDistance(point1, point2):
    return int(
        math.sqrt(
            (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        )
    )

class SearchUtils(object):

    def executeSearch(self, fn, arg):
        start = time.time()
        solutions = fn(arg)
        end = time.time()
        return solutions, (end - start) * 1000

    def searchResult(self, fn, arg):

        solutions, eslapseTime = self.executeSearch(fn, arg)
        utils = PrintUtils()
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
