import time
from colorama import Fore, Style

lines = [
    Fore.YELLOW + "        **" + Style.RESET_ALL,
    Fore.GREEN + "        Te" + Style.RESET_ALL,
    Fore.GREEN + "       Te a" + Style.RESET_ALL,
    Fore.GREEN + "      Te amo" + Style.RESET_ALL,
    Fore.GREEN + "     Te amo m" + Style.RESET_ALL,
    Fore.GREEN + "    Te amo muc" + Style.RESET_ALL,
    Fore.GREEN + "   Te amo mucho" + Style.RESET_ALL,
    Fore.GREEN + "  Te amo mucho mi" + Style.RESET_ALL,
    Fore.GREEN + " Te amo mucho mi am" + Style.RESET_ALL,
    Fore.GREEN + "Te amo mucho mi amor" + Style.RESET_ALL,
    Fore.WHITE + "       |   |" + Style.RESET_ALL,
    Fore.WHITE + "       |   |" + Style.RESET_ALL
]

for line in lines:
    print(line)
    time.sleep(0.5)