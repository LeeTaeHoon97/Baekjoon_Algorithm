import sys
input=sys.stdin.readline

#하나씩 가져오면서 그수의 자릿수를 같이 기억,
#4자리수를 출력해야된다면 첫수의 범위는 가장왼편~ 천의자리 수까지의 범위
#그 이후는 골라진 수에서~ 백의자리, 십의자리, 일의자리 범위로 줄어듬
########################이렇게하면 시간초과

#1)수를 하나씩 가져와서 비교하는데, 이 수가 스택의 값보다 클경우, 스택과 해당데이터를 교체,후 k--
#1-1)스택의 값을 교체 한다는것은 수를 하나 지웠다는 것과 같은 의미
#2) 하나씩 가져온 수가 스택의값보다 작을경우, 스택에 추가해준다. 이후 (1) 시행
#만약 9876과 같이 모든수가 스택의 값보다 작은 데이터의경우 ,뒤에서부터 k개 만큼 수를 지워주면 가장큰수가 된다.

if __name__ == '__main__':
    n,k=[int(i) for i in input().split()]
    num=input().rstrip()
    lst=[]
    ans=""
    stack=[]
    for i in num:
        lst.append(int(i))

    for i in range(n):
        while k>0 and stack and stack[-1]<lst[i]:
            stack.pop()
            k-=1

        stack.append(lst[i])
    for i in range(len(stack)-k):
        ans+=str(stack[i])
    print(ans)