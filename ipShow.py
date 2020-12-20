#!/usr/bin/python3

import os 
import sys
import requests
import json
from colorama import Fore, Back, Style

# getting api urls
get_api = requests.get("https://pastebin.com/raw/ZLiLZjMC")
api_url_list = get_api.text.split()


def getIP():    # perform request to get public real ip in json format
    request = requests.get(api_url_list[0])
    return json.loads(json.dumps(request.json()))

def getIPInfo(ip):  # perform request to get info about ip
    api_url_list[1] = str(api_url_list[1] + str(ip))
    request = requests.get(api_url_list[1])
    return json.loads(json.dumps(request.json()))

def torDetector(ip):    # search in database if IP is a tor exit node
    request = requests.get(api_url_list[2])
    tor_exit_nodes_list = request.text.split()

    if ip in tor_exit_nodes_list:
        return True
    elif ip not in tor_exit_nodes_list:
        return False
    else:
        return None

def main():     # main method

    json_ip = getIP()
    json_ip_info = getIPInfo(json_ip["ip"]) 
       
#-------------- Printing IP ----------------------------------
        
    print(" ")
    print("IP" + " --> " + json_ip["ip"])

# --------------- Printing IP info -----------------------------
    keys_list = []
    values_list = []

    for key in json_ip_info:
        keys_list.append(str(key))
        
    for value in json_ip_info.values():
        values_list.append(value)
       
    i = 0
    for item in range(len(keys_list)):
        print(str(keys_list[i]) + " --> " + str(values_list[i]))
        i = i + 1

        if i == 13:
            break

# ---------------- Checking if IP is in tor exit node database ---
    print(" ")
    print("Tor exit node" + " --> " + str(torDetector(json_ip["ip"])))

#----------------------- Calling main method ----------------------

try:

    main()  # Here main is called


except requests.exceptions.ConnectionError:
    print("ConnectionError - Check internet connection:(")
    print("please check your interent connection")
    sys.exit()
except requests.exceptions.HTTPError:
    print("HTTPError -- API is not sending valid requests :(")
    sys.exit()
except requests.exceptions.ProxyError:
    print("ProxyError -- Proxy is refusing connections :(")
    sys.exit()
except requests.exceptions.SSLError:
    print("SSLError  :(")
    sys.exit()
except requests.exceptions.Timeout:
    print("Timeout - Connection with server expired :(")
    sys.exit()

