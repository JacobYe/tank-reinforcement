# -*- coding: utf-8 -*-

import numpy as np
import time


class Infer:
    ORDER_NORMAL = [
        ('move', ''),
        ('turnTo', 'UP'),
        ('turnTo', 'DOWN'),
        ('turnTo', 'LEFT'),
        ('turnTo', 'RIGHT')
    ]

    ORDER_ALL = ORDER_NORMAL + [
        ('fire', 'UP'),
        ('fire', 'DOWN'),
        ('fire', 'LEFT'),
        ('fire', 'RIGHT')
    ]

    def __init__(self, game_map, tank_speed):
        """
        初始化
        :param game_map: 地图
        :param tank_speed: 坦克速度
        """
        self.game_map = np.array(game_map, dtype=np.int32)
        self.tank_speed = tank_speed

    def _prob(self, sp_list):
        p_dict = {}
        for st, pb in sp_list:
            to_pos, to_dir = st
            st_stack = []
            for order in self.ORDER_NORMAL:
                c_pos, c_dir = self._next(to_pos, to_dir, order[0], order[1], self.tank_speed)
                if self._is_in_forest(c_pos):
                    st_stack.append((c_pos, c_dir))
            for s in st_stack:
                if s in p_dict:
                    p_dict[s] += 1.0 / (len(sp_list) * len(st_stack))
                else:
                    p_dict[s] = 1.0 / (len(sp_list) * len(st_stack))
            sp_list = self._sort_dict(p_dict)
        return sp_list

    def _next(self, tank_pos, tank_dir, order_act, order_dir, tank_speed):
        if order_act == 'fire':
            return tank_pos, tank_dir
        elif order_act == 'turnTo':
            return tank_pos, order_dir
        elif order_act == 'move':
            source_pos = tank_pos
            if tank_dir == 'UP':
                for i in range(tank_speed):
                    new_pos = (source_pos[0] - 1, source_pos[1])
                    if self._is_move_probable(new_pos):
                        source_pos = new_pos
                return source_pos, tank_dir
            elif tank_dir == 'DOWN':
                for i in range(tank_speed):
                    new_pos = (source_pos[0] + 1, source_pos[1])
                    if self._is_move_probable(new_pos):
                        source_pos = new_pos
                return source_pos, tank_dir
            elif tank_dir == 'LEFT':
                for i in range(tank_speed):
                    new_pos = (source_pos[0], source_pos[1] - 1)
                    if self._is_move_probable(new_pos):
                        source_pos = new_pos
                return source_pos, tank_dir
            elif tank_dir == 'RIGHT':
                for i in range(tank_speed):
                    new_pos = (source_pos[0], source_pos[1] + 1)
                    if self._is_move_probable(new_pos):
                        source_pos = new_pos
                return source_pos, tank_dir

    def _is_move_probable(self, pos):
        # 检查移动是否可行
        if self.game_map[pos[0]][pos[1]] != 0 and self.game_map[pos[0]][pos[1]] != 2:
            return False
        return True

    def _is_in_forest(self, pos):
        # 迭代过程中不可能出森林
        if self.game_map[pos[0]][pos[1]] != 2:
            return False
        return True

    def _sort_dict(self, dict):
        # 按值排序字典, 正则化概率, 返回有序列表
        p_sum = sum(dict.values())
        dict = {k: v / p_sum for k, v in dict.items()}
        return sorted(dict.items(), key=lambda d: d[1], reverse=True)

    def get_pos_dir(self, tank_pos, tank_dir, round):
        """
        坐标+方向 的概率分布 (从大到小)
        :param tank_pos: 坦克初始坐标<tuple>
        :param tank_dir: 坦克初始方向<string>
        :param round: 迭代轮数<int>
        :return: list<tuple>; tuple: (pos, dir, p)
        """
        sp_list = [((tank_pos, tank_dir), 1)]
        for r in range(round):
            sp_list = self._prob(sp_list)
        return sp_list

    def get_pos(self, tank_pos, tank_dir, round):
        """
        坐标 的概率分布 (从大到小)
        :param tank_pos: 坦克初始坐标<tuple>
        :param tank_dir: 坦克初始方向<string>
        :param round: 迭代轮数<int>
        :return: list<tuple>; tuple: (pos, p)
        """
        sp_list = self.get_pos_dir(tank_pos, tank_dir, round)
        pos_dict = {}
        for st, pb in sp_list:
            if st[0] in pos_dict:
                pos_dict[st[0]] += pb
            else:
                pos_dict[st[0]] = pb
        return sorted(pos_dict.items(), key=lambda d: d[1], reverse=True)


if __name__ == '__main__':
    gamemap = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    tank_pos = (7, 4)
    tank_dir = "RIGHT"
    start = time.time()
    # 初始化
    forest = Infer(gamemap, 2)
    # 调用 get_pos_dir()
    ra = forest.get_pos_dir(tank_pos, tank_dir, 10)
    end = time.time()
    print(ra)
    print('Time: ', (end-start)*1000, 'ms')
    # 调用 get_pos()
    rb = forest.get_pos(tank_pos, tank_dir, 4)
    print(rb)
