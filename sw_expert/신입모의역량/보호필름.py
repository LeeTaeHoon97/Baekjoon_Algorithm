#pass여부를 검사하는 IsPass 구현에서 지나치게 많은 반복이 이루어져 시간초과가 발생하였다.

def IsPass(lst):
    global W,D,K
    for c in range(W):
        cnt=1
        for r in range(D-1):
            if lst[r][c] == lst[r+1][c]:
                cnt+=1
            else:
                cnt=1
            if cnt>=K:
                break
        if cnt<K:
            return False
    return True
def deepcopy(arr):
    t1=[]
    for i in arr:
        t1.append(i)
    return t1
def DFS(lst,cnt,idx=0):
    global ans,visit_row,D,W,A_lst,B_lst

    if IsPass(lst):
        ans=min(ans,cnt)
        return
    else:
        for i in range(idx,D):
            if not visit_row[i]:
                visit_row[i] = 1
                if cnt+1>=ans:
                    visit_row[i] = 0
                    break
                prev=lst[i]
                lst[i] = A_lst  # A cell로 변경
                DFS(deepcopy(lst), cnt + 1,i+1)

                if cnt+1>=ans:
                    lst[i]=prev
                    visit_row[i] = 0
                    break
                lst[i] = B_lst  # B cell로 변경
                DFS(deepcopy(lst), cnt + 1,i+1)
                lst[i]=prev
                visit_row[i] = 0
                if cnt+1>=ans:
                    break

T = int(input())

for problem_num in range(T):
    D,W,K=[int(i) for i in input().split()]             # D=height , W=weight,
    cells=[]
    visit_row=[0 for i in range(D)]
    ans=D+1
    A_lst = [0 for i in range(W)]
    B_lst = [1 for i in range(W)]
    for i in range(D):
        cells.append([int(i) for i in input().split()])

    DFS(cells,0)
    print(f"#{problem_num+1} {ans}")
