import sys
from itertools import permutations
import copy

input = sys.stdin.readline
"""
1. 회전연산 순서의 경우의수를 가져온다.
2. 회전함수 함수 구현
"""

if __name__ == '__main__':
    def Rotate(r):
        #start
        y0=r[0]-1
        x0=r[1]-1

        #end
        y1=r[0]-1
        x1=r[1]-1

        for n in range(r[2],0,-1):
            temp=copied_arr[y0-n][x1+n]
            # 우측이동
            copied_arr[y0-n][x0-n+1:x1+n+1]=copied_arr[y0-n][x0-n:x1+n]
            # 왼쪽 상승
            for row in range(y0-n,y1+n):
                copied_arr[row][x0-n]=copied_arr[row+1][x0-n]
            # 좌측이동
            copied_arr[y1+n][x0-n:x1+n]=copied_arr[y1+n][x0-n+1:x1+n+1]
            # 우측 하강
            for row in range(y1+n-1,y0-n-1,-1):
                copied_arr[row+1][x1+n]=copied_arr[row][x1+n]

            copied_arr[y0-n+1][x1+n]=temp

    def Get_min(arr):
        lst=[]
        for i in arr:
            lst.append(sum(i))

        return  min(lst)

    n,m,k=[int(i) for i in input().split()]
    arr=[]
    for _ in range(n):
       arr.append([int(i) for i in input().split()])
    rotate_cal=[]
    for _ in range(k):
        rotate_cal.append([int(i) for i in input().split()])
    lst=list(permutations(rotate_cal))
    Min=float("inf")

    #회전함수의 경우의 수
    for i in lst:
        copied_arr=copy.deepcopy(arr)
        for j in i:
            Rotate(j)
        semi_Min=Get_min(copied_arr)
        if semi_Min<Min:
            Min=semi_Min

    print(Min)