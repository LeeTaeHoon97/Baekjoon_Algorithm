import sys
input=sys.stdin.readline

#n명의 사람을 k조로 분리
#사람들은 인접해야하며 ,1명도 인정
#티셔츠 비용은 각 조당 최장키-최단키, 즉 1명이면 0원


if __name__ == '__main__':
    n,k=[int(i) for i in input().split()]
    if k==n:            #아이의 수만큼 조가 존재시 각 조에 아이가 존재가능하므로 가격 0
        print(0)
    else:
        lst=[int(i) for i in input().split()]

        dlst=[]
        for i in range(1,len(lst)):
            dlst.append(lst[i]-lst[i-1])
        dlst.sort()
        for _ in range(k-1):
            dlst.pop()
        print(sum(dlst))
