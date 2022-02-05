import sys
input = sys.stdin.readline
"""
단순 구현
"""

if __name__ == '__main__':
    def Simul():
        global  d,r,c
        ans=0
        go_1=False
        while True: #1
            if board[r][c]==0:
                board[r][c]=2
                ans+=1
            for _ in range(4): #2
                y,x=dir[(d-1)%4]
                if board[r+y][c+x]==0:  #a
                    d-=1
                    r=r+y
                    c=c+x
                    go_1=True
                    break
                elif board[r+y][c+x]!=0:  #b
                    d-=1
                    continue
            if go_1:
                go_1=False
                continue
            if board[r+dir[(d+2)%4][0]][c+dir[(d+2)%4][1]]==2:
                r+=dir[(d+2)%4][0]
                c+=dir[(d+2)%4][1]
            else:
                print(ans)
                break

    n,m=[int(i) for i in input().split()]
    r,c,d=[int(i) for i in input().split()]
    board=[]
    dir =[[-1,0],[0,1],[1,0],[0,-1]]

    for i in range(n):
        temp=[int(i) for i in input().split()]
        board.append(temp)

    Simul()
