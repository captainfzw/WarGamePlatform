import Stone

class Player():
    '''
    玩家信息

    Args:
        Chess_Board: 玩家的地图视图
        chess_list: 玩家的棋子列表（存ID）
        user_id: 为玩家分配的一个ID标识
    '''
    def __init__(self,Chess_Board,chess_list, user_id):
        self.Chess_Board = Chess_Board
        self.chess_list = chess_list
        self.user_id = user_id

    def get_Chess_Board(self):
        return self.Chess_Board
    
    def get_chess_list(self):
        return self.chess_list
    
    def get_user_id(self):
        return self.user_id

    def chess_check(self, chess_id):
        if chess_id in self.chess_list:
            return True
        else:
            return False
    

class Game():
    '''
    游戏初始化

    Args:
        Chess_Board: 图视图
        chess_list_id: 棋子列表（存ID）
        chess_list_object: dict，棋子ID和棋子实体的键值对。
        player_list: 为玩家分配的一个ID标识
    '''
    def __init__(self,Chess_Board, chess_list_id, chess_list_object, player_list_id, player_list_object):
        self.Chess_Board = Chess_Board
        self.chess_list = chess_list
        self.chess_list_object = chess_list_object
        self.player_list_id = []
        self.player_list_object = {}
        '''
        根据游戏人数
        初始化
        创建游戏地图 map
        创建游戏棋子 chess_list
        创建玩家
        '''

    
    def get_player(self,player_id):
        '''
        根据ID获取Player对象
        '''
        if player_id in self.get_player_list_id:
            return self.player_list_object['player_id']
        else:
            return None
    
    def get_Chess_Board(self):
        return self.Chess_Board
    
    def get_chess_list_id(self):
        return self.get_chess_list_id
    
    def get_chess_list_objcet(self):
        return self.get_chess_list_objcet
    
    def get_player_list_id(self):
        return self.player_list_id
    
    def get_player_list_object(self):
        return self.player_list_object