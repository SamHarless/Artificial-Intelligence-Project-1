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
from util import Stack, Queue, PriorityQueue
#from searchAgents import manhattanHeuristic, euclideanHeuristic

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

def stringToDirections(list):
    from game import Directions
    newList=[]
    for item in list:
        if item=="South":
            newList.append(Directions.SOUTH)
        elif item=="West":
            newList.append(Directions.WEST)
        elif item=='North':
            newList.append(Directions.NORTH)
        elif item=='East':
            newList.append(Directions.EAST)
        else:
            newList.append(item)
        
        
    return newList
            



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    #print("4,5 Succesors", problem.getSuccessors((4,5)))

    print("DFS")

    stack=Stack()
    dict={}
    dict[problem.getStartState()]=(None, None, None) 
    stack.push((problem.getStartState(), None, None))

    while not stack.isEmpty():
        #print("TOP OF LOOP")
        
        currNodeTuple=stack.pop()

        #print(currNodeTuple)
        currNode=currNodeTuple[0]
        dict[currNode]=(currNodeTuple[2], currNodeTuple[1])
        #print(currNode)
        #print(dict)

        if problem.isGoalState(currNode):
            #print(currNode)
            
            #FOUND GOAL NEED TO DO SOMETHING
            #first make the list by appending for Big O reasons (dont want to push back other elements), then need to reverse 
            reversedList=[]
            while problem.getStartState() != currNode:
                reversedList.append(dict[currNode][0])
                currNode=dict[currNode][1]


            #REVERSE LIST
            index=len(reversedList)-1
            stringList=[]
            while index >= 0:
                stringList.append(reversedList[index])
                index-=1
            
            
            #print(stringToDirections(stringList))


            return stringToDirections(stringList)
            


        for successor in problem.getSuccessors(currNode):#add the tuple reference
            #print(successor)
            if successor[0] in dict:# if we have seen this node before
                pass
            else: #if we have not seen this node before, need to put it in the stack and add how we got to it to the dictionary 
                stack.push((successor[0], currNode, successor[1]))
                #dict[successor[0]]=(successor[1], currNode)

            

    #implement a search node class, which can then call the getSuccessors method

    

    #use getSuccerors
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    #print(problem.getStartState())

    print("Calling BFS: ", problem.getStartState())

    
    #hate question 5, so this checks to see if we are doing a regular BFS or a corner one, and does different things for each
    if len(problem.getStartState()) == 1 or len(problem.getStartState())<3:
        q=Queue()
        q.push((problem.getStartState(), None, None))
        dict={}
        #dict[problem.getStartState()]=(None, None, None)

        

        while not q.isEmpty():

            currNodeTuple=q.pop()

            #print(currNodeTuple)
            currNode=currNodeTuple[0]
            if currNode not in dict:
                dict[currNode]=(currNodeTuple[2], currNodeTuple[1])

                if problem.isGoalState(currNode):
                    reversedList=[]
                    while problem.getStartState() != currNode:
                        reversedList.append(dict[currNode][0])
                        currNode=dict[currNode][1]


                    #REVERSE LIST
                    index=len(reversedList)-1
                    stringList=[]
                    while index >= 0:
                        stringList.append(reversedList[index])
                        index-=1
                    
                    
                    #print(stringToDirections(stringList))


                    return stringToDirections(stringList)
                


                
                for succ in problem.getSuccessors(currNode):
                    if succ[0] in dict:
                        pass
                    else:
                        #q.push(succ[0])
                        q.push((succ[0], currNode, succ[1]))
                        #dict[succ[0]]=(succ[1], currNode)


    else:
        #print("ELSE")
        q=Queue()
        #print(problem.getStartState())
        q.push(((problem.getStartState()), None, None)) #(staterepresentation, direction, cameFrom)

        visitedDict={}

        #print("Tester: ", problem.getSuccessors(problem.getStartState()))
        #print("HERE")
        while not q.isEmpty():
            
            currNodeTuple=q.pop()
            #print("Curr: ", currNodeTuple)

            if currNodeTuple[0] not in visitedDict:
                visitedDict[currNodeTuple[0]]=(currNodeTuple[1], currNodeTuple[2]) #(action, nodeFrom)



                if problem.isGoalState(currNodeTuple[0]):
                    #print(currNodeTuple)
                    #do some shite
                    reversedList=[]
                    #reversedList.append(currNodeTuple[1])
                    currNode=visitedDict[currNodeTuple[2]]
                    while currNode[1] != problem.getStartState():
                        reversedList.append(currNode[0])
                        currNode=visitedDict[currNode[1]]
                        #print(currNode)
                    reversedList.append(currNode[0])
                    #print(reversedList)

                    index=len(reversedList)-1
                    stringList=[]
                    while index >= 0:
                        stringList.append(reversedList[index])
                        index-=1

                    #print(stringList)
                    #return ['West', 'West', 'West', 'South', 'South', 'South', 'South', 'North', 'North', 'North', 'North', 'North', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'East']
                    return stringList



                for succ in problem.getSuccessors(currNodeTuple[0]):
                    if (succ[0], currNodeTuple[0][1], succ[2]) in visitedDict:
                        pass
                    #getSucc will return: ((x,y), N/S/W/E, (False, False, True, False))
                    else:
                        q.push(((succ[0], currNodeTuple[0][1], succ[2]), succ[1], currNodeTuple[0]))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    pq=PriorityQueue()
    pq.push((problem.getStartState(),None, None, 0),0)#start has a cost of 0 bc you are alrady there

    print("UCS")

    dict={}

    while not pq.isEmpty():

        

        currNodeTuple=pq.pop()
        currNode=currNodeTuple[0]
        if currNode not in dict:
            dict[currNode]=(currNodeTuple[1], currNodeTuple[2], currNodeTuple[3])
            
            if problem.isGoalState(currNode):
                reversedList=[]
                while problem.getStartState() != currNode:
                    reversedList.append(dict[currNode][0])
                    currNode=dict[currNode][1]


                #REVERSE LIST
                index=len(reversedList)-1
                stringList=[]
                while index >= 0:
                    stringList.append(reversedList[index])
                    index-=1
                
                
                #print(stringToDirections(stringList))


                return stringToDirections(stringList)

            
            for succ in problem.getSuccessors(currNode):
                if succ[0] in dict:
                    pass
                else:
                    #need to keep track of the cumulative cost
                    cost=dict[currNode][2]+succ[2]
                    pq.push((succ[0], succ[1], currNode, cost), cost)
                    #dict[succ[0]]=(succ[1], currNode, cost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    #print("SHITTER MOMENT")
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    #from searchAgents import manhattanHeuristic, euclideanHeuristic    
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    print(problem)
    print(problem.getStartState())

    print("HELLO")


    if len(problem.getStartState()) == 1 or len(problem.getStartState())<3:
        pq=PriorityQueue()
        pq.push((problem.getStartState(), None, None, 0),0)#start has a cost of 0 bc you are alrady there

        dict={}

        #print(problem.getSuccessors(problem.getStartState()))


        while not pq.isEmpty():
            currNodeTuple=pq.pop()
            currNode=currNodeTuple[0]
            #print(currNodeTuple)
            if currNode not in dict:
                dict[currNode]=(currNodeTuple[1],currNodeTuple[2],currNodeTuple[3])
                
                if problem.isGoalState(currNode):
                    reversedList=[]
                    while problem.getStartState() != currNode:
                        reversedList.append(dict[currNode][0])
                        currNode=dict[currNode][1]
                    #REVERSE LIST
                    index=len(reversedList)-1
                    stringList=[]
                    while index >= 0:
                        stringList.append(reversedList[index])
                        index-=1
                    #print(stringToDirections(stringList))
                    return stringToDirections(stringList)   

                
                for succ in problem.getSuccessors(currNode):
                    if succ[0] in dict:
                        pass
                    else:
                        #need to keep track of the cumulative cost
                        cost=currNodeTuple[3]+succ[2]
                        costWH=cost+heuristic(succ[0],problem)
                        pq.push((succ[0], succ[1], currNode, cost), costWH)
                        #dict[succ[0]]=(succ[1], currNode, cost)

                        #0 is name of node
                        #1 is action to get to it
                        #2 is the node it came from (one we are currently looking at)
                        #cost includes heuristic, which it shouldnt
    else:
        from searchAgents import cornersHeuristic
        #print("ELSE")
        q=Queue()
        #print(problem.getStartState())
        q.push(((problem.getStartState()), None, None)) #(staterepresentation, direction, cameFrom)

        visitedDict={}

        pq=PriorityQueue()
        pq.push((problem.getStartState(), None, None, 0), 0) 
        #(state, direction to get here, cameFrom, costSoFar)
        #print("Tester: ", problem.getSuccessors(problem.getStartState()))
        #print("HERE")
        while not pq.isEmpty():
            
            currNodeTuple=pq.pop()
            #print("Curr: ", currNodeTuple)
            #print(currNodeTuple[0])

            if currNodeTuple[0] not in visitedDict:
                visitedDict[currNodeTuple[0]]=(currNodeTuple[1], currNodeTuple[2]) #(action, nodeFrom)



                if problem.isGoalState(currNodeTuple[0]):
                    #print(currNodeTuple)
                    #do some shite
                    reversedList=[]
                    #reversedList.append(currNodeTuple[1])
                    currNode=visitedDict[currNodeTuple[2]]
                    while currNode[1] != problem.getStartState():
                        reversedList.append(currNode[0])
                        currNode=visitedDict[currNode[1]]
                        #print(currNode)
                    reversedList.append(currNode[0])
                    #print(reversedList)

                    index=len(reversedList)-1
                    stringList=[]
                    while index >= 0:
                        stringList.append(reversedList[index])
                        index-=1

                    return stringList



                for succ in problem.getSuccessors(currNodeTuple[0]):
                    if succ[0] in visitedDict:
                        pass
                    else:
                        cost=currNodeTuple[3]+1
                        angie=cornersHeuristic(succ, problem)
                        #print(type(angie))
                        #ssprint(angie)
                        costWH=cost+angie
                        #getSucc will return: ((x,y), N/S/W/E, (False, False, True, False))
                        pq.push(((succ[0], currNodeTuple[0][1], succ[2]), succ[1], currNodeTuple[0], cost), costWH)


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

