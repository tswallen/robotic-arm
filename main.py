import numpy as np
import matplotlib.pyplot as plt

joints = np.array([
    (30, 6),
    (90, 5),
    (20, 3)
],
    dtype=[('angle', 'f4'), ('length', 'f4')]
    )

points = np.array([
    (0, 0)
],
    dtype=[('x', 'f4'), ('y', 'f4')]
    )

points2 = []

for index, (angle, length) in np.ndenumerate(joints):
    
    x = length * np.cos(angle)
    y = length * np.sin(angle)

    points2.append((x,y))


print(points2)


plt.show()