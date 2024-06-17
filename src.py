import json
from colorit import *
from time import sleep as sleep
import ctypes
import psutil
import os
import socket
import re
import subprocess
import requests
import fade



home_dir = os.path.expanduser("~")

appdata_path = os.path.join(home_dir, 'AppData', 'Roaming')

def write():
    f = open("cmds.txt", "a")
    f.write("""
0 - exit console
1 - scan ip if is it active
2 - listen ip connections
3 - start putty
4 - lower down ping
5 - command prompt
6 - ip pinger
7 - run forest run animation
8 - rename display name
                                
""")
    f.close()

# Define the ANSI escape codes for colors
END = '\33[0m'
BOLD = '\33[1m'
ITALIC = '\33[3m'
URL = '\33[4m'
BLINK = '\33[5m'
BLINK2 = '\33[6m'
SELECTED = '\33[7m'

BLACK = '\33[30m'
RED = '\33[31m'
GREEN = '\33[32m'
YELLOW = '\33[33m'
BLUE = '\33[34m'
VIOLET = '\33[91m'
BEIGE = '\33[36m'
WHITE = '\33[37m'

BLACKBG = '\33[40m'
REDBG = '\33[41m'
GREENBG = '\33[42m'
YELLOWBG = '\33[43m'
BLUEBG = '\33[44m'
VIOLETBG = '\33[45m'
BEIGEBG = '\33[46m'
WHITEBG = '\33[47m'

GREY = '\33[90m'
RED2 = '\33[91m'
GREEN2 = '\33[92m'
YELLOW2 = '\33[93m'
BLUE2 = '\33[94m'
VIOLET2 = '\33[95m'
BEIGE2 = '\33[96m'
WHITE2 = '\33[97m'

GREYBG = '\33[100m'
REDBG2 = '\33[101m'
GREENBG2 = '\33[102m'
YELLOWBG2 = '\33[103m'
BLUEBG2 = '\33[104m'
VIOLETBG2 = '\33[105m'
BEIGEBG2 = '\33[106m'
WHITEBG2 = '\33[107m'

def load_logos():
    if os.path.exists('console.json'):
        with open('console.json', encoding='utf-8') as f:
            data = json.load(f)
        return data['logos']
    else:
        download_json()
        with open('console.json', encoding='utf-8') as f:
            data = json.load(f)
        return data['logos']
        

def print_logo(logo_config):
    print(logo_config['logo'])

def load_chosen_logo():
    # Function to load the chosen logo configuration from JSON
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            chosen_logo = json.load(f)
        return chosen_logo
    else:
        f = write

def choose_logo():
    logos = load_logos()
    
    print("Available logo configurations:")
    for i, logo in enumerate(logos):
        print(f"{i + 1}. {logo['name']}")
    
    while True:
        try:
            choice = int(input("Choose a logo config: "))
            if 1 <= choice <= 5:
                chosen_logo = logos[choice - 1]
                
                # Save the chosen logo configuration to a JSON file
                save_chosen_logo(chosen_logo)
                
                return chosen_logo
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_chosen_logo(chosen_logo):
    # Example function to save chosen logo configuration to a JSON file
    with open('config.json', 'w') as f:
        json.dump(chosen_logo, f)


url = "https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe"
console_json = """{
  "logos": [
    {
      "name": "blue",
      "VIOLET": "\\u001b[34m",
      "WHITE2": "\\u001b[37m",
      "RED": "\\u001b[34m",
      "END": "\\u001b[0m",
      "logo": "\\u001b[34m ██████\\u001b[37m╗\\u001b[34m██\\u001b[37m╗ \\u001b[34m██████\\u001b[37m╗ \\u001b[34m█████\\u001b[37m╗ \\u001b[34m██████\\u001b[37m╗  \\u001b[34m█████\\u001b[37m╗ \\n\\u001b[34m██\\u001b[37m╔════╝\\u001b[34m██\\u001b[37m║\\u001b[34m██\\u001b[37m╔════╝\\u001b[34m██\\u001b[37m╔══\\u001b[34m██\\u001b[37m╗\\u001b[34m██\\u001b[37m╔══\\u001b[34m██\\u001b[37m╗\\u001b[34m██\\u001b[37m╔══\\u001b[34m██\\u001b[37m╗\\n\\u001b[34m██\\u001b[37m║     \\u001b[34m██\\u001b[37m║\\u001b[34m██\\u001b[37m║     \\u001b[34m███████\\u001b[37m║\\u001b[34m██\\u001b[37m║  \\u001b[34m██\\u001b[37m║\\u001b[34m███████\\u001b[37m║\\n\\u001b[34m██\\u001b[37m║     \\u001b[34m██\\u001b[37m║\\u001b[34m██\\u001b[37m║     \\u001b[34m██\\u001b[37m╔══\\u001b[34m██\\u001b[37m║\\u001b[34m██\\u001b[37m║  \\u001b[34m██\\u001b[37m║\\u001b[34m██\\u001b[37m╔══\\u001b[34m██\\u001b[37m║\\n\\u001b[37m╚\\u001b[34m██████\\u001b[37m╗\\u001b[34m██\\u001b[37m║╚\\u001b[34m██████\\u001b[37m╗\\u001b[34m██\\u001b[37m║  \\u001b[34m██\\u001b[37m║\\u001b[34m██████\\u001b[37m╔╝\\u001b[34m██\\u001b[37m║  \\u001b[34m██\\u001b[37m║\\n \\u001b[37m╚═════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝\\n\\u001b[0mDisclaimer: \\u001b[31mWe are not responsible for any damage caused by cicada\\u001b[0m"
    },
    {
      "name": "light yellow",
      "VIOLET": "\\u001b[93m",
      "WHITE2": "\\u001b[37m",
      "RED": "\\u001b[93m",
      "END": "\\u001b[0m",
      "logo": "\\u001b[93m ██████\\u001b[37m╗\\u001b[93m██\\u001b[37m╗ \\u001b[93m██████\\u001b[37m╗ \\u001b[93m█████\\u001b[37m╗ \\u001b[93m██████\\u001b[37m╗  \\u001b[93m█████\\u001b[37m╗ \\n\\u001b[93m██\\u001b[37m╔════╝\\u001b[93m██\\u001b[37m║\\u001b[93m██\\u001b[37m╔════╝\\u001b[93m██\\u001b[37m╔══\\u001b[93m██\\u001b[37m╗\\u001b[93m██\\u001b[37m╔══\\u001b[93m██\\u001b[37m╗\\u001b[93m██\\u001b[37m╔══\\u001b[93m██\\u001b[37m╗\\n\\u001b[93m██\\u001b[37m║     \\u001b[93m██\\u001b[37m║\\u001b[93m██\\u001b[37m║     \\u001b[93m███████\\u001b[37m║\\u001b[93m██\\u001b[37m║  \\u001b[93m██\\u001b[37m║\\u001b[93m███████\\u001b[37m║\\n\\u001b[93m██\\u001b[37m║     \\u001b[93m██\\u001b[37m║\\u001b[93m██\\u001b[37m║     \\u001b[93m██\\u001b[37m╔══\\u001b[93m██\\u001b[37m║\\u001b[93m██\\u001b[37m║  \\u001b[93m██\\u001b[37m║\\u001b[93m██\\u001b[37m╔══\\u001b[93m██\\u001b[37m║\\n\\u001b[37m╚\\u001b[93m██████\\u001b[37m╗\\u001b[93m██\\u001b[37m║╚\\u001b[93m██████\\u001b[37m╗\\u001b[93m██\\u001b[37m║  \\u001b[93m██\\u001b[37m║\\u001b[93m██████\\u001b[37m╔╝\\u001b[93m██\\u001b[37m║  \\u001b[93m██\\u001b[37m║\\n \\u001b[37m╚═════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝\\n\\u001b[0mDisclaimer: \\u001b[31mWe are not responsible for any damage caused by cicada\\u001b[0m"
    },
    {
      "name": "red",
      "VIOLET": "\\u001b[31m",
      "WHITE2": "\\u001b[37m",
      "RED": "\\u001b[31m",
      "END": "\\u001b[0m",
      "logo": "\\u001b[31m ██████\\u001b[37m╗\\u001b[31m██\\u001b[37m╗ \\u001b[31m██████\\u001b[37m╗ \\u001b[31m█████\\u001b[37m╗ \\u001b[31m██████\\u001b[37m╗  \\u001b[31m█████\\u001b[37m╗ \\n\\u001b[31m██\\u001b[37m╔════╝\\u001b[31m██\\u001b[37m║\\u001b[31m██\\u001b[37m╔════╝\\u001b[31m██\\u001b[37m╔══\\u001b[31m██\\u001b[37m╗\\u001b[31m██\\u001b[37m╔══\\u001b[31m██\\u001b[37m╗\\u001b[31m██\\u001b[37m╔══\\u001b[31m██\\u001b[37m╗\\n\\u001b[31m██\\u001b[37m║     \\u001b[31m██\\u001b[37m║\\u001b[31m██\\u001b[37m║     \\u001b[31m███████\\u001b[37m║\\u001b[31m██\\u001b[37m║  \\u001b[31m██\\u001b[37m║\\u001b[31m███████\\u001b[37m║\\n\\u001b[31m██\\u001b[37m║     \\u001b[31m██\\u001b[37m║\\u001b[31m██\\u001b[37m║     \\u001b[31m██\\u001b[37m╔══\\u001b[31m██\\u001b[37m║\\u001b[31m██\\u001b[37m║  \\u001b[31m██\\u001b[37m║\\u001b[31m██\\u001b[37m╔══\\u001b[31m██\\u001b[37m║\\n\\u001b[37m╚\\u001b[31m██████\\u001b[37m╗\\u001b[31m██\\u001b[37m║╚\\u001b[31m██████\\u001b[37m╗\\u001b[31m██\\u001b[37m║  \\u001b[31m██\\u001b[37m║\\u001b[31m██████\\u001b[37m╔╝\\u001b[31m██\\u001b[37m║  \\u001b[31m██\\u001b[37m║\\n \\u001b[37m╚═════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝\\n\\u001b[0mDisclaimer: \\u001b[31mWe are not responsible for any damage caused by cicada\\u001b[0m"
    },
    {
      "name": "light violet",
      "VIOLET": "\\u001b[95m",
      "WHITE2": "\\u001b[37m",
      "RED": "\\u001b[95m",
      "END": "\\u001b[0m",
      "logo": "\\u001b[95m ██████\\u001b[37m╗\\u001b[95m██\\u001b[37m╗ \\u001b[95m██████\\u001b[37m╗ \\u001b[95m█████\\u001b[37m╗ \\u001b[95m██████\\u001b[37m╗  \\u001b[95m█████\\u001b[37m╗ \\n\\u001b[95m██\\u001b[37m╔════╝\\u001b[95m██\\u001b[37m║\\u001b[95m██\\u001b[37m╔════╝\\u001b[95m██\\u001b[37m╔══\\u001b[95m██\\u001b[37m╗\\u001b[95m██\\u001b[37m╔══\\u001b[95m██\\u001b[37m╗\\u001b[95m██\\u001b[37m╔══\\u001b[95m██\\u001b[37m╗\\n\\u001b[95m██\\u001b[37m║     \\u001b[95m██\\u001b[37m║\\u001b[95m██\\u001b[37m║     \\u001b[95m███████\\u001b[37m║\\u001b[95m██\\u001b[37m║  \\u001b[95m██\\u001b[37m║\\u001b[95m███████\\u001b[37m║\\n\\u001b[95m██\\u001b[37m║     \\u001b[95m██\\u001b[37m║\\u001b[95m██\\u001b[37m║     \\u001b[95m██\\u001b[37m╔══\\u001b[95m██\\u001b[37m║\\u001b[95m██\\u001b[37m║  \\u001b[95m██\\u001b[37m║\\u001b[95m██\\u001b[37m╔══\\u001b[95m██\\u001b[37m║\\n\\u001b[37m╚\\u001b[95m██████\\u001b[37m╗\\u001b[95m██\\u001b[37m║╚\\u001b[95m██████\\u001b[37m╗\\u001b[95m██\\u001b[37m║  \\u001b[95m██\\u001b[37m║\\u001b[95m██████\\u001b[37m╔╝\\u001b[95m██\\u001b[37m║  \\u001b[95m██\\u001b[37m║\\n \\u001b[37m╚═════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝\\n\\u001b[0mDisclaimer: \\u001b[31mWe are not responsible for any damage caused by cicada\\u001b[0m"
    },
    {
        "name": "green",
        "VIOLET": "\\u001b[32m",
        "WHITE2": "\\u001b[37m",
        "RED": "\\u001b[32m",
        "END": "\\u001b[0m",
        "logo": "\\u001b[32m ██████\\u001b[37m╗\\u001b[32m██\\u001b[37m╗ \\u001b[32m██████\\u001b[37m╗ \\u001b[32m█████\\u001b[37m╗ \\u001b[32m██████\\u001b[37m╗  \\u001b[32m█████\\u001b[37m╗ \\n\\u001b[32m██\\u001b[37m╔════╝\\u001b[32m██\\u001b[37m║\\u001b[32m██\\u001b[37m╔════╝\\u001b[32m██\\u001b[37m╔══\\u001b[32m██\\u001b[37m╗\\u001b[32m██\\u001b[37m╔══\\u001b[32m██\\u001b[37m╗\\u001b[32m██\\u001b[37m╔══\\u001b[32m██\\u001b[37m╗\\n\\u001b[32m██\\u001b[37m║     \\u001b[32m██\\u001b[37m║\\u001b[32m██\\u001b[37m║     \\u001b[32m███████\\u001b[37m║\\u001b[32m██\\u001b[37m║  \\u001b[32m██\\u001b[37m║\\u001b[32m███████\\u001b[37m║\\n\\u001b[32m██\\u001b[37m║     \\u001b[32m██\\u001b[37m║\\u001b[32m██\\u001b[37m║     \\u001b[32m██\\u001b[37m╔══\\u001b[32m██\\u001b[37m║\\u001b[32m██\\u001b[37m║  \\u001b[32m██\\u001b[37m║\\u001b[32m██\\u001b[37m╔══\\u001b[32m██\\u001b[37m║\\n\\u001b[37m╚\\u001b[32m██████\\u001b[37m╗\\u001b[32m██\\u001b[37m║╚\\u001b[32m██████\\u001b[37m╗\\u001b[32m██\\u001b[37m║  \\u001b[32m██\\u001b[37m║\\u001b[32m██████\\u001b[37m╔╝\\u001b[32m██\\u001b[37m║  \\u001b[32m██\\u001b[37m║\\n \\u001b[37m╚═════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝\\n\\u001b[0mDisclaimer: \\u001b[31mWe are not responsible for any damage caused by cicada\\u001b[0m"
    }]
}"""

def download_json():
    json_string = f'{console_json}'

# Parse JSON string
    data = json.loads(json_string)

# Write data to a JSON file
    with open('console.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Send a GET request to the URL
response = requests.get(url)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Define the local filename to save the downloaded file
local_filename = "putty.exe"

# Write the content of the response to a file

er = "fatal error: "

ctypes.windll.kernel32.SetConsoleTitleW("Cicada")
init_colorit()

def show_active_connections():
    try:
        while True:
            # Execute the netstat command
            result = subprocess.run(['netstat', '-an'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Check if the command executed successfully
            if result.returncode == 0:
                # Split the output into lines
                output_lines = result.stdout.splitlines()

                # Iterate over each line and filter active connections
                for line in output_lines:
                    if "ESTABLISHED" in line or "LISTEN" in line:
                        print(line)
            else:
                # Print error message if the command failed
                print("Error executing netstat command:", result.stderr)
            
            # Wait for a few seconds before running again
            sleep(0.2)
    except KeyboardInterrupt:
        print("\\nKeyboardInterrupt detected. Exiting...")

def logo(logo_config):
    # Function to print the logo based on the configuration
    print(f"{logo_config['logo']}")

def logo():
    chosen_logo = load_chosen_logo()
    if not chosen_logo:
        chosen_logo = choose_logo()
    
    cls()
    print_logo(chosen_logo)

def is_ip_active(ip):
    param = '-c' if os.name != 'nt' else '-n'
    null = '>/dev/null 2>&1' if os.name != 'nt' else '>nul 2>&1'
    command = f"ping {param} 1 {ip} {null}"

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def user():
    if os.path.exists('user'):
        os.chdir('user')    
    else:
        os.mkdir('user')
        os.chdir('user')
def load():

    os.chdir(appdata_path)
    if os.path.exists('cicada-sploit'):
        os.chdir('cicada-sploit')
        user()
        gui()
    else:
        print(f"couldnt find user directory")
        sleep(0.76)
        print(f"making user directory...")
        sleep(2)
        os.mkdir('cicada-sploit')
        os.chdir('cicada-sploit')
        user()
        gui()

def gui():
    cls()
    logo()
    username_file = "name.json"

    if os.path.exists(username_file):
        with open(username_file, "r") as json_file:
            data = json.load(json_file)
            username = data.get("username", "unknown user")
        print(f"{VIOLETBG2}Tip: use 'help' command{END}")
        int = input(f"""
┌────({RED}{username}{END})-[{VIOLET}cicada-sploit{END}]
│
└──{RED}#{END} """)
        if int == "0":
            exit()
        elif int == "1":
                cls()
                logo()
                ip = input(f"""
┌────({RED}{username}{END})-[{GREEN}cicada-sploit{END}]
│
└──{RED}#{END} """)
                if is_ip_active(ip):
                    print(f"{ip}: {GREEN}is active{END}")
                    sleep(3)
                else:
                    print(f"{ip}: {RED}is not active{END}")
                    sleep(3)
                gui()
        elif int == "2":
                show_active_connections()
                gui()
        elif int == "3":
            if os.path.exists('putty.exe'):
                subprocess.Popen(["putty.exe"])
            else:
                print(f"{er}couldnt find putty.exe")
                print("downloading putty...")
                sleep(1.2)
                with open(local_filename, 'wb') as file:
                    file.write(response.content)
                subprocess.Popen(["putty.exe"])
            gui()
        elif int == "4":
             os.system('ipconfig /flushdns')
             sleep(2)
             gui() 
        elif int == "5":
            os.system("start cmd.exe")
            gui()
        elif int == "6":
            if os.path.exists('pinger.bat'):
                os.system('start pinger.bat')
                gui()
        elif int == "7":
            os.system('curl ascii.live/forrest')
        elif int == "8":
            username = input("Rename display to: ")

    # Save the username to a JSON file
            data = {"username": username}
            with open(username_file, "w") as json_file:
                json.dump(data, json_file)

            print("Display renamed" + END)
            sleep(1.2)
            gui()
        elif int == "9":
            choose_logo()
            gui()
        elif int == "help":
                    cmds = f"""
{RED}0 {END}- exit console
{RED}1 {END}- scan ip if is it active
{RED}2 {END}- listen ip connections
{RED}3 {END}- start putty
{RED}4 {END}- lower down ping
{RED}5 {END}- command prompt
{RED}6 {END}- ip pinger
{RED}7 {END}- run forest run animation
{RED}8 {END}- change display name
{RED}9 {END}- change logo color
"""
                    print(cmds)      
                    os.system('pause')
                    gui()

        else:
            print(f"{END}please enter a valid option and try again")
            sleep(1.5)
            cls()
            gui()

    else:
        username = input("Display Name: ")

    # Save the username to a JSON file
        data = {"username": username}
        with open(username_file, "w") as json_file:
            json.dump(data, json_file)

        print(WHITE2 + "username saved" + END)
        sleep(1.2)
        gui()

load()