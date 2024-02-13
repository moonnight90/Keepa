# import os
# import requests
# ses = requests.Session()
# ses.headers.update({
#     'Pragma': 'no-cache',
#     'Origin': 'https://keepa.com',
#     'Accept-Language': 'en-US,en;q=0.9,ur;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#     'Upgrade': 'websocket',
#     'Cache-Control': 'no-cache',
#     'Sec-WebSocket-Protocol': '8rj4ssmcujfh3j7ofh9ntrnj6vlmnc88vros1n9islr6sbbu4v0c18fi3kgon2a9',
#     'Connection': 'Upgrade',
#     'Sec-WebSocket-Version': '13',
#     'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
# })

# def f(i):
#     print(i.removesuffix('.json'))
#     while True:
#         res = ses.get(f'https://api.bookscouter.com/v4/prices/sell/{i.removesuffix('.json')}')
#         if res.status_code !=429:break
#     try:
#         print(res.json()['prices'][0]['price'])
#     except KeyError: 
#         print(res.json(),res.status_code)
# for i in os.listdir('files'):
#     f(i)

# # f('9780307742483')


import pandas as pd
tmp = {"ASIN":234,"Name":"Ahmad","LastName":"Raza"}

print(list)
df = pd.DataFrame([tmp])
print(df)
tmp = {"ASIN":234,"Name":"Ahmad","LastName":"R"}

keys = list(tmp.keys())
keys.remove('ASIN')
print
df.loc[df['ASIN'] == 234, keys] = [tmp[key] for key in keys]
print(df)