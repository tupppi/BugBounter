# USAGE : 
  #     multithreading(taskToTest,listdir("DB"),200)
  #     This runs taskToTest function on a loop of listdir("DB") with 200 threads
# USAGE : 
  #     multiprocessing(taskToTest,listdir("DB"),200)
  #     This runs taskToTest function on a loop of listdir("DB") with 200 processes
# EXPLANATIONS : 
  #  1. call multithreading or multiprocessing functions
  #  2. multithreading => I/O Consuming => do GET on a list of URLS
  #  3. multiprocessing => CPU/RAM Consuming => Calculating or cracking hashes
  #  multithreading is inside one processes and RAM, shares things
  #  multiprocessing is in seperated processes and RAM, parallel execution not shares
# EXAMPLES : 
  # def taskToTest(url):
  #   try:
  #     URL = "http://localhost:8000/"+str(url)
  #     r = requests.get(url=URL)
  #     time.sleep(5)
  #     # print(f"{URL} ===>  {r.status_code}")
  #   except:
  #     pass
      
  # start_time = time.time()
  # multithreading(taskToTest,listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB"),200, "Get URLS on google.com")
  # print("--- %s seconds ---" % (time.time() - start_time))

  # start_time = time.time()
  # multiprocessing(taskToTest,listdir("/home/tup/Desktop/__HardWorkPaysOff__/BugBounty/tupiRepo/Bunter/DB"),200, "Get URLS on google.com")
  # print("--- %s seconds ---" % (time.time() - start_time))

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from tqdm import tqdm


def multithreading(func, args, workers, taskDesc):
  # with ThreadPoolExecutor(workers,max_workers=7) as ex:  
  #     res = ex.map(func, args)
  # return res
  if len(taskDesc) != 0:
    with ThreadPoolExecutor(max_workers=workers) as executor:
      results = list(tqdm(executor.map(func, args, timeout=None, chunksize=1), total=len(args), desc=taskDesc))
    return results
  else:
    with ThreadPoolExecutor(max_workers=workers) as executor:
      results = list(executor.map(func, args, timeout=None, chunksize=1), total=len(args))
    return results

  

def multiprocessing(func, args, workers, taskDesc):  
  # with ProcessPoolExecutor(max_workers=7) as ex:  
  #     res = ex.map(func, args)
  # return res
  if len(taskDesc) != 0:
    with ProcessPoolExecutor(max_workers=workers) as executor:
      results = list(tqdm(executor.map(func, args, timeout=None, chunksize=1), total=len(args), desc=taskDesc))
    return results
  else:
    with ProcessPoolExecutor(max_workers=workers) as executor:
      results = list(executor.map(func, args, timeout=None, chunksize=1), total=len(args))
    return results

