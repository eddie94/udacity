from ROBOT_CLASS import *
from p_controller import *
from pd_controller import *
from pid_controller import  *

my_robot=robot()
my_robot.set(0,2,0)
# my_robot = my_robot.move(0.2,1)
# my_robot.sense()
# print(my_robot.d)
#p_run(my_robot, 0.7, 20, 1.0)
#pd_run(my_robot,0.2,0.2,20,1)
pid_run(my_robot,0.05,0.0,0.0,100,0.1)