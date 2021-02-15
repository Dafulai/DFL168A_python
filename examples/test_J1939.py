import DFL168A, keyboard
from DFL168A import J1939
from DFL168A.J1939 import PGN61444
x,Y=DFL168A.begin('COM4',57600,DFL168A.PROTOCOL.J1939,250000,1.0)
print("Reason:")
print(Y)
if x and Y!=DFL168A.REASON.SLEEP_WARN:
    #y=DFL168A.ATCommand('AT SP A')
    #DFL168A.DigitalCommand('FEEC')  #Vin
    #DFL168A.DigitalCommand('FEE8')
    #DFL168A.HandleResponse(DFL168A.ReturnStr)
    while True:
        if keyboard.is_pressed('q'):
            break
        print("Sleep Warning True?:")
        print (str(DFL168A.SleepWarning))
        r,VIN=J1939.getVin()
        if r:
            print(VIN)
        else:
            print('fail in VIN') 
        r, DTC_Num,SPN,FMI,CM,OC=J1939.getDTC(DTCFormat=4) 
        if r:
            print("DTC Num: \r\n")  
            print(DTC_Num)  
        else:
            print('fail in getting DTC') 
        r=J1939.clearDTC()
        if r:
            print('Clear DTC sucess \r\n')   
        else:
            print('fail in clear DTC\r\n') 
        r=PGN61444.refresh()    
        if r:
            print("PGN61444 Success") 
            r,lat=PGN61444.getActualEngineTorque()
            if r:
                print('aCtual EngineTorq is %f \r\n'% lat)
            else:
                print('aCtual EngineTorq wrong \r\n') 
            r,lat=PGN61444.getEngineSpeed()
            if r:
                print('Engine speed is %f \r\n'% lat)
            else:
                print('Engine speed wrong \r\n')        
        else:
            print("PGN61444 Fail")       
DFL168A.End()
    