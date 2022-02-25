import sys
input = sys.stdin.readline


"""
평범한 순열 구하기이나.

s가 0일경우
0 -1 +1 도 범위에 포함되게끔 해야된다는점.

Sum이 []일 경우 예외처리를 해줘야됨



"""

if __name__ == '__main__':
    n,s=[int(i) for i in input().split()]
    board=[int(i) for i in input().split()]
    visit=[0 for i in range(n+1)]
    Sum=[]
    ans=0
    def lstSum(lst):
        t=0
        for i in lst:
            t+=i
        return t

    def solution(idx):
        global ans,Sum,t
        if len(Sum)>0 and lstSum(Sum)==s:
            ans+=1
        for i in range(idx,n):
            if not visit[i]:
                visit[i]=1
                Sum.append((board[i]))
                solution(i)
                Sum.pop()
                visit[i]=0

    solution(0)
    print(ans)

