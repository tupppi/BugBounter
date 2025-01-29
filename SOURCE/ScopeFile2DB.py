from os import path
from SOURCE.DBHandler import *
import subprocess

#################################
#################################
#################################
#################################
## --------------------------- ##
# def targetFetch():
#   inScope = input(Fore.LIGHTYELLOW_EX + "InScope File? " + Style.RESET_ALL)
#   outOfScope = input(Fore.LIGHTYELLOW_EX + "OutOfScope File? " + Style.RESET_ALL)
#   programName = input(Fore.LIGHTYELLOW_EX + "Program Name? " + Style.RESET_ALL)
  
#   print(Fore.LIGHTCYAN_EX + f"\nThe InScope.LSD file is : {inScope}" + Style.RESET_ALL)
#   print(Fore.LIGHTCYAN_EX + f"The OutOfScope.LSD file is : {outOfScope}" + Style.RESET_ALL)
#   print(Fore.LIGHTCYAN_EX + f"The proram name is : {programName}" + Style.RESET_ALL)
  
#   print(Fore.LIGHTBLUE_EX + """\nMoving forward to create:
#     cidrTargets.LSD
#     mobileTargets.LSD
#     webTargets.LSD
#     iotTargets.LSD
# files for processing!\n""" + Style.RESET_ALL)
# TODO: This part will be completed later on.
# This should read the InScope.LSD (even OutOfScope.LSD) file and process 
# them accordingly to create proper *Targets.LSD files for further processing
# by other modules like reconer
# slackFetch("vulns","CONGRATS, NEW 90+% VULN HAS BEEN DETECTED!")

# For now we create these files by hand
## ---------------------------- ##

# This function transfers from program files to DB
# making everything ready for processing, relations, recons.
def scopeFile2DB(progName):
  progPath = "/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/BountProjects/" + progName + "/"
  # progCidrTar = 
  # progMobileTar = 
  # progIotTar = 
  # print(f"We have program web target file : {progWebTar}")
  progWebTar = progPath + "resources/webTargets.LSD"
  if path.exists(progWebTar):
    #print(f"Target file exists for {progName}")
    try:
      file = open(progWebTar, 'r')
      lines = file.readlines()
  
      for line in lines:
        if line != "":
          line = line.strip()
          line = line.encode("ascii", "ignore").decode()
          line = str(line).lower()
          line = line.replace("https://","")
          line = line.replace("http://","")
          line = line.replace(".*","")
          line = line.replace("(","")
          line = line.replace(")","")
          if line[0] == "*":
            if line[1] in "qwertyuiopasdfghjklzxcvbnm":
              line = line[1:]
          line = subprocess.getoutput(f"echo {line} | cut -d '/' -f 1")

          # Check for domains, each domain at least has one . inside of it right ????
          # This way nothing shero ver will be inside scopes table
          # This if will escape inputs that are not domains (don't have dots)
          # if "." in line:
          # input(f"The target I want to add now is : {line}")
          if line != "":
            insertToScopes(progName, line, "domain", "primary web domain")
    except Exception as e:
      print(f"WE HAVE A WEIRED PROBLEM!\npath : {progWebTar}")
      pass
  else:
    #print(f"AHHH, webTargets.LSD file for {progName} has not been created yet :(")
    # input("DONE! You can check later on.")
    pass