
def deepcopy(arr):
    temp=[]
    for i in arr:
        temp.append(i)
    return  temp

t_type={1:{'dx':[0,1,0,-1],'dy':[1,0,-1,0]},
        2:{'dx':[0,0,0,0],'dy':[1,0,-1,0]},
        3:{'dx':[0,1,0,-1],'dy':[0,0,0,0]},
        4:{'dx':[0,1,0,0],'dy':[0,0,-1,0]},
        5:{'dx':[0,1,0,0],'dy':[1,0,0,0]},
        6:{'dx':[0,0,0,-1],'dy':[1,0,0,0]},
        7:{'dx':[0,0,0,-1],'dy':[0,0,-1,0]}}




T=int(input())

def DFS(goal,cnt,r,c):
    global board,answer_lst,visit,t_type,N,M,DP


    if cnt < DP[r][c]:                          # 해당 관측시점이 이미 기록된 시점(DP)보다 늦게 올경우, 해당 경로는 이미 탐색한 경로를 다시 찾는 것이므로 건너뜀
        DP[r][c]=cnt

        s=board[r][c]


        dy = t_type[s]['dy']
        dx = t_type[s]['dx']

        answer_lst.add((r,c))
        if goal==cnt:
            # answer_lst
            return

        if not visit :
            visit[r][c]=1



        for i in range(4):
            nr=r+dy[i]
            nc=c+dx[i]
            if nr>=0 and nr<=N-1:
                if nc>=0 and nc<=M-1:
                    # print(board[nr][nc])
                    if board[nr][nc] != 0:
                        if (dy[i]!=0 and t_type[board[nr][nc]]['dy'][(i+2)%4] ==dy[i]*(-1)) or (dx[i]!=0 and t_type[board[nr][nc]]['dx'][(i+2)%4] ==dx[i]*(-1))  :     #하수도 간 연결됨
                            DFS(goal,cnt+1,nr,nc)
        visit[r][c] = 0




for problem_num in range(T):
    N,M,R,C,L=[int(i) for i in input().split()]
    board=[]
    answer_lst=set()
    visit=[[0 for i in range(M)]for i in range(N)]
    DP=[[30 for i in range(M)]for i in range(N)]
    for __ in range(N):
        board.append([int(i) for i in input().split()])

    DFS(L,1,R,C)

    print(f"#{problem_num+1} {len(answer_lst)}")

