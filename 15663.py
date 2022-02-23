import sys
input = sys.stdin.readline


"""
단순 순열 구현
-------------------실패
not in lst ~ 구문 사용으로인한 시간초과 발생

set과 tuple을 이용하여 해결
"""

def convert_tuple(lst):
    return tuple(lst)
if __name__ == '__main__':
    n,m=[int(i) for i in input().split()]
    lst=[int(i) for i in input().split()]
    lst.sort()
    visit=[0 for i in range(n+1)]
    ans=[]
    tmp=set()
    def solution(idx,goal,cnt):
        global tmp
        if cnt==goal:
            if tuple(ans) not in tmp:
                print(" ".join(ans))
                tmp.add(convert_tuple(ans))
            return

        for i in range(idx,n):
            if not visit[i]:
                visit[i]=1
                ans.append(str(lst[i]))
                solution(idx,m,cnt+1)
                ans.pop()
                visit[i]=0

    solution(0,m,0)