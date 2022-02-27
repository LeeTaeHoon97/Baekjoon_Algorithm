import sys
input = sys.stdin.readline


"""

"""

if __name__ == '__main__':
    def get_prime(num):
        tmp=[0,0,0]+[1 for i in range(3,num+1)]
        for i in range(2,4):
            t=i
            while t+i<=num:
                t+=i
                tmp[t]=0

        return [idx for idx,val in enumerate(tmp) if val==1]
    plst=[[0,0] for i in range(100001)]
    while True:
        n=int(input())
        if n==0:
            break
        if plst[n]!=[0,0]:
            print(f"{n} = {plst[n][0]} + {plst[n][1]}")
        else:
            lst=get_prime(n)
            left,right=0,len(lst)-1

            while left<=right:
                    if lst[left]+lst[right]==n:
                        print(f"{n} = {lst[left]} + {lst[right]}")
                        plst[n]=[lst[left],lst[right]]
                        break
                    elif lst[left]+lst[right]>n:
                        right-=1
                    else :
                        left+=1

            if left>=len(lst) or right<0:
                print("Goldbach's conjecture is wrong.")


