import DFL168A, keyboard
from DFL168A import J1708
x,Y=DFL168A.begin('COM4',57600,DFL168A.PROTOCOL.J1708,250000,1.0)
print("Reason:")
print(Y)
if x and Y!=DFL168A.REASON.SLEEP_WARN:    
    while True:
        if keyboard.is_pressed('q'):
            break
        print("Sleep Warning True?:")
        print (str(DFL168A.SleepWarning))
        '''
        r,VIN=J1708.getVIN()
        if r:
            print(VIN)
        else:
            print('fail in VIN') 
            '''
        r, DTC_Num,MID,PID_SID,IsPID,FMI,IsActive,OccurrenceExist,OccurrenceCount=J1708.getDTC()
        if r:
            print("DTC Num: ")  
            print(DTC_Num) 
            print("MID: ")  
            print(MID)  
            print("PID_SID: ")  
            print(PID_SID)  
            print("IsPID: ")  
            print(IsPID) 
            print("FMI: ")  
            print(FMI) 
            print("IsActive: ")  
            print(IsActive) 
            print("OccurrenceExist: ")  
            print(OccurrenceExist)
            print("OccurrenceCount: ")  
            print(OccurrenceCount) 
        else:
            print('fail in getting DTC') 
             
DFL168A.End()
    