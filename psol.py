import os
import sys 
import time 
import requests
from termcolor import colored
from colorama import Fore, Style, Back, init
from prettytable import PrettyTable

init()

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey

INFO = f'{B}[{G}INFO{B}]'
ERROR = f'{Y}[{R}!{Y}]{R}'
sign = f'{G}[{B}*{G}]{C}'

def clear_screen():
    operating_system = os.name
    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print(f"{ERROR} System unknown !{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Y}[{R}ERROR{Y}]{W}: {e}")
clear_screen()

def spin():
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    for _ in range(1):
        for i in spinner:
            message = f"[*] {Fore.BLUE}Checking your internet connection...[{i}]{Style.RESET_ALL}"
            colored_message = colored(message, 'blue', attrs=['bold'])
            sys.stdout.write(f"\r{colored_message}   ")
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write("\r")
    sys.stdout.flush()
    done_message = colored("[+] Your Internet connection has been verified", 'yellow', attrs=['bold'])
    sys.stdout.write("\033[K") 
    print(done_message)
    time.sleep(1)

spin()

def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

if check_internet_connection():
    print(f"{sign} Internet connection is available. You can proceed with execution.{W}")
    time.sleep(0.25)
else:
    print(f"{ERROR} No internet connection !{W}")
    exit()

def clear_screen():
    operating_system = os.name

    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"An error occurred: {e}")

clear_screen()

print(f'''
                     {B}. 
                    {B}/ \\{W}
  ____  ____        {B}| |{W}
 |  _ \/ ___|  ___  {B}| |{W}  
 | |_) \___ \ / {R}_{W} \ {B}|.|{W}   
 |  __/ ___) | {R}(0){W} |{B}|.|{W}  
 |_|   |____/ \_{R}^{W}_/ {B}|:|{W}  
                    {B}|:|{W}  
                 {W}~{Y}\==8==/{W}~{W}
                     {R}8{W}
                     {R}0{W} 
 +--------------------------+
 |{Back.RED}{W} port sharer open launche {Style.RESET_ALL}|
 +--------------------------+  

{R}+------------------------------------------------------------------+
{R}|{G} GitHub{W} : {B}MohmmadALbaqer {W}|{Y} https://www.github.com/MohmmadALbaqer/ {R}|
{R}|{G} Instagram{W} :{B} r94xs {W}      |{Y} https://www.instagram.com/r94xs/       {R}|
{R}+------------------------------------------------------------------+{W}''')

port = input(f"{sign} please Enter numper port: {Y}")
print(f"{W}")

command = f"ssh -R 80:localhost:{port} serveo.net"

print(f"{B}[{G}+{B}] {Style.RESET_ALL}If you are waiting for a long time in downloading click to exit {Y}[Ctrl {W}+{Y} C{Y}]{W}")

table = PrettyTable()
table.field_names = [f"{G}ID{W}", f"{R}Port{W}", f"{M}Command{W}"]

table.add_row([f"{Y}1{W}", port, command])

print(table)

os.system(command)

