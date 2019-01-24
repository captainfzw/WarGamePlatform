import Controller
import Stone
import Game
import ChessBoard
import json


def if __name__ == "__main__":
    '''
    初始化棋盘，棋子，玩家
    '''
    chessboard = Chess_Board(village, chess_list, gradiant_board , landform_board, row = 29, col = 33)
    chess_list_id = []
    chess_list_objcet = {}
    player_list_id = []
    player_list_object = {}

    game = Game(chessboard,chess_list_id, chess_list_objcet, player_list_id, player_list_object)

    Controller con = Controller()
    Communicator comm = Communicator()
    message = json.load('')
    
    '''
    发送并获取
    获取AI消息
    和AI进行初始化
    pass
    待填补
    '''
    #游戏开始
    while(True):
        player_id = game.get_current_player()
        message = comm.send_message(player_id)
        infoclass = message['InfoClass']
        if infoclass == 'Action':
            chess_id = ['ChessID']
            action = message['action']

            if action == 'move':
                pass
            
            if action == 'hide':
                pass
            
            if action == 'conquer':
                pass

            if action == 'car':
                pass

            if action == 'fire':
                pass
        
        if infoclass == 'System':
            pass
        
        if infoclass == 'Error':
            pass
        
        if game.end():
            break
    #结算本场每个player_id得分，和胜负
    player_score= {}
    #1.结算占领要点分值
    for Id in range(chessboard.Get_Village_Count()):
        player_score[Id] = chessboard.Get_Village_Score(Id) + player_score[Id]
    #2.结算兵力分值
    for player_id in player_list_id:
        for chess_id in chess_list_id:
            chess = game.get_chess(chess_id)
            stone = chess.get_stone()
            if chess.is_alive():
                player_score[player_id] = player_score[player_id] + stone.get_score()

    player_result = sorted(player_score.items(), key=lambda kv: kv[1])
    '''
    展示游戏结果
    ‘’‘
