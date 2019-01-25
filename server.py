import socket
import threading
import time
import json

class Game():
    def __init__(self):
        self.action_stack = [0,1]

    def get_current_player(self):
        return self.action_stack[0]
    
    def update_action_stack(self):
        temp = self.action_stack[0]
        del self.action_stack[0]
        self.action_stack.append(temp)
    
def tcplink(sock, addr,player_id,game):
    print('Accept new connection from %s:%s...' % addr)
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
        mess = json.loads(data)
        print(mess)
        infoclass = mess['InfoClass']
        if infoclass == 'end' or not data:
            print('end roud')
            data = json.dumps({'mess':"end"})
            sock.send(data.encode('utf-8'))
            game.update_action_stack()
            my_turn = False
            continue
        mess = json.dumps({'mess':'success'})
        sock.send(mess.encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9909))
s.listen(5)
id_list = [0,1]
game = Game()
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr,id_list[-1], game))
    id_list.pop()
    t.start()