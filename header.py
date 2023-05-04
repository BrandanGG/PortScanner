import pyfiglet
from colorama import Fore, Back, Style



def head():
    style = Fore.LIGHTMAGENTA_EX+'-'*100
    ascii_banner = pyfiglet.figlet_format('PORT SCANNER', font='slant')
    ascii_banner = Fore.RED + ascii_banner
    print(style)
    print(ascii_banner)
    print(style)
    print('Developed by Brandan\ngithub.com/BrandanGG')
    print(Style.RESET_ALL)


head()

