import sys
input=sys.stdin.readline

#가장 높은점수를 마감일에 가장 가깝게 풀어야 최대점수가 만들어진다.

if __name__ == '__main__':
    n=int(input())
    lst=[]
    ans=[0 for i in range(1001)]
    for i in range(n):
        d,w=[int(i) for i in input().split()]
        lst.append([d,w])
    lst.sort(key=lambda x:(-x[1]))

    for d,w in lst:
        for j in range(d,0,-1):
            if ans[j]==0:
                ans[j]=w
                break
print(sum(ans))
