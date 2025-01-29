from SOURCE.DBHandler import dbConnect,dbDisconnect,dbPath


def queryStats(targetName):
  conn = dbConnect(targetName)
  if conn: # if database exists:
    try:
      # DB MAGIC
      cur = conn.cursor()
      # Create TARGETS table       
      # Sample insert a row of data
      cur.execute('''select count(DISTINCT _id) from SCOPES''')
      numScopes = cur.fetchone()[0]
      cur.execute('''select count(DISTINCT _id) from TARGETS''')
      numTAR = cur.fetchone()[0]
      cur.execute('''select count(DISTINCT _id) from URLS''')
      numURL = cur.fetchone()[0]
      cur.execute('''select count(DISTINCT _id) from VULNS where (isReported = 'true')''')
      numVULNReported = cur.fetchone()[0]
      cur.execute('''select count(DISTINCT _id) from VULNS where (isReported = 'false')''')
      numVULNNotReported = cur.fetchone()[0]
      # Save (commit) the changes
      dbDisconnect(conn)
      return(numScopes,numTAR,numURL,numVULNReported,numVULNNotReported)
      # except Exception as e:
      # print(f"Exception occured as : {e}") 
    except:
      pass
      # input("Continue?")
  else:
    pass