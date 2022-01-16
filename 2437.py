import sys
input=sys.stdin.readline

if __name__ == '__main__':
    n=int(input())
    lst=[int(i) for i in input().split()]
    lst.sort()
    Sum=0
    ans=0
    for i in range(n):
        if Sum+1<lst[i]:
            break
        else:
            Sum+=lst[i]

    print(Sum+1)
