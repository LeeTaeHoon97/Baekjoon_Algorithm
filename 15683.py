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


def See(r, c, dir,board):
    temp = [-1, 0, 1, 2, 3, 4, 5]
    if dir == "up":
        while -1 < r:
            nr = r - 1
            if nr > -1 and board[nr][c] in temp:
                if board[nr][c] == 0:
                    board[nr][c] = -1
                r = nr
            else:
                break
    elif dir == "right":
        while c < m:
            nc = c + 1
            if nc < m and board[r][nc] in temp:
                if board[r][nc] == 0:
                    board[r][nc] = -1
                c = nc
            else:
                break
    elif dir == "down":
        while r < n:
            nr = r + 1
            if nr < n and board[nr][c] in temp:
                if board[nr][c] == 0:
                    board[nr][c] = -1
                r = nr
            else:
                break
    elif dir == "left":
        while -1 < c:
            nc = c - 1
            if nc > -1 and board[r][nc] in temp:
                if board[r][nc] == 0:
                    board[r][nc] = -1
                c = nc
            else:
                break
    return board



def Simul(board, data):
    # cctv의 종류와 주어진 방향에 맞춰, 전개.
    global n, m
    lst, dir = data
    cctv, r, c = lst
    if cctv == 1:
        if dir==0:
            board=See(r,c,"right",board)
        elif dir==1:
            board=See(r,c,"down",board)
        elif dir==2:
            board=See(r,c,"left",board)
        elif dir==3:
            board=See(r,c,"up",board)
    elif cctv == 2:
        if dir == 0:
            board=See(r,c,"right",board)
            board=See(r,c,"left",board)

        elif dir == 1:
            board=See(r,c,"up",board)
            board=See(r,c,"down",board)


    elif cctv == 3:
        if dir == 0:  # up right
            board=See(r,c,"up",board)
            board=See(r,c,"right",board)

        elif dir == 1:  # right down
            board=See(r,c,"right",board)
            board=See(r,c,"down",board)

        elif dir == 2:  # down left
            board=See(r,c,"down",board)
            board=See(r,c,"left",board)

        elif dir == 3:  # left up
            board=See(r,c,"left",board)
            board=See(r,c,"up",board)


    elif cctv == 4:
        if dir == 0:  # u l r
            board=See(r,c,"up",board)
            board=See(r,c,"left",board)
            board=See(r,c,"right",board)

        elif dir == 1:  # u d r
            board=See(r,c,"up",board)
            board=See(r,c,"down",board)
            board=See(r,c,"right",board)

        elif dir == 2:  # d l r
            board=See(r,c,"down",board)
            board=See(r,c,"left",board)
            board=See(r,c,"right",board)

        elif dir == 3:  # u d l
            board=See(r,c,"up",board)
            board=See(r,c,"down",board)
            board=See(r,c,"left",board)

    elif cctv == 5:
        if dir == 0:
            board=See(r,c,"up",board)
            board=See(r,c,"down",board)
            board=See(r,c,"left",board)
            board=See(r,c,"right",board)


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
        if cnt < Min:
            Min = cnt

    print(Min)
