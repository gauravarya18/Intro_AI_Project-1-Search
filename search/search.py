#Orignal work of Gaurav Arya (B17CS023)
#Collaborators - Shubhankar Gaikwad (B17CS023)
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
from util import Stack
from util import Queue
from util import PriorityQueue
import copy

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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    new_stack=Stack()
    visited_states=[]
    state=()
    temp_state=()
    actionsTillnow=[]

    state=problem.getStartState()
    new_stack.push((state,[]))
    # visited_states.append(state)
    print "hey10"
    while True:

        temp_state=new_stack.pop()
        state=temp_state[0]
        actionsTillnow=temp_state[1][:]
        #print actionsTillnow
        #print "#################"
        #actionsTillnow.append(temp_state[1])

        if(problem.isGoalState(state)):
            print "Done!!"
            return actionsTillnow
            break
        elif(not(state in visited_states)):
            visited_states.append(state)
        else:
            continue

        
        successors=()
        successors=problem.getSuccessors(state)
 

        #print "current_state",state
        #print successors
        temp_actions=[]
        
        for i in successors:
            if(not(i[0] in visited_states)):
                temp_actions=actionsTillnow[:]
                #print temp_actions
                temp_actions.append(i[1])
                #print temp_actions
                new_stack.push((i[0],temp_actions))
                #print "add" , i[0]

    #print visited_states
    print "hey11"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    new_stack=Queue()
    visited_states=[]
    state=()
    temp_state=()
    actionsTillnow=[]
    
    state=problem.getStartState()
    new_stack.push((state,[]))
    visited_states.append(state)
    
    while True :

        temp_state=new_stack.pop()
        state=temp_state[0]
        actionsTillnow=temp_state[1][:]
        

        if(problem.isGoalState(state)):
            return actionsTillnow
    
        
        # if(not(state in visited_states)):
        #     visited_states.append(state)
        
        successors=()
        successors=problem.getSuccessors(state)
 
        temp_actions=[]
        
        for i in successors:
            if(not(i[0] in visited_states)):
                temp_actions=actionsTillnow[:]
                temp_actions.append(i[1])
                new_stack.push((i[0],temp_actions))
                visited_states.append(i[0])

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    state=()
    state=problem.getStartState()
    costTillNow=0
    actionsTillnow=[]
    visited_states=[]

    new_pq=PriorityQueue()
    new_pq.push((state,actionsTillnow,costTillNow),costTillNow)

    while True :

        temp=new_pq.pop()
        state=temp[0]
        costTillNow=temp[2]
        actionsTillnow=temp[1]

        if(problem.isGoalState(state)):
            print "Done!!"
            return actionsTillnow
            break
        elif(not(state in visited_states)):
            visited_states.append(state)
        else:
            continue

        
        # successors=()
        successors=problem.getSuccessors(state)
        # print state
        # print costTillNow
        # print actionsTillnow 
        # print successors
        # temp_actions=[]
        for i in successors:
            
            temp_actions=actionsTillnow[:]
            temp_actions.append(i[1])
            tempCost=costTillNow + i[2]
            new_pq.push((i[0],temp_actions,tempCost),tempCost)

        

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
import searchAgents
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state=()
    state=problem.getStartState()
    costTillNow=0
    actionsTillnow=[]
    visited_states=[]

    new_pq=PriorityQueue()
    new_pq.push((state,actionsTillnow,costTillNow,0),costTillNow)
    while not(new_pq.isEmpty()) :

        temp=new_pq.pop()
        state=temp[0]
        GoalcostTillNow=temp[2]
        heuristics_disTillnow=temp[3]
        costTillNow=temp[2]-temp[3]
        actionsTillnow=temp[1]

        if(problem.isGoalState(state)):
            print "Done!!"
            return actionsTillnow
            break
        elif(not(state in visited_states)):
            visited_states.append(state)
        else:
            continue

        # successors=()
        successors=problem.getSuccessors(state)
        # print state
        # print costTillNow
        # print actionsTillnow 
        # print successors
        # temp_actions=[]
        for i in successors:
            
            temp_actions=actionsTillnow[:]
            temp_actions.append(i[1])
            tempCost=costTillNow + i[2]
            heuristics_dis=heuristic(i[0],problem)
            new_pq.push((i[0],temp_actions,tempCost+heuristics_dis,heuristics_dis),tempCost+heuristics_dis)
        

    util.raiseNotDefined()
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
