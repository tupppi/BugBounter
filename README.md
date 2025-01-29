# Basically this is a framework for scanning and finding vulnerabilities in a more bug bounty style on a list of domains and urls.

# HOW IT WORKS : 
 1. Search for bug bounty programs and fetch scopes.
 2. Find as much as subdomains possible by first quering online sources, then it goes to fuzzing millions of subdomains on each target.
 3. Find as much as urls and parameters as possible.
 4. Launch hundreds of attack modules on each target based on its attack rules, or config files.
 5. Save the results in sqlite DB for now, later on it can be DynamoDB.

# What it scans :
 1. Capable of running scans against domain targets, like DNS addresses to find new subs
 2. Capable of running attacks on web modules running on following common ports : 80,443,8000,8080-8090,81,8443,8888,900,9000,9001,9080-9090,9443,591,10000,1080,280,2301,2381,3000,3001,3128,5000,5432,5800,66,7001,5490,7002,9418
 3. Capable of running attacks on services like MYSQL, SSH and others.

# Goals
1. Writing this tools is to find vulnerabilities over various services and report them back in DB and also slack channel.
2. Using already developed tools, parsing their outputs and passing over the processed data into input of the next tool.
3. Blackbox approach is taken as method of afcing targets when writing the code.


# FEATURES :
1. Ability to pull targets from all bug bounty programs including DeliveryHero program on hackerone
2. It is capable of manual adding targets into its lifecycle, any target that is added will go through all the reconnaissance and fuzzing processes.
3. Multiprocessing and multithreading is implemented to spead things up, even without using clustering and kubernetes.
4. It has a mechanism to not repeat itself on anything. Every module has a key, which is automatically generated based on its signature hashsum, the program checks if this specific module has been executed before on this specific target, if so it is not executed and goes to next one.
5. Ability to force the program to repeat itself.
6. Uses multiple tools to findout every subdomain that is publicly available.
7. Uses a wordlist of 6 million words for fuzzing new subdomains.
8. Checks multiple ports on the app to make sure if any application is running or not : ports 80,443,8000,8080-8090,81,8443,8888,900,9000,9001,9080-9090,9443,591,10000,1080,280,2301,2381,3000,3001,3128,5000,5432,5800,66,7001,5490,7002,9418
9. Prevents any duplicate data to be written in DB.
10. Uses multiple attack tools to attack targets already scanned and profiled.
11. Capable of integrating other fuzzing or attack tools inside of it.
12. Query online databases of cached URLs and important paths in order to use it for other fuzzing attacks.
13. Add a crawler to add urls to URL module.
14. BlindXss Fuzzer
15. SQLi Injector
16. Add attack modules to work on those URLs indexed.



# TODOs
1. Add wordpress vulnerability scanner
2. Add service fuzzer, like mysql bruteforcer or CVE finder on services other than web.
3. Send msgs to DH specific channels in slack.
4. Write more nuclei modules for it.
5. Usinsg service fuzzers when an asset is found, like MSSQL or MYSQL fuzzing.
6. Writing a module to specifically work on SQL injections, using SQLMAP on parameters that are suspectable to attacks.

# INSTALLATION
1. Git clone
2. Install dependencies
3. For now you need to create the data folder structure, will work to free from this.
4. Run Bunter.py
5. Target DeliveryHero program there on any module you like.
