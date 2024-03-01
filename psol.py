import os
from colorama import Fore, Style, Back
from prettytable import PrettyTable

os.system("clear")

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
 {Fore.RED}<--------------------------------------------------------------------->
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW}   https://www.github.com/MohmmadALbaqer/  {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW}   https://www.instagram.com/r94xs/        {Fore.RED}|
 {Fore.RED}+---------------------------------------------------------------------+{Style.RESET_ALL}                 
''')

port = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.BLUE}please Enter numper port: {Fore.YELLOW}")
print(f"{Style.RESET_ALL}")

command = f"ssh -R 80:localhost:{port} serveo.net"

table = PrettyTable()
table.field_names = [f"{Fore.GREEN}ID{Style.RESET_ALL}", f"{Fore.RED}Port{Style.RESET_ALL}", f"{Fore.MAGENTA}Command{Style.RESET_ALL}"]

table.add_row([f"{Fore.YELLOW}1{Style.RESET_ALL}", port, command])

print(table)

os.system(command)
