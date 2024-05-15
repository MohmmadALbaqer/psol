import os
import socket
import requests
import datetime
from prettytable import PrettyTable

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[93;1m" + "[" + "\033[91;1m" + "ERROR" + "\033[93;1m" + "]" + "\033[91;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"

now = datetime.datetime.now()
formatted_time = now.strftime("%I:%M %p")
formatted_day = now.strftime("%A")

date_day = "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "]" + "\033[97;1m" + "(" + "\033[93;1m" + formatted_day + "\033[95;1m" + f" {now:%B %D %Y}" + "\033[97;1m" + ")" + "\033[94;1m" + "[" + "\033[92;1m" + "Time" + "\033[94;1m" + "]" + "\033[93;1m" + "[" + "\033[91;1m" + formatted_time + "\033[93;1m" + "]" + "\033[97;1m"

__all__ = ['R', 'G', 'B', 'Y', 'C', 'M', 'W', 'D', 'sign', 'Enter', 'ERROR', 'INFO', 'warning', 'Complete', 'Failed', 'Sorry', 'data']

def clear_screen():
    operating_system = os.name

    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print("Unknow operating system.")
    except Exception as e:
        print(f"{ERROR} occurred: {W}{e}")

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

{date_day}  
{R}+------------------------------------------------------------------+
{R}|{G} GitHub{W} : {B}MohmmadALbaqer {W}|{Y} https://www.github.com/MohmmadALbaqer/ {R}|
{R}|{G} Instagram{W} :{B} r94xs {W}      |{Y} https://www.instagram.com/r94xs/       {R}|
{R}+------------------------------------------------------------------+{W}''')

def check_tunnel_status(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('serveo.net', 22))
        s.close()
        return f"{B}Online{W}"
    except Exception as e:
        return f"{R}Offline{W}"

def get_region():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get('country')
    except Exception as e:
        return "Unknown"

def generate_web_interface_link(port):
    return f"{G}http://127.0.0.1:{S}{D}{port}{W}"

def main():
    port = input(f"{Enter} Please enter port number: {Y}")
    print(date_day)
    tunnel_status = check_tunnel_status(port)
    region = get_region()
    web_interface_link = generate_web_interface_link(port)

    command = f"ssh -R 80:localhost:{port} serveo.net"
    print(f"{sign} {W}To stop and exit press or click {Y}[Ctrl {W}+{Y} C{Y}]{W}")
    table = PrettyTable()
    table.field_names = [f"{B}ID{W}", f"{G}Services{W}", f"{M}Information{W}"]

    table.add_row([f"{G}1{W}", f"{C}Port{W}", Y + port + W])
    table.add_row([f"{G}2{W}", f"{C}Region{W}", Y + region + W])
    table.add_row([f"{G}3{W}", f"{C}Tunnel Status{W}", tunnel_status + W])
    table.add_row([f"{G}4{W}", f"{C}Web Interface{W}", web_interface_link + W])
    table.add_row([f"{G}5{W}", f"{C}Command{W}", B + command + W])

    print(table)
    os.system(command)

if __name__ == "__main__":
    main()
