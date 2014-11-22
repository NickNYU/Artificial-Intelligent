"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())


  nextState = (nextx, nexty)
  action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]

  successors.append( ( nextState, action, cost) )
  """
  "*** YOUR CODE HERE ***"
  stack = util.Stack()
  stack.push(problem.getStartState())
  visited = set()
  parentTable = []
  while (not stack.isEmpty()):
      state = stack.pop()
      if (problem.isGoalState(state)):
          break
      if (state not in visited):
          visited.add(state)
          for successor in problem.getSuccessors(state):
              statePosition = successor[0]
              stack.push(statePosition)
              parentTable.append([state, successor[0], successor[1]])   #state is the current state, successor[0] is the parent state, succesor[1] is the movatition
  path = []
  currentState = state
  while (currentState != problem.getStartState()):
      for parent in parentTable:
          if (parent[1] == currentState):
              currentState = parent[0]
              path.append(parent[2])
              break
  path.reverse()
  return path
  util.raiseNotDefined()









def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  queue = util.Queue()
  queue.push(problem.getStartState())
  visited = set()
  parentTable = []
  while (not queue.isEmpty()):
    state = queue.pop()
    if(problem.isGoalState(state)):
      break
    if(state not in visited):
      visited.add(state)
      successors = problem.getSuccessors(state)
      for successor in successors:
        statePosition = successor[0]
        queue.push(statePosition)
        parentTable.append([state, successor[0], successor[1]])

  path = []
  currentState = state
  while(currentState != problem.getStartState()):
    for parent in parentTable:
          if (parent[1] == currentState):
              currentState = parent[0]
              path.append(parent[2])
              break

  path.reverse()
  return path

  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  pQueue = util.PriorityQueue()

  item = [problem.getStartState(), problem.getStartState(), 0, None]
  priority = 0
  pQueue.push( item, priority )

  visited = set()
  parentTable = []
  path = []

  while (not pQueue.isEmpty()):
      state = pQueue.pop()
      parentTable.append([state[0], state[1], state[3]])
      if (problem.isGoalState(state[1])):
          break
      currentPoint = state[1]
      if (currentPoint not in visited):
          visited.add(currentPoint)
          for successor in problem.getSuccessors(currentPoint):
            cost = state[2] + successor[2]
            action = successor[1]
            nextPoint = successor[0]
            pQueue.push([currentPoint, nextPoint, cost, action], cost)

  currentState = state[1]
  while (currentState != problem.getStartState()):
      for parent in parentTable:
          if (parent[1] == currentState):
              currentState = parent[0]
              path.insert(0, parent[2])
              break
  return path
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  pQueue = util.PriorityQueue()

  item = [problem.getStartState(), problem.getStartState(), 0, None]
  priority = 0
  pQueue.push( item, priority )

  visited = set()
  parentTable = []
  path = []

  while (not pQueue.isEmpty()):
      state = pQueue.pop()
      parentTable.append([state[0], state[1], state[3]])
      if (problem.isGoalState(state[1])):
          break
      currentPoint = state[1]
      if (currentPoint not in visited):
          visited.add(currentPoint)
          for successor in problem.getSuccessors(currentPoint):
            cost = state[2] + successor[2]
            action = successor[1]
            nextPoint = successor[0]
            pQueue.push([currentPoint, nextPoint, cost, action], cost + heuristic(nextPoint, problem))

  currentState = state[1]
  while (currentState != problem.getStartState()):
      for parent in parentTable:
          if (parent[1] == currentState):
              currentState = parent[0]
              path.append(parent[2])
              break
  path.reverse()
  return path
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch