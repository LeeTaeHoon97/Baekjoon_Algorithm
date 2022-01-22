import sys

input = sys.stdin.readline



if __name__ == '__main__':
    n,m=[int(i) for i in input().split()]
    S=[]
    for i in range(n):
        S.append(input())
    ans=0
    for i in range(m):
        temp=input()
        if temp in S:
            ans+=1
    print(ans)