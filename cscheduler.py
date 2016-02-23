class scheduler :

    pList = []
    rList = [] # result list
    def __init__(self, tpList):
        """pList 초기화. PID설정 및 프로세스별 필요 소모시간 설정"""
        for i in range(0, len(tpList)):
            self.enqueue(scheduler.pList, i + 1, tpList[i])

    def enqueue(self, pList, PID, npTime, wTime = 0, pTime = 0):
        """
        :param pList: pList[i] = [PID, npTime, wTime, pTime]
        :param PID: Process ID
        :param npTime: 각 프로세스별 필요 소모시간
        :param wTime: 각 프로세스 waiting time
        :param pTime: 각 프로세스 professing time
        :return: 0
        """
        pList.append([PID, npTime, wTime, pTime])
        return 0


    def dequeue(self):
        return scheduler.pList.pop()


    def lifo(self, CAT, pList):
        flag = 0; # flag가 0일때만 dequeue
        rList = [] # result List

        while 1:
            if flag == 0:
                process = self.dequeue()
                flag = 1
            if (process[1] <= CAT):
                for i in range(0, len(self.pList)):
                    self.pList[i][2] = self.pList[i][2] + process[1]
                    self.pList[i][3] = self.pList[i][3] + process[1]
                process[3] = process[3] + process[1]
                self.enqueue(rList, process[0], process[1], process[2], process[3])
                flag = 0
                if len(pList) == 0:
                    break
            else:
                for i in range(0, len(pList)):
                    self.pList[i][2] = self.pList[i][2] + CAT # 현재 처리되고 있지 않은 다른 process의 waiting time이 allocation time만큼씩 증가
                    self.pList[i][3] = self.pList[i][3] + CAT # 다른 process의 processing time이 allocation time만큼씩 증가
                process[1] = process[1] - CAT # 현재 처리되고 있는 프로세스의 남은 처리 요구 시간이 allocation time만큼씩 감소
                process[3] = process[3] + CAT # 현재 처리되고 있는 프로세스의 processing time이 CAT만큼 증가
        return rList


def selectScheduler(sNum, CAT, sche):
    """ 스케쥴러 선택
     1이면 FIFO, 2이면 SJF, 3이면 LIFO, 3만구현"""
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
        return sche.lifo(CAT, sche.pList)
    else:
        print("잘못된 접근입니다.")

if __name__ == "__main__":
    # Input CPU Allocation Time
    while 1:
        CAT = int(input('Enter CPU Allocation Time : '))
        if CAT >= 3:
            break

    # file open
    try:
        with open('A.txt', 'r') as f:
            # file로부터 List에 담아, string으로 들어온 것을 공백 단위로 쪼개 int로 변환하여 리스트에 넣는다
            # tpList : temporary process list
            tpList = [int(i) for i in (f.read()).split()]
            sche = scheduler(tpList)

            # scheduler calling
            pList = selectScheduler(int(input("Enter Scheduler # (1: FIFO / 2: SJF / 3: LIFO)")), CAT, sche)

            for i in range(len(pList) - 1, -1, -1):
                print("PID : %d\t Waiting Time : %d, Processing Time : %d\n" %(pList[i][0], pList[i][2], pList[i][3]))
    except Exception as e:
        print(e)