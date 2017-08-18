from math import *
import random

landmarks=[[0,0],[0,100],[100,0],[100,100]]                                         #landmarks which the robot is going to sense
landmark_name=['landmark 1','landmark 2','landmark 3','landmark 4']                 #the name of each landmark
world_size=100                                                                      #the maximum of the x and y axis
max_steering_angle=pi/4                                                             #thr robot cannot steer more than the max steering angle

class robot():

    def __init__(self):
        self.x=random.random()*world_size                                           #initialize the robot's x axis somwhere in the world
        self.y=random.random()*world_size                                           #initialize the robot's y axis somwhere in the world
        self.orientation=random.random()*2*pi                                       #initialize where the robot is heading
         #the forward, turn, sense noise is initialized into 0
        self.forward_noise=0
        self.turn_noise=0
        self.sense_noise=0
        self.d=[]                                                                   #a list that contains the robots distance from each landmark
        self.num_collision = 0                                                      #not used yet

    def __repr__(self):                                                             #when printing your robot, it shows your x,y,orientation
        return('[x=%.6s y=%.6s orient=%.6s]' % (str(self.x),str(self.y),str(self.orientation)))

    def set(self,new_x,new_y,new_orient):                                           #function that sets the robots position

        if new_orient<0 or new_orient>=2*pi:
            raise(ValueError, 'orientation must be between 0~2pi')
        if new_x<0 or new_x>=world_size:
            raise (ValueError, 'x is out of bound')
        if new_y<0 or new_y>=world_size:
            raise (ValueError, 'y is out of bound')

        self.x=float(new_x)
        self.y=float(new_y)
        self.orientation=float(new_orient)

    def set_noise(self,new_f_noise,new_t_noise,new_s_noise):                        #function that sets the robots noise(forward, turn sense)
        self.forward_noise=float(new_f_noise)
        self.turn_noise=float(new_t_noise)
        self.sense_noise=float(new_s_noise)

    def check_collision(self, grid):
        '''
        check how much times the robot crashes
        currently not used yet

        use this function to check how precisely it goes to the goal
        less crashes, more accurate
        '''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dist = sqrt((self.x - float(i)) ** 2 + (self.y - float(j)) ** 2)
                    if dist < 0.5:
                        self.num_collision += 1
                        return False

    def check_goal(self, goal, threshold = 1):              #check how far the robot is from the goal
        dist = sqrt( (float(goal[0]) - self.x)**2 + (float(goal[1]) - self.y) **2 )
        return dist<threshold

    def move(self,turn,forward):
        '''
        the robot can move around the world
        the robot itself turns, and then move forward

        :param turn: how much the robot moves
        :param forward: how much the robot goes forward
        :return: returns a robot class after moving
        '''
        x=0
        y=0

        if forward<0:
            raise (ValueError, 'robot cannot move backwards')

        if turn > max_steering_angle:
            turn = max_steering_angle

        orientation = self.orientation + float(turn) + random.gauss(0.0,self.turn_noise)
        orientation %= 2*pi

        dist = float(forward) + random.gauss(0.0,self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)

        x %= world_size
        y %= world_size

        res = robot()
        res.set(x,y,orientation)
        res.set_noise(self.forward_noise,self.turn_noise,self.sense_noise)

        return res

    def sense(self):                #senses the distance from each landmark

        tmp=[]

        for i in range(len(landmarks)):
            distance_x=self.x-landmarks[i][0]
            distance_y=self.y-landmarks[i][1]
            value=abs(sqrt(pow(distance_x,2)+pow(distance_y,2)))
            tmp.append(value)
        self.d=tmp

    def Gaussian(self, mu, sigma, x):
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))

    def measurement_prob(self, distance):

        '''
        :param distance: the actual distance the robot senses
        :return: the probability of how different a particle's sense data is to the actual sense data
        '''
        prob=1

        for i in range(len(landmarks)):
            dist = sqrt( (self.x - landmarks[i][0]) ** 2 + ( self.y - landmarks[i][1] ) ** 2 )
            prob *= self.Gaussian(dist, self.sense_noise, distance[i])
        return prob