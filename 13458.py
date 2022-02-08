import sys
input = sys.stdin.readline


"""
"""

if __name__ == '__main__':
    n=int(input())
    board=[int(i)for i in input().split()]
    b,c=[int(i) for i in input().split()]
    ans=[0 for i in range(n)]

    for i in range(n):
        person=0
        person+=1
        board[i]-=b
        if board[i]<=0:
            ans[i] = person
            continue
        else:
            person+=board[i]//c
            board[i]=board[i]%c
            if board[i]>0:
                person+=1
            ans[i]=person

    print(sum(ans))