import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process
from tkinter import *

master = Tk()

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

w = Scale(master, from_=0, to=100, variable=joints[1][0])
w.pack()

l = Label(master, textvariable=joints[1][0])
l.pack()

def test():
    print(joints)

b = Button(master, command=test)
b.pack()

def renderVisualisation():
    x_cache, y_cache = 0.0, 0.0
    for index, (angle, length) in np.ndenumerate(joints):

        x = np.add(np.multiply(length, np.cos(np.radians(angle))), x_cache)
        y = np.add(np.multiply(length, np.sin(np.radians(angle))), y_cache)

        points[index] = (x, y)

        x_cache, y_cache = x, y

    x, y = zip(*points)
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.plot(x, y)
    plt.show()

def renderUI():
    mainloop()

def moveJoint(joint, value):
    joints[(joint,)][0] = value

if __name__ == '__main__':
    Process(target=renderVisualisation).start()