import sys
from copy import deepcopy
input = sys.stdin.readline


"""
1. 좋아하는 학생이 가장 많이 인접한 칸에 들어간다.  -> 좋아하는 학생들이 자리에 앉아있는지 탐색, 있으면 가장 인접한 좌표 반환
                                                없거나 그 반환값의 개수가 2개 이상일경우 2번 방법으로
2. 인접빈칸이 많은곳에들어간다.                  ->1에서 전달받은 배열이 없을경우 전체 탐색, 있을경우 그 배열만 탐색
3. 좌측위부터 들어간다.                          ->2에서 정렬되게 탐색하였으므로 가장 처음 발견된곳이 가장작은칸임

1초는 약 1억번의 탐색시간
n의 최대범위는 20이므로 시간초과가 걸릴일은 없어보임.

"""

def show(lst):
    for i in lst:
        print(i)
    print('--------------------------')

def simul(board,students):
    global n
    def func1(f):
        temp=set()
        res=[]
        for r in range(1,n+1):
            for c in range(1,n+1):
                if board[r][c] in f:
                    if r-1>0:
                        bboard[r-1][c]+=1
                        temp.add((r-1,c))
                    if r+1<n+1:
                        bboard[r+1][c]+=1
                        temp.add((r+1,c))
                    if c-1>0:
                        bboard[r][c-1]+=1
                        temp.add((r,c-1))
                    if c+1<n+1:
                        bboard[r][c+1]+=1
                        temp.add((r,c+1))
        Max=-1
        for i in temp:
            y,x=i
            if Max<bboard[y][x]:
                Max=bboard[y][x]
                res=[]
            if Max==bboard[y][x]:
                res.append([y,x])
        print(res,len(res))
        return (False,res)if len(res)==1 else (True,res)

    def func2(lst,b):
        def get_cnt(r,c):
            cnt=0
            if r - 1 > 0 and b[r - 1][c] == 0:
                cnt+=1
            if r + 1 < n + 1 and b[r + 1][c] == 0:
                cnt += 1
            if c - 1 > 0 and b[r][c - 1] == 0:
                cnt += 1
            if c + 1 < n + 1 and b[r][c + 1] == 0:
                cnt += 1
            return [cnt,r,c]
        Max=0
        t=[]
        cnt=[]
        if len(lst)>1:
            for r,c in lst:
                cnt.append(get_cnt(r,c))
            cnt.sort(key=lambda x:x[1])
            cnt.sort(key=lambda x:x[2])
            cnt.sort(key=lambda x:x[0])
            return cnt[0]
        else:           #전체탐색
            for r in range(1,n+1):
                for c in range(1,n+1):
                    cnt.append(get_cnt(r,c))
            cnt.sort(key=lambda x:x[1])
            cnt.sort(key=lambda x:x[2])
            cnt.sort(key=lambda x:x[0])
            return cnt[-1]


    for student in students:
        bboard=deepcopy(board)
        stu,fav=student[0],student[1::]         #student,favorite
        val_func1=func1(fav)
        if val_func1[0]:
            _,y,x=func2(val_func1[1],board)
            board[y][x]=stu
        else:

            for y,x in val_func1[1]:
                board[y][x]=stu

    return board

def get_ans(b,studs):
    ans=0
    def check(r,c,lst):
        cnt=0
        if r - 1 > 0 and b[r - 1][c] in lst:
            cnt+=1
        if r + 1 < n + 1 and b[r + 1][c] in lst:
            cnt += 1
        if c - 1 > 0 and b[r][c - 1] in lst:
            cnt += 1
        if c + 1 < n + 1 and b[r][c + 1] in lst:
            cnt += 1
        return cnt
    for i in studs:
        s,f=i[0],i[1::]
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                if b[r][c]==s:
                    temp=check(r,c,f)
                    ans+=0 if temp==0 else 10**(temp-1)
    return ans
if __name__ == '__main__':

    n= int(input())
    board=[[-1 for i in range(n+1)]]+[[-1]+[0 for i in range(n)]for i in range(n)]
    students=[]
    for i in range(n*n):
        students.append([int(i) for i in input().split()])

    b=simul(board,students)
    ans=get_ans(b,students)
    show(board)
    print(ans)