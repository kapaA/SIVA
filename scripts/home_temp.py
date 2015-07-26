import serial
import MySQLdb
from datetime import datetime
from pytz import timezone
import time, sys
from terminaltables import AsciiTable, DoubleTable

ser = serial.Serial('/dev/ttyACM0', 115200)

#------------------------------------------------------------------------------
#-------------------------- Database settings ---------------------------------
#------------------------------------------------------------------------------
cursor = None
db = None

mySQLHost = "localhost";
mySQLUser = "root";
mySQLdb   = "siva";
mySQLpw   = "draco";


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
           if (len(data) == 6 ):
               table_data = [
               ['Device','dest','type','seq','bat', 'temp'],
               [data[0],data[1],data[2],data[3],data[4],data[5]]
               ]
               table = DoubleTable(table_data, 'Shiva Home Control')
               table.inner_row_border = True
               table.justify_columns[2] = 'right'
               print(table.table)
               if('4' == data[0]):
                   with open("test.txt", "a") as myfile:
                       now_utc = datetime.now(timezone('CET'))
                       t = now_utc.strftime("%Y-%m-%d %H:%M:%S")
                       s = "{}: {} {} {} {} {} {}\n".format(t, data[0],data[1],data[2],data[3],data[4],data[5])
                       myfile.write(s)
                   myfile.close()
                   
               if('1' == data[0]):
                   with open("test_solar.txt", "a") as myfile:
                       now_utc = datetime.now(timezone('CET'))
                       t = now_utc.strftime("%Y-%m-%d %H:%M:%S")
                       s = "{}: {} {} {} {} {} {}\n".format(t, data[0],data[1],data[2],data[3],data[4],data[5])
                       myfile.write(s)
                   myfile.close()
              
               if('2' == data[0]):
                   with open("test_solar_2.txt", "a") as myfile:
                       now_utc = datetime.now(timezone('CET'))
                       t = now_utc.strftime("%Y-%m-%d %H:%M:%S")
                       s = "{}: {} {} {} {} {} {}\n".format(t, data[0],data[1],data[2],data[3],data[4],data[5])
                       myfile.write(s)
                   myfile.close()
                   
               if('3' == data[0]):
                   with open("test_solar_3.txt", "a") as myfile:
                       now_utc = datetime.now(timezone('CET'))
                       t = now_utc.strftime("%Y-%m-%d %H:%M:%S")
                       s = "{}: {} {} {} {} {} {}\n".format(t, data[0],data[1],data[2],data[3],data[4],data[5])
                       myfile.write(s)
                   myfile.close()
                   
                   
               if('5' == data[0]):
                   with open("test_solar_5.txt", "a") as myfile:
                       now_utc = datetime.now(timezone('CET'))
                       t = now_utc.strftime("%Y-%m-%d %H:%M:%S")
                       s = "{}: {} {} {} {} {} {}\n".format(t, data[0],data[1],data[2],data[3],data[4],data[5])
                       myfile.write(s)
                   myfile.close()     
                   
              #sys.stdout.write('%s %s %s %s\r' % (data[0], data[2], data[3], data[4]))
               #sys.stdout.flush()
               if('1'==data[0]):
                   loc = "Living Room"
               elif('2'==data[0]):
                   loc = "out"
               elif('3'==data[0]):
                   loc = "out"
               elif('4'==data[0]):
                   loc = "out"
               elif('5'==data[0]):
                   loc = "out" 
               elif('6'==data[0]):
                   loc = "out"     
               else:
                   loc = "undefined error"
                   return 0
                   
                   
               now_utc = datetime.now(timezone('CET'));
               t = now_utc.strftime("%Y-%m-%d %H:%M:%S");  
               
               qry = """UPDATE temperature SET  seq=%s, temp=%s, bat=%s WHERE id='%s'""" % (data[3],data[5],data[4],data[0])
               sendMySQLQry(qry)
    
               if('6' == data[2]):
                   #  0     1      2     3     4      5     6
                   # ID | DEST | TYPE | SEQ | BAT | TEMP | HUM
                   qry = """INSERT INTO tempMeas (id, room, seq, bat, temp, hum, time) VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s')""" % (data[0], loc, data[3], data[4],data[5], data[5] ,t);
                   sendMySQLQry(qry)
                   
           else:
               print "invalid data"
               print data

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