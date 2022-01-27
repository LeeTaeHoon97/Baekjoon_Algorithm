import sys

input = sys.stdin.readline
from collections import defaultdict

"""

트리의조건
1. 사이클이 없어야됨    => 탐색알고리즘을 통해 갔던곳을 재방문할경우 사이클이 성립된다는걸 뜻함
2. 노드의 부모는 오직 하나 (1번의 조건에 해당)
3. 루트는 오직 하나    => 루트 노드의 개수(a) = 전체 노드의 수 - child 노드의 수 , 이때 a의 값이 1이 나와야 함
4. 빈 리스트도 트리
5. 고립된 노드가 없어야 함 (3번의 조건에 해당)

"""

if __name__ == '__main__':

    def dfs(start):
        stack = [start]
        visit = []
        while stack:
            node = stack.pop()
            if node in visit:
                return False
            visit.append(node)
            if node in graph:
                stack.extend(graph[node])
        return True

    k = 0
    while True:
        graph = defaultdict(list)
        nodes = set()
        child = set()
        k += 1
        toggle=True
        is_tree=True
        while toggle:
            lst=[int(i) for i in input().split()]
            for i in range(0,len(lst),2):
                if lst[i]==0 and lst[i+1]==0:
                    toggle=False
                if lst[i]==-1 and lst[i+1]==-1:
                    sys.exit()
                graph[lst[i]].append(lst[i+1])
                nodes.add(lst[i])
                nodes.add(lst[i+1])
                child.add(lst[i+1])


        root = nodes - child

        #트리가 비었을경우
        if nodes=={0} and child=={0}:
            print(f'Case {k} is a tree.')
            continue
        # 루트가 두개 이상일 경우
        if len(root) != 1:
            print(f'Case {k} is not a tree.')
            continue

        #트리가 사이클이 생길경우 트리가 아니다.
        if not dfs(root.pop()):
            is_tree=False
        if is_tree:
            print(f'Case {k} is a tree.')
        else:
            print(f'Case {k} is not a tree.')
