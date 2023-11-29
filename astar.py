from map import GridMap, Point

from setting import *

class Node():
    def __init__(self, point:Point, parent:Point) -> None:
        self.point = point
        self.f_score = 0
        self.g_score = 0
        self.h_score = 0

        self.parent = parent
        
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.point == other.point
        return False

    # '<' Operator
    def __lt__(self, other):
        return self.g_score < other.g_score

    # '<=' Operator
    def __le__(self, other):
        return self.g_score <= other.g_score

    # '>' Operator
    def __gt__(self, other):
        return self.g_score > other.g_score

    # '>=' Operator
    def __ge__(self, other):
        return self.g_score >= other.g_score

    def set_score(self, g_score, h_score):
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = self.g_score + self.h_score

    def get_point(self):
        return self.point


class Astart():
    def __init__(self, gmap:GridMap) -> None:
        self.gmap = gmap

    def start(self):
        open_list = []
        close_list = []
        wall_point_list = self.gmap.get_wall_point_list()
        
        start_point = self.gmap.get_start_point()
        finish_point = self.gmap.get_finish_point()

        # start
        node = Node(start_point, None)
        close_list.append(node)

        success = False
        while True:
            near_node_list = self.get_near_node(node, close_list, wall_point_list)
            open_list = self.merge_node(near_node_list, open_list)
            if len(open_list) == 0:
                break
            node = self.get_minimum_f_score_node(open_list)
            close_list.append(node)
            if self.check_finish(close_list, finish_point):
                success = True
                break
        
        print('< result : %s >'%( 'SUCESS' if success else 'FAIL'))
        result = self.get_result(close_list[-1])
        if success:
            # except start point and finish point
            self.show_result(result[1:-1])
        else:
            # except start point
            self.show_result(result[:-1])


    def check_finish(self, close_list:list, finish_point:Point):
        for node in close_list:
            if node.get_point() == finish_point:
                return True        
        return False


    def get_near_node(self, node:Node, close_list:list, wall_point_list:list):
        near_node_list = []
        h, w = self.gmap.get_gmap_shape()

        p = node.get_point()
        if p.y > 0:
            point = Point(p.x, p.y-1)
            # if this point is not wall
            if not point in wall_point_list:
                up_node = Node(point, node)
                # if this node is not exist in close list
                if not up_node in close_list:
                    up_node.set_score(node.g_score+COST, self.calc_h_score(up_node.get_point()))
                    near_node_list.append(up_node)
        if p.y < h-1:
            point = Point(p.x, p.y+1)
            # if this point is not wall
            if not point in wall_point_list:
                down_node = Node(point, node)
                # if this node is not exist in close list
                if not down_node in close_list:
                    down_node.set_score(node.g_score+COST, self.calc_h_score(down_node.get_point()))
                    near_node_list.append(down_node)
        if p.x > 0:
            point = Point(p.x-1, p.y)
            # if this point is not wall
            if not point in wall_point_list:
                left_node = Node(point, node)
                # if this node is not exist in close list
                if not left_node in close_list:
                    left_node.set_score(node.g_score+COST, self.calc_h_score(left_node.get_point()))
                    near_node_list.append(left_node)
        if p.x < w-1:
            point = Point(p.x+1, p.y)
            # if this point is not wall
            if not point in wall_point_list:
                right_node = Node(point, node)
                # if this node is not exist in close list
                if not right_node in close_list:
                    right_node.set_score(node.g_score+COST, self.calc_h_score(right_node.get_point()))
                    near_node_list.append(right_node)

        return near_node_list

    def calc_h_score(self, now_point:Point):
        finish_point = self.gmap.get_finish_point()
        return abs(finish_point.x - now_point.x) + abs(finish_point.y - now_point.y)

    def get_minimum_f_score_node(self, open_list:list):
        f_score_list = [node.f_score for node in open_list]
        minimum_f_score = min(f_score_list)
        idx = f_score_list.index(minimum_f_score)
        return open_list.pop(idx)
    
    def merge_node(self, near_node_list:list, open_list:list):
        new_node_list = []
        for node in near_node_list:
            if node in open_list:
                idx = open_list.index(node)
                if open_list[idx] > node:
                    open_list[idx] = node

            else:
                new_node_list.append(node)

        open_list += new_node_list
        return open_list

    def get_result(self, node:Node):
        path = []

        node_tmp = node
        while True:
            path.append(node_tmp.get_point())
            if node_tmp.parent is None:
                break
            else:
                node_tmp = node_tmp.parent
                
        return path

    def show_result(self, result:list):
        gmap = self.gmap.get_gmap()
        for p in result:
            x, y = p.x, p.y
            gmap[y,x] = PATH
        print(gmap)


    def show_point_in_list(self, node_list:list):
        for node in node_list:
            print('[%d, %d]'%(node.point.x, node.point.y))
        


def main():    
    pass



if __name__ == '__main__':
    main()