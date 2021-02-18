def crawler(url):
    """ubike2.0網站爬蟲各站點及租借車輛資訊"""
    # requests
    import requests
    # ubike2.0 站點和租借資訊網址
    r = requests.get(url)

    # chromedriver.exe位址
    path = "C:\\Users\\Ching-Chung\\Documents\\NTU courses\\2020_autumn\\Programming for Business Computing\\chromedriver.exe"


    # 使用selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument('--headless')

    # 使用selenium打開目標網址
    chrome = webdriver.Chrome(path)
    chrome.get(url)

    page = chrome.page_source
    # 關閉chrome
    chrome.close()

    # beautifulsoup4
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page, features="html.parser")
    attr0 = {"class": "page"}
    tr_page = soup.find_all(attrs=attr0)

    # station: 站點資訊的list
    station = []
    for tag in tr_page:
        data = tag.find_all(text=True)
        station.append(data)
    for i in range(len(station)):
        station[i].pop(0)
        station[i].pop(0)
    return station


def importData(path, station):
    """匯入ubike2.0站點位置座標(刪除可還為0者)"""
    import csv
    data = []
    with open(file=path, newline='') as csvfile:
        content = csv.reader(csvfile)
        for rows in content:
            data.append(rows)
        data.pop(0)
    for i in range(len(data)):
        data[i].append(station[i][0])
        data[i].append(station[i][1])
    return data


url = 'https://taipei.youbike.com.tw/station/2_list?_id=5e0d9644bae27166af1d5903'
station = crawler(url)
print(station)
doc_path = "C:\\Users\\Ching-Chung\\Documents\\NTU courses\\2020_autumn\\Programming for Business Computing\\Youbike2.0經緯度.csv"
data1 = importData(doc_path, station)

for i in range(len(data1)):
    print(data1[i])
    print("===")