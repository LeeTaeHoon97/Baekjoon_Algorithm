
def Rotate(lst,flag):

    if flag==-1:            # left
        temp=lst[0]
        for i in range(len(lst)-1):
            lst[i]=lst[i+1]
        lst[-1]=temp
        return  lst
    if flag==1:             #right
        temp = lst[-1]
        for i in range(len(lst) - 1, 0, -1):
            lst[i] = lst[i - 1]
        lst[0] = temp
        return lst

def Search(lst,idx,flag):             #회전할 톱니 탐색
    global left_check_idx,right_check_idx
    plan=[[idx,flag]]

    next_flag=flag

    #오른쪽방향
    for i in range(idx,4):
        if lst[i][right_check_idx]+lst[i+1][left_check_idx]==1:
            next_flag=next_flag*(-1)
            plan.append([i+1,next_flag])
        else:
            break
    next_flag=flag
    #왼쪽방향
    for i in range(idx,1,-1):
        if lst[i][left_check_idx]+lst[i-1][right_check_idx]==1:
            next_flag=next_flag*(-1)
            plan.append([i - 1, next_flag])
        else:
            break
    return plan


def solve(rlst):
    global lst
    for i,flag in rlst:
        lst[i]=Rotate(lst[i],flag)


T = int(input())
left_check_idx=6                                             # 톱니가 맞물리는 지점은 2 또는 6
right_check_idx=2
for problem_num in range(T):
    K = int(input())            #자석 회전 횟수
    lst=[[]]                    #원래 맵
    K_lst=[]
    ans=0
    for _ in range(4):
        lst.append([int(i) for i in input().split()])
    for _ in range(K):          #자석 회전 정보
        K_lst.append([int(i) for i in input().split()])

    for cmd_lst in K_lst:
        visit = [0 for i in range(5)]
        idx = cmd_lst[0]
        flag = cmd_lst[1]  # 1 or -1 , 1은 시계방향(r) -1은 반시계(l)

        plan=Search(lst,idx,flag)
        solve(plan)
    ans=(lst[1][0]*1) + (lst[2][0]*2) + (lst[3][0]*4) + (lst[4][0]*8)

    print(f"#{problem_num+1} {ans}")
