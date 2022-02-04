import sys
from itertools import combinations
input = sys.stdin.readline
"""
브루트 포스방법으로 풀었음.
치킨집중 M개의 치킨집만 남기는 경우의수를 구한다.
해당 경우의수를 돌면서 치킨거리가 가장 짧은 값을 구한다.
|r1-r2| + |c1-c2| 거리공식
"""


def search(homes,stores):
    def get_dist(home,shop):
        return abs(home[0]-shop[0])+abs(home[1]-shop[1])

    total_dist=0

    for h in homes:
        mMin=sys.maxsize
        for s in stores:
            dist=get_dist(h,s)
            if dist<mMin:
                mMin=dist
        total_dist+=mMin
    return  total_dist

if __name__ == '__main__':
    n,m=[int(i) for i in input().split()]
    board=[]
    chicken_shop=[]
    home=[]
    Min=sys.maxsize
    for i in range(n):
        temp=[int(i) for i in input().split()]
        for j in range(len(temp)):
            if temp[j]==1:
                home.append([i,j])
            elif temp[j]==2:
                chicken_shop.append([i,j])
        board.append(temp)

    survived_store=list(combinations(chicken_shop,m))
    for i in survived_store:
        d=search(home,i)
        if d<Min:
            Min=d

    print(Min)