import serial
import MySQLdb
from datetime import datetime
from pytz import timezone
import time, sys
from terminaltables import AsciiTable, DoubleTable

ser = serial.Serial('/dev/ttyACM0', 57600)

#------------------------------------------------------------------------------
#-------------------------- Database settings ---------------------------------
#------------------------------------------------------------------------------
cursor = None
db = None

mySQLHost = "localhost";
mySQLUser = "root";
mySQLdb   = "siva";
mySQLpw   = "xxxx";


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
    
    table_data = []
    
    try:
        line = ser.readline()
        data = line.rstrip('\r')
        data = data.rstrip('\n')
        data = data.split(' ');
        if data != ' ':
           if (len(data) == 5 ):
               table_data = [
               ['Device','temp','hum','seq'],
               [data[0],data[3],data[2],data[4]]
               ]
               table = DoubleTable(table_data, 'Shiva Home Control')
               table.inner_row_border = True
               table.justify_columns[2] = 'right'
               print(table.table)
               #sys.stdout.write('%s %s %s %s\r' % (data[0], data[2], data[3], data[4]))
               #sys.stdout.flush()
               if('1'==data[0]):
                   loc = "Living Room"
               elif('2'==data[0]):
                   loc = "Master Bedroom"
               elif('3'==data[0]):
                   loc = "out"
               else:
                   loc = "undefined error"
                   
                   return 0
                   
               qry = """UPDATE temperature SET temp=%s, hum=%s, seq=%s WHERE id='%s'""" % (data[3],data[2],data[4],data[0])
               sendMySQLQry(qry)
    
               now_utc = datetime.now(timezone('CET'))
               t = now_utc.strftime("%Y-%m-%d %H:%M:%S");
               
               qry = """INSERT INTO tempMeas (id, room, step, temp, hum, time) VALUES ('%s', '%s', '%s','%s', '%s', '%s')""" % (data[0], loc, data[4], data[3],data[2], t);
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