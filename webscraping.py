from bs4 import BeautifulSoup
import pandas as pd
import requests

for num in range(0,225,25):
    url = f'https://finance.yahoo.com/gainers/?count=25&offset={num}'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    webpage = requests.get(url,headers= headers)
    soup = BeautifulSoup(webpage.text,'html.parser')
    
    name = []
        
    price=soup.find_all(class_='Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)')
    changes = soup.find_all(class_="Va(m) Ta(end) Pstart(20px) Fz(s)")
    marketcap = []
    market = soup.find_all(class_='Va(m) Ta(end) Pstart(20px) Pend(10px) W(120px) Fz(s)')
    for i in market:
        marketcap.append(i.text)
        
    company = soup.find_all(class_='Va(m) Ta(start) Px(10px) Fz(s)')
    for i in company:
        name.append(i.text)

    def findprice(price):
        share,change,changeper = [],[],[]
        for i in range(0,len(price),3):
            share.append(price[i].text)

        for i in range(1,len(price),3):
            change.append(price[i].text)

        for i in range(2,len(price),3):
            changeper.append(price[i].text)
        return share,change,changeper

    
    def findvolume(changes):    
        volume,avgvol,pe_ratio = [],[],[]
        for i in range(0,len(changes),3):
            volume.append(changes[i].text)

        for i in range(1,len(changes),3):
            avgvol.append(changes[i].text)

        for i in range(2,len(changes),3):
            pe_ratio.append(changes[i].text)
        return volume,avgvol,pe_ratio

    d = {'name':name,'price':findprice(price)[0],'change':findprice(price)[1],'change in %':findprice(price)[2],'volume':findvolume(changes)[0],'avg volume':findvolume(changes)[1],'market cap':marketcap,'pe ratio':findvolume(changes)[2]}
    df = pd.DataFrame(d)
    df.to_csv('gainers.csv',mode='a',index=False,header=False)

