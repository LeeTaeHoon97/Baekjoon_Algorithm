import sys

input = sys.stdin.readline

from itertools import combinations

import copy

"""
처음에 입력받은 가로선을 추가
이후 가로선(가지)의 경우의수 구현
최소값 구현
만약 cnt가 0이나올경우 바로 stop
----------------------------시간초과
첫번째 원인 : Min이 3개를 벗어나는 경우 -1처리해주지 않음
----------------------------시간초과
두번째 원인 : 경우의수를 구할때 전체 경우의수를 구해버림
----------------------------시간초과
세번째 원인 : 자체구현한 combination 알고리즘이 엄청난 시간을 소비함
"""
def show(board):
    for i in board:
        print(i)
    print("----------------")

def combi(idx,goal,cnt,stack=[]):
    global lst,visit,comb
    def make_arr(l):
        tmp=[]
        for i in l:
            tmp.append(i)
        return tmp
    if cnt==goal:
        comb.append(make_arr(stack))
        return

    for i in range(idx,len(lst)):
        if not visit[i]:
            visit[i]=1
            stack.append(lst[i])
            combi(i,goal,cnt+1,stack)
            stack.pop()
            visit[i]=0

def simul(branch,cnt):
    global Min
    if cnt>Min:
        return
    b_board=copy.deepcopy(branch_board)
    for temp in branch:
        if temp!=[]:
            y,x=temp
            b_board[y][x]=1

    # print(branch)
    # show(b_board)

    for start in range(1,n+1):
        end=start
        for y in range(1,h+1):
            if b_board[y][start-1]==1:
                start-=1
            elif b_board[y][start]==1:
                start+=1
        if end!=start:
            return
    if cnt<Min:
        Min=cnt
    return

if __name__ == '__main__':

    n,m,h=[int(i) for i in input().split()]
    Min=sys.maxsize
    branch_board=[[-1 for i in range(n)]]+[[-1]+[0 for _ in range(n-1)]+[-1]for _ in range(h)]
    branch=[]    #입력된 가지
    for _ in range(m):
        y,x=[int(i) for i in input().split()]
        branch.append([y,x])
        branch_board[y][x]=1
    if len(branch)==0:
        print('0')
    else:
        lst = []
        for i in range(1,h+1):
            for j in range(1,n):
                if not branch_board[i][j]:
                    lst.append([i,j])

        comb=[]
        combs=[]                        #결과적으로 combination이 저장될 리스트
        visit=[0 for i in range(len(lst))]

        for i in range(4):
            combi(0, i, 0)
            combs.append(comb)
            comb=[]
        for j in combs:
            for z in j:
                simul(branch+list(z),len(list(z)))
                if Min==0:
                    break
        if Min>3:
            print("-1")
        else:
            print(Min)

