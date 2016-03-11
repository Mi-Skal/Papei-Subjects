# Convex hull of a random set of points:

from scipy.spatial import ConvexHull
import numpy as np
from math import sqrt

points = np.random.rand(30, 2)   # 30 random points in 2-D
hull = ConvexHull(points)

maxp = np.amax(points , axis = 0)
minp = np.amin(points , axis = 0)

maxX = maxp[0]      #Megista kai elaxista x,y
maxY = maxp[1]
minX = minp[0]
minY = minp[1]


a = sqrt((( minX-maxX)**2) + ((minY-minY)**2))
b = sqrt((( maxX-maxX)**2) + ((maxY-minY)**2))


# Plot it:

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')


plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')


def in_hull(p, hull):
	from scipy.spatial import Delaunay
	if not isinstance(hull,Delaunay):
		hull = Delaunay(hull)
		
	return hull.find_simplex(p)>=0

randpoints = np.random.rand(1000,2)

table = in_hull(randpoints,points)

x = np.count_nonzero(table)

E = (x/1000.0)*a*b
print "The Area of the Convex Hull is:" , E




		
