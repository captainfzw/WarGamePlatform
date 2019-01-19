class Chess_Board(object):
	"""
	棋盘类
	Args:
		row % 行数，默认29
		col % 列数，默认33
		
		village_count 				%村庄数量
		village[id][2]     %村庄_id位置:Village[id][0]->行；Village[id][1]->列
		village_state[id] 	%村状态： Village_State[] = False -> 未占领 ； Village_State[] = x ——>被x那方 占领
		
		village  			%村庄信息三元组（（x1,y1,state) ...(xn,yn,state)）
 		gradiant_board[row][col]   %棋盘_row_col:坡度 
		landform_board[row][col]   %棋盘_row_col:地形
		chess[row][col][chess_num] %棋盘_row_col_棋子id 
	"""
	def __init__(self, village, chess, gradiant_board , landform_board, row = 29, col = 33 ):
		self.__row = row
		self.__col = col
		# self.__chess = [[[] for y in range(col)] for x in range(row)]  	 #list 生成棋子初始为空		
		self.__village = village
		self.chess = chess 
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

	#初始化棋子
	# def Init_Chess(self,chess_count,chess):
	# 	for i in range(chess_count):
	# 		self.__chess[chess[i][0]][chess[i][1]].append(chess[i][2])
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

	#删除棋子
	def Remove_One_Chess(self,chess):
		self.__chess[chess[0]][chess[1]].remove(chess[2])

	#增加棋子
	def Add_One_Chess(self,chess):
		self.__chess[chess[0]][chess[1]].append(chess[2])

	#获取棋盘信息
	def Get_All_Info(self):
		return self.__village, self.__chess, self.__landform_board, self.__gradiant_board

	def Get_Village(self):
		return self.__village

	def Get_Chess(self):
		return self.__chess

	def Get_Landform(self):
		return self.__landform_board

	def Get_Gradiant(self):
		return self.__gradiant_board
	
	#移动棋子
	def Move_Chess(self,from_chess,to_chess):
		self.Add_One_Chess(to_chess)
		self.Remove_One_Chess(from_chess)

	#村庄占领状态改变 
	def Change_State_of_Village(self, Id, new_state):
		self.village[Id][2] = new_state

	def Debug(self):
		print(self.__chess)
		print(self.__gradiant_board)
		print(self.__landform_board)
		pass
		print()


	