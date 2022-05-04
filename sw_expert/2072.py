# import sys
# input = sys.stdin.readline


"""
"""

if __name__ == '__main__':
   n=int(input())
   for i in range(n):
        res=0
        tcase=[int(i) for i in input().split()]
        for j in tcase:
            if j%2==1:
                res+=j
        print(f"#{i+1} {res}")