import os
import sys 
import time 
import requests
from termcolor import colored
from colorama import Fore, Style, Back
from prettytable import PrettyTable

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
    print(f"{Fore.GREEN}[*] Internet connection is available. You can proceed with execution.{Style.RESET_ALL}")
    time.sleep(0.25)
else:
    print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.RED} No internet connection !{Style.RESET_ALL}")
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
                     {Fore.BLUE}. 
                    {Fore.BLUE}/ \\{Style.RESET_ALL}
  ____  ____        {Fore.BLUE}| |{Style.RESET_ALL}
 |  _ \/ ___|  ___  {Fore.BLUE}| |{Style.RESET_ALL}  
 | |_) \___ \ / {Fore.RED}_{Style.RESET_ALL} \ {Fore.BLUE}|.|{Style.RESET_ALL}   
 |  __/ ___) | {Fore.RED}(0){Style.RESET_ALL} |{Fore.BLUE}|.|{Style.RESET_ALL}  
 |_|   |____/ \_{Fore.RED}^{Style.RESET_ALL}_/ {Fore.BLUE}|:|{Style.RESET_ALL}  
                    {Fore.BLUE}|:|{Style.RESET_ALL}  
                 {Fore.WHITE}~{Fore.YELLOW}\==8==/{Fore.WHITE}~{Style.RESET_ALL}
                     {Fore.RED}8{Style.RESET_ALL}
                     {Fore.RED}0{Style.RESET_ALL} 
 +--------------------------+
 |{Back.RED} port sharer open launche {Style.RESET_ALL}|
 +--------------------------+  

{Fore.RED}+------------------------------------------------------------------+
{Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
{Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.comr94xs/        {Fore.RED}|
{Fore.RED}+------------------------------------------------------------------+{Style.RESET_ALL}''')

port = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.BLUE}please Enter numper port: {Fore.YELLOW}")
print(f"{Style.RESET_ALL}")

command = f"ssh -R 80:localhost:{port} serveo.net"

print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.BLUE}If you want to exit click {Fore.YELLOW}[Ctrl+c]{Style.RESET_ALL}")

table = PrettyTable()
table.field_names = [f"{Fore.GREEN}ID{Style.RESET_ALL}", f"{Fore.RED}Port{Style.RESET_ALL}", f"{Fore.MAGENTA}Command{Style.RESET_ALL}"]

table.add_row([f"{Fore.YELLOW}1{Style.RESET_ALL}", port, command])

print(table)

os.system(command)

