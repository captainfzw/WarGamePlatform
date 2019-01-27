import collections

class Chess_Board(object):
	"""
	棋盘类
	Args:
		row % 行数，默认29
		col % 列数，默认33

		village[id][3]     %村庄_id位置:Village[id][0]->行；Village[id][1]->列; Village[id][2] -> 村庄状态
		village_score[id]        % 村庄的分数

		gradiant_board[row][col]   %棋盘_row_col:坡度
		landform_board[row][col]   %棋盘_row_col:地形
		chess_list[row][col][chess_num] %棋盘_row_col_棋子id，保存对应坐标位置的id：e.g. chess_list[x][y][0] = chess_id
		chess_id_list : 保存棋子id
	"""
	def __init__(self, village ,village_score, chess_id_list, chess_list, gradiant_board , landform_board, row = 29, col = 33 ):
		self.__row = row
		self.__col = col
		# self.chess = [[[] for y in range(col)] for x in range(row)]  	 #list 生成棋子初始为空
		# 初始化村庄位置、分值
		self.__village = village
		self.__village_score = village_score
		self.__chess_id_list = chess_id_list
		self.__chess_list = chess_list
		self.__gradiant_board = gradiant_board	  #初始化坡度为开阔地
		self.__landform_board = landform_board     #初始化地形为开阔地
		# print("pls: input the villages' row and col separate as: Init_Village(village_count,([x1,y1]...[xn,yn])) ")
	
	#初始化村庄
	# def Init_Village(self, village_count, villages):
	# 	self.__village_count = village_count
	# 	% self.__village = [[ [] for two in range(2)] for count in village_count]
	# 	for i in range(village_count):
	# 		village[i][0] = villages[i][0]	#村庄横坐标
	# 		village[i][1] = villages[i][1]	#村庄纵坐标
	# 		village_state[i] = False		#村庄未被占领
	# 		__landform_board[villages[i][0]][villages[i][1]] = 1  #居民地
	# 	for i in range(village_count):
	# 		self.__village.append((villages[i][0],villages[i][1],village_state[i])) # village_id: (x,y,state)
	# 	print("pls: input the chess as : Init_Chess(chess_count,([x1,y1,id],[x2,y2,id],...,[xn,yn,id]))")

	#初始化棋子 parameters format: chess: (x,y,chess_id)
	# def Init_Chess(self,chess_count,chess):
	# 	for i in range(chess_count):
	# 		self.__chess_list[chess[i][0]][chess[i][1]].append(chess[i][2])
	# 	print("pls: input the road as : Init_Road(road_count,((x1,y1),(x2,y2),...,(xn,yn)))")

	# #初始化普通道路
	# def Init_Road(self,road_count,road):
	# 	for i in range(road_count):
	# 		self.__landform_board[road[i][0]][road[i][1]] = 2		#普通道路
	# 	print("pls: input the highroad as : Init_HighRoad(highroad_count,((x1,y1),(x2,y2),...,(xn,yn)))")

	# #初始化公路
	# def Init_HighRoad(self,highroad_count,highroad):
	# 	for i in range(highroad_count):
	# 		self.__landform_board[highroad[i][0]][highroad[i][1]] = 3 #公路
	# 	print("pls: input the gradiant as: Init_Gradiant((gradiant1,...,gradiant_row*col))" )

	# #初始化坡度
	# def Init_Gradiant(self,gradiant):
	# 	for x in row:
	# 		for y in col:
	# 			__gradiant_board[x][y] = gradiant[x*row + y] #坡度
	# 	print("ALl Done. Let's begin!") 


	def judge_chess(self,position):
		position_x = position[0]
		position_y = position[1]
		if position_x >= 0 and position_x < self.__row and position_y >= 0 and position_y < self.__col:
			return True
		else:
			return False

	#删除棋子，删除棋子前判断是否合法，删除棋子不判断
	def remove_one_chess(self,chess):
		position = []
		position.append(chess[0])# (x
		position.append(chess[1]) # y)
		self.__chess_list[chess[0]][chess[1]].remove(chess[2])


	#增加棋子: 增加前judge棋子是否合法，增加函数不判断
	def add_one_chess(self,chess):
		position = list()
		position.append(chess[0])# (x
		position.append(chess[1]) # y)
		self.__chess_list[chess[0]][chess[1]].append(chess[2])


	#获取棋盘信息
	def get_all_info(self):
		return self.__village, self.__chess_list, self.__landform_board, self.__gradiant_board

	def get_village(self):
		return self.__village

	def get_position_chess_list(self):
		return self.__chess_list

	def get_landform(self):
		return self.__landform_board

	def get_gradiant(self):
		return self.__gradiant_board

	#移动棋子: parameter_format:(x1,y1,chess_id) -> (x2,y2,chess_id)
    #1.判断（x2,y2) 合法性；2.判断（x2,y2)是否在其周围6格
	def move_chess(self,from_chess,to_chess):
		if self.judge_chess(to_chess):
			#even row：
			if from_chess[0]%2 == 0:
				dir_x = [-1 ,-1 ,1 ,1 ,0 ,0 ]
				dir_y = [0 ,1 ,0 ,1 ,-1 ,1 ]
				for x,y in zip(dir_x,dir_y):
					temp_x = from_chess[0]
					temp_y =  from_chess[1]
					if temp_x + x == to_chess[0] and temp_y + y == to_chess[1]:
						self.add_one_chess(to_chess)
						self.remove_one_chess(from_chess)
						return True
				return False
			#odd row:
			else:
				dir_x = [-1,-1,1,1,0,0]
				dir_y = [-1,0,-1,0,-1,1]
				for x,y in zip(dir_x,dir_y):
					temp_x = from_chess[0]
					temp_y = from_chess[1]
					if temp_x + x == to_chess[0] and temp_y + y == to_chess[1]:
						self.add_one_chess(to_chess)
						self.remove_one_chess(from_chess)
						return True
				return False
		else:
			return False

	#移动到左上角格子 : paramaters: {"x:x_value","y:y_value"}
	def move_left_top(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.judge_chess(origin_pos['x']-1,origin_pos['y']):
				position = list()
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False
		else:
			if self.judge_chess(origin_pos['x']-1,origin_pos['y']-1):
				position = list()
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']-1) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False

	#移动到右上角格子
	def move_right_top(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.judge_chess(origin_pos['x']-1,origin_pos['y']+1):
				position = list()
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']+1) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False
		else:
			if self.judge_chess(origin_pos['x']-1,origin_pos['y']):
				position = list()
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False
	#左下移
	def move_left_bottom(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.judge_chess(origin_pos['x']+1,origin_pos['y']):
				position = list()
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False
		else:
			if self.judge_chess(origin_pos['x']+1,origin_pos['y']-1):
				position = list()
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']-1) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False

	#右下移
	def move_right_bottom(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.judge_chess(origin_pos['x']+1,origin_pos['y']+1):
				position = list()
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']+1) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False
		else:
			if self.judge_chess(origin_pos['x']+1,origin_pos['y']):
				position = list()
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
			else:
				return False

	#左移动
	def move_left(self,origin_pos):
		if self.judge_chess(origin_pos['x'],origin_pos['y']-1):
				position = list()
				position.append(origin_pos['x'])# (x
				position.append(origin_pos['y']-1) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
		else:
			return False
	#右移动
	def move_right(self,origin_pos):
		if self.judge_chess(origin_pos['x'],origin_pos['y']+1):
				position = list()
				position.append(origin_pos['x'])# (x
				position.append(origin_pos['y']+1) # y)
				self.add_one_chess(position)

				position2 = list()
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.remove_one_chess(position2)
		else:
			return False
		#需要双方能够通视，如此则也行可以不考虑阻碍点
	#此处只求两个坐标的距离。不考虑其他任何关系
	def bfs_shortest_distance(self, current_pos, destination_pos):
		queue = collections.deque(current_pos)
		value_board = [[0 for y in range(self.__col)] for y in range(self.__row)]
		while queue:
			current_xy = queue.pop()
			# x is in even row
			if current_xy[0] % 2 == 0:
				dir_x = [-1 ,-1 ,1 ,1 ,0 ,0 ]
				dir_y = [0 ,1 ,0 ,1 ,-1 ,1 ]
				for x , y in zip(dir_x,dir_y):
					next_x = x  + current_xy[0]
					next_y = y + current_xy[1]
					next_xy = list()
					next_xy.append(next_x)
					next_xy.append(next_y)
					if self.judge_chess(next_xy) and (not value_board[next_x][next_y] == 0) :
						value_board[next_x][next_y] = value_board[current_xy[0]][current_xy[1]] + 1
						if next_x == destination_pos[0] and next_y == destination_pos[1]:
							return value_board[next_x][next_y]
						else:
							queue.appendleft(next_xy)


			else:
				dir_x = [-1,-1,1,1,0,0]
                dir_y = [-1,0,-1,0,-1,1]
                for x , y in zip(dir_x,dir_y):
					next_x = x  + current_xy[0]
					next_y = y + current_xy[1]
					next_xy = list()
					next_xy.append(next_x)
					next_xy.append(next_y)
					if self.judge_chess(next_xy) and (not value_board[next_x][next_y] == 0) :
						value_board[next_x][next_y] = value_board[current_xy[0]][current_xy[1]] + 1
						if next_x == destination_pos[0] and next_y == destination_pos[1]:
							return value_board[next_x][next_y]
						else:
							queue.appendleft(next_xy)



	#BFS 扫描出当前局面下的可视的对手棋子
	#1. 将己方的所有棋子的十格范围内的对手的人员棋子放入list。
	#2. 将己方的所有棋子的25格范围内的可以通视的对手的车辆棋子（车上的人）放入list。
	#3. asumin that no chess obstructe sight
	#4. 通视时考虑了对手是否隐蔽

	#获取玩家当前时刻得到的非本方棋子
	def get_player_vision(self,game , player_id):
		player = game.get_player(player_id)
		chess_list = player.get_chess_list()
		vision_list = list()
		for chess_id_1 in chess_list:
			if player.chess_is_belonged_to(chess_id_1):
				for chess_id_2 in chess_list:
					if chess_id_2 not in vision_list:
						if not player.chess_is_belonged_to(chess_id_2):
							distance = self.cal_distance(game,chess_id_1,chess_id_2)
							chess = game.get_chess(chess_id_2)
							stone = chess.get_stone()
							if stone.get_stone_type() == 'Solider' and distance <= 10 and stone.get_state() != 'hidden':
								vision_list.append(chess_id_2)
							elif stone.get_stone_type() == 'Solider' and distance <= 5 and stone.get_state() == 'hidden':
								vision_list.append(chess_id_2)
							elif stone.get_stone_type() == 'chariot' and distance <= 25 and stone.get_state() != 'hidden':
								vision_list.append(chess_id_2)
							elif stone.get_stone_type() == 'chariot' and distance <= 12 and stone.get_state() == 'hidden':
								vision_list.append(chess_id_2)
		player.set_army_chess_list(vision_list)
		return vision_list

	#判断当前玩家是否能够观察到对方某棋子
	def is_in_player_vision(self,game , player_id, arm_id):
		vision_list = self.get_player_vision(game,player_id)
		if arm_id in vision_list:
			return True
		else :
			return False
		
	#广搜确定棋子间的最短距离
	#此处假设一定可达
	def cal_distance(self,game, chess_id, army_id):
		chess = game.get_chess(chess_id)
		player_chess_x = chess.get_x()
		player_chess_y = chess.get_y()
		current_pos = list()
		current_pos.append(player_chess_x)
		current_pos.append(player_chess_y)

		_army = game.get_chess(army_id)
		army_chess_x = _army.get_x()
		army_chess_y = _army.get_y()
		destination_pos = list()
		destination_pos.append(army_chess_x)
		destination_pos.append(army_chess_y)

		distance = self.bfs_shortest_distance(current_pos,destination_pos)
		return distance


	#村庄占领状态改变
	def change_state_of_village(self, Id, new_state):
		self.__village[Id][2] = new_state

	def get_village_state(self, Id):
		return self.__village[Id][2]

	def get_village_score(self, Id):
		return self.__village_score[Id]

	def get_village_count(self):
		return len(self.__village)

	def chess_is_in(self,chess_id):
		if chess_id in self.__chess_id_list:
			return True
		else:
			return False

	def debug(self):
		print(self.__chess_list)
		print(self.__gradiant_board)
		print(self.__landform_board)
		pass
		print()


