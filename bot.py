import requests
from bs4 import BeautifulSoup

URL = "https://www.sunsirs.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_tdi():
    r = requests.get(URL, headers=headers, timeout=20)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(" ", strip=True).upper()

    if "TDI" in text:
        print("✅ TDI پیدا شد")
    else:
        print("❌ TDI پیدا نشد")

    # برای تست، چند خط شامل TDI را چاپ می‌کنیم
    for line in soup.get_text("\n").split("\n"):
        if "TDI" in line.upper():
            print(line.strip())

if __name__ == "__main__":
    print("در حال جستجوی TDI ...")
    get_tdi()
