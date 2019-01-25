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
    
    
    def end_round(self, game , player_id):
        '''
        结束回合，根据player的ID进行结算
        1. 结束射击
        2. 更新行动力
        对于本方没有行动棋子的降低1极疲劳：进行疲劳状态更新
        '''
        '''
        shot
        pass
        '''
        player = game.get_player(player_id)
        chess_list = player.get_chess_list()
        for chess_id in chess_list:
            chess = game.get_chess(chess_id)
            stone = chess.get_stone(chess)
            if stone.get_stone_type() == 'Solider' and stone.get_move() == False:
                fatigue = stone.get_fatigue()
                if fatigue > 0 :
                    stone.set_fatigue(fatigue - 1)

        self.refull_stone_mobility(game,player_id)


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
        #更新plyer_id的所有"活着"的棋子的行动力为"其最大行动力"
        chess_list_id = game.get_chess_list_id()
        player = game.get_player(player_id)
        for chess_id in chess_list_id:
            if player.chess_is_belonged_to(chess_id):
                chess = game.get_chess(chess_id)
                if chess.is_alive():
                    stone = chess.get_stone(chess)
                    stone.set_current_mobility(stone.get_max_mobility())

    
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
            return False
        # 是否有足够的行动力以及是否被压制
         if stone.get_current_mobility() <= 0 or stone.get_supress():
            return False

        # 假设是士兵，判断是否进入疲劳状态
    #  '''
    #     人员存在疲劳状态，具体表现为，连续机动2格（或爬陡坡），
    #     变为1级疲劳状态，处于1级疲劳状态的人员棋子，再机动1格即变成2级疲劳状态，
    #     处于2级疲劳状态的人员棋子不能再进行机动。
    #  '''
         _x = chess.get_x()
         _y = chess.get_y()
         from_chess = []
         from_chess.append(_x)
         from_chess.append(_y)
         from_chess.append(chess_id)

         to_chess = []
         to_chess.append(pos['x'])
         to_chess.append(pos['y'])
         to_chess.append(chess_id)

         if stone.get_stone_type() == 'Solider':
            fatigue = stone.get_fatigue()
            if fatigue == 2:
                return False
            elif fatigue == 1:
                if chess_board.Move_Chess(from_chess,to_chess):
                    stone.set_fatigue(2)
                    stone.set_move(True)
                else:
                    return False
            elif fatigue == 0 and stone.get_move() == True:
                    if chess_board.Move_Chess(from_chess,to_chess):
                        stone.set_fatigue(1)
                    else:
                        return False
         # """
         #    车辆棋子根据机动消耗表，及当前路况和距离范围内的路况，计算行动后的位置
         #     车移动时，人也要移动
         #  """
         if stone.get_stone_type() == 'chariot':

             pass

        ！！！ 这部分没更新
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

    #若棋子被压制 ，False ，表示操作失败
    #若 1. 车辆棋子行动力不小于初始机动力的一半
    #   2.人员棋子机动力不等于0，且未被压制，
    #   3. 车能装的下
    # 则乘车
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

        if car_supress == False and solider_supress == False and solider_stone.get_current_mobility():
            mobility = car_stone.get_current_mobility() - car_stone.get_max_mobility()/2
            #
            if  mobility >= 0 and car_stone.load_solider(solider_id):
                solider_stone.set_current_mobility(0)
                solider_stone.set_move(True)
                car_stone.set_current_mobility(mobility)
                return True
            else:
                return False
        else:
            return False


    #若车辆棋子被压制 ，False ，表示操作失败
    #若 1. 车辆棋子行动力不小于初始机动力的一半
    #   2.人员棋子机动力不等于0，且未被压制，
    #   3. 车上确实有这个人
    # 则下车
    def get_off_car(self,game, player_id, solider_id, car_id):
        '''
        执行下车操作
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

        if car_supress == False and solider_supress == False and solider_stone.get_current_mobility() :
            mobility = car_stone.get_current_mobility() - car_stone.get_max_mobility()/2
            if  mobility >= 0 and car_stone.unload_solider(solider_id):
                solider_stone.set_current_mobility(0)
                solider_stone.set_move(True)
                car_stone.set_current_mobility(mobility)
                return True
            else:
                return False
        else:
            return False

        # '''
        # 转换棋子状态到隐蔽状态
        # 定义：车子隐蔽时，车上的人全部隐蔽，将人的机动力设置为0，车子机动力减半
        # '''
    def hidden_action(self,game, player_id, chess_id):
        chess = game.get_chess(chess_id)
        stone = chess.get_stone()
        player = game.get_player(player_id)
        chess_board = game.get_chess_board()
        # 棋子是否属于玩家，以及棋子ID是否在棋盘上
        if not player.chess_is_belonged_to(chess_id) or not chess_board.chess_is_in(chess_id):
            return False

        if stone.get_stone_type() == 'Solider':
            #棋子行动力大于0 且 当前不在机动状态 则可以隐蔽（机动状态不能切换其他状态）
            if stone.get_current_mobility() > 0 and stone.get_move() == False:
                stone.set_current_mobility(0)
                stone.set_state("hidden")
            else:
                return False
        elif stone.get_stone_type() == 'chariot':
            if stone.get_current_mobility() - stone.get_max_mobility()/2 >= 0:
                stone.set_current_mobility(stone.get_current_mobility() - stone.get_max_mobility()/2)
                #车上的人的棋子都隐蔽
                for solider_chess_id in stone.Get_Passengers():
                    solider_chess = solider_chess_id.get_chess()
                    solider_stone = solider_chess.get_stone()
                    solider_stone.set_current_mobility(0)
                    solider_stone.set_state("hidden")
                stone.set_state("hidden")
                return True
            else:
                return False
        else:
            return False

    def conquer_village(self,game, player_id,chess_id, village_id):
        # '''
        # 征服操作
        #
        # '''
        player = game.get_player(player_id)
        chess_board = game.get_chess_board()
        # 棋子是否属于玩家，以及棋子ID是否在棋盘上
        if not player.chess_is_belonged_to(chess_id) or not chess_board.chess_is_in(chess_id):
            return False
        if not chess_board.chess_is_in(village_id):
            return False

        conquer_chess = game.get_chess(chess_id)
        conquer_stone = conquer_chess.get_stone()
        village_chess = game.get_chess(village_id)
        village_stone = village_chess.get_stone()
        #棋子id是否正确
        if not player.chess_is_belonged_to(chess_id) or not chess_board.chess_is_in(chess_id):
            return False
        #村庄id 是否正确
        if not chess_board.chess_is_in(village_id) or village_id >= chess_board.Get_Village_Count():
            return False

        village_x = conquer_chess.get_x()
        village_y = conquer_chess.get_y()
        #1.检查当前位置是否有对方棋子
        chess_position_list = chess_board.Get_Position_Chess_List()
        chess_list = chess_position_list[village_x][village_y]
        for chess_id in chess_list:
            if not player.chess_is_belonged_to(chess_id):
                return False
        #2.检查周围6格是否有对方棋子
        if conquer_chess.get_x() == village_x and conquer_chess.get_y() == village_y:
            if village_x%2 == 0:
                dir_x = [-1,-1,1,1,0,0]
                dir_y = [0,1,0,1,-1,1]
                #周围6个格子上的所有棋子
                for _x , _y in zip(dir_x,dir_y):
                    around_chess_x = _x + village_x
                    around_chess_y = _y + village_y
                    position = []
                    position.append(around_chess_x)
                    position.append(around_chess_y)
                    if not chess_board.Judge_Chess(position):
                        continue
                    chess_board_list = chess_board.Get_Position_Chess_List()
                    chess_list = chess_board_list[around_chess_x][around_chess_y]
                    #周围某一个格子上的所有棋子
                    for chess_id in chess_list:
                        #周围有棋子属于对方，未占领
                        if not player.chess_is_belonged_to(chess_id):
                            return False
                #则，周围6格棋子的所有棋子都属于己方或者不存在
                chess_board.Change_State_of_Village(village_id,player_id)
                return True
            else:
                dir_x = [-1,-1,1,1,0,0]
                dir_y = [-1,0,-1,0,-1,1]
                for _x , _y in zip(dir_x,dir_y):
                    around_chess_x = _x + village_x
                    around_chess_y = _y + village_y
                    chess_board_list = chess_board.Get_Position_Chess_List()
                    chess_list = chess_board_list[around_chess_x][around_chess_y]
                    #周围某一个格子上的所有棋子
                    for chess_id in chess_list:
                        #周围有棋子属于对方，未占领
                        if not player.chess_is_belonged_to(chess_id):
                            return False
                #则，周围6格棋子的所有棋子都属于己方或者不存在
                chess_board.Change_State_of_Village(village_id,player_id)
                return True
        else:
            return False
    '''
    移除压制函数
    
    '''
