from SOURCE.DBHandler import *


def initDB(progName):
  # create a database connection to a SQLite database
  conn = dbConnect(progName)
  cur = conn.cursor()
  
  # # Set auto vacum
  # try:  
  #   # CREATE SCOPE TABLE
  #   cur.execute('''PRAGMA auto_vacuum = 1''')
  #   # cur.execute('''VACUUM''')
  # except Exception as e:
  #   print(f"EXCEPTION in SCOPES: {e}")
  
  try:  
    # CREATE SCOPE TABLE
    cur.execute('''CREATE TABLE IF NOT EXISTS SCOPES
      (_id INTEGER PRIMARY KEY AUTOINCREMENT, progName text NOT NULL, progAdr text NOT NULL, progType text NOT NULL DEFAULT "domain", progDsc text, isCritical text DEFAULT 'true', keyID BLOB, lastUpdate DATETIME DEFAULT (datetime('now','localtime')) NOT NULL, UNIQUE(progAdr, progType))''')
  except Exception as e:
    print(f"EXCEPTION in SCOPES: {e}")
  
  try:
    # Create TARGETS table
    # targetURI example = https://api.google.com:8443
    # NOTE: there is not / at the end of targets since this considers a url!
    cur.execute('''CREATE TABLE IF NOT EXISTS TARGETS
      (_id INTEGER PRIMARY KEY AUTOINCREMENT, progName text NOT NULL, progAdr text NOT NULL, targetURI text NOT NULL, statusCode INTEGER NOT NULL, targetTitle TEXT, targetTech TEXT ,isLive text DEFAULT 'true', keyID BLOB, lastUpdate DATETIME DEFAULT (datetime('now','localtime')) NOT NULL, UNIQUE(progName,progAdr,targetURI))''')
  except Exception as e:
    print(f"EXCEPTION in TARGETS: {e}")
  
  try:
    # Create URLS table
    # url = https://api.google.com:8443/dangrousMethod?id=somethingBLAH&sort=uniq
    # progAdr = *.google.com
    # targetURI = https://api.google.com:8443
    # urlTxt = /dangrousMethod
    # params = ?id=somethingBLAH&sort=uniq
    cur.execute('''CREATE TABLE IF NOT EXISTS URLS
      (_id INTEGER PRIMARY KEY AUTOINCREMENT, progName text NOT NULL, progAdr text NOT NULL, targetURI text NOT NULL, fullURLTxt text NOT NULL, statusCode INTEGER, targetTitle TEXT, targetTech TEXT, isLive text DEFAULT 'true', keyID BLOB, lastUpdate DATETIME DEFAULT (datetime('now','localtime')) NOT NULL, UNIQUE(progName,progAdr,targetURI,fullURLTxt))''')
  except Exception as e:
    print(f"EXCEPTION in URLS: {e}")
  
  try:
    cur.execute('''CREATE TABLE IF NOT EXISTS VULNS
      (_id INTEGER PRIMARY KEY AUTOINCREMENT, progName text NOT NULL, progAdr text NOT NULL, targetURI text NOT NULL, fullURLTxt text NOT NULL, vulnCat text NOT NULL, vulnName text NOT NULL, severity text NOT NULL, vulnDsc text, vulnPath text NOT NULL, fullPayload text, isReported text DEFAULT 'false', keyID BLOB, lastUpdate DATETIME DEFAULT (datetime('now','localtime')) NOT NULL, UNIQUE(progName,progAdr,targetURI,fullURLTxt,vulnCat,vulnName,severity,vulnDsc,vulnPath))''')
  except Exception as e:
    print(f"EXCEPTION in VULNS: {e}")
    
  # Save (commit) the changes
  dbDisconnect(conn)
  
