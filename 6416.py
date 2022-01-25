import sys
input = sys.stdin.readline

"""
dict을 key=간선의 도착 노드, val= 간선의 출발노드
"""

if __name__ == '__main__':


    toggle=True
    toggle2=True
    is_tree=True
    k=1
    while True:
        graph = dict()
        while True :
            # temp = list(map(int, input().split()))
            temp=[int(i) for i in input().rstrip().split()]
            while len(temp)>0:
                s=temp.pop(0)
                e=temp.pop(0)
                if s<0 and e<0:
                    toggle=False
                    toggle2=False
                    break
                if s==0 and e==0:
                    toggle2=False
                    break
                if e not in graph:
                    graph[e]=[]
                graph[e].append(s)
            if toggle2==False:
                break
        z=set()

        print(set().union(set(i) for i in graph.values()]))
        for key in graph:
            if len(graph[key])!=1:
                is_tree=False
                break
            idx=graph[key][0]
            if idx in graph and graph[idx][0]==key:
                is_tree=False
                break

        if toggle==False:
            break

        if is_tree:
            print(f"Case {k} is a tree.")
        else:
            print(f"Case {k} is not a tree.")
        k+=1
        toggle2=True
        is_tree=True

