import sys

input = sys.stdin.readline

from itertools import product

import copy

"""
1~4 까지 경우의수
x
1~2까지 경우의수
x
1~4까지 경우의수
x
1~4까지 경우의수
가 나와서
1111~4244까지 나올수있게끔 해야됨
-> 곱집합(product)사용하여 브루트포스

배열안의 엘리먼트들을 언패킹 할때 *오퍼레이터를 사용한다.

--------------------------------------------------------
cctv2~5는 cctv1을 이용해서 만들 수 있다.



"""

def show(board):
    for i in board:
        print(i)
    print("--------------------")
def Simul(board, data):
    # cctv의 종류와 주어진 방향에 맞춰, 전개.
    global n, m
    lst, dir = data
    cctv, r, c = lst
    temp = [-1, 0, 1, 2, 3, 4, 5]
    if cctv == 1:
        while -1<r < n and -1< c < m:
            if dir == 0:
                nc = c + 1
                if nc < m and board[r][nc] in temp:
                    if board[r][nc] == 0:
                        board[r][nc] = -1
                    c = nc
                else:
                    break
            elif dir == 1:
                nr = r + 1
                if nr<n and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            elif dir == 2:
                nc = c - 1
                if nc > -1 and board[r][nc] in temp:
                    if board[r][nc] == 0:
                        board[r][nc] = -1
                    c=nc
                else:
                    break
            elif dir == 3:
                nr = r - 1
                if nr>-1 and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
    elif cctv==2:
        if dir == 0:
            c1,c2=c,c
            while -1<c1:
                nc1 = c1 - 1
                if nc1 > -1 and board[r][nc1] in temp:
                    if board[r][nc1] == 0:
                        board[r][nc1] = -1
                    c1 = nc1
                else:
                    break
            while c2 < m:
                nc2 = c2 + 1
                if nc2 < m and board[r][nc2] in temp:
                    if board[r][nc2] == 0:
                        board[r][nc2] = -1
                    c2 = nc2
                else:
                    break
        elif dir==1:
            r1,r2=r,r
            while -1<r1:
                nr1 = r1 - 1
                if nr1 > -1 and board[nr1][c] in temp:
                    if board[nr1][c] == 0:
                        board[nr1][c] = -1
                    r1 = nr1
                else:
                    break
            while r2 < n:
                nr2 = r2 + 1
                if nr2 < n and board[nr2][c] in temp:
                    if board[nr2][c] == 0:
                        board[nr2][c] = -1
                    r2 = nr2
                else:
                    break

    elif cctv == 3:
        pr=r
        if dir==0:      #up right
            while r>-1:
                nr=r-1
                if nr>-1 and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c<m:
                nc=c+1
                if nc<m and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break

        elif dir==1:    #right down
            while r<n:
                nr=r+1
                if nr<n and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c<m:
                nc=c+1
                if nc<m and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
        elif dir==2:    #down left
            while r<n:
                nr=r+1
                if nr<n and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c>-1:
                nc=c-1
                if nc>-1 and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
        elif dir==3:    #left up
            while r>-1:
                nr=r-1
                if nr>-1 and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c>-1:
                nc=c-1
                if nc>-1 and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break

    elif cctv == 4:
        pr=r
        if dir==0:          #u l r
            while r>-1:
                nr=r-1
                if nr>-1 and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c>-1:
                nc=c-1
                if nc>-1 and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
            while c<m:
                nc=c+1
                if nc<m and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
        elif dir==1:                #u d r
            while r>-1:
                nr=r-1
                if nr>-1 and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while r<n:
                nr=r+1
                if nr<n and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c<m:
                nc=c+1
                if nc<m and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break

        elif dir==2:              # d l r
            while r<n:
                nr=r+1
                if nr<n and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c>-1:
                nc=c-1
                if nc>-1 and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
            while c<m:
                nc=c+1
                if nc<m and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
        elif dir==3:              # u d l
            while r>-1:
                nr=r-1
                if nr>-1 and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while r<n:
                nr=r+1
                if nr<n and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c>-1:
                nc=c-1
                if nc>-1 and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
    elif cctv==5:
        pr=r
        if dir==0:
            while r>-1:
                nr=r-1
                if nr>-1 and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while r<n:
                nr=r+1
                if nr<n and board[nr][c] in temp:
                    if board[nr][c]==0:
                        board[nr][c]=-1
                    r=nr
                else:
                    break
            while c>-1:
                nc=c-1
                if nc>-1 and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break
            while c<m:
                nc=c+1
                if nc<m and board[pr][nc] in temp:
                    if board[pr][nc]==0:
                        board[pr][nc]=-1
                    c=nc
                else:
                    break

    return board


def Get_blind(board):
    cnt = 0
    for i in board:
        for j in i:
            if j == 0:
                cnt += 1
    return cnt


if __name__ == '__main__':
    cctv1 = [0, 1, 2, 3]  # cctv가 4방향이 전부 다를경우 사용(1,3,4)
    cctv2 = [0, 1]  # cctv가 2방향만 다를경우 사용(2)
    cctv3 = [0]  # cctv가 한방향만 가질경우(5)
    Min = sys.maxsize
    dirs_of_cctvs = []
    cctvs = []
    n, m = [int(i) for i in input().split()]
    board = []
    for i in range(n):
        temp = [int(i) for i in input().split()]
        board.append(temp)
        for j in range(m):
            if temp[j] == 1 or temp[j] == 3 or temp[j] == 4:
                dirs_of_cctvs.append(cctv1)
                cctvs.append([temp[j], i, j])
            elif temp[j] == 2:
                dirs_of_cctvs.append(cctv2)
                cctvs.append([temp[j], i, j])
            elif temp[j] == 5:
                dirs_of_cctvs.append(cctv3)
                cctvs.append([temp[j], i, j])

    for dir in list(product(*dirs_of_cctvs)):  # cctv 방향의 모든 경우의수
        cctv_datas = list(zip(cctvs, dir))  # 각 cctv의 방향정보를 해당 cctv의 종류와 좌표데이터에 통합
        c_board = copy.deepcopy(board)  # c_board=copied_board
        for data in cctv_datas:
            c_board = Simul(c_board, data)
        cnt = Get_blind(c_board)
        # show(c_board)
        if cnt < Min:
            Min = cnt

    print(Min)
