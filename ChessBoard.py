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
		chess[row][col][chess_num] %棋盘_row_col_棋子id
	"""
	def __init__(self, village ,village_score, chess_list, gradiant_board , landform_board, row = 29, col = 33 ):
		self.__row = row
		self.__col = col
		# self.chess = [[[] for y in range(col)] for x in range(row)]  	 #list 生成棋子初始为空
		# 初始化村庄位置、分值
		self.__village = village
		self.__chess_list = chess_list
		self.__gradiant_board = gradiant_board	  #初始化坡度为开阔地
		self.__landform_board = landform_board     #初始化地形为开阔地
		self.__village_score = village_score
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
	def Init_Chess(self,chess_count,chess):
		for i in range(chess_count):
			self.__chess_list[chess[i][0]][chess[i][1]].append(chess[i][2])
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


	def Judge_Chess(self,position):
		position_x = position[0]
		position_y = position[1]
		if position_x >= 0 and position_x < self.__row and position_y >= 0 and position_y < self.__col:
			return True
		else:
			return False

	#删除棋子
	def Remove_One_Chess(self,chess):
		position = []
		position.append(chess[0])# (x
		position.append(chess[1]) # y)
		if self.Judge_Chess(position):
			self.__chess_list[chess[0]][chess[1]].remove(chess[2])

	#增加棋子
	def Add_One_Chess(self,chess):
		position = []
		position.append(chess[0])# (x
		position.append(chess[1]) # y)
		if self.Judge_Chess(position):
			self.__chess_list[chess[0]][chess[1]].append(chess[2])

	#获取棋盘信息
	def Get_All_Info(self):
		return self.__village, self.__chess_list, self.__landform_board, self.__gradiant_board

	def Get_Village(self):
		return self.__village

	def Get_Position_Chess_List(self):
		return self.__chess_list

	def Get_Landform(self):
		return self.__landform_board

	def Get_Gradiant(self):
		return self.__gradiant_board

	#移动棋子: parameter_format:(x1,y1,chess_id) -> (x2,y2,chess_id)
    #1.判断（x2,y2) 合法性；2.判断（x2,y2)是否在其周围6格
	def Move_Chess(self,from_chess,to_chess):
		if self.Judge_Chess(to_chess):
			#even row：
			if from_chess[0]%2 == 0:
				dir_x = [-1,-1,1,1,0,0]
				dir_y = [0,1,0,1,-1,1]
				for x,y in zip(dir_x,dir_y):
					temp_x = from_chess[0]
					temp_y =  from_chess[1]
					if temp_x + x == to_chess[0] and temp_y + y == to_chess[1]:
						self.Add_One_Chess(to_chess)
						self.Remove_One_Chess(from_chess)
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
						self.Add_One_Chess(to_chess)
						self.Remove_One_Chess(from_chess)
						return True
				return False
		else:
			return False

	#移动到左上角格子 : paramaters: {"x:x_value","y:y_value"}
	def Move_Left_Top(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.Judge_Chess(origin_pos['x']-1,origin_pos['y']):
				position = []
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False
		else:
			if self.Judge_Chess(origin_pos['x']-1,origin_pos['y']-1):
				position = []
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']-1) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False

	#移动到右上角格子
	def Move_Right_Top(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.Judge_Chess(origin_pos['x']-1,origin_pos['y']+1):
				position = []
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']+1) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False
		else:
			if self.Judge_Chess(origin_pos['x']-1,origin_pos['y']):
				position = []
				position.append(origin_pos['x']-1)# (x
				position.append(origin_pos['y']) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False
	#左下移
	def Move_Left_Bottom(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.Judge_Chess(origin_pos['x']+1,origin_pos['y']):
				position = []
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False
		else:
			if self.Judge_Chess(origin_pos['x']+1,origin_pos['y']-1):
				position = []
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']-1) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False

	#右下移
	def Move_Right_Bottom(self,origin_pos):
		if origin_pos['x']%2 == 0:
			if self.Judge_Chess(origin_pos['x']+1,origin_pos['y']+1):
				position = []
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']+1) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False
		else:
			if self.Judge_Chess(origin_pos['x']+1,origin_pos['y']):
				position = []
				position.append(origin_pos['x']+1)# (x
				position.append(origin_pos['y']) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
			else:
				return False

	#左移动
	def Move_Left(self,origin_pos):
		if self.Judge_Chess(origin_pos['x'],origin_pos['y']-1):
				position = []
				position.append(origin_pos['x'])# (x
				position.append(origin_pos['y']-1) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
		else:
			return False

	def Move_Right(self,origin_pos):
		if self.Judge_Chess(origin_pos['x'],origin_pos['y']+1):
				position = []
				position.append(origin_pos['x'])# (x
				position.append(origin_pos['y']+1) # y)
				self.Add_One_Chess(position)

				position2 = []
				position2.append(origin_pos['x'])# (x
				position2.append(origin_pos['y']) # y)
				self.Remove_One_Chess(position2)
		else:
			return False


	#村庄占领状态改变
	def Change_State_of_Village(self, Id, new_state):
		self.__village[Id][2] = new_state

	def Get_Village_State(self, Id):
		return self.__village[Id][2]

	def Get_Village_Score(self, Id):
		return self.__village_score[Id]

	def Get_Village_Count(self):
		return len(self.__village)

	def chess_is_in(self,chess_id):
		if chess_id in self.__chess_list:
			return True
		else:
			return False

	def Debug(self):
		print(self.__chess_list)
		print(self.__gradiant_board)
		print(self.__landform_board)
		pass
		print()


