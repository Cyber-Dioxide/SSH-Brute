from colorama import  Style,Fore
import random

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

RAN = random.choice(all_col)

LG = Style.BRIGHT+Fore.LIGHTGREEN_EX
G = Style.BRIGHT+Fore.GREEN
LC = Style.BRIGHT+Fore.LIGHTCYAN_EX
C = Style.BRIGHT+Fore.CYAN
LY =  Style.BRIGHT+Fore.LIGHTYELLOW_EX
Y = Style.BRIGHT+Fore.YELLOW
R = Style.BRIGHT+Fore.RED
LR = Style.BRIGHT+Fore.LIGHTRED_EX
W = Style.BRIGHT+Fore.LIGHTWHITE_EX