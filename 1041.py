import sys
input=sys.stdin.readline

#주사위의 1면만 보이는경우
#주사위의 2면만 보이는경우
#주사위의 3면만 보이는경우 를 각각 합친다.
#주사위는 마주보는 면을 제외한 나머지면은 항상 인접함
#마주보는 면의 최솟값은 3쌍이 나옴(1,6)(2,5)(3,4)
#이를 정렬하여 면의 개수에 맞춰 가져오면 된다.



if __name__ == '__main__':
    n=int(input())
    lst=[int(i) for i in input().split()]
    Sum=0
    minlst=[min(lst[0],lst[5]),min(lst[1],lst[4]),min(lst[2],lst[3])]
    minlst.sort()
    if n==1:
        Sum=sum(lst)-max(lst)
    else:
        n1 = (n - 2) * (n - 2) + (n - 1) * (n - 2) * 4
        n2 = (n - 2) * 4 + (n - 1) * 4
        n3 = 4
        Sum+=n1*minlst[0]
        Sum+=n2*(minlst[0]+minlst[1])
        Sum+=n3*(minlst[0]+minlst[1]+minlst[2])

    print(Sum)