import datetime
import time
import os

def beep_sound():
    if os.name=="nt": #windows
        import winsound
        winsound.Beep(1000,1000)
    else:
        print(f"\a") #bell character
        
        
    
def countdown_timer(hours, minutes, seconds):
    total_seconds = hours *3600 + minutes*60 + seconds
    
    print(f"\n Coundown timer started for {hours}h {minutes}m {seconds}s")
    
    while total_seconds>0:
        h,remainder= divmod(total_seconds,3600)
        m,s= divmod(remainder,60)
        print(f"\nTime remaining: {h:02}:{m:02}:{s:02}")
        time.sleep(1)
        total_seconds-=1
    print(f"\nTime is up!!")
    print(f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    beep_sound()

hours = int(input("Enter hours:"))
minutes = int(input("Enter minutes:"))
seconds = int(input("Enter seconds:"))
countdown_timer(hours, minutes,seconds)