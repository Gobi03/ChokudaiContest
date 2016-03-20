def makelist(n, m):
	return [[0 for i in range(m)] for j in range(n)]

A = [0]*31

# input
for i in range(1, 31):
	A[i] = [0] + list(map(int, input().split()))


#--------------------------------------------------#
# 関数置き場
#--------------------------------------------------#

# True 返せばゲーム終了
def isAllZero():	
	for i in range(1, 31):
		for j in range(1, 31):
			if A[i][j] > 0:
				return False
	return True

# 座標が正規の範囲にあるか
def isSound(pair):
	y = pair[0]
	x = pair[1]
	return (y >= 1 and x >= 1 and y <= 30 and x <= 30)

# 割当て
def assign(a,b,c,d):
	res = []
	if isSound(a):
		res += [a]
	if isSound(b):
		res += [b]
	if isSound(c):
		res += [c]
	if isSound(d):
		res += [d]
	return res

# 壁際に向かう方向優先順で行ける座標返す
def nextCoord(y, x):
	res = []
	U = (y-1, x)
	D = (y+1, x)
	R = (y, x+1)
	L = (y, x-1)
	if y <= 15 and x <= 15:
		res = assign(D,R,U,L)
	elif y <= 15 and x > 15:
		res = assign(D,L,U,R)
	elif y > 15 and x <= 15:
		res = assign(U,R,D,L)
	else:
		res = assign(U,L,D,R)

	return res

# max値の座標返す
def maxCoord():
	res = (0, 0)
	MAX = 0
	for i in range(1, 31):
		for j in range(1, 31):
			if A[i][j] > MAX:
				MAX = A[i][j]
				res = (i, j)
	return res
#--------------------------------------------------#



while not isAllZero():
	# 始点決める
	start = maxCoord()
	sy = start[0]
	sx = start[1]

	print(sy, sx)
	A[sy][sx] -= 1

	# 次点ある限り進む
	flag = True
	while flag:
		nextlist = nextCoord(sy, sx)
		if len(nextlist) == 0: # 次点ない
			flag = False
		else:                  # 次点ある
			flag = False
			for yx in nextlist:
				ny = yx[0]
				nx = yx[1]
				if A[ny][nx] > 0: # 着地点見つけたら
					# turn process
					print(ny, nx)
					A[ny][nx] -= 1
					# prepare for next turn
					sy = ny
					sx = nx
					# end process
					flag = True
					break
