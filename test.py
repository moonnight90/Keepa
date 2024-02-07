import json
import websocket
import base64
import zlib


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
        print('without')
    except:
        a = zlib.decompress(base64.b64decode(msg),-zlib.MAX_WBITS)
        print('maxbit')
    finally:
        return a

def send():
    d = {"path":"pro/category","domainId":1,"categoryIds":[-1],"l":"keepa.com","u":"/","ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","h":"y05NLUjUS87PBQA=","id":22,"fp":{"i":"1tf91gi","r":"c/Rz93FV0PDMK0nN0VEAUxpBmgqhHi4K7kWJBRmZycUKZkYGChoGFQYGBgamlobmmgoumUWpySXGLoaGCmXF8abxBgoFYEpHwQUkqAkA","t":1707339354701},"version":7,"user":"8rj4ssmcujfh3j7ofh9ntrnj6vlmnc88vros1n9islr6sbbu4v0c18fi3kgon2a9"}

    a = zlib.compress(json.dumps(d).encode())
    ws.send_binary(a)


sent = False

while True:

    rev = base64.b64encode(ws.recv()).decode('utf-8')
    msg = decompress_msg(rev)
    print(msg.decode())

    if not sent:
        # send()
        sent = not sent




