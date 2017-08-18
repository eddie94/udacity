grid = [[0,1,0,0,0,0],
        [0,1,0,0,0,0],                      #the maze our robot is moving
        [0,1,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,0,0,1,0]]

init = [0,0]
goal = [len(grid) -1 , len(grid[0]) -1 ]
cost = 1

move = [[-1 , 0],   #up
        [0 , -1],   #left
        [1 , 0],    #down
        [0 , 1]]    #right

move_name = ['^','<','v','>']

def search(grid, init, goal, cost, heuristic):

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h

    open = [[f,g,h,x,y]]
    count = 0
    found = False
    resign = False

    while not found and not resign:
        if len(open)==0:
            resign = True
            print('fail')
        else:
            open.sort()
            open.reverse()
            next = open.pop()

            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = count
            count += 1

        if x == goal[0] and y == goal[1]:
            found = True
        else:
            for i in range(len(move)):
                x2 = x + move[i][0]
                y2 = y + move[i][1]

                if x2>=0 and x2<len(grid) and y2>=0 and y2 < len(grid[0]):
                    print(x2, y2)

                    if closed[x2][y2]==0 and grid[x2][y2]==0:
                        g2 = g + cost
                        h2 = heuristic[x2][y2]
                        f2 = g2 + h2
                        open.append([f2,g2,h2,x2,y2])
                        closed[x2][y2]=1
                        action[x2][y2] = i
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    path = [[x,y]]

    while x != init[0] or y != init[1]:

        x2 = x - move[action[x][y]][0]
        y2 = y - move[action[x][y]][1]
        path.append([x2,y2])
        policy[x2][y2] = move_name[action[x][y]]
        x = x2
        y = y2

    for row in policy:
        print(row)
    path.reverse()
    print(path)
    for i in range(len(expand)):
        print(expand[i])
    return expand

def heuristic(grid):

    h = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

    for i in range(len(h)):
        for j in range(len(h[0])):
            h[-1-i][-1-j] = i+j

    return h

hu = heuristic(grid)

search(grid, init, goal, cost, hu)