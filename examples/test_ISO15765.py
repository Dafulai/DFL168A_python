import DFL168A, keyboard
from DFL168A import ISO15765
x,Y=DFL168A.begin('COM4',57600,DFL168A.PROTOCOL.AUTO)
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
        r,VIN=ISO15765.getVIN()
        if r:
            print(VIN)
        else:
            print('fail in VIN') 
        r, DTC_Num,DTC=ISO15765.getDTC() 
        if r:
            print("DTC Num: ")  
            print(DTC_Num) 
            print("DTC: ")  
            print(DTC)  
        else:
            print('fail in getting DTC') 
        r,VehicleSpeed=ISO15765.getVehicleSpeed()
        if r:
            print("Vehicle Speed: %8.3f" % VehicleSpeed)                 
        r=ISO15765.clearDTC()
        if r:
            print('Clear DTC sucess \r\n')   
        else:
            print('fail in clear DTC\r\n') 
             
DFL168A.End()
    