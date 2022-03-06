import sys

input = sys.stdin.readline


"""
처음에 입력받은 가로선을 추가
이후 가로선(가지)의 경우의수 구현
최소값 구현
만약 cnt가 0이나올경우 바로 stop
----------------------------시간초과
첫번째 원인 : Min이 3개를 벗어나는 경우 -1처리해주지 않음
----------------------------시간초과
두번째 원인 : 경우의수를 구할때 전체 경우의수를 구해버림
----------------------------시간초과
세번째 원인 : 자체구현한 combination 함수가 엄청난 시간을 소비함
----------------------------시간초과
네번째 원인 : 경우의수를 구하고 그 경우의수를 반복문을 도는것과.
재귀적으로 바로 탐색해 나가는것은 속도를 약 절반으로 줄일수 있다.
----------------------------시간초과
다섯번째 원인 : 사다리의 위치를 담은 의미없는 stack을 사용한 부분에서 시간낭비
----------------------------시간초과
여섯번째 원인 : dfs의 if문 사용에 논리문제로 인한 시간낭비 발생
"""

def dfs(idx,cnt):
    global lst,visit,ans

    if cnt>=ans:
        return
    if simul():
        ans=cnt
        return

    for i in range(idx,len(lst)):
        y,x=lst[i]
        if not visit[y][x]:
            visit[y][x]=1
            dfs(i+1,cnt+1)
            visit[y][x]=0

def simul():
    for start in range(1,n+1):
        end=start
        for y in range(1,h+1):
            if visit[y][start-1]==1:
                start-=1
            elif visit[y][start]==1:
                start+=1
        if end!=start:
            return False
    return True

if __name__ == '__main__':

    n,m,h=[int(i) for i in input().split()]
    ans=4
    visit = [[0 for i in range(n+1)]for i in range(h+1)]

    for _ in range(m):
        y,x=[int(i) for i in input().split()]
        visit[y][x]=1

    if m==0:
        print('0')
    else:
        lst = []
        for i in range(1,h+1):
            for j in range(1,n):
                if not visit[i][j]:
                    lst.append([i,j])

        dfs(0,0)
        print(ans if ans<4 else -1)

