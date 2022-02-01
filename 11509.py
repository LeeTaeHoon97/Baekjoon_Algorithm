import sys
input = sys.stdin.readline
"""
첫번째 아이디어
마지막 과녁을 맞추기 위해선
무조건 최소 한발의 화살이 필요하다.
마지막 과녁부터 역으로 출발해 다른 과녁을 지나는지 체크 -> 시간초과


두번째 아이디어
O(n2)이 시간초과 하였으므로
배열 하나로 해결할수 있어야함

board라는 과녁의 위치를 인덱스로 갖는 배열에 인덱스값 위치를 조정 
"""
#첫번째
if __name__ == '__main__':
  n=int(input())
  h=[int(i) for i in input().split()]

  board=[0 for i in range(1000001)]
  
  ans=0
  for i in h:
    if board[i]==0:
      ans+=1
      board[i-1]+=1
    else:
      board[i]-=1
      board[i-1]+=1
      
    
  print(ans)

# #첫번째
# if __name__ == '__main__':
#   n=int(input())
#   h=[int(i) for i in input().split()]

 

#   ans=0
#   while len(h)>0:
#     ans+=1
#     now_h=h.pop()
#     idx=len(h)-1
#     while len(h)>0 and idx>=0:

#       if now_h+1==h[idx]:
#         now_h+=1
#         h.pop(idx)
#       idx-=1
  
#   print(ans)