
def deepcopy(board):
    temp1=[]
    temp2=[]
    for i in board:
        for j in i:
            temp1.append(j)
        temp2.append(temp1)
        temp1=[]
    return temp2

def spread():
    global board,r,c
    nboard=deepcopy(board)
    #새 보드로 연산하고 한번에 이전보드값으로 옮김
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]

    for i in range(r):
        for j in range(c):
            if board[i][j]>4:
                spread_cnt=0
                for z in range(4):
                    nr=i+dr[z]
                    nc=j+dc[z]
                    if 0<=nr<r and 0<=nc<c and board[nr][nc]!=-1:        #이동 가능할경우
                        spread_cnt+=1
                        remain_dust=board[i][j]
                        nboard[nr][nc]+=remain_dust//5
                nboard[i][j]-=((remain_dust//5)*spread_cnt)

    board=deepcopy(nboard)
    del nboard


def operation(pos):
    global board,r,c
    anti_clock,clock=pos

    #anti clock side
    r1,c1=anti_clock
    for i in range(r1-1,0,-1):
        board[i][0]=board[i-1][0]
    for j in range(0,c-1):
        board[0][j]=board[0][j+1]
    for i in range(0,r1):
        board[i][c-1]=board[i+1][c-1]
    for j in range(c-1,1,-1):
        board[r1][j]=board[r1][j-1]
    board[r1][1]=0

    #clock side
    r2,c2=clock
    for i in range(r2+1,r-1):
        board[i][0]=board[i+1][0]
    for j in range(0,c-1):
        board[r-1][j]=board[r-1][j+1]
    for i in range(r-1,r2,-1):
        board[i][c-1]=board[i-1][c-1]
    for j in range(c-1,1,-1):
        board[r2][j]=board[r2][j-1]
    board[r2][1]=0


# def show(board):
#     for i in board:
#         print(i)
#     print('------------')

def get_device_pos():
    global board

    for i in range(r):
        for j in range(c):
            if board[i][j]==-1:
                return [[i,j],[i+1,j]]

def get_ans():
    global board
    cnt=0
    for i in board:
        for j in i:
            cnt+=j
    return cnt
r,c,t=[int(i) for i in  input().split()]
board=[]

for _ in range(r):
    board.append([int(i) for i in input().split()])


device_pos=get_device_pos()
for i in range(t):
    spread()
    operation(device_pos)

print(get_ans()+2)          #-1로 감소되는 부분 다시 셈