import os # for os._exit()

class scheduler :

    pList = []
    def __init__(self):
        '''pList 초기화. PID설정 및 프로세스별 필요 소모시간 설정'''
        for i in range(0, len(tpList)):
            lifo.enqueue(pList, i+1, tpList[i])

    def enqueue(self, PID, npTime, wTime=0, pTime=0):
        pList.append([PID, npTime, wTime, pTime])
        return 0


    def dequeue(self):
        return pList.pop()


    def lifo(self, CAT, pList):
        '''npTime : 각 프로세스별 필요 소모시간
        wTime : 각 프로세스 waiting time
        pTime : 각 프로세스 professing time
        pList[i] = [PID, npTime, wTime, pTime] '''

        flag =0; # flag가 0일때만 dequeue
        rList=[] # result List

        while 1:
            # print("pList:") # for dbg
            # print(pList)
            # print("\n")
            if flag==0:
                process = scheduler.dequeue(pList)
                flag=1
            if (process[1] <= CAT):
                for i in range(0, len(pList)):
                    pList[i][2]=pList[i][2]+process[1]
                    pList[i][3]=pList[i][3]+process[1]
                process[3]=process[3]+process[1]
                scheduler.enqueue(rList, process[0], process[1], process[2], process[3])
                # print("rList:") # for dbg
                # print(rList)
                # print(pList)
                # print("\n")
                flag=0
                if len(pList)==0:
                    break
            else:
                for i in range(0, len(pList)):
                    pList[i][2]=pList[i][2]+CAT # 현재 처리되고 있지 않은 다른 process의 waiting time이 allocation time만큼씩 증가
                    pList[i][3]=pList[i][3]+CAT # 다른 process의 processing time이 allocation time만큼씩 증가
                process[1]=process[1]-CAT # 현재 처리되고 있는 프로세스의 남은 처리 요구 시간이 allocation time만큼씩 감소
                process[3]=process[3]+CAT # 현재 처리되고 있는 프로세스의 processing time이 CAT만큼 증가
                # print(process[3]) # for dbg



        return rList


def selectScheduler(sNum, CAT, sche):
    # 스케쥴러 선택
    # 1이면 FIFO, 2이면 SJF, 3이면 LIFO, 3만구현
    if sNum == 1:
        print("Calling FIFO...")
        # fifo(CAT) # 구현안함
        return
    elif sNum == 2:
        print("Calling SJF...")
        # sjf(CAT) # 구현안함
        return
    elif sNum == 3:
        print("Calling LIFO...")
        return scheduler.lifo(CAT, sche)
    else:
        print("잘못된 접근입니다.")
        os._exit(1)


if __name__=="__main__":
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
    # file로부터 List에 담는다.
    # spList : string process list
    spList = f.readline()

    # string으로 들어온 것을 공백 단위로 쪼개 리스트에 넣는다
    # tpList : temporary process list
    tpList = [int(i) for i in spList.split()]

    sche = scheduler()

    # npTime : 각 프로세스별 필요 소모시간
    # wTime : 각 프로세스 waiting time
    # pTime : 각 프로세스 professing time
    # pList[i] = [PID, npTime, wTime, pTime]



    # scheduler calling
    pList = selectScheduler(int(input("Enter Scheduler # (1: FIFO / 2: SJF / 3: LIFO)")), CAT, sche)

    for i in range(len(pList)-1, -1, -1):
        print("PID : %d\t Waiting Time : %d, Processing Time : %d\n" %(pList[i][0], pList[i][2], pList[i][3]))

    # file close
    try:
        f.close()
    except Exception as e:
        print(str(e))
        os._exit(1)
