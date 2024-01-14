#   Copyright (c) 2024 sigmaphoned All rights reserved.
#   GitHub: github.com/sigmaphoned
import requests
import os
import platform
from colorama import Fore

saves = "saves.txt" 
link = "https://fragment.com/username/" 
banner = f"""
{Fore.RED}made by sigmaphoned

    """ 

#   Funzione check_user
def check_user(username): 
    username = username.strip()
    r = requests.get(f"https://fragment.com/username/{username}", allow_redirects=False)
    response = str(r.text).split('\n')
    if len(response) != 1:
        print(f"{Fore.GREEN}[+]{Fore.RESET} {username} is available for purchase on fragment.com")
    else:
        print(f"{Fore.RED}[-]{Fore.RESET} {username} is not available for purchase on fragment.com")
        #   Below saves usernames NOT available for purchase in a file
        saves_file = open(saves, "a")
        saves_file.write(f"[-] {username}\n")
        saves_file.close()

#   Funzione Main
# Libraries
import requests
import os
import platform
from colorama import Fore

# Variables
saves = "saves.txt"
link = "https://fragment.com/username/"
banner = f"""
{Fore.RED}made by sigmaphoned
    """ 

# Function to check user
def check_user(username): 
    username = username.strip()
    r = requests.get(f"https://fragment.com/username/{username}", allow_redirects=False)
    response = str(r.text).split('\n')
    if len(response) != 1:
        print(f"{Fore.GREEN}[+]{Fore.RESET} {username} is available for purchase on fragment.com")
    else:
        print(f"{Fore.RED}[-]{Fore.RESET} {username} is not available for purchase on fragment.com")
        # Below saves usernames NOT available for purchase in a file
        saves_file = open(saves, "a")
        saves_file.write(f"[-] {username}\n")
        saves_file.close()

# Main function
def main():
    if "linux" in str(platform.platform()).lower():
        os.system("clear")
    else: 
        os.system("cls")
    print(banner)
    wordlist = input(f"{Fore.RESET}[>>] Enter the name of the wordlist file {Fore.GREEN}wordlist{Fore.RESET} -> ")
    try:
        wordlist_file = open(wordlist, "r")
        print(f"{Fore.RESET}[>>] File {wordlist} {Fore.GREEN}loaded{Fore.RESET}!")
        try:
            saves_file = open(saves, "r+")
            print(f"{Fore.RESET}[>>] File {saves} {Fore.GREEN}loaded{Fore.RESET}!")
            saves_file.truncate(0)
            saves_file.close()
            pass
        except FileNotFoundError:
            saves_file = open(saves, "w")
            print(f"{Fore.RESET}[>>] File {saves} {Fore.GREEN}created{Fore.RESET}!")
            saves_file.close()
    except FileNotFoundError:
        print(f"{Fore.RESET}[>>] File {wordlist} {Fore.RED}not found{Fore.RESET}!")
        exit()
    print()
    for username in wordlist_file.readlines():
        check_user(username.lower())
if __name__ == "__main__":
    main()