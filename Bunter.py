# Purpose of this program is to automate most of our bounty

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
