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



"""


def Simul(board, data):
    # cctv의 종류와 주어진 방향에 맞춰, 전개.
    global n, m
    lst, dir = data
    cctv, r, c = lst
    temp = [0, 1, 2, 3, 4, 5]
    if cctv == 1:
        while r < n and c < m:
            if dir == 0:
                nc = c + 1
                if nc < m and board[r][nc] in temp:
                    if board[r][c] == 0:
                        board[r][c] = -1
                    c = nc
            elif dir == 1:
                nr = r + 1
            elif dir == 2:
                nc = c - 1
            elif dir == 3:
                nr = r - 1
    return board


def Get_blind(board):
    cnt = 0
    for i in board:
        for j in i:
            if j == -1:
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
