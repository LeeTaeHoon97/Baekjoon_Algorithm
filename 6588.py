import sys
input = sys.stdin.readline


"""
----------------시간초과
원인 : n을 입력할때마다 에라토스테네스의 체를 구하여 시간초과 발생.

에라토스테네스의 체를 이용할 경우,
초기 한번 전체범위의 소수를 구하면 이후 반복할필요 없음.

------------------틀림
원인 : 에라토스테네스의 체 구현에 실수

------------------개선
get_prime func에서 범위를 제곱근을 취하면 좀더 시간을 줄일수 있다.
------------------개선
소수 리스트를 리턴하는것보다 소수가 매핑된 보드를 이용하여 탐색하는것이 더 효율적이다.
------------------개선
get_prime func에서 조건에 따라 실행되는 while문보다 for문을 사용하는것이 더 효율적이다.
"""

if __name__ == '__main__':
    def get_prime(num):
        tmp=[0,0]+[1 for i in range(2,num+1)]
        for i in range(2,int(1000000**0.5)):
            if tmp[i]:
                for j in range(i+i,1000000,i):
                    tmp[j]=0
        tmp[2]=0
        return tmp

    board=get_prime(1000000)
    cnt=1
    is_not_found=0
    while cnt<100000:           #입력 케이스의 최대는 10만
        n=int(input())
        cnt+=1
        if n==0:
            break

        for i in range(3,n):
            if  board[i]:
                if board[n-i]:
                    print(n,"=",i,"+",n-i)
                    is_not_found=0
                    break
            is_not_found=1

        if is_not_found:
            print("Goldbach's conjecture is wrong.")


