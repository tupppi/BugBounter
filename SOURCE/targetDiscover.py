import subprocess
from SOURCE.DBHandler import inserToTargets, inserToURLS, inserToURLS4Crawler, inserToURLSBatch
import re
import random
# from progress.bar import IncrementalBar
import simplejson
import subprocess


def tarHTTPXDiscovery(progName,progAdr,mainProgAdr):
  ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
  progAdr = ansi_escape.sub('', progAdr)
  progAdr = progAdr.encode("ascii", "ignore").decode()
  progAdr = str(progAdr).strip()

  results = subprocess.getoutput(f"echo {progAdr} | httpx -json -threads 50 -title -tech-detect -status-code -follow-host-redirects -silent -no-fallback -random-agent -ports 80,443,8000,8080-8090,81,8443,8888,900,9000,9001,9080-9090,9443,591,10000,1080,280,2301,2381,3000,3001,3128,5000,5432,5800,66,7001,5490,7002,9418 | jq '.url','.\"status-code\"','.title','.technologies[0]','.failed'")

  try:
    res = results.replace("\n","@%@")
    array = res.split("@%@")
    # input(f"\nresults is now {array}")

    starter = 0
    if array[starter] != "":
      while starter < len(array):
        targetURI = str(array[starter]).replace('"','')
        if ('http://' in targetURI) or ('https://' in targetURI): # to get rid of errors returned by httpx
          statusCode = str(array[starter+1]).replace('"','')
          targetTitle = str(array[starter+2]).replace('"','')
          targetTech = str(array[starter+3]).replace('"','')
          if (array[starter+4]):
            isLive = "true"
          else:
            isLive = "false"
          inserToTargets(progName,mainProgAdr,targetURI,statusCode,targetTitle,targetTech,isLive)
          subprocess.getoutput("rm -f 'resume.cfg'")
          
          #print(progName,progAdr,targetURI,statusCode,targetTitle,targetTech,isLive)
        starter = starter + 5
  except:
    pass
  
def urlQueryAPI(progName,progAdr,targetURI):
  try:
    tmpFile0 = random.random()
    tmpFile1 = random.random()
    # results = subprocess.getoutput(f"waybackurls \"{targetURI}\" | grep \"{targetURI}\" >> ./{tmpFile0}")
    # results = subprocess.getoutput(f"gau -subs \"{targetURI}\" | grep \"{targetURI}\" >> ./{tmpFile0}")
    # results = subprocess.getoutput(f"gauplus -subs \"{targetURI}\" | grep \"{targetURI}\" >> ./{tmpFile0}")
    results = subprocess.getoutput(f"waybackurls \"{targetURI}\" >> ./{tmpFile0}")
    results = subprocess.getoutput(f"gau -subs \"{targetURI}\" >> ./{tmpFile0}")
    results = subprocess.getoutput(f"gauplus -subs \"{targetURI}\" >> ./{tmpFile0}")
    results = subprocess.getoutput(f"sort -u ./{tmpFile0} > ./{tmpFile1}")
    results = subprocess.getoutput(f"mv ./{tmpFile1}  ./{tmpFile0}")
    
    with open(f"{tmpFile0}") as FileObj:
      # bar = IncrementalBar('targetDiscover.py => urlQueryAPI()',max=int(subprocess.getoutput(f"wc -l {tmpFile0} | cut -d \" \" -f 1")))
      # system("clear")
      # for lines in FileObj:
      #   if '?' in lines:
      #     inserToURLS(progName,progAdr,targetURI,lines)
      #   bar.next()
      # bar.finish()
      inserToURLSBatch(progName,progAdr,targetURI,FileObj)
    #   bar.next()
    # bar.finish()
          
    subprocess.getoutput(f"rm -f ./'{tmpFile0}'")
    subprocess.getoutput(f"rm -f ./'{targetURI}'")
  except Exception as e:
    print(f"Exception : {e}")


def letsCrawl(progName,progAdr,targetURI):
  try:
    target = targetURI
    # cmd = ["crawlergo","--wait-dom-content-loaded-timeout=2s","   --tab-run-timeout=4s", "-t 1", "-m 3000", "-c /usr/bin/chromium", "-o json", target, ";sudo killall -9 chromium"]
    cmd = ["crawlergo","--wait-dom-content-loaded-timeout=2s", "--tab-run-timeout=2s", "-t" ,"16", "-m", "6000", "-c" ,"/usr/bin/chromium", "-o" ,"json", target, ";sudo killall -9 chromium"]
    # cmd = ["crawlergo", "-t" ,"16", "-m", "4000", "-c" ,"/usr/bin/chromium", "-o" ,"json", target, ";sudo killall -9 chromium"]
    rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = rsp.communicate()
    # “--[Mission Complete]--” is the end-of-task separator string
    result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
    req_list = result["req_list"]
    print(req_list[0])
    # print(req_list)
    inserToURLS4Crawler(progName,progAdr,targetURI,req_list)
  except Exception as e:
    print(f"Exception : {e}")  
  # with open(f"{tmpFile0}") as FileObj:
  #   bar = IncrementalBar('targetDiscover.py => urlQueryAPI()',max=int(subprocess.getoutput(f"wc -l {tmpFile0} | cut -d \" \" -f 1")))
  #   # system("clear")
  #   for lines in FileObj:
  #     if '?' in lines:
  #       inserToURLS(progName,progAdr,targetURI,lines)
  #     bar.next()
  #   bar.finish()
        
  # subprocess.getoutput(f"rm -f ./'{tmpFile0}'")
  # subprocess.getoutput(f"rm -f ./'{targetURI}'")