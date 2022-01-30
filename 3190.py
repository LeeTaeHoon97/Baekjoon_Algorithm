import sys
from itertools import permutations
import copy

input = sys.stdin.readline
"""
뱀의 머리는 맨위 맨좌측 에서 시작 우방향
사과를 먹는게 목표가 아님,
사과는 그저 뱀의 몸통이 길어지는걸 표현
게임 종료 조건은 머리가 벽에 닿거나, 자신과 닿을경우
"""

if __name__ == '__main__':
    def show():
        print(total_time)
        for i in board:
            print(i)
    def Simul():
        global  total_time
        pos_x=1
        pos_y=1
        dir=[[0,1],[1,0],[0,-1],[-1,0]]      #우회전시 idx+1 좌회전시 idx-1
        dir_idx=0
        snake=[[1,1]]                            #뱀의 몸이 위치한 좌표의 모음
        temp=[1,1]
        is_Eat=False
        while True:
            total_time+=1
            t=snake[-1]
            print("t",t)
            if board[t[0]][t[1]]==1:              #종료조건
                print(total_time)
                break
            elif board[t[0]][t[1]]==2 or board[t[0]][t[1]]==4:             #사과 먹을경우
                is_Eat=True
            if len(time_table)!=0 and total_time==time_table[0][0]:    #주어진 시간초에 방향 변경
                _,d=time_table.pop(0)
                if d=="D":      #오른쪽변경
                    dir_idx+=1
                elif d=="L":    #왼쪽변경
                    dir_idx-=1
            board[t[0]][t[1]]=4
            pos_y=pos_y + dir[(dir_idx)%4][0]   #다음에 이동할 위치
            pos_x=pos_x + dir[(dir_idx)%4][1]
            snake.append([pos_y, pos_x])
            if is_Eat:
                is_Eat=False
                print("eat",snake)
                show()
                continue
            t=snake.pop(0)

            print(snake)

            show()
            board[t[0]][t[1]]=0



    n=int(input())  #보드판 크기
    board=[[1 for i in range(n+2)]]
    board.extend([[1]+[0 for i in range(n)]+[1]for _ in range(n)])
    board.append([1 for i in range(n+2)])
    k=int(input())  #사과 수
    pos_apple=[]    #사과 위치
    total_time=0    #게임 진행 시간
    time_table=[]

    for _ in range(k):
        row,col = [int(i) for i in input().split()]
        board[row][col]=2          #사과의위치는 좌표상에서 2로 표시

    l=int(input()) # 뱀의 방향전환 횟수
    for _ in range(l):
        sec,dir = [i for i in input().split()]
        sec=int(sec)
        time_table.append([sec,dir])
    Simul()