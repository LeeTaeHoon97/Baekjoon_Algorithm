import sys

input = sys.stdin.readline

from itertools import combinations

import copy

"""
처음에 입력받은 가로선을 추가
이후 가로선(가지)의 경우의수 구현
최소값 구현
만약 cnt가 0이나올경우 바로 stop
"""
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
def simul(branch):
    global Min
    return

if __name__ == '__main__':

    n,m,h=[int(i) for i in input().split()]
    Min=sys.maxsize
    branch_board=[[-1 for i in range(n)]]+[[-1]+[0 for _ in range(n-1)]for _ in range(h)]
    branch=[]    #입력된 가지
    for _ in range(m):
        y,x=[int(i) for i in input().split()]
        branch_board[y][x]=1
        branch.append([y,x])
    lst = []
    for i in range(h):
        for j in range(1,n):
            if not branch_board[i][j]:
                lst.append([i,j])

    print(lst)
    for i in branch_board:
        print(i)





    comb=[]
    combs=[]                        #결과적으로 combination이 저장될 리스트
    visit=[0 for i in range(len(lst))]

    # for i in range(1,len(lst)+1):
    #     combi(0, i, 0)
    #     combs.append(comb)
    #     comb=[]
    # for j in combs:
    #     for z in j:
    #         print(branch+list(z))