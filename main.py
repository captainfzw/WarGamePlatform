import Controller
import Stone
import Game
import ChessBoard
import json
import socket
import threading
import time



'''
创建线程
'''
def tcplink(sock, addr, player_id, game):
    # 将plyaer_id 发给玩家
    data = json.dumps({'player_id' : player_id})
    sock.send(data.encode('utf-8'))
    my_turn = False
    while True:
        data = sock.recv(1024)
        if game.get_current_player() == player_id and not my_turn:
            data = json.dumps({'mess':'begin'})
            sock.send(data.encode('utf-8'))
            my_turn = True
            continue
        if not my_turn:
            time.sleep(1)
            data = json.dumps({'mess':'not your turn'})
            sock.send(data.encode('utf-8'))
            continue

        mess = json.lodas(data)
        replay = {}
        infoclass = mess['InfoClass']
        # 结束当前回合
        if infoclass == 'end':
            print('end roud')
            game.update_action_stack()
            game.update_round()
            my_turn = False
            data = json.dumps({'mess':"end"})
            sock.send(data.encode('utf-8'))
            continue
        # 行动
        if infoclass == 'Action':
            player_id = game.get_current_player()
            action = mess['action']
            chess_id = mess['chess_id']
            if action == 'move':
                x = mess['x']
                y = mess['y']
                pos = {'x':x, 'y':y}
                flag = conn.move_chess(game, chess_id, player_id, pos):

            if action == 'hide':
                flag = conn.hidden_action(game, player_id, chess_id ):

            if action == 'conquer':
                village_id = mess['village_id']
                flag = conn.conquer_village(game, player_id, chess_id, village_id)

            if action == 'get_on_car':
                car_id = mess['car_id']
                flag = conn.get_on_car(game,player_id, chess_id, car_id)

            if action == 'get_off_car':
                car_id = mess['car_id']
                flag = conn.get_on_car(game,player_id, chess_id, car_id)

            if action == 'fire':
                target_id = mess['target_id']
                flag = conn.fire_action(game, player_id, chess_id, target_id)
        if flag :
            replay['mess'] = 'Sucess'
        else :
            replay['mess'] = 'Fail'
        data = json.dumps(replay)
        sock.send(data.encode('utf-8'))
    sock.close()
    print 'Connection from %s:%s closed.' % addr

def if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

    cnt = 0
    # 监听端口:
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr,player_list_id[cnt], game))
        cnt += 1
        t.start()
    message = json.load('')



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
