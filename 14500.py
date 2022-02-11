import sys
input = sys.stdin.readline


"""
ㅗ 모양을 제외한 나머지 모양은
dfs로 구현이 가능함.
모든 좌표를 돌면서 만들어지는 도형들의 값들중 최대값을 구한다.
"""

if __name__ == '__main__':
    n,m=[int(i) for i in input().split()]
    board=[]
    ans=0
    visit=[[0 for i in range(m)]for j in range(n)]
    def dfs(ny,nx,cnt,sum):

        global ans
        visit[ny][nx]=1
        if cnt==4:
            ans=max(ans,sum)
            return

        if ny<n-1 and visit[ny+1][nx]==0:
            dfs(ny+1,nx,cnt+1,sum+board[ny+1][nx])
            visit[ny+1][nx]=0
        if ny>0 and visit[ny-1][nx]==0:
            dfs(ny-1,nx,cnt+1,sum+board[ny-1][nx])
            visit[ny-1][nx] = 0
        if nx<m-1 and visit[ny][nx+1]==0:
            dfs(ny,nx+1,cnt+1,sum+board[ny][nx+1])
            visit[ny][nx+1] = 0
        if nx>0 and visit[ny][nx-1]==0:
            dfs(ny,nx-1,cnt+1,sum+board[ny][nx-1])
            visit[ny][nx-1] = 0



    def another(y,x):
        # ㅗ 모양의 최대는 중앙의 값과 중앙을 중심으로 가로세로 4칸중 값이 높은 3칸을 가져온것이 최대값
        global  ans
        lst=[]

        if y<n-1:
            lst.append(board[y+1][x])
        if y > 0 :
            lst.append(board[y-1][x])
        if x < m-1:
            lst.append(board[y][x+1])
        if x > 0:
            lst.append(board[y][x-1])



        if len(lst)>=3:
            lst.sort(reverse=True)
            ans=max(ans,board[y][x]+sum(lst[:3]))



    for _ in range(n):
        temp=[int(i)for i in input().split()]
        board.append(temp)

    for i in range(n):
        for j in range(m):
            dfs(i,j,1,board[i][j])
            visit[i][j] = 0             #dfs함수 처음 시작할때 visit[i][j]를 1로 체크해준것을 풀어줌
            another(i,j)


    print(ans)
