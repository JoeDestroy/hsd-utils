import requests
import json

network = ""
node_port = 0
wallet_port = 0
api_key = ""

node_request = ""
wallet_request = ""

def set_credentials(net, apiKey, ip):
    global network
    global node_port
    global wallet_port
    global api_key
    
    global node_request
    global wallet_request
    
    network = net
    
    if net == "main":
        wallet_port = 12039
    elif net == "testnet":
        wallet_port = 13039
    elif net == "regtest":
        wallet_port = 14039
    elif net == "simnet":
        wallet_port = 15039
    else:
        print("Invalid Network")
        
    node_port = wallet_port - 2;
    
    api_key = apiKey
    
    if api_key == None:
        node_request = "http://" + ip + ":" + str(node_port) + "/"
        wallet_request = "http://" + ip + ":" + str(wallet_port) + "/"
    else:
        node_request = "http://x:" + api_key + "@" + ip + ":" + str(node_port) + "/"
        wallet_request = "http://x:" + api_key + "@" + ip + ":" + str(wallet_port) + "/"


def get_node_info():
    
    ret = requests.get(node_request)
    
    return ret.json()
