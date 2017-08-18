from ROBOT_CLASS import *
import matplotlib.pyplot as plt

def pid_run(robot, pgain, igain, dgain,  n, speed):
    '''
    :param robot: your robot MUST BE A ROBOT CLASS
    :param pgain: the proportional gain
    :param igain: the integral gain
    :param dgain: the derivative gain
    :param n: how much steps you're going to move
    :param speed: how fast the robot moves
    '''
    x_position=[]
    y_position=[]
    integral=0
    previous_error = 0
    cte=50

    for i in range(n):

        x_position.append(robot.x)
        y_position.append(robot.y)
        error = cte - previous_error

        pval = cte * pgain
        ival = integral * igain
        dval = dgain * (previous_error/0.5)

        steer = -pval - ival - dval

        integral += cte*0.5
        previous_error = cte
        cte=robot.y

        robot = robot.move(steer, speed)
    print(x_position)
    print(y_position)
    plt.plot(x_position,y_position)
    plt.title('PID control')
    plt.show()