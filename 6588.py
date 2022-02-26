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

    while True:
        n=int(input())
        if n==0:
            break
        lst=get_prime(n)
        left,right=0,len(lst)-1

        while left<=right:
                if lst[left]+lst[right]==n:
                    print(f"{n} = {lst[left]} + {lst[right]}")
                    break
                elif lst[left]+lst[right]>n:
                    right-=1
                else :
                    left+=1

        if left>=len(lst) or right<0:
            print("Goldbach's conjecture is wrong.")


