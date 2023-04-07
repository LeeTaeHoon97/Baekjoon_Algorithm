

#16:20 시작
#19:37 문제가 풀렸으나 메모리 초과 발생, board를 구성하여 풀어서 생긴 문제.
#board를 이용 하지 않고 풀어 본 적이 없어, 해설 참조


# -1000,-1000 ~ 1000,1000 범위를 벗어나는 원자들은 영원히 만날 일 없으므로 삭제해줘야함
# 좌표 일치여부를 알기위해 ,리스트를 dict으로 변환해주고 ,length > 1인 경우 삭제, 이후 다시 리스트로 바꿔주고 move
# 0.5씩 이동하기 때문에 -1000~1000 범위는 -2000~2000 횟수로 이동하므로 4000번 이동

T = int(input())

# 방향(상 하 좌 우 0 1 2 3)
dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]
for problem_num in range(T):
    N=int(input())                  #원자들의 수

    elem_lst=[]
    ans=0
    for i in range(N):
        # x,y,dir,k = [int(i) for i in input().split()]
        elem_lst.append([int(i) for i in input().split()]) #좌표 , 방향(상 하 좌 우 0 1 2 3) , 에너지량

    #board를 그리지 않고 그냥 좌표 이동시킴, 단 좌표가 일치하면 충돌로 판정

    turn = 0
    while turn < 4000 and len(elem_lst) > 1:
        turn += 1

        # 같은 좌표에 있는지 dict을 이용해 쉽게 검사
        ans_dict = {}
        # elem_lst = list(map(move, elem_lst))

        # move
        for i in range(len(elem_lst)):
            elem_lst[i][0]=elem_lst[i][0]+dx[elem_lst[i][2]]
            elem_lst[i][1]=elem_lst[i][1]+dy[elem_lst[i][2]]

        temp = []
        # list(map(dicts, elem_lst))

        #to dict
        for i in elem_lst:
            x=i[0]
            y=i[1]
            if (x,y) not in ans_dict:
                ans_dict[(x,y)]=[i]
            else:
                ans_dict[(x,y)].append(i)
        # key 하나에 2개 이상의 값이 들어있을경우 ,충돌한것임
        for i in list(ans_dict.keys()):
            if len(ans_dict[i]) > 1:
                for e in ans_dict[i]:
                    ans += e[3]
            else:  # 충돌하지 않은 dict을 elem_lst 형태로 변환
                item=ans_dict[i]
                x=item[0][0]
                y=item[0][1]
                if x<-1000 or x>1000 or y<-1000 or y>1000:          # 시작범위를 벗어난 원자들은 영원히 만나지 않으므로 pass
                    pass
                else:
                    temp.append(item[0])

        elem_lst = temp
    print(f"#{problem_num+1} {ans}")


