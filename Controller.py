import Stone
import config
import Game

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
        

    
    def reset_lis(self):
        self.moving_list = []
        self.fire_list = []
        self.action_list = []

    
    
    def end_round(self, game , player_id):
        '''
        结束回合，根据player的ID进行结算
        '''
        '''
        将player_id对应的所有有行动的棋子进行回合结算
        # !! 增加有action 的棋子的 action_type 
        '''

        player = game.get_player(player_id)
        for chess_id in self.action_list:
            if not player.chess_is_belonged_to(chess_id) :
                pass

    def update_supress(self, game, player_id):
        '''
        在回合开始时更新压制状态

        Args:
            player_id: 需要更新的玩家ID，因为更新操作是对玩家所有的棋子进行的
        '''
        # 对该player_id的玩家的所有棋子进行压制状态取反

        player = game.get_player(player_id)
        chess_list = player.get_chess_list()
        for chess_id in chess_list:
            chess = game.get_chess(chess_id)
            stone = chess.get_stone()
            supress = stone.get_supress()
            if supress == True :
                supress = False
            else:
                supress = True
            stone.set_supress(supress)

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
                if fatigue == 2 :
                    flag = False
                elif fatigue == 1 and chess_move_distance == 1:
                    fatigue = 2
                    flag = True
                elif fatigue == 0 and chess_move_distance == 2:
                    fatigue = 1
                    flag = True
                elif chess_move_dis == 0:
                    fatigue = fatigue -1
                    if fatigue < 0 :
                        fatigue = 0
                    flag = False
        if stone.get_stone_type() == 'chariot':
                """
                车辆棋子根据机动消耗表，及当前路况和距离范围内的路况，计算行动后的位置
                pass
                
                """
        if flag == True:
            #更新 士兵棋子
        else:
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

    #若棋子未被压制 则上车，返回True 。否则，False ，表示操作失败
    def get_on_car(self,game, player_id, solider_id, car_id):
        '''
        执行上车操作
        '''
        player = game.get_player(player_id)
        chess_board = game.get_chess_board()
        # 棋子是否属于玩家，以及棋子ID是否在棋盘上
        if not player.chess_is_belonged_to(solider_id) or not chess_board.chess_is_in(solider_id):
            return False
        if not player.chess_is_belonged_to(car_id) or not chess_board.chess_is_in(car_id):
            return False

        solider_chess = game.get_chess(solider_id)
        solider_stone = solider_chess.get_stone()
        solider_supress = solider_stone.get_supress()

        car_chess = game.get_chess(car_id)
        car_stone = car_chess.get_stone()
        car_supress = car_stone.get_supress()

        if car_supress == False and solider_supress == False:
            solider_chess.set_current_mobility(0)
            solider_chess.set_state("on car") # !!! 待修改
            car_chess.set_current_mobility(car_chess.get_current_mobility()/2) # 减半的定义 ？？
            return True
        else:
            return False


    #若棋子未被压制 则下车，返回True 。否则，False ，表示操作失败
    #player_id 此处未用到？？
    def get_off_car(self,game, player_id, solider_id, car_id):
        '''
        执行下车操作
        '''
        solider_chess = game.get_chess(solider_id)
        solider_stone = solider_chess.get_stone()
        solider_supress = solider_stone.get_supress()

        car_chess = game.get_chess(car_id)
        car_stone = car_chess.get_stone()
        car_supress = car_stone.get_supress()

        if car_supress == False and solider_supress == False:
            solider_chess.set_current_mobility(0)
            solider_chess.set_state("off car") # !!! 待修改
            car_chess.set_current_mobility(car_chess.get_current_mobility()/2) # 减半的定义 ？？
            return True
        else:
            return False

        # '''
        # 转换棋子状态到隐蔽状态
        # '''
    def hidden_action(self,game, player_id, chess_id):
        chess = game.get_chess(chess_id)
        stone = chess.get_stone()
        if stone.get_stone_type() == 'Solider':
            stone.set_current_mobility(0)
            stone.set_state("hidden")
        elif stone.get_stone_type() == 'chariot':  #若车上有人员？？
            stone.set_current_mobility(stone.get_current_mobility()/2)
            stone.set_state("hidden") # 隐蔽状态，被观察距离减半？？

    def conquer_village(self,game, player_id,chess_id, village_id):
        # '''
        # 征服操作
        #
        # '''
        player = game.get_player(player_id)
        chess_board = game.get_chess_board()

        conquer_chess = game.get_chess(chess_id)
        conquer_stone = conquer_chess.get_stone()
        village_chess = game.get_chess(village_id)
        village_stone = village_chess.get_stone()

        if not player.chess_is_belonged_to(chess_id) or not chess_board.chess_is_in(chess_id):
            return False
        if not chess_board.chess_is_in(village_id):
            return False

        village_x = conquer_chess.get_x()
        village_y = conquer_chess.get_y()
        % need a function to create coordinate of village_around_xy_list = []
        if conquer_chess.get_x() == village_chess.get_x() and conquer_chess.get_y() == village_chess.get_y()
            for around_chess_x , around_chess_y in village_around_xy_list:
                #给定坐标位置下的所有棋子。
                chess_board = game.get_Chess_Board()
                chess = chess_board.Get_Chess()
                chess_list = chess[around_chess_x][around_chess_y]
                for chess_id in chess_list:
                    #周围有棋子属于对方，未占领
                    if not player.chess_is_belonged_to(chess_id) :
                        chess_board.Change_State_of_Village(village_id,False)
                        return
            #则，周围6格棋子都属于自己或者不存在
            chess_board.Change_State_of_Village(village_id,player_id)
