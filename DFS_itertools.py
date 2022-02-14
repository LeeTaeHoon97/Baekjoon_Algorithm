import sys
input = sys.stdin.readline


"""
"""
def make_arr():
    global  stack
    temp = []
    for i in stack:
        temp.append(i)
    return temp

def combination(goal,idx,cnt):
    global lst,comb,visit,stack
    if cnt==goal:
        comb.append(make_arr())
        return
    for i in range(idx,len(lst)):       # 조합은 1 2 3 과 2 1 3이 같은값이므로, 시작지점보다 작은 수가 이후 오지 않게(2 ,1 -> X) 한다.
        if visit[i]==0:
            visit[i]=1
            stack.append(lst[i])
            combination(goal,i,cnt+1)
            stack.pop()
            visit[i]=0

def permutation(goal,cnt):
    global lst,perm,visit,stack
    if cnt==goal:
        perm.append(make_arr())
        return

    for i in range(len(lst)):
        if visit[i]==0:
            visit[i]=1
            stack.append(lst[i])
            permutation(goal,cnt+1)
            stack.pop()
            visit[i]=0
def combination_replace(goal,idx,cnt):
    global lst,comb_r,visit,stack
    if cnt==goal:
        comb_r.append(make_arr())
        return

    for i in range(idx,len(lst)):
        stack.append(lst[i])
        combination_replace(goal,i,cnt+1)
        stack.pop()
    return
if __name__ == '__main__':
    lst=[1,2,3,4,5]
    stack=[]
    comb=[]
    perm=[]
    comb_r=[]

    visit=[0 for i in range(len(lst))]
    combination(3,0,0)
    stack=[]            #global 변수 stack combination과 permutation이 공유하므로 초기화해줌
    permutation(3,0)
    stack = []
    combination_replace(3,0,0)
    print(comb_r)
