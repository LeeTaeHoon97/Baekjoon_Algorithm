from collections import deque

def bfs(R,C):
    global board,visit,N,ans
    # 우측방향기준, 직진할건지 회전할건지만 알면 됨
    deck=deque()

    deck.append([R,C,[board[R][C]],0,0])            # r,c, cafes, rotate_cnt, direction

    # 1,1    -1,1     -1,-1  1,-1
    dr=[1,-1,-1,1]
    dc=[1,1,-1,-1]

    visit[R][C]=1
    while deck:
        r,c,cafes,rcnt,dir=deck.pop()


        if 2*N-2 < len(cafes):
            continue

        #종료 조건
        if [r,c]==[R,C] and rcnt==3:                        # 세번 회전 이후 원래 위치로 왔을 경우
            ans=max(ans,len(cafes))


        for i  in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            #방향이 같을 경우
            if dir==i:

                if 0<=nr<N and 0<=nc<N :
                    if board[nr][nc] not in cafes:
                        deck.append([nr,nc,cafes + [board[nr][nc]],rcnt,i])
                    if [nr,nc]==[R,C] and rcnt==3:
                        deck.append([nr,nc,cafes,rcnt,i])

            #방향이 다를 경우
            if 0 <= nr < N and 0 <= nc < N and rcnt<3:
                if board[nr][nc] not in cafes:
                    deck.append([nr,nc,cafes +[board[nr][nc]],rcnt+1,i])
                if [nr,nc]==[R,C] and rcnt+1==3:
                    deck.append([nr,nc,cafes,rcnt+1,i])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    board=[]
    ans=-1
    for i in range(N):
        board.append([int(i) for i in input().split()])

    visit=[[0 for i in range(N)]for i in range(N)]

    # bfs(0,2)
    for r in range(N):
        for c in range(N):
            bfs(r,c)
    print(f'#{test_case} {ans}')




# 1
# 4
# 9 8 9 8
# 4 6 9 4
# 8 7 7 8
# 4 5 3 5

# 2*N-2 < len(cafes):
