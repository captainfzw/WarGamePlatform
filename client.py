import socket
import threading
import time
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9909))
# 接收欢迎消息:
data = s.recv(1024).decode('utf-8')
mess = json.loads(data)
print('player_id : %d' % mess['player_id'])
my_turn = False
while True:
    while not my_turn:
        time.sleep(1)
        data = 'My turn?'
        s.send(data.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        mess = json.loads(data)
        print(mess)
        if mess['mess'] == 'begin':
            my_turn = True
    info = input('input\n')
    if info == 'end':
        my_turn = False
    mess = {'InfoClass':info}
    data = json.dumps(mess)
    s.send(data.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    mess = json.loads(data)
    print(mess['mess'])
