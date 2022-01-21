import sys
from itertools import combinations
import copy

input = sys.stdin.readline


# 1) 궁수의 조합
# 2) 적 병력의 이동
# 3) 사거리에 따른 적 제거 (동일거리시 무조건 좌측우선)

def move_map(graph):  # 2)
    graph.pop()
    graph.insert(0, [0 for i in range(m)])
    return graph
def kill(soldier):  # 3)
    copied_graph
    cnt = 0
    temp=[]
    #각 병사가 쏠 최우선 좌표를 추출
    for i in soldier:
        lst = []
        for row in range(n):
            for col in range(m):
                if copied_graph[row][col]==1:
                    atk_range=abs(n-row)+abs(i-col)
                    if atk_range<=r:
                        lst.append([atk_range,row,col])
        lst.sort( key=lambda x:(x[0],x[2]))

        if lst:
            _,Row,Col=lst.pop(0)
            temp.append([Row,Col])

    for row,col in temp:
        if copied_graph[row][col]==1:
            copied_graph[row][col]=0
            cnt+=1
    return cnt


def simulation(soldier, graph):
    kill_num = 0
    global copied_graph
    copied_graph = copy.deepcopy(graph)

    for i in range(n + 1):
        kill_num += kill(soldier)
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
        ans = max(simulation(soldier, graph), ans)

    print(ans)
