from collections import deque
import random

def get_random_numbers():
    numbers = random.sample(range(1, 51), 3)
    return numbers


lst=[]
for i in range(5):
    random.seed(i)
    lst.append(get_random_numbers())

print(lst)

print("디폴트 정렬(1순위로 첫항 2순위로 둘째항 3순위로 셋째항을 기준으로 크기 정렬)")
print(sorted(lst))

print("1순위 첫째항 크기 2순위 둘째항 크기역순 3순위 셋째항 역순 정렬)")

sorted_lst=sorted(lst,key=lambda x:(x[0],-x[1],-x[2]))
print(sorted_lst)

print("1순위 둘째항 크기 3순위 첫째항 역순 정렬)")

sorted_lst=sorted(lst,key=lambda x:(x[1],-x[0]))

print(sorted_lst)

#
# #배열을 정렬할때 1순위는 두번째요소 크기순, 2순위는 세번째요소(크기역순) 으로 정렬하기 연습
#
# def deepcopy(arr):
#     temp=[]
#     for i in arr:
#         temp.append(i)
#     return temp
#
# def BFS(board,start,goal):
#     global d,visit,ans
#     d.append(start)
#     dr=[1,0,-1,0]
#     dc=[0,1,0,-1]
#
#     visit[start[0]][start[1]] = 1
#     while d:
#         r,c=d.popleft()
#         for i in range(4):
#             nr=r+dr[i]
#             nc=c+dc[i]
#             if 0<=nr<4 and 0<=nc<6 and  not visit[nr][nc] and board[nr][nc]==1:
#                 d.append([nr,nc])
#                 visit[nr][nc]=1
#                 foot_print[nr][nc]=[r,c]
#             if [nr,nc]==goal:
#                 print(d)
#                 return
#
#
# d=deque()
# ans=[]
# board=[[1,0,1,1,1,1],
#        [1,0,1,0,1,0],
#        [1,0,1,0,1,1],
#        [1,1,1,0,1,1]]
#
# foot_print=[[[9,9] for i in range(len(board[0]))] for i in range(len(board))]
# visit=[[0 for i in range(len(board[0]))] for i in range(len(board))]
# start = [0,0]
# end = [3,5]
#
# BFS(board,start,end)
#
# for i in visit:
#     print(i)
#
# print(d)
# for i in foot_print:
#     print(i)
#
#
# r,c=end
#
# ans=[end]
# while True:
#     ans.append(foot_print[r][c])
#     r,c=foot_print[r][c]
#     if [r,c]==start:
#         break
# print("foot print")
# print(list(reversed(ans)))
#
#
#


#
# def deepcopy(arr):
#     t=[]
#     for i in arr:
#         t.append(i)
#     return  t
#
#
# def permute(goal, cnt, lst, stack=[]):
#     global perm, visit
#
#     if goal == cnt:
#         perm.append(deepcopy(stack))
#         return
#
#     for i in range(len(lst)):
#         if not visit[i]:
#             visit[i] = 1
#             stack.append(lst[i])
#             permute(goal, cnt + 1, lst, stack)
#             stack.pop()
#
#             visit[i] = 0
#
#
# def combi(goal, cnt, lst, idx,stack=[]):
#     global comb, visit
#
#     if goal == cnt:
#         comb.append(deepcopy(stack))
#         return
#
#     for i in range(idx,len(lst)):
#         if not visit[i]:
#             visit[i] = 1
#             stack.append(lst[i])
#             combi(goal, cnt + 1, lst,i, stack)
#             stack.pop()
#
#             visit[i] = 0
#
#
#
#
#
#
#
# perm=[]
# comb=[]
# lst=[1,2,3,4,5]
# visit=[0 for i in range(len(lst))]
#
# permute(2,0,lst)
# combi(2,0,lst,0)
#
# print(perm)
# print(comb)