import sys
input = sys.stdin.readline

"""
input:
3
-1 0 1
2


tree : {-1: [0], 0: [1], 1: []}

output:1
위와 같은 경우, 빈배열의 형태로 딕셔너리가 존재하는경우도 포함하여 계산해야됨.
"""



if __name__ == '__main__':
    n=int(input())
    graph=dict()
    ans=[]

    temp=[int(i) for i in input().split()]

    for idx,val in enumerate(temp):
        if val not in graph:
            graph[val]=[]
        graph[val].append(idx)

    remove_idx=int(input())

    graph[temp[remove_idx]].remove(remove_idx)

    def Search(key):
        cnt=0
        for i in graph[key]:
            if i not in graph or len(graph[i])==0:
               cnt+=1
            else:
                cnt+=Search(i)
        return cnt

    print(Search(-1))

