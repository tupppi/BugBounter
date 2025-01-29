from os import listdir
import random
from SOURCE.InitDB import initDB
from SOURCE.ScopeFile2DB import scopeFile2DB
# from progress.bar import IncrementalBar
from SOURCE.ConcurrentPowers import multithreading


def initMOD():
  # lets do all the initializations
  # everything that can happen on startup
  
  projPath = "/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/res/BountProjects/"
  dirs = listdir(projPath)
  _ = random.sample(dirs, len(dirs))
  
  multithreading(initDB, _, 100, "MainMenu.py => mainMenu() => initDB()")
  multithreading(scopeFile2DB, _, 100, "MainMenu.py => mainMenu() => scopeFile2DB()")
  # bar = IncrementalBar('InitMOD.py => initMOD()', max=len(_))
  # for projFile in _:
  #   initDB(projFile)
  #   scopeFile2DB(projFile)
  #   bar.next()
  # bar.finish()