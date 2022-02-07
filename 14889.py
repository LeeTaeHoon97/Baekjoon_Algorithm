import sys
input = sys.stdin.readline
from itertools import combinations


"""
조합을 사용하여 팀 멤버를 구한뒤,
차집합을이용해 A팀 B팀으로 나눈다.
이후 각 팀에서 다시 조합을 사용해 2인1조로 분해하여
각 값을 더한뒤, 그 값들의 차이의 최소를 구함
"""

if __name__ == '__main__':
    n=int(input())

    board=[]
    for _ in range(n):
        board.append([int(i)for i in input().split()])
    combOfTeamA=combinations([int(i+1)for i in range(n) ],n//2)
    members=set([i+1 for i in range(n)])
    ans=sys.maxsize


    for teamA in combOfTeamA:
        Ascore = 0
        Bscore = 0
        teamA=list(teamA)
        teamB=list(members-set(teamA))
        for i, j in list(combinations(teamA, 2)):
            Ascore += board[i - 1][j - 1]
            Ascore += board[j - 1][i - 1]
        for i,j in list(combinations(teamB,2)):
            Bscore+=board[i-1][j-1]
            Bscore += board[j - 1][i - 1]

        if ans>abs(Ascore-Bscore):
            ans=abs(Ascore-Bscore)

    print(ans)