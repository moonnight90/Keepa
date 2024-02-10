import json
import os
import time
import pandas as pd
import websocket
import base64
import zlib
import threading
from requests import Session
from datetime import datetime
import getpass

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://keepa.com',
    'Accept-Language': 'en-US,en;q=0.9,ur;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Upgrade': 'websocket',
    'Cache-Control': 'no-cache',
    'Sec-WebSocket-Protocol': '8rj4ssmcujfh3j7ofh9ntrnj6vlmnc88vros1n9islr6sbbu4v0c18fi3kgon2a9',
    'Connection': 'Upgrade',
    'Sec-WebSocket-Version': '13',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
}

ses = Session()
ses.headers.update(headers)

ws = websocket.WebSocket()
ws.connect('wss://push.keepa.com/apps/cloud/?app=keepaWebsite&version=2.0',header=headers)
ws.binaryType = "arraybuffer";
def decompress_msg(msg):
    try:
        a = zlib.decompress(base64.b64decode(msg))
    except:
        a = zlib.decompress(base64.b64decode(msg),-zlib.MAX_WBITS)
    finally:
        return a

def send_encoded_msg(json_msg):
    encoded_msg = zlib.compress(json.dumps(json_msg).encode())
    ws.send_binary(encoded_msg)




def searchProducts(products):
    for i,product in enumerate(products,start=1):
        i = {"path":"pro/product","refreshProduct":True,"domainId":1,"history":True,"getSellersNoHistory":True,"asin":product,"offerPages":6,"type":"offers","maxAge":0,"id":10000+i,"version":7}
        send_encoded_msg(i)
        time.sleep(0.2)

products_count = 0

def get_bookscouter(isbn):
    url = f"https://api.bookscouter.com/v4/prices/sell/{isbn}"
    resp = ses.get(url)
    prices = resp.json().get('prices',[])
    tmp = {"Bookscouter Price": 0.0,"Bookscouter Company": ''}
    h_p = 0
    for price in prices:
        p = price.get('price',0)
        if p>h_p:
            tmp.update({
                "Bookscouter Price": p,
                "Bookscouter Company": price.get('vendor',{}).get('name',''),
            })
            h_p = p
    return tmp
    

def parse_product(json_d):
    product = json_d.get('products')[0]
    title = product['title']
    
    asin = product['asin']
    ean_no = product['eanList']
    if ean_no:
        ean_no = ', '.join(ean_no)
    offers = product['offers']
    tmp ={"Title":title,"ASIN":asin,"EAN":ean_no,"Price":999999,"Condition":None}
    if offers==None: offers = []
    
    for offer in offers:
        if offer.get('stockCSV',None)==None: continue
        oferPrices = offer['offerCSV']
        
        prices = [oferPrices[i:i+3] for i in range(0,len(oferPrices),3)]
        
        prices = prices[-1]
        if prices[0]>=offer['lastSeen']:continue
        prices = prices[1:]
        t_p = 0
        for price in prices: t_p+=price
        t_p /=100
        condition = offer.get('conditionComment',None)
        condition = "New" if None==condition else condition
        if tmp["Price"]>t_p:
            tmp.update({"Price":t_p,"Condition":condition})
    if product['eanList']:
        tmp.update(get_bookscouter(product['eanList'][0]))
    else:
        tmp.update({"Bookscouter Price":0,"Bookscouter Company":None})
    
    tmp['Price Difference'] = tmp['Bookscouter Price']-tmp['Price']
    tmp['Percentage Difference'] = "%.2f"%((tmp["Price Difference"]/tmp["Price"])*100)
    tmp['Amazon Link'] = f"https://dyn.keepa.com/r/?type=amazon&smile=0&domain=1&asin={tmp['ASIN']}&source=website&path=product"
    tmp['Last Fresh Date and Time'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f"[DONE] {products_count}: {title}")
    pd.DataFrame([tmp]).to_csv('Products.csv',index=False,mode='a',header=not os.path.exists('Products.csv'))

def input_category(json_d):
    categories = json_d['categories']
    cat_list = []
    for key in categories:
        cat = categories[key]
        print(f"{len(cat_list)}> {cat['name']} ({cat['productCount']})")
        cat_list.append(cat['catId'])
    
    return cat_list[int(input('Enter Choice: '))]


def handle_msg(json_msg):
    global products_count,total_product_to_scrape
    global page,tmp_products,category

    if json_msg['id'] == -1:
        send_encoded_msg({"path":"user/session","type":"login","username":username,
                          "password":password,"id":111,"version":7})
    
    elif json_msg['id']==111:
        token = json_msg.get('token',None)
        if token:
            print(f"Login Success ({token[:20]}...)")
            send_encoded_msg({"path":"pro/category","domainId":1,"categoryIds":[-1],"l":"keepa.com","u":"/","ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0","h":"y05NLUjUS87PBQA=","id":112,"fp":{"i":"tncphz","r":"c/Rz93FV0PDMK0nN0VEAUxpBmgqhHi4K7kWJBRmZycUKZkYGChoGFQYGBgamlobmmgoumUWpySXGLoaGCmXF8abxBgoFYEpHwQUkqAkA","t":int(time.time()*1000)},"version":7,"user":token})
        else:
            print(json_msg.get('errors'))

    elif json_msg['id'] == 112:
        if json_msg['status']==200:
            print("Login Success")
            send_encoded_msg({"path":"pro/category","domainId":1,"categoryIds":[-1],"id":222,"version":7})
        else: return True
    elif json_msg['id'] == 222:
        category = input_category(json_msg)
        total_product_to_scrape = int(input("[?] No Products: "))
        d = {"path":"pro/finder","query":{"rootCategory":category,"sort":[["current_SALES","asc"]],"productType":[0,1,2],"page":page,"perPage":20},"domainId":1,"id":56,"version":7}
        send_encoded_msg(d)

    elif json_msg['id']==56:
        if json_msg['status']==200:
            products = json_msg['queryResult']['1']
            threading.Thread(target=searchProducts,args=(products,)).start()
        else:
            print(json_msg)
            return True
    

    elif json_msg['id']>10000:

        if json_msg['status']==200:
            parse_product(json_msg)
            tmp_products+=1
            if tmp_products>=20:
                page+=1
                tmp_products = 0
                d = {"path":"pro/finder","query":{"rootCategory":category,"sort":[["current_SALES","asc"]],"productType":[0,1,2],"page":page,"perPage":20},"domainId":1,"id":56,"version":7}
                send_encoded_msg(d)


        else:
            print(json_msg)
            return True
        
        products_count+=1
        if products_count>=total_product_to_scrape:
            return True
    
def main():
    while True:

        rev = base64.b64encode(ws.recv()).decode('utf-8')
        msg = decompress_msg(rev)
        json_msg = json.loads(msg.decode())
        if handle_msg(json_msg): break
    
    ws.close()

if __name__ == "__main__":
    total_product_to_scrape = 0
    tmp_products = 0
    page = 0
    category = None
    username = input('[?] Username/Email: ')
    password = getpass.getpass(prompt="[?] Password: ")

    main()