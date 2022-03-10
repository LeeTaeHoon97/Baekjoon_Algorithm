import sys
input = sys.stdin.readline


"""
10^5개의 숫자이므로 모든 경우의수는 9*10^4 = 90000개
그리디 문제지만 
브루트 포스도 가능할거같음
-------------------------오버플로우
이유 : 숫자의 개수가 10^5라는뜻 즉 자릿수의 이야기임
ex : 80875542 도 범위에 들어감
이렇게 되면 경우의수가 1억을 넘어가므로 브루트 포스는 불가능
--------------------------

30의 배수에 집중해야됨.
30의 배수는 30 60 90 120 150 180 210 240 270 300 이므로 항상 마지막자리에 0이 와야됨
그리고 이후의 자릿수들의 합이 3의 배수여야 성립함 <- 3의 배수이기 위한 조건을 미리 알고있어야함

"""

if __name__ == '__main__':
    lst= [(i) for i in input().rstrip()]
    lst.sort(reverse=True)
    ans=0
    if lst[-1]=='0':
        for i in lst[::-1]:
            ans+=int(i)
        print("".join(lst) if ans%3==0 else -1)
    else:
        print(-1)