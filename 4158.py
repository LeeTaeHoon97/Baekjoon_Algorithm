import copy
import sys
input = sys.stdin.readline


"""
nlst와 mlst에 각각 따로 인덱스를 사용
--------틀린이유
0 0 이 나올때가지 여러개의 케이스가 들어올수 있음.
"""

if __name__ == '__main__':
    while(True):
        n,m=[int(i) for i in input().split()]
        if n==0 and m==0:
            sys.exit()
        nlst=[]
        mlst=[]
        for i in range(n):
            nlst.append(int(input()))

        for j in range(m):
            mlst.append(int(input()))


        nidx=0
        midx=0

        ans=0
        while(nidx<n and midx<m):
            if nlst[nidx]==mlst[midx]:
                ans+=1
                nidx+=1
                midx+=1
            else:
                if nlst[nidx]>mlst[midx]:
                    midx+=1
                elif nlst[nidx]<mlst[midx]:
                    nidx+=1

        print(ans)