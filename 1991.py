import sys
input = sys.stdin.readline

#처음 트리클래스와 노드 클래스를 사용하려 풀려고 하였으나,
#입력으로 주는 정보가 key 와 value형식으로 전달한다는것에서
#딕셔너리를 사용하여 풀수 있어보여 딕셔너리를 가공함

if __name__ == '__main__':
    n=int(input())
    graph=dict()
    ans=[]
    for i in range(n):
        temp=[z for z in input().split()]
        if temp[0] not in graph:
            graph[temp[0]]=[]                   #공간이 2인 리스트를 만들어 left=0 , right=1로 대응
        for j in range(1,3):
            if temp[j]=='.':
                graph[temp[0]].append(-1)       #자식노드가 없다는걸 표현
            else:
                graph[temp[0]].append(temp[j])


    def preorder(key):
        visit = []
        visit.append(key)
        if graph[key][0] != -1: visit.extend(preorder(graph[key][0]))
        if graph[key][1] != -1: visit.extend(preorder(graph[key][1]))
        return visit
    def inorder(key):
        visit=[]
        if graph[key][0]!=-1:visit.extend(inorder(graph[key][0]))
        visit.append(key)
        if graph[key][1]!=-1:visit.extend(inorder(graph[key][1]))
        return visit
    def postorder(key):
        visit=[]
        if graph[key][0]!=-1:visit.extend(postorder(graph[key][0]))
        if graph[key][1]!=-1:visit.extend(postorder(graph[key][1]))
        visit.append(key)
        return visit
    ans.append(preorder('A'))
    ans.append(inorder('A'))
    ans.append(postorder('A'))

    for i in ans:
        print("".join(i))
