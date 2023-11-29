import numpy as np

from setting import *

def main():
    gmap = GridMap()
    gmap.print_gmap()

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    
class GridMap():
    def __init__(self) -> None:
        self.gmap = None
        self.start_poiint = None
        self.finish_poiint = None
        self.wall_point_list = []
        
        self.my_map()

    def my_map(self):
        self.set_grid_map(9,8)
        self.set_start_point(0,0)
        self.set_finish_point(7,7)
        
        # add wall
        for i in range(1, 8):
            self.add_wall_point(i,2)            
        for i in range(1, 8):
            self.add_wall_point(2,i)
        self.add_wall_point(6,5)
        self.add_wall_point(6,6)
        self.add_wall_point(6,7)
        self.add_wall_point(8,6)
        # self.add_wall_point(7,6)
        
        self.make_grid_map()

    def set_grid_map(self, x, y):
        self.gmap = np.zeros((y, x), dtype=np.uint8)

    def set_start_point(self, x, y):
        self.start_poiint = Point(x, y)

    def set_finish_point(self, x, y):
        self.finish_poiint = Point(x, y)
        
    def add_wall_point(self, x, y):
        self.wall_point_list.append(Point(x, y))

    def make_grid_map(self):
        self.gmap[self.start_poiint.y, self.start_poiint.x] = START
        self.gmap[self.finish_poiint.y, self.finish_poiint.x] = FINISH

        for wall_point in self.wall_point_list:
            self.gmap[wall_point.y, wall_point.x] = WALL

    def get_gmap_shape(self):
        return self.gmap.shape
    
    def get_gmap(self):
        return self.gmap
    
    def get_start_point(self):
        return self.start_poiint

    def get_finish_point(self):
        return self.finish_poiint
    
    def get_wall_point_list(self):
        return self.wall_point_list

    def print_gmap(self):
        print(self.gmap)




if __name__ =='__main__':
    main()
    







        
