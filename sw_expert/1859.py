# import sys
# input = sys.stdin.readline


"""
판매가격이 구매날보다 비쌀경우에만 구입함
그러므로
역순으로 시작해서 판매가격보다 가격이 쌀 경우 그 차만큼 누적.
판매가격보다 비싼 구입가격을 만나면 판매가격 값 변경
이후 반복
"""

if __name__ == '__main__':
   n=int(input())
   for i in range(n):
        res=0
        n=int(input())
        tcase=[int(i) for i in input().split()]
        idx = n-1
        for j in range(n-2,-1,-1):
            if tcase[idx]>tcase[j]:
                res+=tcase[idx]-tcase[j]
            else:
                idx=j
        print(f"#{i+1} {res}")