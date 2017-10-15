import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

home_x = 8.45
home_y = -201.8
home_z = 81.56
home_r = -135

temp_x1 = 193.32
temp_y1 = -194.48
temp_z1 = 15
temp_r1 = -132.77

temp_x2 = 314.22
temp_y2 = -5.22
temp_z2 = 15
temp_r2 = -129.5

zero_x = 117.04
zero_y = -147.6

zero_r1 = 67.42 #outside
zero_r0 = -110.03 #inside
zero_r3 = -23.72 #right

def dobot_init():
    #Load Dll 
    api = dType.load()
    #Connect Dobot
    state = dType.ConnectDobot(api, "", 115200)[0]
    print("Connect status:",CON_STR[state])
    if (state == dType.DobotConnect.DobotConnect_NoError):
        return api
    
def dobot_clean(api):
    #Disconnect Dobot
    dType.DisconnectDobot(api)

def dobot_zero(api):
    # Clean Command Queued
    dType.SetQueuedCmdClear(api)
    print ("relocate zero point......")
    #Async Motion Params Setting
    dType.SetHOMEParams(api, home_x, home_y, home_z, home_r, isQueued = 1)
    dType.SetPTPCommonParamsEx(api, 100, 100, isQueued = 1)
    dType.SetHOMECmdEx(api, temp = 0, isQueued = 1)
    #Start to Execute Command Queued 
    dType.SetQueuedCmdStartExec(api)

def transfer(X, Y):
    if(X < 3):  #X 0 1 2
        if(Y>=8):   #Y 8 9 inside
            x = X + 3
            y = Y
            r = zero_r0
        else:   #Y 0 1 2 3 4 5 6 7
            x = X + 3
            y = Y
            r = zero_r0
    elif(X>5):    #X 6 7 8
        x = X - 3

        y = Y
        r = zero_r1
    else:       #X 3 4 5
        if(Y <= 7):   # Y 0 1 2 3 4 5 6 7 right
            x = X
            y = Y + 3
            r = zero_r3
        else: #Y 8 9  outside
            x = X - 3
            y = Y
            r = zero_r1
    return x, y, r

def moveToPoint(api, X, Y):

    x, y, r = transfer(X, Y)
    # move to temp
    print ("move to ({0}, {1}, {2})".format(x, y ,r))
    # move to point
    dType.SetPTPCmdEx(api, dType.PTPMode.PTPJUMPXYZMode, zero_x + 31.5 * x, zero_y + 31.5 * y, 15, r, isQueued = 1)

def dobot_moveDown(api, length):
    position = dType.GetPose(api)
    print ("down ", length)
    lastIndex = dType.SetPTPCmd(api,dType.PTPMode.PTPMOVLXYZMode, position[0], position[1], position[2] - length, position[3], isQueued = 1)
    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)
    #Wait for Executing Last Command 
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api):
         dType.dSleep(100)
    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)

def dobot_pick(api, x, y):
    moveToPoint(api, x, y)
    dobot_moveDown(api, 16.5)
    print ("pick", x, y)
    lastIndex = dType.SetEndEffectorSuctionCup(api, True, True, isQueued=1)
    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)
    #Wait for Executing Last Command 
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api):
         dType.dSleep(100)
    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)
    dType.dSleep(2000)
    dobot_moveDown(api, -16.5)

def dobot_drop(api, x, y):
    moveToPoint(api, x, y)
    dobot_moveDown(api, 8)
    print ("drop", x, y)
    lastIndex = dType.SetEndEffectorSuctionCupEx(api, False, True, isQueued=1)
    #Start to Execute Command Queued
    dType.SetQueuedCmdStartExec(api)
    #Wait for Executing Last Command 
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api):
         dType.dSleep(100)
    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)
    dobot_moveDown(api, -8)

def attack(api, x_enemy, y_enemy, x_my, y_my):
    dobot_pick(api, x_enemy, y_enemy)
    dobot_drop(api, 4, -2)
    dobot_pick(api, x_my, y_my)
    dobot_drop(api, x_enemy, y_enemy)

def test_r():
    api = dobot_init()
    # dobot_zero(api)
    
    # moveToPoint(api, 4, 4)
    
    # for i in range(6, 9):
    #     # dobot_zero(api)
    #     for j in range(0, 10):
    #         print (i, j)
    #         moveToPoint(api, i, j)

    # moveToPoint(api, 2, 3)

    # dobot_pick(api)
    # dobot_moveDown(api,22)
    # dType.dSleep(1000)
    # dobot_drop(api)
    
    # dobot_clean(api)
    
    dType.SetQueuedCmdStartExec(api)
    dType.SetEndEffectorSuctionCupEx(api, 1, 1, isQueued=1)
    dType.SetPTPCmdEx(api, dType.PTPMode.PTPMOVLXYZINCMode, 0, 0, 0, -10, isQueued=1)
    dType.dSleep(2000)
    dType.SetEndEffectorSuctionCupEx(api, 0, 0, isQueued=1)
    dType.SetPTPCmdEx(api, dType.PTPMode.PTPMOVLXYZINCMode, 0, 0, 0, 10, isQueued=1)
    dType.DobotExec(api)

if __name__ == '__main__':
    api = dobot_init()
    dobot_zero(api)
    for i in range(9):
        for j in range(10):
            print ("i =", i, " j =", j)
            moveToPoint(api, i, j)
    # moveToPoint(api, 3, 9)
    # moveToPoint(api, 4, 0)