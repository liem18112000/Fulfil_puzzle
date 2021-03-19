from algorithms.utils import *
import sys
from copy import deepcopy
class GlobalSearch():

    def __init__(self):
        self._statistic = StatisitcUtils()
        self._limited_depth = 100

    def printStats(self):
        self._statistic.increaseMemory(sys.getsizeof(self))
        self._statistic.statisticResult()

    def breadthFirstSearch(self, problem):
        queue = Queue()
        visited = []
        queue.push( (problem.getStartState(), []) )
        while not queue.isEmpty():
            (cur_node, cur_shapes), cur_path, = queue.pop()
            self._statistic.increaseNodeExpanded()
            if problem.isGoalState((cur_node, cur_shapes)):
                return cur_path
            else:
                if cur_node not in visited:
                    visited.append(cur_node)
                    for child in problem.getSuccessors((cur_node, cur_shapes)):
                        (child_node, child_shapes) , child_path = child
                        fullPath = cur_path + [child_path]
                        queue.push(((child_node, child_shapes), fullPath))
                        self._statistic.increaseMemory(sys.getsizeof(child))
                        self._statistic.increaseNodeSeen()
        return []

    def depthFirstSearch(self, problem, limit_depth = 100):
        myStack = Stack()
        visited = []
        myStack.push((problem.getStartState(), []))

        print("Depth : " + str(limit_depth))

        while not myStack.isEmpty():

            (cur_node, cur_shapes), cur_path = myStack.pop()
            self._statistic.increaseNodeExpanded()

            if problem.isGoalState((cur_node, cur_shapes)):
                return cur_path

            if len(cur_path) < limit_depth:
                for child in problem.getSuccessors((cur_node, cur_shapes)):
                    (child_node, child_shapes), child_path = child
                    if child_node not in visited:
                        visited.append(child_node)
                        fullPath = cur_path + [child_path]
                        myStack.push(((child_node, child_shapes), fullPath))
                        self._statistic.increaseMemory(sys.getsizeof(child))
                        self._statistic.increaseNodeSeen()
        return []

    def iterativeDeepeningSearch(self, problem):
        for i in range(0, max(problem.getStartState()[0].getSize()) + 1):
            new_problem = deepcopy(problem)
            result = self.depthFirstSearch(new_problem, i)
            if result != []:
                return result

        print("Find no solution in ids...")
        return []

    def aStarSearch(self, args):

        problem, heuristic = args

        pqueue = PriorityQueue()

        visited = []

        pqueue.push((problem.getStartState(), [], 0), heuristic(problem.getStartState()) + 0)

        while not pqueue.isEmpty():
            (cur_node, cur_shapes), cur_path, cur_cost = pqueue.pop()
            self._statistic.increaseNodeExpanded()
            if problem.isGoalState((cur_node, cur_shapes)):
                return cur_path

            visited.append(cur_node)

            for child in problem.getSuccessors((cur_node, cur_shapes)):
                (child_node, child_shapes), child_path = child

                if child_node not in visited:
                    visited.append(child_node)
                    fullPath = cur_path + [child_path]
                    totalCost = cur_cost + 1
                    pqueue.push(((child_node, child_shapes), fullPath, totalCost), totalCost + heuristic((child_node, child_shapes)))

                else:
                    pqueue.update(((child_node, child_shapes), fullPath, totalCost), totalCost + heuristic((child_node, child_shapes)))

                self._statistic.increaseNodeSeen()
                self._statistic.increaseMemory(sys.getsizeof(child))

        return []
