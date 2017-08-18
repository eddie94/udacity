class search():

    def __init__(self):
        '''
        grid : the map where the robot is
        path : path
        '''

        self.grid = []
        self.path =[]
        self.init = []
        self.goal = []
        self.cost = 0
        self.move = [[-1, 0],[0, -1],[1, 0],[0, 1]]
        self.move_name = ['^','<','v','>']

    def set_map(self,grid, init, goal):
        self.grid = grid
        self.init = init
        self.goal = goal

    def set_cost(self, cost):

        self.cost = cost

    def heuristic(self,grid):

        h = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

        for i in range(len(h)):
            for j in range(len(h[0])):
                h[-1-i][-1-j] = i+j

        return h

    def search(self, heu):

        closed = [[0 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]
        closed[self.init[0]][self.init[1]] = 1

        expand = [[-1 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]
        action = [[-1 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]

        x = self.init[0]
        y = self.init[1]
        g = 0
        h = heu[x][y]
        f = g + h

        open = [[f,g,h,x,y]]
        count = 0
        found = False
        resign = False

        while not found and not resign:

            if len(open) == 0:
                resign = True
                print("Fail")
            else:
                open.sort()
                open.reverse()
                next = open.pop()

                x = next[3]
                y = next[4]
                g = next[1]
                expand[x][y] = count
                count += 1

            if x == self.goal[0] and y == self.goal[1]:
                found = True
            else:
                for i in range(len(self.move)):

                    x2 = x + self.move[i][0]
                    y2 = y + self.move[i][1]

                    if x2 >= 0 and x2 < len(self.grid) and y2 >= 0 and y2 <len(self.grid[0]):

                        if closed[x2][y2] == 0 and self.grid[x2][y2] == 0:
                            g2 = g + self.cost
                            h2 = heu[x2][y2]
                            f2 = g2 + h2

                            open.append([f2,g2,h2,x2,y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
        policy = [[' ' for row in range(len(self.grid[0]))] for col in range(len(self.grid))]

        x = self.goal[0]
        y = self.goal[1]
        policy[x][y] = '*'
        path = [[x,y]]

        while x != self.init[0] or y != self.init[1]:

            x2 = x - self.move[action[x][y]][0]
            y2 = y - self.move[action[x][y]][1]
            path.append([x2,y2])
            policy[x2][y2] = self.move_name[action[x][y]]
            x = x2
            y = y2

        path.reverse()
        self.path = path

def matrix_to_axis(path,grid):

    for i in range(len(path)):
        path[i][0] = len(grid)-path[i][0]-1
    print(path)
    return path