# import sys
# input = sys.stdin.readline


"""
인코딩표를 문자열로 구현.
레지스터를 상징하는 리스트 구현
이를 6비트 8비트로 분리.
각 비트를 다시 합쳐서 아스키코드로 넣어 출력
"""

if __name__ == '__main__':
   n=int(input())
   board="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
   for i in range(n):
        res=""
        s=input()
        for j in range(0,len(s),4):
            register = ['0'] * 24
            #문자열 데이터를 이진수로 바꾼뒤 6비트 단위로 레지스터에 입력
            lambda_a = 0
            for z in s[j:j+4]:
                data=board.index(z)
                for idx,val in enumerate(format(data,'b').zfill(6)):
                    register[idx+lambda_a]=val
                lambda_a+=6
            #6비트 단위를 8비트단위로 합친 뒤 변환
            for z in [int("0b"+"".join(register[0:8]),2),int("0b"+"".join(register[8:16]),2),int("0b"+"".join(register[16:24]),2)]:
                res+=chr(z)
        print(f"#{i+1} {res}")