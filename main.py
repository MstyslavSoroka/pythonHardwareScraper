import requests as req
from bs4 import BeautifulSoup

file = open("products.csv", "w")
file.write("Title,Component,Price\n")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def detect_type(title):
    t = title.lower()
    if "graphics card" in t or "gpu" in t:
        return "GPU"
    elif "processor" in t or "cpu" in t:
        return "CPU"
    elif "motherboard" in t:
        return "Motherboard"
    elif "memory" in t or "ddr" in t:
        return "RAM"
    elif "power supply" in t or "psu" in t:
        return "PSU"
    elif "ssd" in t or "hdd" in t or "nvme" in t or "tb" in t:
        return "Storage"
    return "Unknown"

def loopProduct(products):
    for p in products: 

        title = p.select_one('.item-title').text.strip()

        price = p.select_one('.price-current').text.strip()
        component = detect_type(title)
        
        file.write(f"\"{title}\",{component},{price}\n")
        print(f"Title: {title}, Price: {price}")
            


for i in range(1, 20):
    res = req.get(f"https://www.newegg.com/global/uk-en/p/pl?N=101582448&page={i}", headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    products = soup.select('.item-cell')
    
    loopProduct(products)
    


file.close()