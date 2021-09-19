import drawSvg as draw
import random
import math
import numpy
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

defaultExtent = {
    "width": 1,
    "height": 1
}

def addSVG():
    return draw.Drawing(400, 400, origin='center', displayInline=False)

def printList(l):
    for x in l:
        print(x, end=', ')

def generatePoints(n, extent=defaultExtent):
    pts = []
    for i in range(n):
        pts.append([(random.random()- 0.5) * extent["width"], (random.random() - 0.5) * extent["height"]])
    return pts

def visualizePoints(svg, pts):
    for pt in pts:
        cx = 1000*pt[0]
        cy = 1000*pt[1]
        r = 100 / math.sqrt(len(pts))
        svg.append(draw.Circle(cx, cy, r,
            fill='red', stroke_width=1, stroke='black'))

points = generatePoints(256)

# Improve points create Voronoi diagram
vor = Voronoi(points)
fig = voronoi_plot_2d(vor)



# meshSVG = addSVG()
# visualizePoints(meshSVG, meshPts)

# Display in Jupyter notebook
#    d.rasterize()  # Display as PNG
# meshSVG # Display as SVG
