import sys
from collections import deque
input = sys.stdin.readline


"""
보드는 1,1~ n,n이다.
보드는 내구도의 정보를 갖는다.

로봇이 움직일 맵을 정의
행이 각각 이어짐 -> mod연산

===========틀린이유
벨트와 함께 로봇이 이동하고,
2번 단계에서 로봇들이 한번더 이동함.

===========틀린이유2
보드라는 리스트를 한칸씩 밀어내는것을 구현하는데 오류가 있었음

===========틀린이유3 
not in 구문 사용으로 인한 시간초과
"""




if __name__ == '__main__':
    n,k = [int(i) for i in input().split()]
    board=[]
    bot_map=[0 for i in range(n*2)]

    board=[int(i) for i in input().split()]
    res=0
    def simul():
        ans=0
        robots=deque([])
        def rotate():   #1          보드판과 로봇들의 위치가 한칸씩 옮겨짐
            global board
            t=board[-1]
            t2=board[:(2*n)-1]
            board=[t]+t2

            #robot들이 올라와있을경우,
            if len(robots)>=1:
                for i in range(len(robots)):
                    bot_map[robots[i]]=0
                    robots[i]+=1
                    bot_map[robots[i]]=1
                if robots[0]==n-1:
                    robots.popleft()
                    bot_map[n-1]=0

        def move_robot():   #2
            for i in range(len(robots)):
                if bot_map[robots[i]+1]==0 and board[(robots[i]+1)]>=1: #2-1
                    board[(robots[i] + 1)]-=1
                    bot_map[robots[i]]=0
                    robots[i]+=1
                    bot_map[robots[i]]=1
            if len(robots) >= 1:
                if robots[0] == n - 1:
                    robots.popleft()
                    bot_map[n-1]=0

        def up_robot():     #3
            if bot_map[0]==0 and board[0]>=1:
                board[0]-=1
                robots.append(0)
                bot_map[0]=1
        def get_cnt():      #4
            tmp=0
            for i in board:
                if i==0:
                    tmp+=1
            return tmp

        while True:
            ans+=1
            rotate()
            move_robot()
            up_robot()
            if get_cnt()>=k:
                break

        return ans

    res=simul()
    print(res)


