import json
import time
import websocket
import base64
import zlib
import threading

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

ws = websocket.WebSocket()

ws.connect('wss://push.keepa.com/apps/cloud/?app=keepaWebsite&version=2.0',header=headers)
msg = "eJw1UNtSqzAU/ZVMnnSGA0mh3JzzANVSpe1YK9bq+BBogAAhGGhtdfx30xl92nuvfVtrfcGODCX0YSeFkZGBFkKeoAZ3ghPW3u6gjzX4h9/ueui//sNvGmzUSk1pR/RMcDW/V7VxjkQlC/HJmoYYYx2Biw1rd+KjB8tHgJGOroACbOsKHG3rEgRd19ANTWM2GGPT0U0bXMSzx8VcAw2rKYhoVotLMCml4NTAI6yrE+rqmuREst8V9fas4ITGy3lSJWvXuQ9XwX8FM8V/pATkHfS/IFNDeMg9XDDVk6rKjIdPz5w+ofvrRYzaJXq6CZJjF/LivZwxK3bqzV34wF9OWRK/1NtoUopoutpGYUF4I1LOC7HnyaY7rZ+juSDRhD9PXZIew0JMtzfd7GOV1O9BHah3g3LSQY5peubYchD+1uCByp6JFvqO8q2nZ0KurKy+59m+ykuzckReeu0g28o+NLzNXPcgRY9bj/WNtPs03VsHlGE3Z2ZdiHZEPPj9A1jSjsc="

ws.binaryType = "arraybuffer";


def decompress_msg(msg):
    try:
        a = zlib.decompress(base64.b64decode(msg))
    except:
        a = zlib.decompress(base64.b64decode(msg),-zlib.MAX_WBITS)
    finally:
        return a

def send():
    d2 = {"path":"pro/category","domainId":1,"categoryIds":[-1],"l":"keepa.com","u":"/","ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0","h":"y05NLUjUS87PBQA=","id":11673,"fp":{"i":"tncphz","r":"c/Rz93FV0PDMK0nN0VEAUxpBmgqhHi4K7kWJBRmZycUKZkYGChoGFQYGBgamlobmmgoumUWpySXGLoaGCmXF8abxBgoFYEpHwQUkqAkA","t":1707477556930},"version":7,"user":"bha97dms0blgbrf2ccslo0f6c6ontccu6h0rbob0pa3apd8jkdml29uscinkj4fk"}
    d = {"path":"pro/finder","query":{"rootCategory":9013971011,"sort":[["current_SALES","asc"]],"productType":[0,1,2],"page":0,"perPage":3},"domainId":1,"id":56,"version":7}
    # d = {"path":"pro/product","offerPages":0,"maxAge":60,"type":"finder","history":False,"domainId":"1","refreshProduct":False,"getTracking":False,"includeDeals":True,"stats":None,"getSubSalesRankAvg":True,"asin":"B09WPP7R6S","id":7795,"version":7}
    # d3 = {"path":"pro/category","domainId":"1","categoryIds":[283155,10177,11047977011,542656,1000,17,10134,2820,3153,3093,3291,119214268011,21420656011,4,2787,3298,10368549011,10368566011,10368617011,28,17443,10368546011,746228,7588890011,7588899011,158573011,6361468011,6190486011,9091108011,9091110011,119757778011,119757788011,7529252011,10239087011,10152210011,9578129011,12591927011,17982296011,17935005011,23,13371,133140011,7538390011,3568218011,2567,4480,9352387011,4736,4601,4747,11023,11070,11128,11170,11196,12678,12683,3568219011,6511973011,10166950011],"includeTrees":True,"id":11683,"version":7}
    # d4 = {"path":"product","history":True,"type":"ws","domainId":1,"asin":"1250178630","maxAge":3,"refreshProduct":False,"id":11686,"version":7}
    for i in [d2,d]:

        a = zlib.compress(json.dumps(i).encode())
        ws.send_binary(a)
        time.sleep(1)


sent = False

def searchProducts(products):
    print("Product Search Started...")
    for product in products:
        i = {"path":"pro/product","offerPages":0,"maxAge":60,"type":"finder","history":False,"domainId":"1","refreshProduct":False,"getTracking":False,"includeDeals":True,"stats":None,"getSubSalesRankAvg":True,"asin":product,"id":3670,"version":7}
        a = zlib.compress(json.dumps(i).encode())
        ws.send_binary(a)

while True:

    rev = base64.b64encode(ws.recv()).decode('utf-8')
    msg = decompress_msg(rev)
    jdata = json.loads(msg.decode())
    if jdata['id']==56:
        if jdata['status']==200:
            products = jdata['queryResult']['1']
            threading.Thread(target=searchProducts,args=(products,)).start()
        else:
            print(jdata)
    
    print(jdata['id'])
    # print(jdata)
    if not sent:
        threading.Thread(target=send).start()
        sent = not sent
    




