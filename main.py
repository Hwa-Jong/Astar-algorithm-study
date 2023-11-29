from map import GridMap
from astar import Astart

from setting import *

def main():    
    gmap = GridMap()
    print('< Map >')
    gmap.print_gmap()
    print('===================================')

    astar = Astart(gmap)
    astar.start()


if __name__=='__main__':
    main()