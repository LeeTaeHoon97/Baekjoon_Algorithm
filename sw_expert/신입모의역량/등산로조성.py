

T=int(input())

def find_start_point(lst,N,_max):
    start_point=[]
    for i in range(N):
        for j in range(N):
            if lst[i][j]==_max:
                start_point.append([i,j])
                if len(start_point)==5:
                    return start_point
    return start_point

def DFS(map_lst,i,j,visit,IsUsingK,goal_lst):
    global ans,N,K

    goal_lst.append(map_lst[i][j])
    ans=max(ans,len(goal_lst))

    if not visit[i][j]:
        visit[i][j]=1
        if i-1 >= 0:                                    #up
            if map_lst[i - 1][j] < map_lst[i][j] and not visit[i-1][j]:
                DFS(map_lst, i - 1, j, visit, IsUsingK, goal_lst)

                goal_lst.pop()

        if j-1>=0:                                      #left
            if map_lst[i][j-1] < map_lst[i][j]and not visit[i][j-1]:
                DFS(map_lst, i , j-1, visit, IsUsingK, goal_lst)

                goal_lst.pop()

        if i+1<=N-1:                                    #down
            if map_lst[i + 1][j] < map_lst[i][j] and not visit[i+1][j]:
                DFS(map_lst, i + 1, j, visit, IsUsingK, goal_lst)

                goal_lst.pop()

        if j+1<=N-1:                                    #right
            if map_lst[i][j+1] < map_lst[i][j] and not visit[i][j+1]:
                DFS(map_lst, i , j+1, visit, IsUsingK, goal_lst)

                goal_lst.pop()

    if IsUsingK :
        if i - 1 >= 0:  # up
            if map_lst[i - 1][j]>= map_lst[i][j] and map_lst[i-1][j]-K < map_lst[i][j] and not visit[i-1][j]:
                IsUsingK=False
                prev=map_lst[i-1][j]
                map_lst[i-1][j]=map_lst[i][j]-1
                DFS(map_lst,i-1,j,visit,IsUsingK,goal_lst)
                IsUsingK = True
                map_lst[i - 1][j]=prev
                goal_lst.pop()
        if j - 1 >= 0:  # left
            if map_lst[i][j-1]>= map_lst[i][j] and map_lst[i][j-1]-K < map_lst[i][j] and not visit[i][j-1]:
                IsUsingK=False
                prev=map_lst[i][j-1]
                map_lst[i][j-1]=map_lst[i][j]-1
                DFS(map_lst,i,j-1,visit,IsUsingK,goal_lst)
                IsUsingK = True

                map_lst[i][j-1]=prev
                goal_lst.pop()

        if i + 1 <= N - 1:  # down
            if map_lst[i + 1][j]>= map_lst[i][j] and map_lst[i +1][j]-K < map_lst[i][j] and not visit[i+1][j]:
                IsUsingK=False
                prev=map_lst[i+1][j]
                map_lst[i+1][j]=map_lst[i][j]-1
                DFS(map_lst,i+1,j,visit,IsUsingK,goal_lst)
                IsUsingK = True
                map_lst[i + 1][j]=prev
                goal_lst.pop()
        if j + 1 <= N - 1:  # right
            if map_lst[i ][j+1]>= map_lst[i][j] and map_lst[i][j+1]-K < map_lst[i][j] and not visit[i][j+1]:
                IsUsingK=False
                prev=map_lst[i][j+1]
                map_lst[i][j+1]=map_lst[i][j]-1
                DFS(map_lst,i,j+1,visit,IsUsingK,goal_lst)
                IsUsingK = True
                map_lst[i][j + 1]=prev
                goal_lst.pop()

    visit[i][j] = 0

for cnt in range(T):
    N,K=[int(j) for j in input().split()]
    map_lst=[]
    _max=0
    start_lst=[]
    for _ in range(N):
        temp=[int(z) for z in input().split()]
        _max=max(max(temp),_max)
        map_lst.append(temp)
    start_lst = find_start_point(map_lst,N,_max)

    ans = -1
    for i in start_lst:
        visit=[[0 for _ in range(N)]for __ in range(N)]
        DFS(map_lst,i[0],i[1],visit,True,[])

    print(f"#{cnt+1} {ans}")

