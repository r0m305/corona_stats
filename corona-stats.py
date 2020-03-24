'''
Author: Romeos CyberGypsy
Name: corona-stats.py
(c) romeos
Email: lewiswaigwa30@gmail.com
'''
##############################
#Copying my code will not make you a coder
#seek to understand
##############################
import bs4
import requests
from colorama import *
from termcolor import colored
import sys
import time

class Engine:
    def __init__(self):
        try:
            self.get_stats()

        except KeyboardInterrupt:
            print(colored("[!]Exiting safely...","red"))
            sys.exit()

    def get_stats(self):
        country = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Enter your country name:{Fore.YELLOW}")
        headers = {"User-agent" : "Mozilla/5.1"}
        print(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Searching for {country}'s corona stats")
        try:
            data = requests.get("https://corona-stats.online/"+country, headers = headers)
            soup = bs4.BeautifulSoup(data.text, 'html.parser')
            finding = soup.find_all("pre")

            for line in finding:
                print(colored(line.get_text(),"green"))


        except Exception as e:
            print(colored(e,"red"))

if __name__ == '__main__':
    banner = '''
  _________  _________  ____  ____ _      _____/ /_____ _/ /______
 / ___/ __ \/ ___/ __ \/ __ \/ __ `/_____/ ___/ __/ __ `/ __/ ___/
/ /__/ /_/ / /  / /_/ / / / / /_/ /_____(__  ) /_/ /_/ / /_(__  )
\___/\____/_/   \____/_/ /_/\__,_/     /____/\__/\__,_/\__/____/ '''

    print(colored(banner, "yellow"))
    banner2 = '''
    +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+
    |G|e|t| |c|o|r|o|n|a| |v|i|r|u|s| |u|p|d|a|t|e|s|
    +-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+'''
    print(colored(banner2,"blue"))
    print(colored("[-] Written by Romeos CyberGypsy"))
    obj = Engine()
