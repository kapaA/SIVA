import serial
from datetime import datetime
import time, sys

ser = serial.Serial('/dev/ttyACM0', 115200)

#------------------------------------------------------------------------------
#-------------------------- Database settings ---------------------------------
#------------------------------------------------------------------------------


def getSerialData():
    
    
    try:
        line = ser.readline()
        data = line.rstrip('\r')
        data = data.rstrip('\n')
        data = data.split(' ');
        if data != ' ':
           if (len(data) == 6 ):
              print data
              with open("test.txt", "a") as myfile:
                  s = "{} {} {} {} {} {}\n".format(data[0],data[1],data[2],data[3],data[4],data[5])
                  myfile.write(s)
              myfile.close()

    except (KeyboardInterrupt, SystemExit):
            ser.close()
            



    
    
    
        
#------------------------------------------------------------------------------
# Function...: main
# Return.....: void
# Description: main Function.
# Created....: 02.02.2013 by Achuthan
# Modified...: 
#------------------------------------------------------------------------------
def main():


    while True:
        getSerialData()
            
                
                       
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        closeMySQL()
        print ("Closing")