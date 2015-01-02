from sys import stdout
from time import sleep
import serial
import MySQLdb
import sys
from math import *

ser = serial.Serial('/dev/ttyACM0', 57600)

#------------------------------------------------------------------------------
#-------------------------- Database settings ---------------------------------
#------------------------------------------------------------------------------
cursor = None
db = None

mySQLHost = "localhost";
mySQLUser = "root";
mySQLdb   = "****";
mySQLpw   = "****";


#------------------------------------------------------------------------------
# Function...: startMySQL
# Return.....: true if connection refused else false
# Description: starting mySQL connection
# Created....: 02.02.2013 by Achuthan
# Modified...: 
#------------------------------------------------------------------------------
def startMySQL():
    
    global cursor, db
    try:
        # Open database connection
        db = MySQLdb.connect(host = mySQLHost, user = mySQLUser, db=mySQLdb, passwd = mySQLpw)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        print("Connected to MySQL DB")
        return 0
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        return 1


#------------------------------------------------------------------------------
# Function...: closeMySQL
# Return.....: void
# Description: close the  connection
# Created....: 02.02.2013 by Achuthan
# Modified...: 
#------------------------------------------------------------------------------        
def closeMySQL():
    # disconnect from server
    db.close()


#------------------------------------------------------------------------------
# Function...: sendMySQLQry
# Return.....: return false if sucess else true
# Description: send a simple MySQL qry
# Created....: 02.02.2013 by Achuthan
# Modified...: 
#------------------------------------------------------------------------------        
def sendMySQLQry(qry):
    try:
        print "done"
        cursor.execute(qry);
        db.commit();
        return 0
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        print("Reconnecting to MySQL")
        if(startMySQL()):
            print("MySQL DOWN")
        return 1   


def getSerialData():
    try:
        line = ser.readline()
        data = line.rstrip('\r')
        data = data.rstrip('\n')
        data = data.split(' ');
        if data != ' ':
           print data
           qry = """UPDATE temperature SET temp=%s, seq=%s WHERE id='%s'""" % (data[3],data[4],data[0])
           sendMySQLQry(qry)
           if(1):
                   if(1==data[0]):
                       qry = """INSERT INTO tempMeas (room, step, temp, hum) VALUES ('%s', '%s','%s', '%s')""" % ('Living Room',data[4],data[3],data[2]);
                       sendMySQLQry(qry)
                   elif(2==data[0]):
                       qry = """INSERT INTO tempMeas (room, step, temp, hum) VALUES ('%s', '%s','%s', '%s')""" % ('Master Bedroom',data[4],data[3],data[2]);
                       sendMySQLQry(qry)
                   elif(3==data[0]):
                       qry = """INSERT INTO tempMeas (room, step, temp, hum) VALUES ('%s', '%s','%s', '%s')""" % ('Out',data[4],data[3],data[2]);
                       sendMySQLQry(qry)
                       
    except (KeyboardInterrupt, SystemExit):
            ser.close()
            closeMySQL()



    
    
    
        
#------------------------------------------------------------------------------
# Function...: main
# Return.....: void
# Description: main Function.
# Created....: 02.02.2013 by Achuthan
# Modified...: 
#------------------------------------------------------------------------------
def main():

    #Try connect to MySQL
    if(startMySQL()):
        print("Closing")
        
        #sys.exit (1)
    #If we get conenction
    else:
        while True:
            getSerialData()
            
                
                       
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        closeMySQL()
        print ("Closing")