# Purpose of this program is to automate most of our bounty
# work regardless of the target
# It will:
#  1. first generate target files
#  2. then it goes for recon (finding subdomains and domains, finding urls and parameters
#  3. then it goes to live detections and stuff
#  4. It goes for crawling maybe (for now we might don't have that but in the future yes)
#  5. It goes for testing known exploits and vulnerabilities
#   For example there might be a uniq path or uniq test case which 
#   can be done automatically like XSS, sqli, CVEs, admin panels, subdomain takeovers, etc.
#   all will be tested here and if anything thumbs up, we are going to have it here.
# #NOTE: I am going to use one sqlite database per target for now. It has tables, like targets table, or inscope table, vulnerabilities table and others. This is all I know is good for now.
# In the meantime that automation is going on we have time to get deep in places and stuff.
# The program should present us a main menu of targets on each run. these are those sqlite dbs.

from time import sleep
from SOURCE.InitMOD import initMOD
from SOURCE.MainMenu import mainMenu
from os import system
from colorama import Fore,Style


# Function Definitions
# Main Function
def Main():
  _ = system('clear')
  
  print(Fore.LIGHTGREEN_EX + "\n[+]I'm Bunter and I'm LIVE NOW!")
  sleep(1)
  print(Fore.LIGHTGREEN_EX + "[+]We are getting warmed UP Tupi! ...")
  sleep(1)
  print(Fore.LIGHTGREEN_EX + "[+]Getting things ready now!\n")
  sleep(1)
  
  # Call initMOD()
  initMOD()
  
  # Main menu presets
  flowMod = input("manual ? auto ?\n")
  mainMenu(flowMod)
  
  print(Fore.LIGHTGREEN_EX + "\n[+]We are done at the momment. Loop back again." + Style.RESET_ALL)
  sleep(1)
  print(Fore.LIGHTGREEN_EX + "[+]Don't forget!!! AUTOMATION IS THE KEY. I'm Bunter and I'm alive.\n" + Style.RESET_ALL)
  sleep(1)


#################################
# Program execution starts here    
if __name__ == '__main__':
    Main()




###########TODOS#################
# TODO: Automation is the KEY, Meditation is the KEY, Automate methods, techniques, tactics, uniq exploits, conceret the basics like SCOPE and TARGETS, others can be expanded on and on.
# TODO: Extract as much as automated bug as possible : account takeovers, information disclosures, default logins.
# TODO: ADD ALL PROGRAMS on hackerone, bugcrowd, intigriti and others, most is added automated but some of them need manual work until get automated also.
# TODO: Add bounty programs using google dorks: site: .com inurl: Responsible Disclosure
# TODO: Add this great crawler to the Bunter framework : https://github.com/jaeles-project/gospider
# TODO: Write our google Dorker module to find a lot of good bugs automatically using google, "https://github.com/opsdisk/pagodo", hard to implement since google free api limits 10 searches with 100 results per day and human simulated search get 429 if you are not carefulll enough. But it can be done as a slow module to find good results on all SCOPES of all programs. WE should run ghdb_scraper.py to get the latest dorks from GHDB, and do run other methods to run each dork on all scopes without *. great results awaiting us!!!!!

# TODO: Subdomain takeover attack module, which should constantly look for take overs in an infinite loop.

# TODO: Write target discovery like subdomain discovery with dictionary method : 1. get all subdomains wordlists and put them in a file, sort uniq that file. move forward and extract all scope items with *. in the beginnings e.g. wildcards. do dictionary search on all of them with your dubdomain wordlist, ones with A record will be passed to httpx discovery method.







# TODO: DONE => SLACK VULNS MESSAGES
# TODO: DONE => URLS table should have status code column.
# TODO: DONE => DB STRUCTURE should be hierachical. from SCOPE TABLE TO VULNS.
# TODO: DONE => Write all the basic needs for one program and extend it to others.
# TODO: DONE => Add projects folder to the bunter folder
# TODO: DONE => all DoubleChecks or DCs should return True or full results. one if to handle all.
# TODO: DONE => def doScopeDC():
# TODO: DONE => def updateScopeDC()
# TODO: DONE => Multi threading is below test it.
# TODO: DONE => from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# TODO: DONE => Write multithreading or multiprocessing to the framework, so we can use the full power of whatever hardware we have without running the Bunter multiple times.
############TODOS#################
