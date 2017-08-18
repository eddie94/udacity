from search import *
import matplotlib.pyplot as plt

grid = [[0,1,0,0,0,0],
        [0,1,0,1,0,0],                      #the maze our robot is moving
        [0,1,0,1,1,0],
        [0,1,0,1,1,0],
        [0,0,0,1,1,0]]

init = [0,0]
goal = [len(grid) -1 , len(grid[0]) -1 ]


a = search()
a.set_map(grid, init, goal)
a.set_cost(1)

h = a.heuristic(grid)


a.search(h)
matrix_to_axis(a.path,a.grid)
x_axis = []
y_axis = []
for i in range(len(a.path)):
    x_axis.append(a.path[i][0])
    y_axis.append(a.path[i][1])

plt.plot(y_axis,x_axis)
plt.show()
print(a.path)