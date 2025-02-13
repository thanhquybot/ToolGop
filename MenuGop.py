import requests,re
from colorama import *
from art import *
import os
from concurrent.futures import ThreadPoolExecutor
from data import data1
from time import sleep
import random
import threading
import socket
import dns.resolver
import concurrent.futures
from fake_useragent import UserAgent
ua = UserAgent()
lock = threading.Lock()
condition = threading.Condition()
import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys
import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
import subprocess
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
try:
	from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
	os.system("pip install pystyle")
	from pystyle import Colors, Colorate, Write, Center, Add, Box
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
  
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.05)
  print()
def banner():
 os.system('cls' if os.name == 'nt' else 'clear')
 print(Colorate.Diagonal(Colors.purple_to_red, """
████████╗ ██████╚╗         ████████╗ █████╗  █████╗ ██╗
╚══██╔══╝██║   ██║         ╚══██╔══╝██╔══██╗██╔══██╗██║
   ██║   ██║   ██║   █████╗   ██║   ██║  ██║██║  ██║██║
   ██║   ██║ ████╚╗  ╚════╝   ██║   ██║  ██║██║  ██║██║
   ██║   ╚████████║           ██║   ╚█████╔╝╚█████╔╝██████╗
   ╚═╝    ╚════╗██║           ╚═╝    ╚════╝  ╚════╝ ╚═════╝
               ╚══╝
══════════════════════════════════════════════════════════════
[📝] Admin    : Thành Quý Tool
[📝] Telegram : https://t.me/quyleotool
[📝] Youtube  : https://www.youtube.com/@thanhquytool
══════════════════════════════════════════════════════════════
"""))

banner()
print (Colorate.Diagonal(Colors.blue_to_purple, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.blue_to_purple, "║  Tool Aotu Golike       ║"))
print (Colorate.Diagonal(Colors.blue_to_purple, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.red_to_white, "● [🧸] ➩ Nhập Số | 1.1 | => Tool Golike TikTok"))
print (Colorate.Diagonal(Colors.red_to_white, "● [🧸] ➩ Nhập Số | 1.2 | => Tool Golike Instagram"))
print (Colorate.Diagonal(Colors.red_to_white, "● [🧸] ➩ Nhập Số | 1.3 | => Tool Golike Threads"))
print (Colorate.Diagonal(Colors.red_to_white, "● [🧸] ➩ Nhập Số | 1.4 | => Tool Golike Linkedin"))
print (Colorate.Diagonal(Colors.green_to_cyan, "──────────────────────────────────────────────────────────────"))
chon = str(input (Colorate.Diagonal(Colors.blue_to_cyan, '● [🧸] ➩ Nhập Số: ')))
text='\033[1;37m● \033[1;36mĐang Vào Tool...'
pr(text)
if chon == '1.1' :
    exec(requests.get('https://raw.githubusercontent.com/thanhquybot/ToolGop/main/Golike/GolikeTikTok.py').text)
if chon == '1.2' :
    exec(requests.get('https://raw.githubusercontent.com/thanhquybot/ToolGop/main/Golike/GolikeInstagram.py').text)
if chon == '1.3' :
    exec(requests.get('https://raw.githubusercontent.com/thanhquybot/ToolGop/main/Golike/GolikeThreads.py').text)
if chon == '1.4' :
    exec(requests.get('https://raw.githubusercontent.com/thanhquybot/ToolGop/main/Golike/GolikeLinkedin.py').text)
else :
     exit()