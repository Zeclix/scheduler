import os
import sys


def enqueue(pList, PID, npTime, wTime=0, pTime=0):
    pList.append([PID, npTime, wTime, pTime])
    return 0


def dequeue(pList):
    return pList.pop()


def lifo(CAT, pList):
    # TODO
    return


def scheduler(sNum, CAT, pList):
    # 스케쥴러 선택
    # 1이면 FIFO, 2이면 SJF, 3이면 LIFO, 3만구현
    if sNum == 1:
        print("Calling FIFO...")
        # fifo(CAT) # 구현안함
        return 0
    elif sNum == 2:
        print("Calling SJF...")
        # sjf(CAT) # 구현안함
        return 0
    elif sNum == 3:
        print("Calling LIFO...")
        lifo(CAT)
        return 0
    else:
        print("잘못된 접근입니다.")
        os._exit(1)


# Input CPU Allocation Time
while 1:
    CAT = int(input('Enter CPU Allocation Time : '))
    if CAT >= 3:
        break

# file open
try:
    f = open('A.txt', 'r')
except Exception as e:
    print(str(e))
    os._exit(1)

# TODO
# file로부터 pList에 담는다.
spList = f.readline()

# string으로 들어온 것을 공백 단위로 쪼개 리스트에 넣는다
pList = spList.split()

# 각 스트링을 int로 변환한다
cnt = 0
for i in pList:
    pList[cnt] = int(i)
    cnt = cnt + 1

# pList의 각 구성 요소는 [PID, npTime, wTime, pTime]
# npTime : 각 프로세스별 필요 소모시간
# wTime : 각 프로세스 waiting time
# pTime : 각 프로세스 professing time
# pList[i] = [PID, npTime, wTime, pTime]

# pList 초기화. PID설정 및 프로세스별 필요 소모시간 설정
for i in range(0, len(pList)):
    enqueue(pList, i, pList[i])


# scheduler calling
scheduler(int(input("Enter Scheduler # (1: FIFO / 2: SJF / 3: LIFO)")), CAT, pList)

# file close
try:
    f.close()
except Exception as e:
    print(str(e))
    os._exit(1)
