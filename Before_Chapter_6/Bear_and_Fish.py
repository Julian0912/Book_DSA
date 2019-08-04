# -*- coding:utf8 -*-
# Author: Julian Black
# Function: 
# Attention: !!!Unfinished!!!
import random

__code_list = []


def _random_number():
    """返回一个字符串形式的三位数，作为动物的唯一编码"""
    while True:
        r = ''
        for i in range(3):
            r += str(random.randint(0,9))
        if r not in __code_list:
            __code_list.append(r)
            break
    return r


class River(object):
    """河流本身不拥有每个动物的位置信息，只在呈现时计算每个动物的位置
    河流的位置更新方法是记录新位置后整体清零再重新加入，见change_pos方法

    length        河流长度，是一个大于0的整数
    body          模拟河流主体，是一个length长度的列表，存放动物编号或None
    __move_cache  暂存每个时间步长后，动物的移位申请，以便后续处理，
                  是一个字典，key=动物实例，value=移动方向
                  # 存放二元元组的列表，每个元组储存动物编号和移动方向
    """

    def __init__(self, length: int):
        self.length = length
        self.body = [None] * length
        self.__move_cache = {}

    def rev_pos_wanted(self, ani, delta_dire:int):
        """接收动物的移动申请，并把申请上传给移位缓存

        ani           一个Animal类型
        delta_dire    移动方向，值为-1或1
        """
        # tuple_data = (ani.code, delta_dire)
        # self.__move_cache.append(tuple_data)
        self.__move_cache.setdefault(ani, delta_dire)

    def change_pos(self):
        pos_cache = {}    # key为河流位置；value为申请该位置的动物实例，是一个列表
        for ani, dire in self.__move_cache.items():
            next_pos = ani.pos + dire
            next_entity = self.body[next_pos]    # 要移动的位置占有者（可能为None）
            if next_entity != ani.code and next_entity is not None:
                # 如果某动物的下一个位置不是自身也不是None，即下一个位置原本有动物，则该动物保持不动
                pos_cache[ani.pos] = pos_cache.get(ani.pos, []) + [ani]
            else:
                # 否则移动到下一个位置待命（可能后期会被撤回（如交配或捕食））
                pos_cache[next_pos] = pos_cache.get(next_pos, []) + [ani]
        # to be continued ...
        # 接下来判断是否有捕食或交配行为，然后更新动物的位置信息
        # 判断是否有捕食或交配行为
        for pos, ani_ls in pos_cache.values():
            if len(ani_ls) == 2:
                if ani_ls[0].code[0] == 'b' and ani_ls[1].code[0] == 'f':
                    pos_cache[pos].remove(ani_ls[1])
                elif ani_ls[0].code[0] == 'f' and ani_ls[1].code[0] == 'b':
                    pos_cache[pos].remove(ani_ls[0])
                elif ani_ls[0].code[0] == 'b' and ani_ls[1].code[0] == 'b':
                    pass




    def show(self):
        pass


class Animal(object):
    """动物拥有自身在河流的位置信息"""

    def __init__(self, river: River):
        """子类必须定义一个名为kind的属性来标识物种

        pos    动物在河流中的位置，一个大于等于0小于等于河长度的整数
        code   每个动物的唯一编码，是一个字符串形式的三位数，
               在子类里被改写，不同种的动物加一个作为标识的前缀
        """
        self.river = river
        self.pos = self.__get_pos()
        self.code = _random_number()

    def __get_pos(self):
        """根据河流长度返回一个可用位置"""
        length = self.river.length
        while True:
            p = random.randint(0, length - 1)
            if self.river.body[p] is None:
                self.river.body[p] = self.code    # 将动物编码放入河流主体
                return p

    def want_pos(self):
        """向河流发出位置申请"""
        if self.pos == 0:
            direction = random.choice([0, 1])
        elif self.pos == self.river.length-1:
            direction = random.choice([-1, 0])
        else:
            direction = random.choice([-1, 0, 1])
        self.river.rev_pos_wanted(self, direction)

    def move(self):
        """前进或后退一格（改变自身位置信息）"""

    def mating(self):
        """动物的交配行为"""


class Bear(Animal):
    def __init__(self, river):
        super().__init__(river)
        self.code = 'b'+_random_number()


class Fish(Animal):
    def __init__(self, river):
        super().__init__(river)
        self.code = 'f'+_random_number()


if __name__ == '__main__':
    river_length = int()
    river_509 = River(river_length)
    animals = [Bear(river_509),Bear(river_509),Fish(river_509),Fish(river_509),Fish(river_509)]
    time_step = 10
    while time_step > 0:
        for animal in animals:
            animal.want_pos()
        river_509.change_pos()
        river_509.show()






