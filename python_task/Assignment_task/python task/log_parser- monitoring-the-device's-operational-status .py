#In simple terms, this code reads a log file to: 
#  1. Calculate Device ON Duration: Identifies when the device was turned ON and OFF, calculates the duration it was ON, and prints this duration.
#  2. Record Error Timestamps: Collects and prints the timestamps when the device encountered errors.
# The script helps in monitoring the device's operational status and identifying periods of errors by analyzing the log file.

from datetime import datetime
'''
def readlogfile(filename1):
    with open(filename1, 'r') as file:
        for line in file:
            print(line.strip())  
    

if __name__ == "__main__":
    filename1 = "filename.txt"  
    readlogfile(filename1)

'''

def parselogfile(filename1):
  
   
    error_timestamps=[]
    with open(filename1, 'r') as file:
        for line in file:

            if "Device State: ON" in line:    
                          
                        device_stime = datetime.strptime(line[:15], "%b %d %H:%M:%S")
                
            elif  "Device State: OFF" in line:
                   
                        device_etime = datetime.strptime(line[:15], "%b %d %H:%M:%S")
                        duration = device_etime - device_stime
                        print("Device was on for :", duration , "seconds")

            elif "Device State: ERR" in line:
                    error_timestamps.append(datetime.strptime(line[:15], "%b %d %H:%M:%S"))      
     

    if error_timestamps:
        print("\n  Timestamps of error event :")
        for timestamp in error_timestamps:
            print("  ",timestamp)




if __name__ == "__main__":
    filename1 = "filename.txt"
    parselogfile(filename1)
    
    

