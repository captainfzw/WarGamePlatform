import stone
import config


'''
裁判模块，用来对游戏状态进行结算

'''
class Controller():

    '''
    
    Args:
        moving_list: 移动的棋子ID
        fire_list: 射击的棋子ID
        action_list: 行动的棋子ID（包含上述行动）
        plyaer_list: player_ID的列表
    ''' 
    def __init__(self, plyaer_list):
        self.moving_list = []
        self.fire_list = []
        self.action_list = []
        

    
    def reset_list():
        self.moving_list = []
        self.fire_list = []
        self.action_list = []

    
    
    def end_round(self，game, player_id):
        '''
        结束回合，根据player的ID进行结算
        '''
        pass

    def update_supress(self, game, player_id):
        '''
        在回合开始时更新压制状态

        Args:
            player_id: 需要更新的玩家ID，因为更新操作是对玩家所有的棋子进行的
        '''
        pass
    

    def refull_stone_mobility(self, game, player_id):
        '''
        将棋子的行动力从新填充

        Args:
            player_id: 需要更新的玩家ID，因为更新操作是对玩家所有的棋子进行的
        '''
        pass
    
     def move_chess(self, game, chess_id,player_id,pos):
         '''
        移动棋子，判断移动是否合法，移动过程中还需判断周围是否有蓝方棋子。

        Args:
            chess_id: 移动的棋子的ID
            player_id: 移动的player的ID
            pos: 棋子需要移动到的位置
        '''
        player = game.get_player(player_id)
        chess_board = game.get_chess_board()
        chess = game.get_chess(chess_id)
        stone = chess.get_stone()
        # 棋子是否属于玩家，以及棋子ID是否在棋盘上
        if not player.chess_is_belonged_to(chess_id) or not chess_board.chess_is_in(chess_id):
            return
        # 是否有足够的行动力以及是否被压制
        if stone.get_current_mobility() <= 0 or stone.get_supress():
            return
        # 假设是士兵，判断是否进入疲劳状态
        if stone.get_stone_type() == 'Solider':
            fatigue = stone.get_fatigue()
            if fatigue > 2:
                return
        
        chess_board.move_chess(chess_id, pos)
        #移动后判断附近是否有敌人，有的话进行机会对方进行机会射击
        nearby_army = chess_board.nearby_army(chess_id)
        for arm_chess in nearby_army:
            fire_action(self, game, arm_chess.get_player_id, chess_id, 'opportunity_fire')
        
        #棋子是否阵亡
        if not chess.is_alive():
            return
        # 更新行动力
        stone.set_current_mobility(stone.get_current_mobility() - 1)
        self.action_list.append(chess_id)
        self.moving_list.append(chess_id)
    
    def fire_action(self, game, plyaer_id,chess_id, arm_id, action_type):
        '''
        射击操作

        Args:
            action_type:表示射击的类别
        '''
        if action_type == 'conver_fire':
            pass
        elif action_type == 'moving_fire':
            pass
        elif acton_type == 'opportunity_fire':
            pass
    
    def get_on_car(self,game, player_id, solider_id, car_id):
        '''
        执行上车操作
        '''
        pass
    
    def get_off_car(self,game, player_id, solider_id, car_id):
        '''
        执行下车操作
        '''
        pass
    
    def hidden_action(self,game, player_id, chess_id):
        '''
        转换棋子状态到隐蔽状态
        '''
        pass

    def conquer_village(self,game, plyaer_id,chess_id, village_id):
        '''
        征服操作

        '''
        pass 
    