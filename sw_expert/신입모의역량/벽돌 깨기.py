# 블록은 가장 위의것부터 선택가능 선택된 경우 적혀있는 숫자 반경도 같이 터짐
# 블록이 터지고나면 빈 공간은 한칸씩 내려가 적재됨
# N개의구슬을 던져서 최대 벽돌 파괴를 알아내야함

#최대 경우의수 : 12 * 12 * 12 * 12 = 20736
#중복순열을 구하여 브루트 포스

def deepcopy(arr):
    temp=[]
    for i in arr:
        temp.append(i)
    return temp
def deepcopy2(arr):

    tt=[]
    for i in arr:
        temp = []
        for j in i:
            temp.append(j)
        tt.append(temp)

    return tt

def permute(goal,cnt,lst,stack=[]):
    global perm
    if goal==cnt:
        perm.append(deepcopy(stack))
        return
    for i in range(len(lst)):
        stack.append(lst[i])
        permute(goal,cnt+1,lst,stack)
        stack.pop()

def destroy(r,c):       #p = 블록의 폭파 반경    1~9
    global board,W,H
    p=board[r][c]
    if p!=0:      #현재 블록 파괴
        board[r][c]=0

    for i in range(1,p):    # p >1 인경우
        dx=[i,0,-i,0]
        dy=[0,i,0,-i]
        for j in range(4):
            nc=c+dx[j]
            nr=r+dy[j]
            if nc>=0 and nc<W and nr>=0 and nr<H:
                destroy(nr,nc)

def count_block():
    global board,ans
    cnt=0
    for i in board:
        for j in i:
            if j!=0:
                cnt+=1
    ans=min(cnt,ans)


def refresh():
    global W,H,board

    for c in range(W):
        t=[]
        for r in range(H-1,-1,-1):
            while r<H-1 and board[r+1][c]==0:
                board[r+1][c]=board[r][c]
                board[r][c] = 0
                r+=1


def simul(c):        #c = 부서질 열의 위치
    global board,H

    for r in range(H):
        if board[r][c]!=0:          #처음 만나는 블록
            destroy(r,c)
            refresh()
            break

T = int(input())

for p_num in range(T):
    N,W,H=[int(i) for i in input().split()]
    board=[]
    lst = [i  for i in range(W)]
    perm = []
    ans=12*15+1
    for _ in range(H):
        board.append([int(i) for i in input().split()])

    board_c=deepcopy2(board)
    permute(N,0,lst)
    for p in perm:

        for i in p:
            simul(i)
            count_block()

        board=deepcopy2(board_c)

    print(f"#{p_num+1} {ans}")



