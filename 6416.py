import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict

"""
dict을 key=간선의 도착 노드, val= 간선의 출발노드
"""

# def dfs(start,graph):
#     stack=list(start)
#     visit=[]
#     while stack:
#         node = stack.pop()
#         if node in graph:
#             if node in visit:
#                 return False
#             visit.extend(graph[node])
#             stack.extend(graph[node])
#     return True


if __name__ == '__main__':
    def dfs(root):
        stack = [root]
        visited = set([root])
        while stack:
            node = stack.pop()
            if node in graph:
                for n in graph[node]:
                    if n in visited:
                        return False
                    stack.append(n)
                    visited.add(n)
        return True


    toggle = True
    # is_tree=True
    k = 0
    while toggle:
        graph = defaultdict(list)
        nodes = set()
        child = set()
        k += 1
        toggle2 = True
        while toggle2:
            # temp = list(map(int, input().split()))
            temp = [int(i) for i in input().split()]
            if len(temp) == 0:
                continue
            if temp[0] == -1 and temp[1] == -1:
                sys.exit(0)
            nodes.update(temp)
            for i in range(0, len(temp), 2):
                if temp[i] == 0 and temp[i + 1] == 0:
                    toggle2 = False
                    break
                if temp[i] not in graph:
                    graph[temp[i]] = []
                graph[temp[i]].append(temp[i + 1])
                child.add(temp[i + 1])
        if len(graph) == 0:
            print(f'Case {k} is a tree.')
            continue
            # is_tree=True
        root = nodes - child
        root.remove(0)
        # 루트가 두개이상일경우
        if len(root) != 1:
            print(f'Case {k} is not a tree.')
            continue

        # if not dfs(root,graph):
        #     is_tree=False

        print(f'Case {k} is a tree.' if dfs(root.pop()) else f'Case {k} is not a tree.')

