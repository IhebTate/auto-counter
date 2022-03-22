import os
import base64
import pyperclip
import discord
import random
import re
from discord.ext import commands
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep


def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')


clear()
token = input(Fore.MAGENTA+" root" + Fore.WHITE+"@" + Fore.MAGENTA+"ihebman" +
              Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+"Enter Token: " + Fore.WHITE+" ")


class counter(discord.Client):
    async def on_ready(self):
        os.system(
            f'title [AFK-CHECKER] │ Connected As: {self.user}')
        print(f"""
{Fore.MAGENTA}
{Fore.WHITE}                ██╗██╗  ██╗███████╗██████╗ 
{Fore.MAGENTA}                ██║██║  ██║██╔════╝██╔══██╗
{Fore.WHITE}                ██║███████║█████╗  ██████╔╝
{Fore.MAGENTA}                ██║██╔══██║██╔══╝  ██╔══██╗
{Fore.WHITE}                ██║██║  ██║███████╗██████╔╝
{Fore.MAGENTA}                ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝                  
{Fore.MAGENTA}              ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
{Fore.WHITE}              Dev: {Fore.MAGENTA}GodJustice/Iheb
{Fore.WHITE}                       Loading....
{Fore.MAGENTA}              ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
""")
        print(f"{Fore.MAGENTA}")
        progressbar = tqdm([2, 4, 6, 8, 10])
        for item in progressbar:
            sleep(0.1)
            progressbar.set_description(' Loading: ')

        clear()
        print(f"""
        {Fore.WHITE}                     ██╗██╗  ██╗███████╗██████╗ 
        {Fore.MAGENTA}                     ██║██║  ██║██╔════╝██╔══██╗
        {Fore.WHITE}                     ██║███████║█████╗  ██████╔╝
        {Fore.MAGENTA}                     ██║██╔══██║██╔══╝  ██╔══██╗
        {Fore.WHITE}                     ██║██║  ██║███████╗██████╔╝
        {Fore.MAGENTA}                     ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝                  
        {Fore.MAGENTA}                    ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
        {Fore.WHITE}                      Dev: {Fore.MAGENTA}GodJustice/Iheb
        {Fore.WHITE}                     Trigger Word:{Fore.MAGENTA}['{Fore.WHITE}AFK{Fore.WHITE} CHECK{Fore.WHITE}{Fore.MAGENTA} @user{Fore.WHITE}{Fore.MAGENTA}']
        {Fore.MAGENTA}                    ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙

        """)

    async def on_message(self, x):
        regex = re.findall(r'<@!?([0-9]+)>', x.content)
        if regex and 'afk check' in x.content.lower() and x.author == self.user:
            for i in range(0, 100001):
                await x.channel.send(i)


client = counter()
client.run(token, bot=False)
