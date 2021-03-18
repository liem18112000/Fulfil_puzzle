from algorithms.utils import *

class GlobalSearch():

    def breadthFirstSearch(self, problem):
        queue = Queue()
        visited = []
        queue.push( (problem.getStartState(), []) )
        while not queue.isEmpty():
            (cur_node, cur_shapes), cur_path = queue.pop()
            if problem.isGoalState((cur_node, cur_shapes)):
                return cur_path
            else:
                if cur_node not in visited:
                    visited.append(cur_node)
                    for child in problem.getSuccessors((cur_node, cur_shapes)):
                        (child_node, child_shapes) , child_path = child
                        fullPath = cur_path + [child_path]
                        queue.push(((child_node, child_shapes), fullPath))
        return []
