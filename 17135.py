import sys
from itertools import combinations
import copy
from heapq import heappop, heappush

input = sys.stdin.readline


# 1) 궁수의 조합
# 2) 적 병력의 이동
# 3) 사거리에 따른 적 제거 (동일거리시 무조건 좌측우선)


def move_map(graph):  # 2)
    graph.pop()
    graph.insert(0, [0 for i in range(m)])
    return graph


def kill(soldier, Range):  # 3)
    arr = copied_graph
    remove_list = []
    attacked = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for archer_pos in soldier:
        pq = []  # [거리, x, y]를 우선순위 큐에 삽입
        lst = []
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if arr[i][j] == 1:
                    diff = abs(n - i) + abs(archer_pos - j)
                    if diff <= r:
                        lst.append([diff, j, i])

        lst.sort(key=lambda x: (x[0], x[1]))
        if lst:
            _, x, y = lst.pop(0)
            remove_list.append([y, x])

    for y, x in remove_list:
        if not attacked[y][x]:
            attacked[y][x] = True
            cnt += 1
            arr[y][x] = 0

    return cnt


def simulation(soldier, graph):
    kill_num = 0
    global copied_graph
    copied_graph = copy.deepcopy(graph)

    for i in range(n + 1):
        kill_num += kill(soldier, r)
        copied_graph = move_map(copied_graph)
    return kill_num


if __name__ == '__main__':
    global n, m, r
    n, m, r = [int(i) for i in input().split()]
    ans = 0
    graph = []
    for i in range(n):
        temp = [int(i) for i in input().split()]
        graph.append(temp)

    soldiers = combinations([i for i in range(m)], 3)  # 1)

    for soldier in soldiers:
        # print("-------------------------------")
        ans = max(simulation(soldier, graph), ans)

    print(ans)

# import sys
# from itertools import combinations
# import copy
# input=sys.stdin.readline
#
#
# #1) 궁수의 조합
# #2) 적 병력의 이동
# #3) 사거리에 따른 적 제거
#
#
# def move_map(graph):     #2)
#     graph.pop()
#     graph.insert(0,[0 for  i in range(m)])
#     return graph
#
# def kill(soldier,Range): #3)
#     kill_range=copied_graph[n-Range:]
#
#     corpse = set()
#     for i in soldier:
#         Min = n + m
#         min_r,min_c=[n,m]
#         for r in range(len(kill_range)-1,-1,-1):
#             if 1 not in kill_range[r]:
#                 continue
#             for c in range(m):
#                 if kill_range[r][c]==1:
#                     atk_range=abs(Range-r)+abs(i-c)
#                     if atk_range<=Range and atk_range<Min:       #솔져들은 새롭게 만들어진 맵 kill_range의 아랫줄에 있음
#                         min_r=r
#                         min_c=c
#                         Min=atk_range
#                     elif atk_range==Min:
#                         if c<min_c:
#                             min_r=r
#                             min_c=c
#         if min_r<n and min_c<m:
#                 corpse.add((min_r, min_c))
#
#     # print("병사:", soldier)
#     # print("시체:",corpse)
#     for r,c in corpse:
#         copied_graph[r+n-Range][c]=0
#     return len(corpse)
#
# def simulation(soldier,Range,graph):
#     kill_num=0
#     global copied_graph
#     copied_graph=copy.deepcopy(graph)
#     for i in range(m+1):
#         kill_num+=kill(soldier,Range)
#         copied_graph=move_map(copied_graph)
#     return kill_num
#
# if __name__ == '__main__':
#     global n,m,r
#     n,m,r=[int(i) for i in input().split()]
#     ans=0
#     graph=[]
#     for i in range(n):
#         temp=[int(i) for i in input().split()]
#         graph.append(temp)
#
#     soldiers=combinations([i for i in range(m)],3) #1)
#
#     for soldier in soldiers:
#         # print("-------------------------------")
#         ans=max(simulation(soldier,r,graph),ans)
#
#     print(ans)
