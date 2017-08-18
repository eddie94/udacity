from particle import *

myrobot=robot()
myrobot.set(5,5,0)
myrobot.set_noise(0.05,0.05,5)
myrobot.move(0,10)
myrobot.sense()

print(myrobot.d)

par=particle()
par.make(1000,myrobot)

for i in range(100):
    myrobot.move(0.2,0.01)
    myrobot.sense()
    par.motion(0.2,0.01)
    par.sense()
    par.measure(myrobot)
    par.resampling()
for i in range(100):
    myrobot.move(0,0.1)
    myrobot.sense()
    par.motion(0,0.1)
    par.sense()
    par.measure(myrobot)
    par.resampling()

print(myrobot)
print(myrobot.d)

plt.scatter(myrobot.x,myrobot.y)
plt.scatter(par.x_axis,par.y_axis)
plt.show()