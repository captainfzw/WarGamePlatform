class BaseStone():
    """
    棋子类的基类

    Args:
        stone_type: 士兵是何种类型
        name: 棋子的名字
        max_mobility: 棋子的行动力上限
        current_mobility: 棋子的当前行动力
        weapons: 一个数组，表示携带棋子的武器
        states: 数字，表示棋子的状态
        suppress: bool，表示是否处于被压制状态
        score: 表示棋子的分值
    """
    def __init__(self,  mobility, weapons, states, stone_type, name, suppress, score):
        self.name = name
        self.stone_type = stone_type
        self.max_mobility = mobility
        self.current_mobility = mobility
        self.weapons = weapons
        self.states = states
        self.suppress = suppress
        self.score = score
    
    def set_states(self,states):
        self.states = states

    def set_current_mobility(self,mobility):
        self.current_mobility = mobility
        
    def get_suppress(self):
        return self.suppress
    
    def set_suppress(self,suppress):
        self.suppress = suppress
    
    def get_stone_type(self):
        return self.stone_type
    
    def get_name(self):
        return self.name

    def get_weapons(self):
        return self.weapons
    
    def get_states(self):
        return self.states

    def get_max_mobility(self):
        return self.get_max_mobility

    def get_current_mobility(self):
        return self.current_mobility

    def get_score(self):
        return self.score

class SoliderStone(BaseStone):
    '''
    士兵棋子类

    Args:
        fatigue: 疲劳值
        fire_mark: 标记是否可以进行射击
    '''
    def __init__(self, chess_id, mobility, weapons, states, stone_type, name, fatigue=0):
        super(chess_id, mobility, weapons, states)
        self.stone_type = stone_type
        self.name = name
        self.fatigue = fatigue
        self.fire_mark = True
    
    def get_fatigue(self):
        return self.fatigue

    def set_fatigue(self,fatigue):
        self.fatigue = fatigue
    
    def get_fire_mark(self):
        return self.fire_mark
    
    def set_fire_mark(self,fire_mark):
        self.fire_mark = fire_mark


class Chariot(BaseStone):

    '''
    战车类

    Args:
        capacity: 汽车的承载能力
        armor: 汽车的护甲
        climbing_ablility: 汽车的爬坡能力
        passengers_list: 记录在战车上的士兵ID
        empty_left: 汽车剩余的位置
    '''
    def __init__(self,mobility, weapons, states, stone_type, name, suppress, capacity, armor, climbing_ability,):
        super(mobility, weapons, states, stone_type, name)
        self.capacity = capacity
        self.armor = armor
        self.climbing_ability = climbing_ability
        self.passengers_list = []


    
    def load_solider(self, solider_id):
        '''
        承载士兵的函数

        Args:
            solider_id: 要承载的士兵的ID
        '''
        if len(self.passengers_list) <= self.capacity :
            self.passengers_list.insert(solider_id)
            
            return True
        else:
            return False
    
    
    def unload_solider(self, solider_id):
        '''
        卸下士兵

        Args:
            solider_id: 卸下的士兵的ID
        '''
        if solider_id in self.passengers_list:
            self.passengers_list.remove(solider_id)
            return True
        else:
            return False


class Borad_Chess(object):
    '''
    棋盘棋子类的封装

    Args:
     stone: 具体的棋子
     chess_id: 棋子的ID号
     x,y: 棋盘上的坐标
     plyaer_id:属于哪位玩家
     alive: 表示该棋子是否还活着
    '''
    def __init__(self,stone,chess_id, x, y, plyaer_id):
        self.stone = stone
        self.chess_id = chess_id
        self.x = x
        self.y = y
        self.player_id
        self.alive = True
    
    def set_stone(self,stone):
        self.stone = stone
    
    def set_x(self,x):
        self.x = x
    
    def set_y(self,y):
        self.y = y

    def set_alive(self,alive):
        self.alive = alive
    
    def is_alive(self):
        return self.alive

    def get_chess_id(self):
        return self.chess_id

    def get_player_id(self):
        return self.player_id
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_stone(self):
        return self.stone





    
