import requests

find_content = "gmail.xjiji"
urls = f"https://www.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={find_content}&redirected=true&tmskey=1dom_03_intlgtld"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
resp = requests.get(urls, headers=headers)

print(resp.text)