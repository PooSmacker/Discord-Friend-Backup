import json
import os
import time
import subprocess
import requests
import threading
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def gradient_red_blue(text):
    return f"{Fore.RED}{text}{Fore.BLUE}"

def gradient_blue_green(text):
    return f"{Fore.BLUE}{text}{Fore.GREEN}"

def gradient_green_yellow(text):
    return f"{Fore.GREEN}{text}{Fore.YELLOW}"

def gradient_yellow_red(text):
    return f"{Fore.YELLOW}{text}{Fore.RED}"

ascii_art = gradient_red_blue('''

▓█████▄  ██▀███   ██▓ ██▓███   ██▓███ ▓██   ██▓    ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀ █    ██  ██▓███  
▒██▀ ██▌▓██ ▒ ██▒▓██▒▓██░  ██▒▓██░  ██▒▒██  ██▒   ▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒  ██  ▓██▒▓██░  ██▒
░██   █▌▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▓██░ ██▓▒ ▒██ ██░   ▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▓██  ▒██░▓██░ ██▓▒
░▓█▄   ▌▒██▀▀█▄  ░██░▒██▄█▓▒ ▒▒██▄█▓▒ ▒ ░ ▐██▓░   ▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░▒████▓ ░██▓ ▒██▒░██░▒██▒ ░  ░▒██▒ ░  ░ ░ ██▒▓░   ░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░▒▓▒░ ░  ░  ██▒▒▒    ░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
 ░ ▒  ▒   ░▒ ░ ▒░ ▒ ░░▒ ░     ░▒ ░     ▓██ ░▒░    ▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
 ░ ░  ░   ░░   ░  ▒ ░░░       ░░       ▒ ▒ ░░      ░    ░   ░   ▒   ░        ░ ░░ ░  ░░░ ░ ░ ░░       
   ░       ░      ░                    ░ ░         ░            ░  ░░ ░      ░  ░      ░              

''')

continuething = gradient_red_blue("Press any key to continue")
print(ascii_art)
print(continuething)
input("")

def load_json_from_desktop(filename):
    desktop_path = os.path.expanduser("~/Desktop")
    json_file_path = os.path.join(desktop_path, filename)

    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File '{json_file_path}' not found on the desktop.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{json_file_path}': {e}")
        return None

def save_json_to_file(filename, data):
    desktop_path = os.path.expanduser("~/Desktop")
    json_file_path = os.path.join(desktop_path, filename)

    try:
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to '{json_file_path}'")
    except Exception as e:
        print(f"Error saving data to '{json_file_path}': {e}")

def extract_usernames(data):
    usernames = []

    if isinstance(data, dict) and "relationships" in data:
        relationships = data["relationships"]
        for relationship in relationships:
            user = relationship.get("user")
            if user and "username" in user:
                usernames.append(user["username"])

    return usernames

def main():
    json_filename = 'user.json'

    user_data = load_json_from_desktop(json_filename)

    if user_data is not None:
        usernames = extract_usernames(user_data)

        if usernames:
            with open('usernames.txt', 'w', encoding='utf-8') as txt_file:
                for username in usernames:
                    txt_file.write(username + '\n')
            print("Usernames extracted and saved to usernames.txt in the current directory")
        else:
            print("No usernames found in the input data.")

if __name__ == "__main__":
    main()
    
    print("Press Enter to exit")
    
    while True:
        try:
            input()
            break 
        except KeyboardInterrupt:
            pass  
