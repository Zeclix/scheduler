import os
import sys

def enqueue():
    #TODO
    return

def dequeue():
    #TODO
    return

def lifo(CAT, pList):
    #TODO
    return

def scheduler(sNum, CAT, pList):
    if sNum==1:
        print("Calling FIFO...")
        # fifo(CAT) # 구현안함
        return 0
    elif sNum==2:
        print("Calling SJF...")
        # sjf(CAT) # 구현안함
        return 0
    elif sNum==3:
        print("Calling LIFO...")
        lifo(CAT)
        return 0
    else:
        print("잘못된 접근입니다.")
        os._exit(1)




# Input CPU Allocation Time
while 1:
    CAT = int(input('Enter CPU Allocation Time : '))
    if CAT>=3:
        break


# file open
try:
    f = open('A.txt', 'r')
except Exception as e:
    print(str(e))

# TODO
# file로부터 pList에 담는다.
spList = f.readline()

# string으로 들어온 것을 공백 단위로 쪼개 리스트에 넣는다
pList = spList.split()

# 각 스트링을 int로 변환한다
cnt=0
for i in pList:
    pList[cnt]=int(i)
    cnt=cnt+1


# scheduler calling
scheduler(int(input("Enter Scheduler # (1: FIFO / 2: SJF / 3: LIFO)")), CAT, pList)

# file close
f.close()
