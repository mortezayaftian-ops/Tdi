import requests
from bs4 import BeautifulSoup

URL = "https://www.sunsirs.com/commodity-price/petrochemicals.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_tdi():
    r = requests.get(URL, headers=headers, timeout=20)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text("\n")

    for line in text.splitlines():
        if "TDI" in line.upper():
            print(line.strip())

if __name__ == "__main__":
    print("شروع جستجوی TDI ...")
    get_tdi()
