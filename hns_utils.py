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


def set_credentials_adv(nodePort, walletPort, apiKey, ip):
    global network
    global node_port
    global wallet_port
    global api_key
    
    global node_request
    global wallet_request
    
    network = net
    
    node_port = nodePort
    wallet_port = walletPort
    
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


# Wallet functions

# Gets a list of wallets associated with the HSD Node
def get_wallets():
    
    ret = requests.get(wallet_request + "wallet/")
    
    return ret.json()
    

def create_wallet(id, password):
    
    header = [{"passphrase": str(password)}]
    
    req = requests.put(wallet_request + "wallet/" + id, data=json.dumps(header))
   
 
def reset_wallet_token(walletId):
    
    requests.post(wallet_request + "wallet/" + id + "/retoken")
    
    
def get_wallet_info(walletId):
    
    req = requests.get(wallet_request + "wallet/" + walletId)
    
    return req.json()


# Transaction functions
# To use this, enable --index-tx=true when running HSD

def get_tx(address):
    
    req = requests.get(node_request + "tx/address/" + address)
    
    return req.json()


def get_tx_hash(hash):
    
    req = requests.get(node_request + "tx/" + hash)
    
    return req.json()
