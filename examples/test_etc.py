import DFL168A, keyboard
x,Y=DFL168A.begin('COM4',57600,DFL168A.PROTOCOL.J1708,250000,0.5,9600,1.0)
print("Reason:")
print(Y)
if x and Y!=DFL168A.REASON.SLEEP_WARN: 
    if DFL168A.setSleepDelay(3600):   #delay 1 hour for sleep
        print('DFL168A Sleep delay change to 1 hour')
    while True:
        if keyboard.is_pressed('q'):
            break
        print("Sleep Warning True?:")
        print (str(DFL168A.SleepWarning))
        r,I_button_ID=DFL168A.getOnewireID()
        if r:
            print("I button ID: ")  
            print(I_button_ID)            
        else:
            print('fail in getting I button ID') 
        r, din0=DFL168A.getDIN(0)
        if r:
            print("Din0: ")  
            if din0: print("High") 
            else: print("Low")        
        else:
            print('fail in getting Din0') 
        r, Ain=DFL168A.getAnalog()
        if r:
            print("Analog input: ")  
            print(Ain)        
        else:
            print('fail in getting Analog input')
        r=DFL168A.setDOUT(0,False)
        if r:
            print("Set Dout0 to Low successfully ")                     
        else:
            print('fail in seting Dout0')   
        r=DFL168A.setExitTransparentKey(ord('A'))  #if you don't change default exit charactor, you don't need this statement  
        if r:
            DFL168A.beginTransparentSerial()
            print("Starting access DEV1 transparently ") 
            DFL168A.Ser4DFL168A.write('Hello DFL168A'.encode('utf-8'))
            DFL168A.endTransparentSerial()
            if not DFL168A.TransparentSerialAvailable:
                print('DFL168A end transparent mode, and resume to normal mode')
            else:
                print('Fail in ending transparent mode')
                break
DFL168A.End()
    