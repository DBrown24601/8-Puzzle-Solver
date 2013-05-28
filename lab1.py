def printNode(node):
    for i in range(0,3):
        print node[i], " ",
    print "\n"
    for i in range(3,6):
        print node[i], " ",
    print "\n"
    for i in range(6,9):
        print node[i], " ",
    print "\n"

def finished(node,goal):
    if  (node[1]==goal[1]) and \
        (node[2]==goal[2]) and \
        (node[3]==goal[3]) and \
        (node[4]==goal[4]) and \
        (node[5]==goal[5]) and \
        (node[6]==goal[6]) and \
        (node[7]==goal[7]) and \
        (node[8]==goal[8]) and \
        (node[0]==goal[0]):
        #print("TRUE")
        return True
    else:
        #print("FALSE")
        return False
    

class Node:
    parent = None
    
        


print ("Hello! Please enter the initial state!")
loopCheck = False
CLOSED_NODES = None
CURRENT_NODE = None
while (not loopCheck):
    print ("Be sure to use the following format ((x x x)(x x x)(x x x))")
    isState = raw_input(">: ")
    #print "you entered ", isState
    #((1 2 3)(4 5 6)(7 8 *))
    #((* 8 7)(6 5 4)(3 2 1))
    beginState = list(isState)

    OPEN_NODES = beginState[2:5] + beginState[7:10] + beginState[12:15]
    #print beginS
    printNode(OPEN_NODES)
    
    print "What is the goal state?"
    isGoal = raw_input(">: ")
    print "So you want to get from", isState, " to ", isGoal, "?"
    isGoal = list(isGoal)
    goal = isGoal[2:5] + isGoal[7:10] + isGoal[12:15]
    answer = raw_input(">: ")
    answer=answer.lower()
    loopCheck = answer.startswith('y')
    if(not loopCheck):
        print "Then what is the initial state?"
        
#Data entry loop end

#Main loop begins
finished(OPEN_NODES,goal)
while not finished(OPEN_NODES, goal):
    
            
    
    print("Got out of the loop!")

    
print("Congratulations")




