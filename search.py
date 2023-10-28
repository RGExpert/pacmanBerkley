# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    "*** YOUR CODE HERE ***"

    visited=set()
    
    states=util.Stack()
    dir_taken=util.Stack()

    visited.add(problem.getStartState())
    states.push(problem.getStartState())
    curr_path=[]

    while not states.isEmpty():
        curr_state=states.pop()
        visited.add(curr_state)
        
        if not dir_taken.isEmpty():
            curr_patht=dir_taken.pop()

        if(problem.isGoalState(curr_state)):
           return curr_path

        for succesor in problem.getSuccessors(curr_state):
            if succesor[0] not in visited:
                states.push(succesor[0])
                new_path = curr_path[:]
                new_path.append(succesor[1])  
                dir_taken.push(new_path)  
    return None

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited=set()
    
    states=util.Queue()
    dir_taken=util.Queue()

    visited.add(problem.getStartState())
    states.push(problem.getStartState())
    curr_path=[]

    while not states.isEmpty():
        curr_state=states.pop()
        if not dir_taken.isEmpty():
            curr_path=dir_taken.pop()

        if(problem.isGoalState(curr_state)):
           return curr_path

        for succesor in problem.getSuccessors(curr_state):
            if succesor[0] not in visited:
                states.push(succesor[0])
                visited.add(succesor[0])

                new_path = curr_path[:]
                new_path.append(succesor[1])  
    
                dir_taken.push(new_path)  
    return None

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    visited = set()
    states_directions = util.PriorityQueue()
    
    start_state = problem.getStartState()
    states_directions.push((start_state, [], 0), 0)
    
    while not states_directions.isEmpty():
        curr_state, curr_path, curr_cost = states_directions.pop()
        
        if problem.isGoalState(curr_state):
            return curr_path
        
        if curr_state not in visited:
            visited.add(curr_state)
            for state, direction, cost in problem.getSuccessors(curr_state):
                if state not in visited:
                    new_path = curr_path + [direction]
                    new_cost = curr_cost + problem.getCostOfActions(new_path)
                    states_directions.push((state, new_path, new_cost), new_cost)

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    states_directions = util.PriorityQueue()
    
    start_state = problem.getStartState()
    states_directions.push((start_state, [], 0), 0)
    
    while not states_directions.isEmpty():
        curr_state, curr_path, curr_cost = states_directions.pop()
        
        if problem.isGoalState(curr_state):
            return curr_path
        
        if curr_state not in visited:
            visited.add(curr_state)
            for state, direction, cost in problem.getSuccessors(curr_state):
                if state not in visited:
                    new_path = curr_path + [direction]
                    new_cost = curr_cost + problem.getCostOfActions(new_path) + heuristic(state,problem)
                    states_directions.push((state, new_path, new_cost), new_cost)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
