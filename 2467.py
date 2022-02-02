import sys
input = sys.stdin.readline
"""
0에 가장 가까운 값을 가져야함
"""
if __name__ == '__main__':
  n=int(input())
  h=[int(i) for i in input().split()]
  Min=sys.maxsize
  left =  0
  right = len(h)-1

  ans=[0,0]

  while left<right:
    if abs(h[left]+h[right])<Min:
      Min=abs(h[left]+h[right])
      ans=[h[left],h[right]]


    if h[left]+h[right]>0:
      right-=1
    else:
      left+=1


  print(ans[0],ans[1])

