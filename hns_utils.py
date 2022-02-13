import requests

network = ""
node_port = ""
wallet_port = ""
api_key = ""

def set_credentials(net, api_key, ip):
    network = net
    
    if net == "main":
        wallet_portort = 12039
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


