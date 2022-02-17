import sys
from collections import deque
input = sys.stdin.readline


"""
보드는 1,1~ n,n이다.
행과열이 각각 이어짐 -> mod연산


처음에는 시간초과가 발생하였음 
원인은 38번 라인에 "not in" 구문의 사용.

해결:
보드와 똑같은 크기의 배열을 만든뒤, 구름이 사라지는 곳의 위치를 1 로 변경. 이후 맵핑 

"""

def Rain(cmd):
    global n,m,board
    def Water_copy(lst):           #4
        for y,x in lst:
            t=0
            if y-1>=0 :
                if x-1>=0 and board[y-1][x-1]!=0:
                    t+=1
                if x+1<n and board[y-1][x+1]!=0:
                    t+=1
            if y+1<n:
                if x-1>=0 and board[y+1][x-1]!=0:
                    t+=1
                if x+1<n and board[y+1][x+1]!=0:
                    t+=1
            board[y][x]+=t

    def Count_water():
        for i in range(n):
            for j in range(n):
                if board[i][j]>=2:
                    if Wind[i][j]==0:# 5,  구름이 사라진 칸(물이 모여야되는 칸)에 속한 좌표를 제외하고 r_cloud 갱신
                        board[i][j]-=2
                        r_clouds.append([i,j])

    dir=[[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
    r_clouds=deque([[n-1,0],[n-1,1],[n-2,0],[n-2,1]] )#비구름


    for d,s in cmd:
        w_inc=[]                            #water increase ,이동한 구름들이 사라질 좌표
        nr,nc=dir[d-1]
        nr=nr*s
        nc=nc*s
        Wind = [[0 for i in range(n)] for i in range(n)]
        while len(r_clouds)>0:              #1~3
            r,c=r_clouds.popleft()
            board[(r+nr)%n][(c+nc)%n]+=1
            w_inc.append([(r+nr)%n,(c+nc)%n])
            Wind[(r+nr)%n][(c+nc)%n]=1
        Water_copy(w_inc)                   #4
        Count_water()                       #5

def Get_ans():
    global board
    ans=0
    for i in board:
        for j in i:
            ans+=j
    return ans


if __name__ == '__main__':
    n,m = [int(i) for i in input().split()]
    board=[]
    for _ in range(n):
        temp=[int(i) for i in input().split()]
        board.append(temp)
    command=[]
    for _ in range(m):
        temp=[int(i) for i in input().split()]
        command.append(temp)

    Rain(command)
    print(Get_ans())


