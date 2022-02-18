import sys
from collections import deque
input = sys.stdin.readline


"""
보드는 1,1~ n,n이다.
보드는 내구도의 정보를 갖는다.

로봇이 움직일 맵을 정의
행이 각각 이어짐 -> mod연산


"""




if __name__ == '__main__':
    n,k = [int(i) for i in input().split()]
    board=[]
    bot_map=[0 for i in range(n*2)]

    board=[int(i) for i in input().split()]
    res=0
    def simul():
        ans=0
        bot_map[0]=1
        robots=deque([0])
        toggle=0

        def rotate():   #1
            if len(robots)!=0:
                s=robots[0]
                for i in range(s,s+n*2):
                    if i % (2 * n) == 0:                                #올리는위치
                        if board[i%(2 * n)]>0 and bot_map[i%(2 * n)]!=1:     #내구도가 1이상이고, 해당위치에 로봇이 없을경우
                            robots.append(i % (2 * n))
                            board[i%(2 * n)]-=1
                            bot_map[i%(2 * n)]=1
                            continue
                    if i%(2*n)==n-1:                                    #내리는위치
                        if bot_map[i%(2*n)]==1:
                            robots.popleft()
                            bot_map[i%(2*n)]=0
                            continue
                    if board[(i+1)%(2*n)]>=1 and bot_map[(i+1)%(2*n)]==0:
                        bot_map[(i+1)%(2*n)]=bot_map[(i)%(2*n)]
                        board[(i+1)%(2*n)]-=1
        def get_cnt():
            tmp=0
            for i in board:
                if i==0:
                    tmp+=1
            return tmp

        while True:
            ans+=1
            rotate()
            if get_cnt()>=k:
                break




        return ans

    res=simul()
    print(res)


