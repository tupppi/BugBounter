# This function does multiple actions when called.
# 1. Add all simple targets from scopes table. things like google.com
# => for programs with scope *. =>
# 2. Do reconme methods and add all queried targets to target table.
# 3. Use a wordlist for finding new domains on starred ones.
# 4. bruteforce for finding new dns zones
# 5. Any other new method will be added to the above.
# SUMMARY : 
# method#1: Add simple targets
# method#2: queryMethod(apis, subfinder, assetfinder, ...), for *.DOMAINS
# method#3: wordListMethod(growing wordlist, testing agains each target in scopes), for *.DOMAINS
# method#4: bruteforceMethod(fierce or custom bruteforce), for *.DOMAINS
# check for last update : SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
# we move laterally or horizontally not vertical. so one action per all programs. specially for up to VULNs. for exmaple we fetch all scope files and bring them to DB. we add all simple targets. these two can run on startup.
# we add query based targets for all programs first.
# we add query based urls for all programs first.
# we run vulns based on last record's lastUpdate
from SOURCE.StatsDump import dbPath
from SOURCE.targetDiscover import tarHTTPXDiscovery
from SOURCE.DBHandler import customSQLQuery
from os import listdir
import random
import subprocess,fileinput
from progress.bar import IncrementalBar
from SOURCE.doubleCheck import doScopeDC, updateScopeDC
import dns.resolver


#****************************#
# AUX MODULES USED BY OTHERS:
# Finds dubdomains of a target based on subfinder, amass and others
def subDomQuery(progName,candidateDomain,mainProgAdr):
  nowTmp = random.random()
  subprocess.getoutput(f"rm -f ./'{nowTmp}'")
  subprocess.getoutput(f"subfinder -d {candidateDomain} >> {nowTmp};")
  subprocess.getoutput(f"assetfinder -subs-only {candidateDomain} >> {nowTmp};")
  subprocess.getoutput(f"findomain -t {candidateDomain} >> {nowTmp};")
  subprocess.getoutput(f"sublist3r -d {candidateDomain} >> {nowTmp};")
  nowTmp2 = random.random()
  subprocess.getoutput(f"cat {nowTmp} | grep -i '{candidateDomain}' | grep -iv '@' | grep -iv 'Enumerating subdomains now for' | sort -u > {nowTmp2};")
  
  try:
    with open(f"{nowTmp2}") as FileObj:
      bar = IncrementalBar('transScopesTargets.py => subDomQuery()',max=int(subprocess.getoutput(f"wc -l {nowTmp2} | cut -d \" \" -f 1")))
      # system("clear")
      for lines in FileObj:
        tarHTTPXDiscovery(progName,lines,mainProgAdr)
        bar.next()
      bar.finish()
      
  # except Exception as e:
  #   print(f"EXCEPTION IS {e}")
  except:
    pass
  
  subprocess.getoutput(f"rm -f ./'{nowTmp}'")
  subprocess.getoutput(f"rm -f ./'{nowTmp2}'")
  subprocess.getoutput(f"rm -f ./'{candidateDomain}'")

# Checks each scope *. item with a dictionary
# Candidates with correct A or CNAME records will be sent to tarHTTPXDiscovery 
# From tarHTTPXDiscovery on the rest of the work is token care of
def subDomDict(progName,candidateDomain,mainProgAdr,runMode):
  # tarHTTPXDiscovery(progName,lines,mainProgAdr)
  #  git clone https://github.com/rbsec/dnscan
  # DICT_PATH = '/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/Other_Resources/dnscan/dict/Final.txt'
  if runMode == "long":
    DICT_PATH = '/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/Other_Resources/dnscan/dict/Final-6MIL.txt'
  else:
    DICT_PATH = '/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/Other_Resources/dnscan/dict/Final-1MIL.txt'
  
  # with open('/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/Other_Resources/dnscan/dict/Final.txt') as f:
    # lines = f.readlines()
    # bar = IncrementalBar('transScopesTargets.py => subDomDict()', max=len(lines))
  bar = IncrementalBar('transScopesTargets.py => subDomDict()', max=(int(subprocess.getoutput(f"wc -l {DICT_PATH} | cut -d ' ' -f 1"))))
  for line in fileinput.input(DICT_PATH):
    candidate = line.rstrip() + f'.{candidateDomain}'
    try:
      result = dns.resolver.resolve(candidate, 'A')
      if len(result) != 0:
        tarHTTPXDiscovery(progName,candidate,mainProgAdr)
    except:
      try:
        result = dns.resolver.resolve(candidate, 'CNAME')
        if len(result) != 0:
          tarHTTPXDiscovery(progName,candidate,mainProgAdr)
      except:
        pass
    
    bar.next()
  bar.finish()



#****************************#
def simpleTARMethod(progName):
  myKey = "e7c601b5f1af9a4fafc3fead47d6ab0e"
  
  if (progName == "all") or (progName == ""): # do this on all programs
    
    dirs = listdir(dbPath)
    bar = IncrementalBar('transScopesTargets.py => simpleTARMethod()', max=len(dirs))
    for dbFile in random.sample(dirs, len(dirs)):
      progName = dbFile
      # lets extract simple targets in scope file
      # input(f"dbFile is : {dbFile}")
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr not like '*.%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          # input(f"listOfTargets : {listOfTargets}")
          listOfTargets = [row[0] for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar2 = IncrementalBar('transScopesTargets.py => simpleTARMethod()', max=len(listOfTargets))
            # system("clear")
            for tar in listOfTargets:
              # input(f"we are in for loop and tar is : {tar}")
              # if not doScopeDC(progName,tar,myKey): # if operation is not done before!
              mainProgAdr = tar 
              tarHTTPXDiscovery(dbFile,tar,mainProgAdr)
              updateScopeDC(progName,tar,myKey)
              bar2.next()
            bar2.finish()
      # except Exception as e:
        # print(f"EXCEPTION IN line 45: {e}")
      except:
        pass  
      
      bar.next()
    bar.finish()
  else: # program name is specified
    dirs = listdir(dbPath)
    if progName in random.sample(dirs, len(dirs)):
      dbFile = progName
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr not like '*.%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [row[0] for row in listOfTargets]
          # print("List of targets for program {progName} :")
          # print(listOfTargets)
          if len(listOfTargets) != 0:
            bar = IncrementalBar('transScopesTargets.py => simpleTARMethod()', max=len(listOfTargets))
            # system("clear")
            for tar in listOfTargets:
              # if not doScopeDC(progName,tar,myKey): # if operation is not done before!
              mainProgAdr = tar 
              tarHTTPXDiscovery(dbFile,tar,mainProgAdr)
              updateScopeDC(progName,tar,myKey)
              bar.next()
            bar.finish()
      except:
        pass  
    else:
      print("not found")

def queryTARMethod(progName):
  myKey = "d0fc58b55fcca942f8306629b5f70135"
  
  # The same as simpleTARMethod
  if (progName == "all") or (progName == ""): # do this on all programs
    
    dirs = listdir(dbPath)
    bar = IncrementalBar('transScopesTargets.py => queryTARMethod()', max=len(dirs))
    for dbFile in random.sample(dirs, len(dirs)):
      progName = dbFile
      
      # lets extract simple targets in scope file
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr like '*.%' and progAdr not like '%.*%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [row[0] for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar2 = IncrementalBar('transScopesTargets.py => queryTARMethod()', max=len(listOfTargets))
            # system("clear")
            for tar in listOfTargets:
              progAdr = tar
              # if not doScopeDC(progName,progAdr,myKey): # if operation is not done before!
              mainProgAdr = tar
              # delete *. from the domain:
              tar = tar.replace("*.","")
              
              # lets go and find the subdomains of this
              subDomQuery(dbFile,tar,mainProgAdr) # program name + *.google.com for example
              # print(dbFile,tar)
              updateScopeDC(progName,progAdr,myKey)
              bar2.next()
            bar2.finish()
      except:
        pass
      bar.next()
    bar.finish()
    
  else: # program name is specified
    dirs = listdir(dbPath)
    if progName in random.sample(dirs,len(dirs)):
      dbFile = progName
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr like '*.%' and progAdr not like '%.*%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [row[0] for row in listOfTargets]
      
          if len(listOfTargets) != 0:
            bar = IncrementalBar('transScopesTargets.py => queryTARMethod()', max=len(listOfTargets))
            # system("clear")

            for tar in listOfTargets:
              progAdr = tar
              # delete *. from the domain:
              # if not doScopeDC(progName,progAdr,myKey): # if operation is not done before!
              mainProgAdr = tar
              tar = tar.replace("*.","")
              
              # lets go and find the subdomains of this
              subDomQuery(dbFile,tar,mainProgAdr) # program name + *.google.com for example
              # print(dbFile,tar)
              updateScopeDC(progName,progAdr,myKey)
              bar.next()
            bar.finish()
      except:
        pass  
    else:
      print("not found")
  
def dictTARMethod(progName):
  myKey = "d4926182c5c2dd7222f2ab5fdc83e1d5"
  
  # on each run update the dictionary of subdomains
  # based on current subdomains
  # print("Update the subdubdomain candidates dictionary file.\n")
  # subDomDICTUpdate()
  
  # The same as simpleTARMethod
  if (progName == "all") or (progName == ""): # do this on all programs
    
    dirs = listdir(dbPath)
    bar = IncrementalBar('transScopesTargets.py => dictTARMethod()', max=len(dirs))
    for dbFile in random.sample(dirs, len(dirs)):
      progName = dbFile
      
      # lets extract simple targets in scope file
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr like '*.%' and progAdr not like '%.*%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [row[0] for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar2 = IncrementalBar('transScopesTargets.py => dictTARMethod()', max=len(listOfTargets))
            # system("clear")
            for tar in listOfTargets:
              progAdr = tar
              # if not doScopeDC(progName,progAdr,myKey): # if operation is not done before!
              mainProgAdr = tar
              # delete *. from the domain:
              tar = tar.replace("*.","")
              
              # lets go and find the subdomains of this
              subDomDict(dbFile,tar,mainProgAdr,"short") # program name + *.google.com for example
              # print(dbFile,tar)
              updateScopeDC(progName,progAdr,myKey)
              bar2.next()
            bar2.finish()
      except:
        pass
      bar.next()
    bar.finish()
    
  else: # program name is specified
    dirs = listdir(dbPath)
    if progName in random.sample(dirs,len(dirs)):
      dbFile = progName
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr like '*.%' and progAdr not like '%.*%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [row[0] for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar = IncrementalBar('transScopesTargets.py => dictTARMethod()', max=len(listOfTargets))
            # system("clear")
            for tar in listOfTargets:
              progAdr = tar
              # if not doScopeDC(progName,progAdr,myKey): # if operation is not done before!
              mainProgAdr = tar
              # delete *. from the domain:
              tar = tar.replace("*.","")
              
              # lets go and find the subdomains of this
              subDomDict(dbFile,tar,mainProgAdr,"short") # program name + *.google.com for example
              # print(dbFile,tar)
              updateScopeDC(progName,progAdr,myKey)
              bar.next()
            bar.finish()
      except:
        pass
    else:
      print("not found")

def dictTARMethod_LONGRUN(progName):
  myKey = "99988111123e6fbca5e8d545ffcf0bf1"
  
  # The same as dictTARMethod but with 6 million wordlists
  # The same as simpleTARMethod
  if (progName == "all") or (progName == ""): # do this on all programs
    
    dirs = listdir(dbPath)
    bar = IncrementalBar('transScopesTargets.py => dictTARMethod_LONGRUN()', max=len(dirs))
    for dbFile in random.sample(dirs, len(dirs)):
      progName = dbFile
      
      # lets extract simple targets in scope file
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr like '*.%' and progAdr not like '%.*%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [row[0] for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar2 = IncrementalBar('transScopesTargets.py => dictTARMethod_LONGRUN()', max=len(listOfTargets))
            # system("clear")
            for tar in listOfTargets:
              progAdr = tar
              # if not doScopeDC(progName,progAdr,myKey): # if operation is not done before!
              mainProgAdr = tar
              # delete *. from the domain:
              tar = tar.replace("*.","")
              
              # lets go and find the subdomains of this
              subDomDict(dbFile,tar,mainProgAdr,"long") # program name + *.google.com for example
              # print(dbFile,tar)
              updateScopeDC(progName,progAdr,myKey)
              bar2.next()
            bar2.finish()
      except:
        pass
      bar.next()
    bar.finish()
    
  else: # program name is specified
    dirs = listdir(dbPath)
    if progName in random.sample(dirs,len(dirs)):
      dbFile = progName
      try:
        listOfTargets = customSQLQuery(dbFile,f"select progAdr from SCOPES where progAdr like '*.%' and progAdr not like '%.*%' and (keyID IS NULL OR keyID not like \"%{myKey}%\")")
        if len(listOfTargets) != 0:
          listOfTargets = [row[0] for row in listOfTargets]
          if len(listOfTargets) != 0:
            bar = IncrementalBar('transScopesTargets.py => dictTARMethod()', max=len(listOfTargets))
            # system("clear")
            for tar in listOfTargets:
              progAdr = tar
              # if not doScopeDC(progName,progAdr,myKey): # if operation is not done before!
              mainProgAdr = tar
              # delete *. from the domain:
              tar = tar.replace("*.","")
              
              # lets go and find the subdomains of this
              subDomDict(dbFile,tar,mainProgAdr,"long") # program name + *.google.com for example
              # print(dbFile,tar)
              updateScopeDC(progName,progAdr,myKey)
              bar.next()
            bar.finish()
      except:
        pass
    else:
      print("not found")

def bruteforceTARMethod(progName):
  myKey = "26cd7ac141bed32ed8e0a8bb4db94d11"
  pass