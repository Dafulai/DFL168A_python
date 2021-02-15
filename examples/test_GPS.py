import DFL168A, keyboard
from DFL168A import GPS
x,Y=DFL168A.begin('COM4',57600,DFL168A.PROTOCOL.J1708,250000,0.5,9600,1.0)
print("Reason:")
print(Y)
if x and Y!=DFL168A.REASON.SLEEP_WARN:    
    while True:
        if keyboard.is_pressed('q'):
            break
        print("Sleep Warning True?:")
        print (str(DFL168A.SleepWarning))
        r,Latitude,Longitude,Speed, Time,Date=GPS.getGPSinfo()
        if r:
            print("Latitude: ")  
            print(Latitude) 
            print("Longitude: ")  
            print(Longitude)  
            print("Speed: ")  
            print(Speed)  
            print("Time: ")  
            print(Time) 
            print("Date: ")  
            print(Date) 
        else:
            print('fail in getting GPS information') 
        r, Altitude=GPS.getAltitude()
        if r:
            print("Altitude: ")  
            print(Altitude)             
        else:
            print('fail in getting Altitude') 
        
             
DFL168A.End()
    