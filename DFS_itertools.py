import sys
input = sys.stdin.readline


"""
"""
def deep_copy(arr):
    temp = []
    for i in arr:
        temp.append(i)
    return temp

def combination(goal,cnt,lst,idx,stack=[]):
    global comb,visit
    if cnt==goal:
        comb.append(deep_copy(stack))
        return
    for i in range(idx,len(lst)):       # 조합은 1 2 3 과 2 1 3이 같은값이므로, 시작지점보다 작은 수가 이후 오지 않게(2 ,1 -> X) 한다.
        if not visit[i]:                # 중복체크
            visit[i]=1
            stack.append(lst[i])
            combination(goal,cnt+1,lst,i,stack)
            stack.pop()
            visit[i] = 0

def permutation(goal,cnt,lst,stack=[]):
    global perm,visit
    if cnt==goal:
        perm.append(deep_copy(stack))
        return

    for i in range(len(lst)):
        if not visit[i]:                # 중복체크
            visit[i]=1
            stack.append(lst[i])
            permutation(goal,cnt+1,lst,stack)
            stack.pop()
            visit[i]=0
def combination_replace(goal,cnt,lst,idx,stack=[]):
    global comb_r
    if cnt==goal:
        comb_r.append(deep_copy(stack))
        return

    for i in range(idx,len(lst)):
        stack.append(lst[i])
        combination_replace(goal,cnt+1,lst,i,stack)
        stack.pop()
    return

def product(goal,cnt,lst,stack=[]):
    global prod
    if cnt==goal:
        prod.append(deep_copy(stack))
        return

    for i in range(len(lst)):
        stack.append(lst[i])
        product(goal,cnt+1,lst,stack)
        stack.pop()

if __name__ == '__main__':
    lst=[1,2,3,4,5]
    visit=[0 for i in range(len(lst))]
    comb=[]
    perm=[]
    comb_r=[]
    prod=[]

    combination(3,0,lst,0)
    permutation(3,0,lst)
    combination_replace(3,0,lst,0)
    product(3,0,lst)
    print(comb)
    print(perm)
    print(comb_r)
    print(len(prod))

