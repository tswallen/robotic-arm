import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from multiprocessing import Process
from tkinter import *

master = Tk()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

joints = np.array(
    [
        (0, 0),
        (75, 6),
        (40, 3),
        (270, 2)
    ],
    dtype=[
        ('angle', 'f4'),
        ('length', 'f4')]
)

points = np.zeros(
    (
        joints.size,
    ),
    dtype=[
        ('x', 'f4'),
        ('y', 'f4')
    ]
)

def test(test):
    joints[1][0] = w.get()
    print(joints)

w = Scale(master, from_=0, to=100, variable=joints[1][0], command=test)
w.pack()

def renderVisualisation(test):
    x_cache, y_cache = 0.0, 0.0
    for index, (angle, length) in np.ndenumerate(joints):

        x = np.add(np.multiply(length, np.cos(np.radians(angle))), x_cache)
        y = np.add(np.multiply(length, np.sin(np.radians(angle))), y_cache)

        points[index] = (x, y)

        x_cache, y_cache = x, y

    x, y = zip(*points)
    ax1.clear()
    ax1.plot(x,y)
    plt.xlim(0,10)
    plt.ylim(0,10)

def renderUI():
    mainloop()

def moveJoint(joint, value):
    joints[(joint,)][0] = value

ani = animation.FuncAnimation(fig, renderVisualisation, interval=10)
plt.show()
renderUI()

