
T = int(input())

def rotate():
    global board
    prev=board[-1]
    for i in range(len(board)-1,0,-1):
        board[i]=board[i-1]
    board[0]=prev

def make_board(num):
    global N
    t=[]
    for i in num:
        t.append(i)
    return t

def add_dict(lst):
    global ans,N
    temp=""
    for i in lst:
        temp+=i
        if len(temp)==N//4:
            if temp not in ans:
                ans[temp]=decode(temp)
            temp=""

def decode(str):
    global d_lst
    k=len(str)
    val=0
    for i in range(k):
        val+=16**(k-1-i)*d_lst[str[i]]
    return val


d_lst={'0':0,'1':1,'2':2,'3':3,
       '4':4,'5':5,'6':6,'7':7,
       '8':8,'9':9,'A':10,'B':11,
       'C':12,'D':13,'E':14,'F':15}

for problem_num in range(T):
    N,K=[int(i) for i in input().split()]             # D=height , W=weight,
    num=input()
    ans = {}

    board=make_board(num)

    for i in range(N//4):
        add_dict(board)
        rotate()
    print(f"#{problem_num+1} {sorted(list(ans.values()),reverse=True)[K-1]}")
