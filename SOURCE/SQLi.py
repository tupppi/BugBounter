import subprocess

file_path = "urls-sqli.txt"

# Open the file and read line by line
with open(file_path, "r", encoding="utf-8") as file:
  for line in file:
    url = line.strip()
    # Replace [TARGET] with the URL in the sqlmap command
    command = f"sqlmap -u {url} --batch --random-agent --smart -o --threads=10 --text"

    # Execute the command
    subprocess.run(command, shell=True)
    print("SQLi Tested, Moving to the Next URL !")

print("sqlmap commands executed for all URLs.")