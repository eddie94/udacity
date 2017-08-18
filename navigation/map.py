grid = [[0,0,1,0,0,0],
        [0,0,1,0,0,0],                      #the maze our robot is moving
        [0,0,0,0,1,0],
        [0,0,1,1,1,0],
        [0,0,0,0,1,0]]



init = [0,0]                                #robots initial position
goal = [len(grid)-1, len(grid[0])-1]        #the goal where the robot wants to go

move = [[-1,0],     #up
        [0,-1],     #left
        [1,0],      #down
        [0,1]]      #right
move_name = ['^','<','V','>']

cost = 1                                    #the cost of making a move

def search():                               #searches the way to the goal
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]           #a list that contains information of end of searching
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]          #contains information of what action the robot has to do
    closed[init[0]][init[1]] = 1                                                        # list containing info of nodes that is ended searching

    x = init[0]                                                                         # set the robots initial position
    y = init[1]
    g = 0
    open = [[g,x,y]]
    action[x][y] = g

    found = False
    resign = False

    while not found and not resign:     #loop until goal is found, or cannot find the path

        if len(open) == 0:
            resign = True
            print("fail")
        else:
            open.sort()
            open.reverse()
            next = open.pop()

            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
                print('success')
            else:
                for i in range(len(move)):
                    x2 = x + move[i][0]
                    y2 = y + move[i][1]
                    if x2 >=0 and x2 <len(grid) and y2>=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] ==0:                        #both closed and grid is open
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'

    while x != init[0] or y != init[1]:
        x2 = x - move[action[x][y]][0]
        y2 = y - move[action[x][y]][1]

        policy[x2][y2] = move_name[action[x][y]]

        x = x2
        y = y2

    for row in policy:
        print(row)

    return next

def heuristic(grid):

    h = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

    for i in range(len(h)):
        for j in range(len(h[0])):
            h[-1-i][-1-j] = i+j

    return h

h = heuristic(grid)

print(h)
search()