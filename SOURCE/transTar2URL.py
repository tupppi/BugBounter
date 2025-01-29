import random
from SOURCE.DBHandler import customSQLQuery,dbPath
from progress.bar import IncrementalBar
from os import listdir
from SOURCE.doubleCheck import doTargetDC,updateTargetDC
from SOURCE.targetDiscover import urlQueryAPI,letsCrawl
  


def simpleURLMethod(progName):
  myKey = "f84ef9a94fe09754395f085e11706dcb"
  pass

def queryURLMethod(progName):
  myKey = "6c60eedafccddbbce495b68f57fd7d63"
  if (progName == "all") or (progName == ""): # do this on all programs
    
    dirs = listdir(dbPath)
    bar = IncrementalBar('transTar2URL.py => queryURLMethod()', max=len(dirs))
    for dbFile in random.sample(dirs, len(dirs)):
      progName = dbFile
      # lets extract simple targets in scope file
      # input(f"dbFile is : {dbFile}")
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progName,progAdr,targetURI from TARGETS where (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        random.shuffle(listOfTargets)
        
        if len(listOfTargets) != 0:
          listOfTargets = [(row[0],row[1],row[2]) for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar2 = IncrementalBar('transTar2URL.py => queryURLMethod()', max=len(listOfTargets))
            # system("clear")
            for step in range(len(listOfTargets)):
              progName = listOfTargets[step][0]
              progAdr = listOfTargets[step][1]
              targetURI = listOfTargets[step][2]
              
              # input(f"we are inside loop for listOfTargets (BEFORE doTargetDC!) : "
              #       f"progName : {progName}, progAdr : {progAdr}, targetURI = {targetURI}")
              # if not doTargetDC(progName,progAdr,targetURI,myKey): # if operation is not done before!
              urlQueryAPI(progName,progAdr,targetURI)
              updateTargetDC(progName,progAdr,targetURI,myKey)
              bar2.next()
            bar2.finish()
      except Exception as e:
        print(f"EXCEPTION: {e}")
      # except:
      #   pass
        # Let's run it again if failed.
        # queryURLMethod(progName)
      
      bar.next()
    bar.finish()
  else: # program name is specified
    dirs = listdir(dbPath)
    if progName in random.sample(dirs, len(dirs)):
      dbFile = progName
      
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progName,progAdr,targetURI from TARGETS where (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [(row[0],row[1],row[2]) for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar = IncrementalBar('transTar2URL.py => queryURLMethod()', max=len(listOfTargets))
            for step in range(len(listOfTargets)):
              progName = listOfTargets[step][0]
              progAdr = listOfTargets[step][1]
              targetURI = listOfTargets[step][2]
              # input(f"we are in for loop and tar is : {tar}")
              # if not doTargetDC(progName,progAdr,targetURI,myKey): # if operation is not done before!
              urlQueryAPI(progName,progAdr,targetURI)
              updateTargetDC(progName,progAdr,targetURI,myKey)
              bar.next()
            bar.finish()
      except Exception as e:
        print(f"EXCEPTION : {e}")
      # except:
      #   pass

def crawlerMethod(progName):
  myKey = "3c712b39d6c6bagb9b123d170y4c599c"
  
  if (progName == "all"):
    pass
    # will write this part later
  else:
    dirs = listdir(dbPath)
    if progName in random.sample(dirs, len(dirs)):
      dbFile = progName
      
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progName,progAdr,targetURI from TARGETS where (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        random.shuffle(listOfTargets)
        if len(listOfTargets) != 0:
          listOfTargets = [(row[0],row[1],row[2]) for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar = IncrementalBar('transTar2URL.py => crawlerMethod()', max=len(listOfTargets))
            for step in range(len(listOfTargets)):
              progName = listOfTargets[step][0]
              progAdr = listOfTargets[step][1]
              targetURI = listOfTargets[step][2]
              # input(f"we are in for loop and tar is : {tar}")
              # if not doTargetDC(progName,progAdr,targetURI,myKey): # if operation is not done before!
              letsCrawl(progName,progAdr,targetURI)
              updateTargetDC(progName,progAdr,targetURI,myKey)
              bar.next()
            bar.finish()
      except Exception as e:
        print(f"EXCEPTION : {e}")
      # except:
      #   pass
    
  
  



def dictURLMethod(progName):
  myKey = "3c7c8b39d616ba0b9b72fd170f4c599c"
  pass

def bruteforceURLMethod(progName):
  myKey = "d6e8a48272ae054960312f60b502f227"
  pass
