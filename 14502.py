import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline


"""
일단 보드판을 만듬.
보드판을 읽어오면서 빈칸의 위치,바이러스의 위치를 기억
빈칸의 위치의 조합을 구함
그 조합의 위치를 1로 변경해줬을경우
바이러스들을 시뮬레이션함
바이러스들의 이동이 멈추면, 남은 빈칸의 갯수를 구함
"""

if __name__ == '__main__':
    n,m=[int(i) for i in input().split()]
    empty_lst=[]
    virus_lst=[]
    board=[]
    Max=-1
    def bfs():
        q = deque()
        for i in virus_lst:
            q.append(i)

        while q:
            ny,nx=q.popleft()

            if ny > 0 and bboard[ny - 1][nx] == 0:
                bboard[ny - 1][nx] = 2
                q.append([ny - 1, nx])
            if ny<n-1 and bboard[ny+1][nx]==0:
                bboard[ny+1][nx]=2
                q.append([ny+1,nx])
            if nx>0 and bboard[ny][nx-1]==0:
                bboard[ny][nx-1]=2
                q.append([ny,nx-1])
            if nx<m-1 and bboard[ny][nx+1]==0:
                bboard[ny][nx+1]=2
                q.append([ny,nx+1])



    for i in range(n):
        temp=[int(i)for i in input().split()]
        for j in range(m):
            if temp[j]==0:
                empty_lst.append([i,j])
            elif temp[j]==2:
                virus_lst.append([i,j])
        board.append(temp)
    for walls in  list(combinations(empty_lst,3)):
        bboard = copy.deepcopy(board)
        for y,x in walls:
            bboard[y][x]=1
        bfs()
        cnt=0
        for i in bboard:
            for j in i:
                if j==0:
                    cnt+=1
        if cnt>Max:
            Max=cnt
    print(Max)
