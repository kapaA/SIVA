import MySQLdb
import sys


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
        qry = """INSERT INTO ean13Barcodes (mainCategory,subCategory,barcode,name,quantity,expiryDate) VALUES ('%s', '%s','%s', '%s','%s', '%s')""" % ('comestible','meat',59092,"acp",1,'2014-05-18');
        sendMySQLQry(qry)
        closeMySQL()




























if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        closeMySQL()
        print ("Closing")