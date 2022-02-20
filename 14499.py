import sys
input = sys.stdin.readline


"""
처음 시작할때 주사위의 방향을 알려줌.
이 정보를 기준으로 가상의 주사위를 같이 굴리면서 값을 갱신시켜준다.
주사위는 1차원배열로도 구현이 가능하나, 이해를 위해 2차원 배열로 선언.


주사위를 굴려서 도달한 좌표가 
맵 밖에갈 경우 -1을 리턴함으로써 출력여부를 판단
"""




if __name__ == '__main__':
    cube=[[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]]
    board=[]
    n,m,y,x,k=[int(i) for i in input().split()]
    for i in range(n):
        temp=[int(i) for i in input().split()]
        board.append(temp)
    moves=[int(i) for i in input().split()]

    def roll(dir):
        global x,y
        if dir==1:       #동쪽방향으로 굴리기
            if x+1<m:
                t = cube[1][2]
                cube[1][2] = cube[1][1]
                cube[1][1] = cube[1][0]
                cube[1][0] = cube[3][1]
                cube[3][1] = t

                if board[y][x+1]==0:            #이동한 칸이 0일경우
                    board[y][x+1]=cube[3][1]
                else:                           #이동한 칸이 0이 아닐경우
                    cube[3][1]=board[y][x+1]
                    board[y][x+1]=0
                x+=1
            else:
                return -1
            return cube[1][1]

        elif dir==2:      #서쪽방향으로 굴리기
            if x - 1 >= 0:
                t = cube[1][0]
                cube[1][0] = cube[1][1]
                cube[1][1] = cube[1][2]
                cube[1][2] = cube[3][1]
                cube[3][1] = t


                if board[y][x-1]==0:            #이동한 칸이 0일경우
                    board[y][x-1]=cube[3][1]
                else:                           #이동한 칸이 0이 아닐경우
                    cube[3][1]=board[y][x-1]
                    board[y][x-1]=0
                x-=1
            else:
                return -1
            return cube[1][1]

        elif dir==3:      #북쪽방향으로 굴리기
            if y - 1 >= 0:
                t=cube[0][1]
                for i in range(3):
                    cube[i][1]=cube[i+1][1]
                cube[-1][1]=t

                if board[y-1][x]==0:            #이동한 칸이 0일경우
                    board[y-1][x]=cube[3][1]
                else:                           #이동한 칸이 0이 아닐경우
                    cube[3][1]=board[y-1][x]
                    board[y-1][x]=0
                y-=1
            else:
                return -1
            return cube[1][1]

        elif dir==4:      #남쪽방향으로 굴리기
            if y+1<n:
                t=cube[-1][1]
                for i in range(3,0,-1):
                    cube[i][1]=cube[i-1][1]
                cube[0][1]=t

                if board[y+1][x]==0:            #이동한 칸이 0일경우
                    board[y+1][x]=cube[3][1]
                else:                           #이동한 칸이 0이 아닐경우
                    cube[3][1]=board[y+1][x]
                    board[y+1][x]=0
                y+=1
            else:
                return -1
            return cube[1][1]

    for i in moves:
        ans=roll(i)
        if ans!=-1:
            print(ans)