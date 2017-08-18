from ROBOT_CLASS import *
import matplotlib.pyplot as plt

def pd_run(robot, pgain, dgain, n, speed):

    cte = robot.y
    previous_error=0
    x_position=[]
    y_position=[]

    for i in range(n):

        x_position.append(robot.x)
        y_position.append(robot.y)

        error = cte - previous_error
        steer = -(pgain * cte) - (dgain * (previous_error/0.5))
        robot.move(steer, speed)
        previous_error = cte
        cte = robot.y

    plt.plot(x_position,y_position)
    plt.title('PD control')
    plt.show()