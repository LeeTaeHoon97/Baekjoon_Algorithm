import sys
input = sys.stdin.readline


"""
중간값.
"""

if __name__ == '__main__':
    n=int(input())
    board=[int(i)for i in input().split()]
    board.sort()
    print(board[(n-1)//2])

