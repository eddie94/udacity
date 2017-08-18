from ROBOT_CLASS import robot
import matplotlib.pyplot as plt

def p_run(robot, pgain, n, speed):
    x_position=[]
    y_position=[]
    for i in range(n):
        cte = robot.y
        steer = -pgain * cte
        x_position.append(robot.x)
        y_position.append((robot.y))
        robot.move(steer, speed)

    plt.plot(x_position,y_position)
    plt.title('P control')
    plt.show()