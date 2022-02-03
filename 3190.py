import sys

input = sys.stdin.readline
"""
뱀의 머리는 맨위 맨좌측 에서 시작 우방향
사과를 먹는게 목표가 아님,
사과는 그저 뱀의 몸통이 길어지는걸 표현
게임 종료 조건은 머리가 벽에 닿거나, 자신과 닿을경우



뱀의 몸통 역할을 하는 snake는 철저히 뱀의 몸역할만 수행.
보드를 칠하는건 다른 변수를 사용한다.
사과를 먹을 경우 머리만 하나더 추가되는거니 snake와 보드에만 값을 추가

"""

if __name__ == '__main__':
    def Simul():
        global  total_time
        dir=[[0,1],[1,0],[0,-1],[-1,0]]      #우회전시 idx+1 좌회전시 idx-1
        dir_idx=0
        snake=[[1,1]]                            #뱀의 몸이 위치한 좌표의 모음
        board[1][1]=4
        y=1
        x=1
        while True:
            total_time+=1
            pos_y=y + dir[(dir_idx)%4][0]   #다음에 이동할 위치
            pos_x=x + dir[(dir_idx)%4][1]
            if board[pos_y][pos_x]==1 or board[pos_y][pos_x]==4:              #종료조건
                print(total_time)
                break
            elif board[pos_y][pos_x]==2:             #사과 먹을경우
                board[pos_y][pos_x]=4
                snake.append([pos_y,pos_x])
            else:
                board[pos_y][pos_x] = 4
                snake.append([pos_y, pos_x])
                t = snake.pop(0)
                board[t[0]][t[1]] = 0


            if len(time_table)!=0 and total_time==time_table[0][0]:    #주어진 시간초에 방향 변경
                _,d=time_table.pop(0)
                if d=="D":      #오른쪽변경
                    dir_idx+=1
                elif d=="L":    #왼쪽변경
                    dir_idx-=1
            y = pos_y
            x = pos_x



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