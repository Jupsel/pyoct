# -*- coding: utf-8 -*-
# python octree implementation
# Code Â© Spencer Krum June 2011
# Released underl GPLv3 See LICENSE file in this repository
"""
Octree creating and searching
"""


class Node():
    """
    Class to be a node in my octree
    """

    def __init__(self, parent, xupperlimit, yupperlimit, zupperlimit, xlowerlimit, ylowerlimit, zlowerlimit, name):
        self.parent = parent
        self.xupperlimit = xupperlimit
        self.yupperlimit = yupperlimit
        self.zupperlimit = zupperlimit
        self.xlowerlimit = xlowerlimit
        self.ylowerlimit = ylowerlimit
        self.zlowerlimit = zlowerlimit
        self.xcenter = (self.xupperlimit + self.xlowerlimit) / 2.
        self.ycenter = (self.yupperlimit + self.ylowerlimit) / 2.
        self.zcenter = (self.zupperlimit + self.xlowerlimit) / 2.
        self.name = name

    parent = None
    value = None

    # children
    posXposYposZ = None
    posXposYnegZ = None
    posXnegYposZ = None
    posXnegYnegZ = None
    negXposYposZ = None
    negXposYnegZ = None
    negXnegYposZ = None
    negXnegYnegZ = None

    # array of children
    chidren = [posXposYposZ, posXposYnegZ, posXnegYposZ, posXnegYnegZ, negXposYposZ, negXposYnegZ, negXnegYposZ,
               negXnegYnegZ]

    # position in space
    xupperlimit = None
    yupperlimit = None
    zupperlimit = None

    xlowerlimit = None
    ylowerlimit = None
    zlowerlimit = None

    def get_array_of_children(self):
        """
        helper function to return array of children
        because there is some weird issue where just setting an 
        array variable isn't cutting it
        """
        children = [self.posXposYposZ, self.posXposYnegZ, self.posXnegYposZ, self.posXposYnegZ, self.negXposYposZ,
                    self.negXposYnegZ, self.negXnegYposZ, self.negXnegYnegZ]
        return children

    def print_types(self):
        """
        helper function to printout types of children
        I know, terribly unpythonic of me, rabble rabble
        """
        print type(self.posXposYposZ)
        print type(self.posXposYnegZ)
        print type(self.posXnegYposZ)
        print type(self.posXnegYnegZ)
        print type(self.negXposYposZ)
        print type(self.negXposYnegZ)
        print type(self.negXnegYposZ)
        print type(self.negXnegYnegZ)

    def print_info(self):
        """
        helper function to dump node paramaters
        """
        print "name:\t {0}".format(self.name)
        print "parent:\t {0}".format(self.parent)
        print "value:\t {0}".format(self.value)

        # children
        print "posXposYposZ: \t {0}".format(self.posXposYposZ)
        print "posXposYnegz: \t {0}".format(self.posXposYnegZ)
        print "posXnegYposZ: \t {0}".format(self.posXnegYposZ)
        print "posXnegYnegZ: \t {0}".format(self.posXnegYnegZ)
        print "negXposYposZ: \t {0}".format(self.negXposYposZ)
        print "negXposYnegZ: \t {0}".format(self.negXposYnegZ)
        print "negXnegYposZ: \t {0}".format(self.negXnegYposZ)
        print "negXnegYnegZ: \t {0}".format(self.negXnegYnegZ)

        # position in space
        print "Xupperlimit: \t {0}".format(self.xupperlimit)
        print "Yupperlimit: \t {0}".format(self.yupperlimit)
        print "Zupperlimit: \t {0}".format(self.zupperlimit)

        print "Xlowerlimit: \t {0}".format(self.xlowerlimit)
        print "Ylowerlimit: \t {0}".format(self.ylowerlimit)
        print "Zlowerlimit: \t {0}".format(self.zlowerlimit)

        print "xcenter: \t {0}".format(self.xcenter)
        print "ycenter: \t {0}".format(self.ycenter)
        print "zcenter: \t {0}".format(self.zcenter)
        print ""

    def add(self, payload, coord, level):

        """
        Create a subnode
        """

        if level == 0:
            try:
                self.value.append((coord, payload))

            except AttributeError:
                self.value = []
                self.value.append((coord, payload))

        else:
            level -= 1
            # Determine quadrant
            if coord[0] <= self.xcenter:
                # negX
                if coord[1] <= self.ycenter:
                    # negY
                    if coord[2] <= self.zcenter:
                        # negZ
                        xupperlimit = self.xcenter
                        yupperlimit = self.ycenter
                        zupperlimit = self.zcenter
                        xlowerlimit = self.xlowerlimit
                        ylowerlimit = self.ylowerlimit
                        zlowerlimit = self.zlowerlimit
                        if self.negXnegYnegZ is None:
                            self.negXnegYnegZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "1")
                        self.negXnegYnegZ.add(payload, coord, level)
                    else:
                        # posZ
                        xupperlimit = self.xcenter
                        yupperlimit = self.ycenter
                        zupperlimit = self.zupperlimit
                        xlowerlimit = self.xlowerlimit
                        ylowerlimit = self.ylowerlimit
                        zlowerlimit = self.zcenter
                        if self.negXnegYposZ is None:
                            self.negXnegYposZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "2")
                        self.negXnegYposZ.add(payload, coord, level)
                else:
                    # posY
                    if coord[2] <= self.zcenter:
                        # negZ
                        xupperlimit = self.xcenter
                        yupperlimit = self.yupperlimit
                        zupperlimit = self.zcenter
                        xlowerlimit = self.xlowerlimit
                        ylowerlimit = self.ycenter
                        zlowerlimit = self.zlowerlimit
                        if self.negXposYnegZ is None:
                            self.negXposYnegZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "3")
                        self.negXposYnegZ.add(payload, coord, level)

                    else:
                        # posZ
                        xupperlimit = self.xcenter
                        yupperlimit = self.yupperlimit
                        zupperlimit = self.zupperlimit
                        xlowerlimit = self.xlowerlimit
                        ylowerlimit = self.ycenter
                        zlowerlimit = self.zcenter
                        if self.negXposYposZ is None:
                            self.negXposYposZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "4")
                        self.negXposYposZ.add(payload, coord, level)

            else:
                # posX
                if coord[1] <= self.ycenter:
                    # negY
                    if coord[2] <= self.zcenter:
                        # negZ
                        xupperlimit = self.xupperlimit
                        yupperlimit = self.ycenter
                        zupperlimit = self.zcenter
                        xlowerlimit = self.xcenter
                        ylowerlimit = self.ylowerlimit
                        zlowerlimit = self.zlowerlimit
                        if self.posXnegYnegZ is None:
                            self.posXnegYnegZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "5")
                        self.posXnegYnegZ.add(payload, coord, level)

                    else:
                        # posZ
                        xupperlimit = self.xupperlimit
                        yupperlimit = self.ycenter
                        zupperlimit = self.zupperlimit
                        xlowerlimit = self.xcenter
                        ylowerlimit = self.ylowerlimit
                        zlowerlimit = self.zcenter
                        if self.posXnegYposZ is None:
                            self.posXnegYposZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "6")
                        self.posXnegYposZ.add(payload, coord, level)

                else:
                    # posY
                    if coord[2] <= self.zcenter:
                        # negZ
                        xupperlimit = self.xupperlimit
                        yupperlimit = self.yupperlimit
                        zupperlimit = self.zcenter
                        xlowerlimit = self.zcenter
                        ylowerlimit = self.ycenter
                        zlowerlimit = self.zlowerlimit
                        if self.posXposYnegZ is None:
                            self.posXposYnegZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "7")
                        self.posXposYnegZ.add(payload, coord, level)

                    else:
                        # posZ
                        xupperlimit = self.xupperlimit
                        yupperlimit = self.yupperlimit
                        zupperlimit = self.zupperlimit
                        xlowerlimit = self.xcenter
                        ylowerlimit = self.ycenter
                        zlowerlimit = self.zcenter
                        if self.posXposYposZ is None:
                            self.posXposYposZ = Node(self.name, xupperlimit, yupperlimit, zupperlimit, xlowerlimit,
                                                     ylowerlimit, zlowerlimit, self.name + "8")
                        self.posXposYposZ.add(payload, coord, level)
                        # self.print_info()


class Octree():
    """
    class to hold the whole tree
    """

    def __init__(self, xmax, ymax, zmax, xmin, ymin, zmin, root_coords = (0, 0, 0), maxiter = 7):
        self.Xmax = xmax
        self.Ymax = ymax
        self.Zmax = xmax
        self.Xmin = xmin
        self.Ymin = ymin
        self.Zmin = zmin
        self.root_coords = root_coords
        self.maxiter = maxiter

        self.root = Node('root', xmax, ymax, zmax, xmin, ymin, zmin, "1")

    def debug(self):
        print self.root
        print self.Xmax
        print self.Ymax
        print self.Zmax
        print self.Xmin
        print self.Ymin
        print self.Zmin
        print self.root_coords
        print self.maxiter

    def add_item(self, payload, coord):
        """
        Create recursively create subnodes until maxiter is reached
        then deposit payload in that node
        """

        self.root.add(payload, coord, self.maxiter)

    def find_within_range(self, center, size, shape):
        """
        Return payloads and coordinates of every payload within
        a specified area
        """
        """
        When shape is cube: 
        Search space is defined as the cubic region where each face is 'size'
        distance directly away from the center. 
        """
        """
        Should support "cube", "sphere", "doughnut"
        """
        if shape == "sphere":
            raise NotImplementedError
        elif shape == "doughnut":
            raise NotImplementedError
        elif shape == "cube":
            """
            This deals with things around the center of a node in a box shape
            with a radius of 'size'
            It would be totally good to make a spere search space
            """
            """
            It works by making the (correct I think) assumption that the box
            shape has 8 vertices. To determine the overlap between the search
            space and the node area is hard. We can start by identifying which 
            of the 8 children of the current node overlap with the search space.
            The assumption is that if the search box overlaps in any part with
            a child, then the most extreme vertex will be within the child. 

            Let me put it 2 dimensions with ascii art:

            Fig1. A Quadtree Node Space with children space labeled 

            1,-1--------1,0--------1,1
            |           |           |
            |  child_4  |  child_1  |
            |           |           |
           -1,0---------0,0--------1,0
            |           |           |
            |  child_3  |  child_2  | 
            |           |           |
          (-1,-1)-----(-1,0)-----(-1,1)

            
            The four children of this node are:

            child_1 has the following attributes 

            . node name is posXposY
            . initial value is Null
            . Once recursively filled out, its value is another node
            . it represents the rectangular area between ((0,0),(1,0)) and ((1,0), (1,1))
            . its center is at the center of the rectangular area it represents

             
            Children _2, _3, _4 are much the same

            Fig2. Quadtree Node Space with superimposed search space 


            /-----------------------\ 
            |           |           |
            |           |           |
            |     |-------|         |
            |-----|-------|---------| 
            |     |     | |         |
            |     |-------|         | 
            |           |           |
            \-----------------------/  


            Fig3. Fig2 Zoomed

            /---------------------------------------------------------------\
            |                                                ||   <child_1> |
            |    <child_4>                                   ||  <point A>  |
            |                                                ||        |    |
            |                <selection space>               ||        V    |
            |    0+++++++++++++++++++++++++++++++++++++++++++++++++++++0    |
            |    +                                           ||<exact  +    |
            |    +                             <x-axis>      || center>+    |
            |====+===========================================%%========+====|
            |    +                                           ||        +    |
            |    +                                           ||        +    |
            |    +                                           ||        +    |
            |    +                                          ^||        +    |
            |    +                                          y||        +    |
            |    +                                          -||        +    |
            |    +                                          a||        +    |
            |    +                                          x||        +    |
            |    +                                          i||        +    |
            |    +                                          s||        +    |
            |    +                                          v||        +    |
            |    +                                           ||        +    |
            |    +                                           ||        +    |
            |    0+++++++++++++++++++++++++++++++++++++++++++++++++++++0    |
            |             <child_3>                          ||   <child_2> |
            \---------------------------------------------------------------/


            Fig4. Quadtree Node Space with different superimposed search space 


            /-----------------------\ 
            |           |           |
            |           |           |
            |     |---| |           |
            |-----|---|-------------| 
            |     |   | |           |
            |     |---| |           | 
            |           |           |
            \-----------------------/  


            Fig5. Fig2 Zoomed

            /---------------------------------------------------------------\
            |                                                ||             |
            |    <child_4>                                   ||  <child_1>  |
            |                                    <point B>   ||             |
            |                <selection space>   |           ||             |
            |    0+++++++++++++++++++++++++++0 <--           ||             |
            |    +                           +               ||<exact       |
            |    +                           + <x-axis>      || center>     |
            |====+===========================+===============%%=============|
            |    +                           +               ||             |
            |    +                           +               ||             |
            |    +                           +               ||             |
            |    +                           +              ^||             |
            |    +                           +              y||             |
            |    +                           +              -||             |
            |    +                           +              a||             |
            |    +                           +              x||             |
            |    +                           +              i||             |
            |    +                           +              s||             |
            |    +                           +              v||             |
            |    +                           +               ||             |
            |    +                           +               ||             |
            |    0+++++++++++++++++++++++++++0               ||             |
            |             <child_3>                          ||   <child_2> |
            \---------------------------------------------------------------/



            What we see in Fig2/3 vs Figi4/5 is illustrated by point A, point B
            Points A, B are the points that are the most positive in both X and
            Y. We see that if and only if this 'upper rightmost' point is within 
            child 1, then there is space in the selection overlapping part of 
            child 1. This also follows for children_2, _3, _4 and generalizes to
            the 3D space of the octree. 

            So our litmus test for 'does the selection overlap with a
            childspace?' is whether or not the most extreme(bad wording I know) 
            part of that selection is within the childspace. 
            
            """

            payloads = []
            templist = [self.root]
            list_list = []
            list_list.append([self.root])
            for level in range(self.maxiter):
                list_list.append([])

            # print list_list
            for level in range(self.maxiter):
                for node in list_list[level]:
                    Xedge_max = center[0] + size
                    Xedge_min = center[0] - size
                    Yedge_max = center[1] + size
                    Yedge_min = center[1] - size
                    Zedge_max = center[2] + size
                    Zedge_min = center[2] - size

                    corner0 = (Xedge_max, Yedge_max, Zedge_max)
                    corner1 = (Xedge_max, Yedge_max, Zedge_min)
                    corner2 = (Xedge_max, Yedge_min, Zedge_max)
                    corner3 = (Xedge_max, Yedge_min, Zedge_min)
                    corner4 = (Xedge_min, Yedge_max, Zedge_max)
                    corner5 = (Xedge_min, Yedge_max, Zedge_min)
                    corner6 = (Xedge_min, Yedge_min, Zedge_max)
                    corner7 = (Xedge_min, Yedge_min, Zedge_min)
                    corners = [corner0, corner1, corner2, corner3, corner4, corner5, corner6, corner7]
                    table = ((corner0[0] > node.xcenter), (corner0[1] > node.ycenter), (corner0[2] > node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.posXposYposZ)
                    table = ((corner1[0] > node.xcenter), (corner1[1] > node.ycenter), (corner1[2] < node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.posXposYnegZ)
                    table = ((corner2[0] > node.xcenter), (corner2[1] < node.ycenter), (corner2[2] > node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.posXnegYposZ)
                    table = ((corner3[0] > node.xcenter), (corner3[1] < node.ycenter), (corner3[2] < node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.posXnegYnegZ)
                    table = ((corner4[0] < node.xcenter), (corner4[1] > node.ycenter), (corner4[2] > node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.negXposYposZ)
                    table = ((corner5[0] < node.xcenter), (corner5[1] > node.ycenter), (corner5[2] < node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.negXposYnegZ)
                    table = ((corner6[0] < node.xcenter), (corner6[1] < node.ycenter), (corner6[2] > node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.negXnegYposZ)
                    table = ((corner7[0] < node.xcenter), (corner7[1] < node.ycenter), (corner7[2] < node.zcenter))
                    if not False in table:
                        list_list[level + 1].append(node.negXnegYnegZ)

                    # must remove children that aren't real yet
                    temp_templist = []
                    for node in list_list[level + 1]:
                        try:
                            node.xcenter
                            temp_templist.append(node)
                        except AttributeError:
                            pass
                    list_list[level + 1] = temp_templist

            # print [i.value[0] for i in list_list[-1]], "---"
            payloads = [i.value for i in list_list[-1]]
            # payloads = [i.value[0] for i in list_list[-1]]
            return payloads

        else:
            print "Only Cube is a valid shape"
            raise AttributeError


def find_closest_three(x, y, z, tree):
    """
    function to find the closest three data points to
    a given data point
    """
    # brief sanity checking
    if x >= tree.Xmax or x <= tree.Xmin:
        print "Fail, out of range"
    if y >= tree.Ymax or y <= tree.Ymin:
        print "Fail, out of range"
    if z >= tree.Zmax or z <= tree.Zmin:
        print "Fail, out of range"

    # find the node by coords
    for level in range(tree.maxiter):
        pass


if __name__ == "__main__":
    print "Creating octree"
    tree = Octree(100, 100, 100, -100, -100, -100)
    print "inserting node"
    tree.add_item("derp", (90.34251, 10.1234, 10.9876))
    print "Great success"
    print "inserting node"
    tree.add_item("derp", (10.34251, 10.1234, 10.9876))
    print "Great success"
    print "inserting node"
    tree.add_item("derp", (-10.34251, 10.1234, 10.9876))
    print "Great success"
    print "inserting node"
    tree.add_item("derp", (10.34251, -10.1234, 10.9876))
    print "Great success"
    print "inserting node"
    tree.add_item("derp", (10.34251, 10.1234, -10.9876))
    print "Great success"

    # get some data
    entries = tree.find_within_range((0, 0, 0), 40, "cube")
    for i in entries:
        print i




