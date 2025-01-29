from SOURCE.QueryStats import *
from os import listdir
from colorama import Fore, Style
from SOURCE.SlackFetch import *
from SOURCE.DBHandler import queryTableLU,dbPath
import random


def statsDump():
  scopes = 0
  total = 0
  totalTar = 0
  totalURLS = 0
  totalVULNSReped = 0
  totalVULNSNotReped = 0
  totalVULNS = 0

  print("\nPrograms fetched until now : ")
  dirs = listdir(dbPath)
  dbFiles = random.sample(dirs,len(dirs))
  for files in dbFiles:      
    total = total + 1
    resultsTuple = queryStats(files)
    
    if resultsTuple != None:  # This was added to prevent unpacking tuples
      (numScopes,numTar,numURL,numVULNReported,numVULNNotReported) = resultsTuple
      totalTar = totalTar + numTar
      totalURLS = totalURLS + numURL
      totalVULNSReped = totalVULNSReped + numVULNReported
      totalVULNSNotReped = totalVULNSNotReped + numVULNNotReported
      totalVULNS = totalVULNSReped + totalVULNSNotReped
        
      if numScopes != 0:
        print(Fore.LIGHTGREEN_EX + f"Program #{scopes} : " + Fore.LIGHTRED_EX + str(files) + Fore.LIGHTGREEN_EX + "\n- Number of scope lines : " + Fore.LIGHTRED_EX + str(numScopes) + Fore.LIGHTGREEN_EX + f"\tUpdated: " + Fore.LIGHTRED_EX + str(queryTableLU(files, "SCOPES")) + Fore.LIGHTGREEN_EX + "\n- Number of targets : " + Fore.LIGHTRED_EX + str(numTar) + Fore.LIGHTGREEN_EX + f"\tUpdated: " + Fore.LIGHTRED_EX + str(queryTableLU(files, "TARGETS")) + Fore.LIGHTGREEN_EX + "\n- Number of URLs : " + Fore.LIGHTRED_EX + str(numURL) + Fore.LIGHTGREEN_EX + f"\tUpdated: " + Fore.LIGHTRED_EX + str(queryTableLU(files, "URLS")) + Fore.LIGHTGREEN_EX + "\n- Number of VULNS not reported : " + Fore.LIGHTRED_EX + str(numVULNNotReported) + Fore.LIGHTGREEN_EX + f"\tUpdated: " + Fore.LIGHTRED_EX + str(queryTableLU(files, "VULNS")) + Fore.LIGHTGREEN_EX + "\n- Number of VULNS reported : " + Fore.LIGHTRED_EX + str(numVULNReported) + Style.RESET_ALL)
        print("---------------------------------")
        scopes = scopes + 1
        
        # Send these to slack
        # This is paused for now
  #       try:
  #         slackFetch("bunters",f"""--------------------------------------
  # Program #{scopes} : {files}
  # - Number of scope lines : {numScopes} Updated : {queryTableLU(files, "SCOPES")}
  # - Number of targets : {numTar}  Updated : {queryTableLU(files, "TARGETS")}
  # - Number of URLs : {numURL} Updated : {queryTableLU(files, "URLS")}
  # - Number of VULNS not reported : {numVULNNotReported} Updated : {queryTableLU(files, "VULNS")}
  # - Number of VULNS reported : {numVULNReported}""")
  #       except:
  #       pass
    else: 
      pass
      # resultsTuple was None
      #print("WE HAVE A PROBLEM IN queryStats")
    
  
  print(Fore.LIGHTCYAN_EX)
  print(f"Total number of INITIALIZED program DBs : {total}")
  print(f"Total number of SCOPED program DBs : {scopes}")
  print(f"Total number of TARGETS : {totalTar}")
  print(f"Total number of URLS : {totalURLS}")
  print(f"Total number of VULNS REPORTED : {totalVULNSReped}")
  print(f"Total number of VULNS NOT REPORTED : {totalVULNSNotReped}")
  print(f"Total number of VULNS ALL TOGETHER : {totalVULNS}")
  print(Style.RESET_ALL)
  
  try:
    slackFetch("bunters",f"""--------------------------------------
Total number of INITIALIZED program DBs : {total}
Total number of SCOPED program DBs : {scopes}
Total number of TARGETS : {totalTar}
Total number of URLS : {totalURLS}
Total number of VULNS REPORTED : {totalVULNSReped}
Total number of VULNS NOT REPORTED : {totalVULNSNotReped}
Total number of VULNS ALL TOGETHER : {totalVULNS}
             --------------------------------------""")
  except:
    pass
  print("\nGOOD? I want to go.")