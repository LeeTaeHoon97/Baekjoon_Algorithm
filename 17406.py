import sys

input = sys.stdin.readline
from collections import defaultdict
from itertools import permutations
import copy

"""
1. 회전연산 순서의 경우의수를 가져온다.
2. 회전함수 함수 구현

"""

if __name__ == '__main__':
    def Rotate(r):
        #start
        s0=r[0]-r[2]-1
        e0=r[1]-r[2]-1

        #end
        s1=r[0]+r[2]
        e1=r[1]+r[2]
        print(s0,e0,s1,e1)
        arr=copied_arr[s0:s1][e0:e1]
        for i in copied_arr:
            print(i)
        print("-----------------------")
        for i in arr:
            print(i)
        arr[0][0]=111
        print("-----------------------")
        for i in copied_arr:
            print(i)


    copied_arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    Rotate([2,2,1])


    # def Get_min(arr):
    #     lst=[]
    #     for i in arr:
    #         lst.append(sum(i))
    #
    #     print(min(lst))
    #     return  min(lst)
    #
    # n,m,k=[int(i) for i in input().split()]
    # arr=[]
    # for _ in range(n):
    #    arr.append([int(i) for i in input().split()])
    # rotate_cal=[]
    # for _ in range(k):
    #     rotate_cal.append([int(i) for i in input().split()])
    # lst=list(permutations(rotate_cal))
    # Min=float("inf")
    # #회전함수의 경우의 수
    # for i in lst:
    #     copied_arr=copy.deepcopy(arr)
    #     for j in i:
    #         Rotate(j)
    #     semi_Min=Get_min(copied_arr)
    #     if semi_Min<Min:
    #         Min=semi_Min
    #
    # print(Min)