from os import listdir
from SOURCE.DBHandler import dbConnect, dbDisconnect,dbPath
from colorama import Style
import random

# GLOBALS
sep = "@#@"


def doScopeDC(progName,progAdr,myKey):
  try:
    # input(f"progName : {progName} and progAdr : {progAdr} and myKey : {myKey}")
    conn = dbConnect(progName)
    # input(f"we have conn it is : {conn}")
    cur = conn.cursor()
    
    cur.execute(f'''SELECT progName,progAdr,keyID
                FROM "SCOPES" 
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')

    results = cur.fetchall()
    # input(f"results is : {results}")
    dbDisconnect(conn)
    
    if (len(results) != 0):
      return False # The operation has not ran again this data, run it !
    
    else:
      # input("doScopeDC is True")
      return True # The operation has ran once on this data, so don't repeat!
  except Exception as e:
    print(f"Exception : {e}")
    

# if doScopeDC returns False, we do the operation and update the key
# with operation key plus the previous keys
def updateScopeDC(progName,progAdr,myKey):
  try:
    conn = dbConnect(progName)
    cur = conn.cursor()
    
    cur.execute(f'''SELECT progName,progAdr,keyID
                FROM "SCOPES" 
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')
    
    results = cur.fetchall()
    
    if (len(results) != 0):
      # progName = results[0][0]
      # progAdr = results[0][1]
      if results[0][2] == None:
        keyID = ""
      else:
        keyID = results[0][2]
      
      # input(f"ALL :  {progName} {progAdr} {keyID}")
      finalKey = str(keyID) + str(myKey) + sep
    
      cur.execute(f'''UPDATE SCOPES
                  SET keyID="{finalKey}" 
                  WHERE progName="{progName}"
                  AND progAdr="{progAdr}"
                  ''')
      dbDisconnect(conn)
    else:
      print("PROBLEM (NOT GONNA UPDATE KEYID), 1. DUPLICATE WORK OR 2. WRONG USAGE OF DC UPDATE !")
  except Exception as e:
    print(f"Exception : {e}")

# TODO  def doTargetDC()
# progName,progAdr,targetURI,keyID
def doTargetDC(progName,progAdr,targetURI,myKey):
  try:
    conn = dbConnect(progName)
    # input(f"we have conn it is : {conn}")
    cur = conn.cursor()
      
    cur.execute(f'''SELECT progName,progAdr,targetURI,keyID
                FROM "TARGETS"
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND targetURI = "{targetURI}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')
    
    results = cur.fetchall()
    # input(f"results is : {results}")
    dbDisconnect(conn)
    
    if (len(results) != 0):
      # input("I'm going to return FALSE")
      return False # The operation has not ran again this data, run it !
    
    else:
      # input("I'm going to return TRUE")
      # input("doScopeDC is True")
      return True # The operation has ran once on this data, so don't repeat!
  except Exception as e:
    print(f"Exception : {e}")

# TODO  def updateTargetDC
# # progName,progAdr,targetURI,keyID
def updateTargetDC(progName,progAdr,targetURI,myKey):
  try:
    conn = dbConnect(progName)
    cur = conn.cursor()
    
    cur.execute(f'''SELECT progName,progAdr,targetURI,keyID
                FROM "TARGETS" 
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND targetURI = "{targetURI}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')

    results = cur.fetchall()
    
    if (len(results) != 0):
      # progName = results[0][0]
      # progAdr = results[0][1]
      if results[0][3] == None:
        keyID = ""
      else:
        keyID = results[0][3]
      
      # input(f"ALL :  {progName} {progAdr} {keyID}")
      finalKey = str(keyID) + str(myKey) + sep
    
      cur.execute(f'''UPDATE TARGETS
                  SET keyID="{finalKey}" 
                  WHERE progName="{progName}"
                  AND progAdr="{progAdr}"
                  AND targetURI = "{targetURI}"
                  ''')
      dbDisconnect(conn)
    else:
      print("PROBLEM (NOT GONNA UPDATE KEYID), 1. DUPLICATE WORK OR 2. WRONG USAGE OF DC UPDATE !")
  except Exception as e:
    print(f"Exception : {e}")
    
# TODO  def doURLDC()
def doURLDC(progName,progAdr,targetURI,fullURLTxt,myKey):
  try:
    conn = dbConnect(progName)
    cur = conn.cursor()
    
    cur.execute(f'''SELECT progName,progAdr,targetURI,fullURLTxt,keyID
                FROM "URLS"
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND targetURI = "{targetURI}"
                AND fullURLTxt = "{fullURLTxt}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')

    results = cur.fetchall()
    # input(f"results is : {results}")
    dbDisconnect(conn)
    
    if (len(results) != 0):
      return False # The operation has not ran again this data, run it !
    
    else:
      # input("doScopeDC is True")
      return True # The operation has ran once on this data, so don't repeat!
  except Exception as e:
    print(f"Exception : {e}")

# TODO  def updateURLDC()
def updateURLDC(progName,progAdr,targetURI,fullURLTxt,myKey):
  try:
    conn = dbConnect(progName)
    cur = conn.cursor()
    
    cur.execute(f'''SELECT progName,progAdr,targetURI,fullURLTxt,keyID
                FROM "URLS" 
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND targetURI = "{targetURI}"
                AND fullURLTxt = "{fullURLTxt}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')

    results = cur.fetchall()
    
    if (len(results) != 0):
      # progName = results[0][0]
      # progAdr = results[0][1]
      if results[0][4] == None:
        keyID = ""
      else:
        keyID = results[0][4]
      
      # input(f"ALL :  {progName} {progAdr} {keyID}")
      finalKey = str(keyID) + str(myKey) + sep
    
      cur.execute(f'''UPDATE URLS
                  SET keyID="{finalKey}" 
                  WHERE progName="{progName}"
                  AND progAdr="{progAdr}"
                  AND targetURI = "{targetURI}"
                  AND fullURLTxt = "{fullURLTxt}"
                  ''')
      dbDisconnect(conn)
    else:
      print("PROBLEM (NOT GONNA UPDATE KEYID), 1. DUPLICATE WORK OR 2. WRONG USAGE OF DC UPDATE !")  
  except Exception as e:
    print(f"Exception : {e}")

# TODO  def doVULNDC()
def doVULNDC(progName,progAdr,targetURI,fullURLTxt,vulnName,myKey):
  try:
    conn = dbConnect(progName)
    cur = conn.cursor()
    
    cur.execute(f'''SELECT progName,progAdr,targetURI,fullURLTxt,vulnName,keyID
                FROM "VULNS"
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND targetURI = "{targetURI}"
                AND fullURLTxt = "{fullURLTxt}"
                AND vulnName = "{vulnName}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')

    results = cur.fetchall()
    # input(f"results is : {results}")
    dbDisconnect(conn)
    
    if (len(results) != 0):
      return False # The operation has not ran again this data, run it !
    
    else:
      # input("doScopeDC is True")
      return True # The operation has ran once on this data, so don't repeat!
  except Exception as e:
    print(f"Exception : {e}")
  
# TODO  def updateVulnDC()
def updateVULNDC(progName,progAdr,targetURI,fullURLTxt,vulnName,myKey):
  try:
    conn = dbConnect(progName)
    cur = conn.cursor()
    
    cur.execute(f'''SELECT progName,progAdr,targetURI,fullURLTxt,vulnName,keyID
                FROM "VULNS" 
                WHERE progName = "{progName}"
                AND progAdr = "{progAdr}"
                AND targetURI = "{targetURI}"
                AND fullURLTxt = "{fullURLTxt}"
                AND vulnName = "{vulnName}"
                AND (keyID IS NULL OR keyID NOT LIKE "%{myKey}%")
                ''')

    results = cur.fetchall()
    
    if (len(results) != 0):
      # progName = results[0][0]
      # progAdr = results[0][1]
      if results[0][5] == None:
        keyID = ""
      else:
        keyID = results[0][5]
      
      # input(f"ALL :  {progName} {progAdr} {keyID}")
      finalKey = str(keyID) + str(myKey) + sep
    
      cur.execute(f'''UPDATE VULNS
                  SET keyID="{finalKey}" 
                  WHERE progName="{progName}"
                  AND progAdr="{progAdr}"
                  AND targetURI = "{targetURI}"
                  AND fullURLTxt = "{fullURLTxt}"
                  AND vulnName = "{vulnName}"
                  ''')
      dbDisconnect(conn)
    else:
      print("PROBLEM (NOT GONNA UPDATE KEYID), 1. DUPLICATE WORK OR 2. WRONG USAGE OF DC UPDATE !")
  except Exception as e:
    print(f"Exception : {e}")

# TODO  def cleanKEY(progName,tableNAME,key)
def cleanKEY():
  try:
    # lets clean a keys for this table
    print(Style.RESET_ALL + "Welcome to clean KEY function, I will erased keys you say from tables you say!")
    progName = input("enter exit => exit, all => clean key from all programs, "
                    "or simply enter program name : ")
    if progName == "":
      # system("clear")
      cleanKEY() # not good answer entered !
    elif progName == "all":
      tableNAME = input("Please enter the table name you want to clean keys from : ")
      myKey = input("Please enter the key you want to erase from table : ")

      dirs = listdir(dbPath)
      for prog in random.sample(dirs,len(dirs)):
        progName = prog
        
        # Let's find the keyID and delete it:
        try:
          conn = dbConnect(progName)
          cur = conn.cursor()
          
          cur.execute(f'''
                      UPDATE "{tableNAME}" 
                      SET keyID=REPLACE(keyID, "{myKey}@#@", "")
                      WHERE keyID LIKE "%{myKey}%"
                      ''')
          dbDisconnect(conn)
        except:
          pass
    elif progName == "exit":
      return None
    
    else:
      tableNAME = input("Please enter the table name you want to clean keys from : ")
      myKey = input("Please enter the key you want to erase from table : ")
      # check if program exists!
      dirs = listdir(dbPath)
      if progName in random.sample(dirs,len(dirs)):
        try:
          conn = dbConnect(progName)
          cur = conn.cursor()
          cur.execute(f'''
                    UPDATE "{tableNAME}" 
                    SET keyID=REPLACE(keyID, "{myKey}@#@", "")
                    WHERE keyID LIKE "%{myKey}%"
                    ''')
          dbDisconnect(conn)
          print("CLEANED SUCCESSFULLY!")
        except:
          pass
      else:
        print("Program name does not exists!")
        cleanKEY()
  except Exception as e:
    print(f"Exception : {e}")
      
# TODO Add dns record type to targets table 