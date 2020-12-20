#!/usr/bin/python3

import os 
import sys
import requests
import json

# getting api urls
get_api = requests.get("https://pastebin.com/raw/ZLiLZjMC")
api_url_list = get_api.text.split()


def clear():    # Just to clean terminal
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def getIP():    # perform request to get public real ip in json format
    request = requests.get(api_url_list[0])
    return json.loads(json.dumps(request.json()))

def getIPInfo(ip):        # perform request to get info about ip
    api_url_list[1] = str(api_url_list[1] + str(ip))
    request = requests.get(api_url_list[1])
    return json.loads(json.dumps(request.json()))


def main():     # main method
    try:

        json_ip = getIP()
        json_ip_info = getIPInfo(json_ip["ip"]) 
       
        keys_list = None
        for item in json_ip_info:

            keys_list.append(str(item))
            print(keys_list) 

                # Defining exceptions
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


# -------------------------------------------------------
main()          # Here main is called
