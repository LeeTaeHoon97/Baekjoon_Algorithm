import sys
input=sys.stdin.readline
#각 집중국은 센서영역 조절가능
#적어도 하나의 집중국 통신

# 단, 집중국의 수신 가능영역의 길이는 0이상 <- 즉 집중국은 점으로 위치할수 있음 이럴경우 거리는 0
#각 센서가 전부 연결된 하나의 수직선을 그린뒤,
#이 수직선의  센서간 거리가 가장 긴 거리순으로 제거하여 k개의 수직선으로 분리시킨다.
# 즉 2개로 분리한다면 1번 자르고, 3개로 분리시킨다면 2번 잘라 분리


if __name__ == '__main__':
    n=int(input())
    k = int(input())
    if k>=n:            #센서의 수만큼 기지국이 존재시 각 센서에 기지국이 존재가능하므로 거리는 0
        print(0)
    else:
        lst=[int(i) for i in input().split()]
        lst.sort()
        dlst=[]
        for i in range(1,len(lst)):
            dlst.append(lst[i]-lst[i-1])
        dlst.sort()
        for _ in range(k-1):
            dlst.pop()
        print(sum(dlst))
