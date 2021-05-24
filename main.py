import os
import requests
import time
import sys
os.system('mode con: cols=130 lines=30')
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
def Clear():
    os.system('cls')
    print(colorText(verinfo))
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
verinfo = '''[[red]]
                                           ▄█   ▄█▄    ▄████████    ▄███████▄     ███     
                                          ███ ▄███▀   ███    ███   ███    ███ ▀█████████▄ 
                                          ███▐██▀     ███    ███   ███    ███    ▀███▀▀██ 
                                         ▄█████▀     ▄███▄▄▄▄██▀   ███    ███     ███   ▀ 
                                        ▀▀█████▄    ▀▀███▀▀▀▀▀   ▀█████████▀      ███     
                                          ███▐██▄   ▀███████████   ███            ███     
                                          ███ ▀███▄   ███    ███   ███            ███     
                                          ███   ▀█▀   ███    ███  ▄████▀         ▄████▀   
                                          ▀           ███    ███                            [[white]]
                                          '''

print(colorText(verinfo))
i=1
while i == 1:
    try:
        what = eval(input(colorText('''No Command Line Arguements found, fallback to procedural mode  
          
[[green]][1] Wallet Search
[2] Transaction Info
[3] About
[4] Help[[white]]
[[blue]]Input : [[white]]''')))
        if type(what) == int:
            i = 2
        else:
            raise TypeError
    except TypeError:
        print("Invalid Input")
        os.system('cls')
        print(colorText(verinfo))
#Transaction Info Block
if what == 1:
    Clear()
    wallet = input(colorText("[[green]]Wallet & Type(Example: LKnF9CELAZf2LztVFu1Rq5TmwMJUfrX2uh,litecoin):[[green]][[cyan]] "))
    infomer = wallet.split(',')
    wall = infomer[0]
    type = infomer[1]
    endpoint = f"https://api.blockchair.com/{type}/dashboards/address/{wall}"

    try:
        r = requests.get(endpoint)
    except:
        print(colorText("[[red]]Network Request Failed, Trying again in 3sec...[[white]]"))
        time.sleep(3)
        try:
            r = requests.get(endpoint)
        except:
            print("[[red]]Request Failed Again, Check your network.[[white]]")


    jsonr = r.json()
    print(colorText("[[white]] Please wait..."))
    Clear()
    '''Variables Defined For Easy Access.'''
    raw_bal = str(json_extract(jsonr,'balance_usd'))
    p_bal = raw_bal.replace('[','').replace(']','') + " USD" #BALANCE OF Wallet
    raw_trans = str(json_extract(jsonr,'transaction_count'))
    p_trans = raw_trans.replace('[','').replace(']','') #Transaction Count
    raw_firstseen = str(json_extract(jsonr,'first_seen_receiving'))
    p_firstseen = raw_firstseen.replace('[','').replace(']','').replace('\'','')
    raw_spentusd = str(json_extract(jsonr,'spent_usd'))
    p_spentusd = raw_spentusd.replace('[','').replace(']','') + " USD"
    raw_receivedusd = str(json_extract(jsonr, 'received_usd'))
    p_receivedusd = raw_receivedusd.replace('[', '').replace(']', '') + " USD"
    raw_lastseen = str(json_extract(jsonr, 'last_seen_receiving'))
    p_lastseen = raw_lastseen.replace('[', '').replace(']', '').replace('\'', '')
    '''ENDS HERE'''

    infologic = \
f'''\t
    [[blue]]First Seen On Blockchain : [[cyan]]{p_firstseen}
    [[blue]]Spent USD                : [[cyan]]{p_spentusd}                                                     
    [[blue]]Current Balance          : [[cyan]]{p_bal}
    [[blue]]Received USD             : [[cyan]]{p_receivedusd}                                 
    [[blue]]Transactions Count       : [[cyan]]{p_trans}
    [[blue]]Last Seen                : [[cyan]]{p_lastseen}[[white]]                                                     
'''
    print(colorText(infologic))

if what == 2:
    Clear()
    wallet = input(
        colorText("[[green]]Transaction hash & Type(Example: hash,litecoin):[[green]][[cyan]] "))
    infomer = wallet.split(',')
    wall = infomer[0]
    type = infomer[1]
    endpoint = f"https://api.blockchair.com/{type}/dashboards/transaction/{wall}"
    try:
        r = requests.get(endpoint)
    except:
        print(colorText("[[red]]Network Request Failed, Trying again in 3sec...[[white]]"))
        time.sleep(3)
        try:
            r = requests.get(endpoint)
        except:
            print("[[red]]Request Failed Again, Check your network.[[white]]")

    jsonr = r.json()
    print(colorText("[[white]] Please wait..."))
    Clear()
    '''Define vars and print'''
if what == 3:
    print("made by Port007")
if what == 4:
    Clear()
    u_text= \
'''[[green]]Supported Crypto Currencies:[[blue]]

    1. Bitcoin(bitcoin)
    2. Bitcoin Cash(bitcoin-cash)
    3. Litecoin(litecoin)
    4. bitcoin-sv
    5. Dogecoin
    6. Dash
    7. Groestlcoin
    8. Zcash[[white]]'''
    print(colorText(u_text))
os.system('pause')
sys.exit()