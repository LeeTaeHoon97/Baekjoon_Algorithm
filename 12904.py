import sys
from itertools import product

input = sys.stdin.readline
"""
처음엔 중복순열을 만들어
하나씩 넣어서 방법을 찾는
브루트 포스 방법을 사용하였으나
메모리 초과가 발생.

두번째 방법은 
완성된 T의 마지막에 오는 알파벳을
제거해주면서 처음의 S와 일치하는지 여부를 판단
"""
if __name__ == '__main__':
  def func1(s):
    return s[:-1]

  def func2(s):  
    s=s[:-1]
    s=s[-1::-1]
    return s
  
  S=[i for i in input().rstrip()]
  T=[i for i in input().rstrip()]

  while len(T)>len(S):
    if T[-1]=='A':
      T=func1(T) 
    elif T[-1]=='B':
      T=func2(T)
  
  if S==T:
    print(1)
  else:
    print(0)



# #using product
# if __name__ == '__main__':
#   def func1(s):
#     s+='B'
#     return s

#   def func2(s):  
#     s=s[-1::-1]+'A'
#     return s
  
#   S=input().rstrip()
#   T=input().rstrip()

#   lst = [1, 2]
#   r= len(T)-1
#   func_product = list(product(lst, repeat=r))

#   ans=0

#   for i in func_product:
#     temp=S
#     for j in i:
#       if j==1:
#         temp=func1(temp)
#       elif j==2:
#         temp=func2(temp)
#     if temp==T:
#       ans=1
#       break
#   print(ans)