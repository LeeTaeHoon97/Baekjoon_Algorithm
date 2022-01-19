import sys
input=sys.stdin.readline

#파이프가 가로일때 이동경우의수 2개 , 가로일때 벽에 가면 이동이 멈춤
#파이프가 세로일때 이동경우의 수 2개   세로일때 벽에가면 이동이멈춤
# 파이프가 대각일때 이동 경우의 수 3개 대각일때 벽에가면 이동이 멈춤

#dp
if __name__ == '__main__':
    n=int(input())
    lst=[[0 for i in range(n+1)]]
    dp=[[[0 for _ in range(n+1)] for _ in range(n+1)]for _ in range(3)] #dp의 3차원은 파이프 방향을 [0 1 2]로 표현

    for i in range(n):
        temp=[0]+[int(i) for i in input().split()]
        lst.append(temp)
    #가로 0 세로 1 대각 2
    dp[0][1][2]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 and j==2: continue
            if lst[i][j]==0:
                dp[0][i][j]=dp[0][i][j-1]+dp[2][i][j-1]
                dp[1][i][j]=dp[1][i-1][j]+dp[2][i-1][j]
                if lst[i-1][j]==0 and lst[i][j-1]==0:
                    dp[2][i][j]=dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1]
    # d=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
    ans=0
    for i in dp:
        ans+=i[n][n]
    print(ans)


"""
완전탐색
if __name__ == '__main__':
    n=int(input())
    lst=[]
    ans=0
    for i in range(n):
        temp=[int(i) for i in input().split()]
        lst.append(temp)
    if lst[n-1][n-1]==1:
        print(0)
    else:
        s=[0,1,0]
        stack=[s]
        while stack:
            row,col,pipe_state=stack.pop()      #pipestate : 가로 0 세로 1 대각 2
            if row ==n-1 and col==n-1:
                ans+=1
                continue

            if pipe_state==0 or pipe_state==2:
                #우측이동이 가능한지
                if col+1<n and lst[row][col+1]!=1:
                        stack.append([row,col+1,0])

            if pipe_state==1 or pipe_state==2:
                #세로이동
                if row+1<n and lst[row+1][col]!=1:
                        stack.append([row+1,col,1])

            if pipe_state==0 or pipe_state==1 or pipe_state==2:
                #대각이동
                if col+1<n and row+1<n and lst[row+1][col+1]!=1 and lst[row][col+1]!=1 and lst[row+1][col]!=1:
                    stack.append([row + 1, col + 1,2])
        print(ans)
"""

"""
deque와 popleft를 쓰면 시간초과한다.
list와 pop으로 사용하면 통과.
"""