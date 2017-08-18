from Robot.ROBOT_CLASS import *
import matplotlib.pyplot as plt
import random

class particle():

    def make(self,number, r):
        '''

        :param number: the number of particles
        :param r: the actual robot MUST BE A ROBOT CLASS
        :return: a list of particles
                 particles are also ROBOT CLASS
        '''

        particles = []

        for i in range(number):
            '''
            scatter the particles
            particles are randomly scattered and heading randomly
            '''
            par = robot()
            par.forward_noise = r.forward_noise
            par.turn_noise = r.turn_noise
            par.sense_noise = r.sense_noise
            particles.append(par)

        return particles

def resample(par, w):
    '''
    :param par: the list of particles
    :param w: particles importance weight
    :return: a list of new particles
    '''
    new_par = []

    for i in range(len(par)):
        index = int(random.random() * len(par))
        beta = 0
        mw = max(w)
    '''
    resmaples particles by using the resampling wheel algorithm
    take a look at udacity CS373 unit 3
    '''
    for i in range(len(par)):
        beta = random.random() * 2 * mw

        while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % len(par)

        new_par.append(par[index])

    return new_par

def weight(par, r):
    '''

    :param par: the list of particles
    :param r: your robot MUST BE ROBOT CLASS
    :return: a list of importance weight
             the list is the same size of particles
              each weight indicates the particles importance weight
    '''
    w = []

    for i in range(len(par)):
        w.append(par[i].measurement_prob(r.d))

    return w

def visualize(r,p):

    tmp_x=[]
    tmp_y=[]

    for i in range(len(p)):
        tmp_x.append(p[i].x)
        tmp_y.append((p[i].y))

    plt.scatter(tmp_x, tmp_y)
    plt.scatter(r.x,r.y)

    plt.show()