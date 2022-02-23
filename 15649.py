import sys
input = sys.stdin.readline


"""
단순 순열 구현
"""


if __name__ == '__main__':
    n,m=[int(i) for i in input().split()]
    visit=[0 for i in range(n+1)]
    ans=[]
    def solution(idx,goal,cnt):
        if cnt==goal:
            print(" ".join(ans))
            return

        for i in range(idx,n+1):
            if not visit[i]:
                visit[i]=1
                ans.append(str(i))
                solution(idx,m,cnt+1)
                ans.pop()
                visit[i]=0

    solution(1,m,0)