import sqlite3


# GLOBALS
bountyPath = "/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/"
dbPath = bountyPath + "tupiRepo/Bunter/DB/"

# NOTE (IMPORTANT) : This function takes NAME OF DB ONLY and HANDLES THE PATH ITSELF, just send DB name!
def dbConnect(progName):
  dbFile = dbPath + progName
  conn = None
  try:
    # DB MAGIC
    conn = sqlite3.connect(dbFile)
    if conn:
      #print(f"Database connected successfully!")
      return conn
    else:
      print("NO DB FILE FOUND!")
      return False
  # except Exception as e:
    # print(f"EXCEPTION : {e}")

  except: 
    pass
    
def dbDisconnect(connObject):
  #print(f"Database commited successfully!")
  if connObject:
    connObject.commit()
    connObject.close()
    #print(f"Database closed successfully!")

def insertToScopes(progName,progAdr,progType,progDsc):
  conn = dbConnect(progName)
  cur = conn.cursor()
  try:
    cur.execute('''INSERT INTO SCOPES (progName,progAdr,progType,progDsc) VALUES (?,?,?,?)''',(progName,progAdr,progType,progDsc))
  except Exception as e:
    print(f"EXCEPTION : {e}")
  # except:
  #   pass
  dbDisconnect(conn)

def inserToTargets(progName,progAdr,targetURI,statusCode,targetTitle,targetTech,isLive):
  conn = dbConnect(progName)
  cur = conn.cursor()
  try:
    cur.execute('''INSERT INTO TARGETS (progName,progAdr,targetURI,statusCode,targetTitle,targetTech,isLive) VALUES (?,?,?,?,?,?,?)''',(progName,progAdr,targetURI,statusCode,targetTitle,targetTech,isLive))
  except Exception as e:
    print(f"EXCEPTION : {e}")
  # except:
  #   pass
  dbDisconnect(conn)

def inserToURLS(progName,progAdr,targetURI,fullURLTxt):
  try:
    conn = dbConnect(progName)
    cur = conn.cursor()
    cur.execute('''INSERT INTO URLS (progName,progAdr,targetURI,fullURLTxt) VALUES (?,?,?,?)''',(progName,progAdr,targetURI,fullURLTxt))
    # except Exception as e:
      # print(f"EXCEPTION inserToURLS: {e}")
    # except:
    #   pass
    dbDisconnect(conn)
  except Exception as e:
    print(f"Exception : {e}")

def inserToURLSBatch(progName,progAdr,targetURI,fullURLTxtFile):
  # try:
    
  conn = dbConnect(progName)
  cur = conn.cursor()
  # try:
  for fullURLTxt in fullURLTxtFile:
    try:
      cur.execute('''INSERT INTO URLS (progName,progAdr,targetURI,fullURLTxt) VALUES (?,?,?,?)''',(progName,progAdr,targetURI,fullURLTxt))
# except Exception as e:
    # print(f"EXCEPTION inserToURLS: {e}")
    except Exception as e:
      print(f"Exception : {e}")
  dbDisconnect(conn)
  # except Exception as e:
  #   print(f"Exception : {e}")
  
def inserToURLS4Crawler(progName,progAdr,targetURI,fullURLTxtFile):
  # try:
  conn = dbConnect(progName)
  cur = conn.cursor()
  # try:
    # input("Before inserting to DB")
  for fullURLTxt in fullURLTxtFile:
    try:
      cur.execute('''INSERT INTO URLS (progName,progAdr,targetURI,fullURLTxt) VALUES (?,?,?,?)''',(progName,progAdr,targetURI,fullURLTxt['url']))
    except Exception as e:
      print(f"EXCEPTION inserToURLS: {e}")
  # except:
  #   pass
  dbDisconnect(conn)
  # except Exception as e:
  #   print(f"Exception: {e}")

# (progName,progAdr,targetURI,fullURLTxt,vulnCat,vulnName,severity,vulnDsc text,vulnPath,fullPayload)

def inserToVULNS(progName,progAdr,targetURI,fullURLTxt,vulnCat,vulnName,severity,vulnDsc,vulnPath,fullPayload):
  conn = dbConnect(progName)
  cur = conn.cursor()
  try:
    cur.execute('''INSERT INTO VULNS (progName,progAdr,targetURI,fullURLTxt,vulnCat,vulnName,severity,vulnDsc,vulnPath,fullPayload) VALUES (?,?,?,?,?,?,?,?,?,?)''',(progName,progAdr,targetURI,fullURLTxt,vulnCat,vulnName,severity,vulnDsc,vulnPath,fullPayload))
  except Exception as e:
    print(f"EXCEPTION insertToVULNS: {e}")
  # except:
  #   pass
  dbDisconnect(conn)

def customSQLQuery(progName,fullQuery):
  conn = dbConnect(progName)
  cur = conn.cursor()
  try:
    #return(cur.execute(fullQuery))
    cur.execute(fullQuery)
    return(cur.fetchall())
  # except Exception as e:
    # print(f"EXCEPTION in customSQLQuery: {e}")
  except:
    pass
  dbDisconnect(conn)
  
def queryTableLU(progName,tblName):
  conn = dbConnect(progName)
  cur = conn.cursor()
  cusQu = f"SELECT lastUpdate FROM {tblName} ORDER BY _id DESC LIMIT 1;"
  cur.execute(cusQu)
  
  for item in cur.fetchall():                                                             
    return item[0]
