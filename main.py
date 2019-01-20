import Controller
import Stone
import Game
import ChessBoard
import json


def if __name__ == "__main__":
    '''
    初始化棋盘，棋子，玩家
    '''
    chessboard = Chessboard()
    chess_list_id = []
    chess_list_objcet = {}
    player_list_id = []
    player_list_object = {}

    Game = game(chessboard,chess_list_id, chess_list_objcet, player_list_id, player_list_object)

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
        
    '''
    展示游戏结果
    ‘’‘