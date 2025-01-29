from os import listdir
from colorama import Fore, Style
from os import system
# from progress.bar import IncrementalBar
from SOURCE.StatsDump import *
from SOURCE.InitDB import *
from SOURCE.ScopeFile2DB import *
from SOURCE.transScopes2Targets import simpleTARMethod,queryTARMethod,dictTARMethod,dictTARMethod_LONGRUN
from SOURCE.doubleCheck import cleanKEY
from SOURCE.transTar2URL import queryURLMethod, crawlerMethod
from SOURCE.Exploiter import attackLauncher,runner
from subprocess import getoutput
from SOURCE.ConcurrentPowers import multiprocessing, multiprocessing, multiprocessing, multiprocessing, multithreading


def mainMenu(flowMod):
  if flowMod == "auto":
    # STATS
    ######################
    _ = system('clear')
    # statsDump()
    
    # DB INIT, SCOPE TABLE FROM FILE
    ######################
    print("SCRIPT EXECUTION AND FILE OPERATIONS INITIATING ...")
    print("I will pull new program scopes, add them to databases ready to be processed.")
    newProgPath = "/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/extractor.sh"
   
    getoutput(newProgPath)
    
    projPath = "/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/BountProjects/"
    _ = listdir(projPath)
    random.shuffle(_)
   
    # multiprocessing(initDB, _, 100, "MainMenu.py => mainMenu() => initDB()")
    # multiprocessing(scopeFile2DB, _, 100, "MainMenu.py => mainMenu() => scopeFile2DB()")
    
    multithreading(initDB, _, 20, "MainMenu.py => mainMenu() => initDB()")
    multithreading(scopeFile2DB, _, 20, "MainMenu.py => mainMenu() => scopeFile2DB()")
    # bar = IncrementalBar('MainMenu.py => mainMenu()', max=len(_))
    # for projFile in _:
    #   initDB(projFile)
    #   scopeFile2DB(projFile)
    #   bar.next()
    # bar.finish()
    print("Initializations done, Scope files are fetched!")
    
    # TABLE TARGETS CREATE
    ######################
    allDBs = listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB/")
    random.shuffle(allDBs)
    
    # multiprocessing(simpleTARMethod,allDBs,5,"MainMenu.py => auto mode => simpleTARMethod()")
    # multiprocessing(queryTARMethod,allDBs,5,"MainMenu.py => auto mode => queryTARMethod()")
    # multiprocessing(dictTARMethod,allDBs,5,"MainMenu.py => auto mode => dictTARMethod()")
    
    multiprocessing(simpleTARMethod,allDBs,5,"MainMenu.py => auto mode => simpleTARMethod()")
    multiprocessing(queryTARMethod,allDBs,5,"MainMenu.py => auto mode => queryTARMethod()")
    multiprocessing(dictTARMethod,allDBs,5,"MainMenu.py => auto mode => dictTARMethod()")
    multiprocessing(dictTARMethod_LONGRUN,allDBs,5,"MainMenu.py => auto mode => dictTARMethod()")
    
    # simpleTARMethod("all")
    # queryTARMethod("all")
    # dictTARMethod("all")
    # dictTARMethod(progName)
    # bruteforceTARMethod(progName)
    # statsDump()

    # TABLE URLS CREATE
    ######################
    # simpleURLMethod(targetURI)
   
    # multiprocessing(queryURLMethod,allDBs,5,"MainMenu.py => auto mode => queryURLMethod()")
    multiprocessing(queryURLMethod,allDBs,5,"MainMenu.py => auto mode => queryURLMethod()")
   
    # queryURLMethod("all")
    # dictTARMethod(targetURI)
    # bruteforceTARMethod(targetURI)
    # statsDump()
    
    # Let's run the attacks
    ######################
    attackLauncher("all","all")

    # Let's loop all over again
    mainMenu("auto")
    
  else:
    while True:
      _ = system('clear')
      
      print(Fore.LIGHTGREEN_EX + "\n[+]I'm Bunter and I'm LIVE NOW!")
      print(Fore.LIGHTGREEN_EX + "[+]We are getting warmed UP Tupi! ...")
      print(Fore.LIGHTGREEN_EX + "[+]Getting things ready now!\n")
      print(Fore.LIGHTMAGENTA_EX + """CHOICES:
      0. STATS.
          Number of programs, targets, vulns.
      1. SCOPES.
          Check for new targets in scope files. (SCOPES TABLE) 
      2. TARGETS.
          SCOPES TABLE items reconed, fuzzed and bruteforced for as much as targets! (TARGETS TABLE)
      2.5 _ TEMP _ Do dictionary method target discovery _ SHORT RUN (1 MILLION)
      2.6 _ TEMP _ Do dictionary method target discovery _ LONG RUN (6 MILLION)
      3. URLS.
          Check for new urls and endpoints. (URLS TABLE)
          (all assets in target table will be waybacked, gau, gau+ 
          and others, spidered and crawled for new endpoints!)
      3.5 Crawler
      4. VULNS.
          Check for new vulns. (VULNS TABLE)
          (check targets and urls tables for vulnerabilities, 1 vulnerability per target or url. SPRAYING!)
      5. cleanKEY.
          clean keys from a TAble:
      
      6. Run nuks 
      => exit?""" + Style.RESET_ALL)
      choice = str(input())
      
      if choice == "0":
        # do stats
        _ = system('clear')
        statsDump()
      
      elif choice == "1":
        # do scopes
        # DB INIT, SCOPE TABLE FROM FILE
        ######################
        print("SCRIPT EXECUTION AND FILE OPERATIONS INITIATING ...")
        print("I will pull new program scopes, add them to databases ready to be processed.")
        newProgPath = "/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/extractor.sh"
       
        getoutput(newProgPath)
        
        projPath = "/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/BountProjects/"
        _ = listdir(projPath)
        random.shuffle(_)
        # multiprocessing(initDB, _, 100, "MainMenu.py => mainMenu() => initDB()")
        # multiprocessing(scopeFile2DB, _, 100, "MainMenu.py => mainMenu() => scopeFile2DB()")
        
        multithreading(initDB, _, 20, "MainMenu.py => mainMenu() => initDB()")
        multithreading(scopeFile2DB, _, 20, "MainMenu.py => mainMenu() => scopeFile2DB()")
        # bar = IncrementalBar('MainMenu.py => mainMenu()', max=len(_))
        # for projFile in _:
        #   initDB(projFile)
        #   scopeFile2DB(projFile)
        #   bar.next()
        # bar.finish()
        print("Initializations done, Scope files are fetched!")    
      
      elif choice == "2":
        answer = input("Name a program or type \"all\"!\n")
        if answer == "all":
          allDBs = listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB/")
          random.shuffle(allDBs)

          # multiprocessing(simpleTARMethod,allDBs,5,"MainMenu.py => manual mode => simpleTARMethod()")          
          # multiprocessing(queryTARMethod,allDBs,5,"MainMenu.py => manual mode => queryTARMethod()")
          # multiprocessing(dictTARMethod,allDBs,5,"MainMenu.py => manual mode => dictTARMethod()")
          
          
          multiprocessing(simpleTARMethod,allDBs,3,"MainMenu.py => manual mode => simpleTARMethod()")
          multiprocessing(queryTARMethod,allDBs,3,"MainMenu.py => manual mode => queryTARMethod()")
          # multithreading(dictTARMethod,allDBs,5,"MainMenu.py => manual mode => dictTARMethod()")
          # multithreading(dictTARMethod_LONGRUN,allDBs,5,"MainMenu.py => manual mode => dictTARMethod()")

        else:  
          simpleTARMethod(answer)
          queryTARMethod(answer)
          # dictTARMethod(answer)
          # dictTARMethod_LONGRUN(answer)
                
        # dictTARMethod(progName)
        # bruteforceTARMethod(progName)
        # statsDump()
      elif choice == "2.5":
        #************************************#
        answer = input("Name a program or type \"all\"!\n")
        
        if answer == "all":
          allDBs = listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB/")
          random.shuffle(allDBs)
          multiprocessing(dictTARMethod,allDBs,4,"MainMenu.py => manual mode => dictTARMethod()")
        
        else:
          dictTARMethod(answer)
        #************************************#
        
      elif choice == "2.6":
        #************************************#
        answer = input("Name a program or type \"all\"!\n")
        
        if answer == "all":
          allDBs = listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB/")
          random.shuffle(allDBs)
          multiprocessing(dictTARMethod_LONGRUN,allDBs,4,"MainMenu.py => manual mode => dictTARMethod()")
        
        else:
          dictTARMethod_LONGRUN(answer)
        #************************************#
      
      elif choice == "3":
        # simpleURLMethod(targetURI)
        answer = input("Name a program or type \"all\"!\n")
        if answer == "all":
          allDBs = listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB/")
          random.shuffle(allDBs)
          # multiprocessing(queryURLMethod,allDBs,5,"MainMenu.py => manual mode => queryURLMethod()")
          multithreading(queryURLMethod,allDBs,1,"MainMenu.py => manual mode => queryURLMethod()")
        else:  
          queryURLMethod(answer)
        # dictTARMethod(targetURI)
        # bruteforceTARMethod(targetURI)
        # statsDump()
      
      elif choice == "3.5":
        answer = input("Name a program or type \"all\"!\n")
        if answer == "all":
          allDBs = listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB/")
          random.shuffle(allDBs)
          # multiprocessing(queryURLMethod,allDBs,5,"MainMenu.py => manual mode => queryURLMethod()")
          multithreading(crawlerMethod,allDBs,1,"MainMenu.py => manual mode => queryURLMethod()")
        else:  
          crawlerMethod(answer)

      elif choice == "4":
        #do vulns
        answer1 = input("all OR Attack Name?")
        answer2 = input("all OR Program Name?")
        attackLauncher(answer1,answer2)

        while (answer1 == "all" and answer2 == "all"):
          attackLauncher("all","all")
          
        
        # statsDump()
      elif choice == "6":
	#do vulns using nuclei
        answer1 = input("all OR TARGET NAME?")
        answer2 = input("all OR TEMPLATE NAME [YOU SHOULD GIVE ME FULL YAML/YML PATH]")
        runner(answer1,answer2)
        while (answer1 == "all"):
          runner(answer1,answer2)
  
      elif choice == "5":
        cleanKEY()
        
        # statsDump()
      
      elif choice == "exit":
        break
      else:
        print("What??")
        continue
