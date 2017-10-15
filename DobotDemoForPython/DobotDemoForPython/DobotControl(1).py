import sys,threading,time
import DobotDllType as dType
import math
import time

api = dType.load()

errorString = [
    'Success',
    'NotFound',
    'Occupied']

def start_com(zero):
    pos = [250, 0, 30, 0]
    comlist = ["COM9","COM7","COM8"]         #3个com口
    dobotID=[0,0,0,0,0]
    print(" =", dobotID)
    for i in range(0,3):
        result = dType.ConnectDobot(api, comlist[i],115200)
        if result[0] == 0:
            print(" =", dobotID,result)
            dobotID[i]=result[3]
    print("Start dobot motion:dobotId =", dobotID)
    for i in dobotID:
       dType.SetQueuedCmdStartExec(api, dobotID[i])
    
    
    pos1_grab=[194.5,211,-38,44]#第一个点
    pos1_place=[276,0,26,0]

    pos2_grab=[220,80,20,-77]#第二个设备抓取点
    pos2_color=[190,80,20,-77]
    pos2_place=[250,-131,27,-2]

    pos3_garb=[255, 0, 0, 0,  200]#第三个设备的抓取点
    pos3_place=[255,0,50,0,1000]
    

    h_r=0
    h_g=0
    h_b=0

    for i in range(0,2):
    #while(True):           
#第一台机械臂的动作
        #Type.SetWAITCmdEx(api, dobotID[0], 10, isQueued=0)
        dType.SetEndEffectorSuctionCupEx(api, dobotID[0], 1, 1, isQueued=1)
        dType.SetPTPCmdEx(api, dobotID[0], 0, pos1_grab[0], pos1_grab[1], pos1_grab[2], pos1_grab[3],isQueued=1)
        dType.SetPTPCmdEx(api, dobotID[0], 0, pos1_place[0], pos1_place[1], pos1_place[2], pos1_place[3],isQueued=1)
        dType.SetEndEffectorSuctionCupEx(api, dobotID[0], 0, 0, isQueued=1)
        dType.SetPTPCmdEx(api, dobotID[0], 0, pos1_grab[0], pos1_grab[1], pos1_grab[2]+30, pos1_grab[3],isQueued=1)
        print("1---")
        # dType.SetWAITCmd(api, dobotID[0], 1000, isQueued=0)
      
#传送带传感器动作

        dType.SetEMotorEx(api, dobotID[0], 0, 1, 10000,  isQueued=1)
        dType.SetInfraredSensor(api, dobotID[1],  1, 1)
        print(dType.GetInfraredSensor(api, dobotID[1], 1))
        while(True):
            print(dType.GetInfraredSensor(api, dobotID[1], 1))
            if dType.GetInfraredSensor(api, dobotID[1], 1)==[1] :
                break
            dType.SetWAITCmd(api, dobotID[1], 100, isQueued=1)
        dType.SetEMotorEx(api, dobotID[0], 0, 0, 10000,  isQueued=1) 
        
#第二台机械臂的动作        

        dType.SetEndEffectorSuctionCupEx(api, dobotID[1], 1, 1, isQueued=1)
        dType.SetPTPCmdEx(api, dobotID[1], 0, pos2_grab[0], pos2_grab[1], pos2_grab[2], pos2_grab[3],isQueued=1)
        dType.SetColorSensor(api, dobotID[1],  1, 2)  
        dType.SetPTPCmdEx(api, dobotID[1], 0, pos2_color[0], pos2_color[1], pos2_color[2], pos2_color[3],isQueued=1)
        dType.SetWAITCmd(api, dobotID[1], 700, isQueued=1)
        while(True):#识别颜色
            print("out",dType.GetColorSensor(api, dobotID[1]))
            if dType.GetColorSensor(api, dobotID[1])!=[0,0,0] :
                resultcolor=dType.GetColorSensor(api, dobotID[1])
                print(resultcolor)
                break
            print("99")
            dType.SetWAITCmd(api, dobotID[1], 600, isQueued=1)
        print("88")

#码垛
        if resultcolor[0]:
            dType.SetPTPCmdEx(api, dobotID[1], 0, pos2_place[0], pos2_place[1]+35, pos2_place[2]+(30*h_r), pos2_place[3],isQueued=1)
            h_r+=1
        if resultcolor[1]:
            dType.SetPTPCmdEx(api, dobotID[1], 0, pos2_place[0], pos2_place[1], pos2_place[2]+(30*h_g), pos2_place[3],isQueued=1)
            h_g+=1
        if resultcolor[2]:
            dType.SetPTPCmdEx(api, dobotID[1], 0, pos2_place[0], pos2_place[1]-35, pos2_place[2]+(30*h_b), pos2_place[3],isQueued=1)
            h_b+=1

        dType.SetWAITCmd(api, dobotID[1], 600, isQueued=1)
        dType.SetEndEffectorSuctionCupEx(api, dobotID[1], 0, 0, isQueued=1)
        print("2---")    
       
    dType.SetDeviceWithL(api, dobotID[2],  1)
    dType.SetHOMECmdEx(api, dobotID[2],  200,  isQueued=1)

    #first
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_garb[0], pos3_garb[1], pos3_garb[2]+30, pos3_garb[3],  pos3_garb[4], isQueued=1)#red
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 1, 1, isQueued=1)
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_place[0], pos3_place[1], pos3_place[2], pos3_place[3],  pos3_place[4], isQueued=1)
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 0, 0, isQueued=1)

    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_garb[0], pos3_garb[1], pos3_garb[2]+30, pos3_garb[3],  pos3_garb[4]-35, isQueued=1)#green
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 1, 1, isQueued=1)
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_place[0], pos3_place[1], pos3_place[2], pos3_place[3],  pos3_place[4], isQueued=1)
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 0, 0, isQueued=1)

    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_garb[0], pos3_garb[1], pos3_garb[2]+30, pos3_garb[3],  pos3_garb[4]-70, isQueued=1)#blue
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 1, 1, isQueued=1)
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_place[0], pos3_place[1], pos3_place[2], pos3_place[3],  pos3_place[4], isQueued=1)
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 0, 0, isQueued=1)

    #second
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_garb[0], pos3_garb[1], pos3_garb[2], pos3_garb[3],  pos3_garb[4], isQueued=1)#red
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 1, 1, isQueued=1)
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_place[0], pos3_place[1], pos3_place[2], pos3_place[3],  pos3_place[4], isQueued=1)
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 0, 0, isQueued=1)

    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_garb[0], pos3_garb[1], pos3_garb[2], pos3_garb[3],  pos3_garb[4]-35, isQueued=1)#green
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 1, 1, isQueued=1)
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_place[0], pos3_place[1], pos3_place[2], pos3_place[3],  pos3_place[4], isQueued=1)
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 0, 0, isQueued=1)

    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_garb[0], pos3_garb[1], pos3_garb[2], pos3_garb[3],  pos3_garb[4]-70, isQueued=1)#blue
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 1, 1, isQueued=1)
    dType.SetPTPWithLCmdEx(api, dobotID[2], 0, pos3_place[0], pos3_place[1], pos3_place[2], pos3_place[3],  pos3_place[4], isQueued=1)
    dType.SetEndEffectorSuctionCupEx(api, dobotID[2], 0, 0, isQueued=1)
    


# dType.      
#SetInfraredSensor(api, dobotId,  isEnable, infraredPort)红外传感器设置
#GetInfraredSensor(api, dobotId, infraredPort)           获取
#SetColorSensor(api, dobotId,  isEnable, colorPort)      颜色传感器设置
#GetColorSensor(api, dobotId)                            获取
#SetEMotorSEx(api, dobotId, index, isEnabled, speed, distance,  isQueued=0) 扩展电机的速度与距离
#SetEMotorEx(api, dobotId, index, isEnabled, speed,  isQueued=0):
#SetDeviceWithL(api, dobotId,  isWithL)设置滑轨使能
#SetHOMECmdEx(api, dobotId,  temp,  isQueued=0):执行回零功能
#SetPTPWithLCmdEx(api, dobotId, ptpMode, x, y, z, rHead,  l, isQueued=0):

maxDobotConnectCount = 20

if __name__ == '__main__':
    threads = []
    print("Start search dobot, count:", maxDobotConnectCount)
    #for i in range(0, maxDobotConnectCount):
    #    result = dType.ConnectDobot(api, "",115200)
    zero=["l",52]
    t1 = threading.Thread(target=start_com,args=(zero[0],))
    threads.append(t1)
    t1.setDaemon(True)
    t1.start()

    for t in threads:
        t.join()

    dType.DobotExec(api)
