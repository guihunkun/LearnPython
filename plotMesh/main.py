import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def read_Nodes(node_file):
    Nodes = []
    f = open(node_file)
    lines = f.readlines()
    for line in lines:
        data = re.findall(r'\d+\.?\d*', line)
        id = int(data[0])
        x = float(data[1])
        y = float(data[2])
        da = [x, y]
        Nodes.append(da)
    return Nodes


def read_Triangles(triangle_file):
    Triangles = []
    Tags = []
    f = open(triangle_file)
    lines = f.readlines()
    for line in lines:
        data = re.findall(r'\d+\.?\d*', line)
        id = int(data[0])
        id_1 = int(data[1])
        id_2 = int(data[2])
        id_3 = int(data[3])
        tag = float(data[4])
        da = [id_1, id_2, id_3]
        Triangles.append(da)
        Tags.append(tag)
    return Triangles, Tags


def plotMesh(Nodes, Triangles, Tags, showNodeId = True, showTriangleId = True, showTriangleTag = False):
    fig, ax = plt.subplots()
    patches = []
    triangleId = 0
    colors = []
    for triangle in Triangles:
        triangleId = triangleId + 1
        polygon = []
        colors.append(Tags[triangleId-1])
        for id in triangle:
            polygon.append(Nodes[id-1])
        for i in range(len(polygon)):
            line_x = []
            line_y = []
            line_x.append(polygon[i][0])
            if i+1 == len(polygon) :
                line_x.append(polygon[0][0])
            else:
                line_x.append(polygon[i+1][0])
            line_y.append(polygon[i][1])
            if i+1 == len(polygon) :
                line_y.append(polygon[0][1])
            else:
                line_y.append(polygon[i+1][1])
            plt.plot(line_x, line_y, 'r-')
        patches.append(Polygon(polygon, True))
        center_x = sum([_[0] for _ in polygon]) / len(polygon)
        center_y = sum([_[1] for _ in polygon]) / len(polygon)
        if showTriangleId :
            ax.annotate(triangleId, (center_x, center_y), color='red', weight='bold', fontsize=7, ha='center', va='center')
    if showNodeId :
         nodeId = 0
         for node in Nodes:
             nodeId = nodeId + 1
             ax.annotate(nodeId, (node[0], node[1]), color='black', weight='bold', fontsize=9, ha='center', va='center')
    collection = PatchCollection(patches)
    if showTriangleTag :
        collection.set_array(np.array(colors))
    ax.add_collection(collection)
    fig.colorbar(collection, ax=ax)
    ax.axis('equal')
    plt.show()


if __name__ == "__main__":
    node_file = "Nodes.txt"
    triangle_file = "Triangles.txt"
    Nodes = read_Nodes(node_file)
    Triangles, Tags = read_Triangles(triangle_file)
    showNodeId = False
    showTriangleId = False
    plotMesh(Nodes, Triangles, Tags, showNodeId, showTriangleId)
