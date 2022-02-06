import sys
input = sys.stdin.readline
"""
n이 60보다 적을경우
35이하의 수는 0에서 더한 수가 최단수이다.

그리고  36이상의 수는
60-(60-36)이 최단수이다.

또한 일의자리가 5이하인경우 0에서 더한수가 최단,
6이상인경우 10-(10-6)이 최단수이다.
"""

if __name__ == '__main__':

    t=int(input())
    tcase=[]
    for _ in range(t):
        tcase.append(int(input()))
    for i in tcase:
        ans=[0,0,0,0,0]     #+60 +10 -10 +1 -1
        temp=i//60
        ans[0]+=temp
        i=i%60

        if i<=35:
            ten = i // 10
            one = i % 10
            ans[1]+=ten
            if one<=5:
                ans[3]+=one
            else:
                ans[1]+=1
                ans[4]+=(10-one)%10
        else:
            i=60-i
            ten = i // 10
            one = i % 10
            ans[0]+=1
            ans[2]+=ten
            if one <= 5:
                ans[4] += one
            else:
                ans[2] += 1
                ans[3] += (10 - one) % 10

        print(*ans)

