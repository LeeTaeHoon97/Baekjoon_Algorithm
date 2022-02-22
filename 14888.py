import sys
input = sys.stdin.readline


"""
+ = 1
- = 2
* = 3
// = 4
매칭 시킨뒤

입력받는 원소의 값만큼 상기의 데이터를 리스트화, 이후 순서를 구함. 



"""
def deep_copy(arr):
    temp = []
    for i in arr:
        temp.append(i)
    return temp

def permute(goal,cnt,lst,stack=[]):
    global per,visit
    if cnt==goal:
        per.append(deep_copy(stack))
        return
    for i in range(len(lst)):
        if not visit[i]:
            visit[i]=1
            stack.append(lst[i])
            permute(goal,cnt+1,lst,stack)
            stack.pop()
            visit[i]=0

if __name__ == '__main__':
    n=int(input())
    a=[int(i) for i in input().split()]
    lst=[]
    tmp=[int(i) for i in input().split()]
    for i in range(4):
        for j in range(tmp[i]):
            lst.append(i+1)

    visit=[0 for i in range(len(lst))]
    per=[]
    permute(len(lst),0,lst)
    Max=-1000000000
    Min=sys.maxsize
    for i in per:
        idx=1
        ans=a[0]
        for j in i:
            if j==1:
               ans+=a[idx]
            elif j==2:
               ans-=a[idx]
            elif j==3:
               ans=ans*a[idx]
            elif j==4:
                if ans<0:
                    ans=((ans*(-1))//a[idx])*(-1)
                else:
                    ans=ans//a[idx]

            idx+=1
        if ans>Max:
            Max=ans
        if ans<Min:
            Min=ans

    print(Max)
    print(Min)
