import sys
input = sys.stdin.readline


"""
반드시 순회가 가능하므로
모든 섬의경우를 구할필요 없이
특정 섬에서부터 순회되는 최소값을 구하면됨.

1번섬 (idx는 0)부터 시작하였을경우
마지막 도착지가 0을 가리킬경우 순회가 끝난경우이다.

또한 재귀진행중 더해나간 섬들의 비용이 
이미 나온 Min값을 초과할경우 ,바로 종료한다.
"""

if __name__ == '__main__':
    n=int(input())
    board=[]
    for i in range(n):
        temp=[int(i) for i in input().split()]
        board.append(temp)
    visit=[0 for i in range(n+1)]
    ans=[]
    Min=sys.maxsize
    def solution(y,goal,cnt):
        global Min
        if cnt==goal and 0==y:
            if sum(ans)<Min:
                Min=sum(ans)
            return
        if sum(ans)>Min:
            return

        if not visit[y]:
            visit[y]=1
            for j in range(n):
                if board[y][j]>0:
                    ans.append((board[y][j]))
                    solution(j,goal,cnt+1)
                    ans.pop()
            visit[y]=0

    solution(0,n,0)
    print(Min)