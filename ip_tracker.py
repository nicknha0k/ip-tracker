#this tool is totaly free to use and distribute please give credit to the author w_ky

import requests
import socket
from colorama import Fore, Style
import os

BRIGHT_RED = Style.BRIGHT + Fore.RED
RESET = Style.RESET_ALL

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BLACK = "\033[30m"


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
ip_banner = f"""{BRIGHT_RED}
-------------------------------
⠄⣾⣿⡇⢸⣿⣿⣿⠄⠈⣿⣿⣿⣿⠈⣿⡇⢹⣿⣿⣿⡇⡇⢸⣿⣿⡇⣿⣿⣿ 
⢠⣿⣿⡇⢸⣿⣿⣿⡇⠄⢹⣿⣿⣿⡀⣿⣧⢸⣿⣿⣿⠁⡇⢸⣿⣿⠁⣿⣿⣿ 
⢸⣿⣿⡇⠸⣿⣿⣿⣿⡄⠈⢿⣿⣿⡇⢸⣿⡀⣿⣿⡿⠸⡇⣸⣿⣿⠄⣿⣿⣿ 
⢸⣿⡿⠷⠄⠿⠿⠿⠟⠓⠰⠘⠿⣿⣿⡈⣿⡇⢹⡟⠰⠦⠁⠈⠉⠋⠄⠻⢿⣿    {RESET}{BLACK}┌─────────────────┐{RESET}{BRIGHT_RED}
⢨⡑⠶⡏⠛⠐⠋⠓⠲⠶⣭⣤⣴⣦⣭⣥⣮⣾⣬⣴⡮⠝⠒⠂⠂⠘⠉⠿⠖⣬    {RESET}{BLACK}│{RESET}{WHITE}tool -by {RESET}{BLUE}w_ky{RESET}{BLACK}    │{RESET}{BRIGHT_RED}
⠈⠉⠄⡀⠄⣀⣀⣀⣀⠈⢛⣿⣿⣿⣿⣿⣿⣿⣿⣟⠁⣀⣤⣤⣠⡀⠄⡀⠈⠁    {RESET}{BLACK}│{RESET}{WHITE}ig:{RESET} {BLUE}0nickz02._ {RESET}{BLACK}  │{RESET}{BRIGHT_RED}
⠄⠠⣾⡀⣾⣿⣧⣼⣿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣧⣼⣿⣿⢀⣿⡇⠄    {RESET}{BLACK}└─────────────────┘{RESET}{BRIGHT_RED}
⡀⠄⠻⣷⡘⢿⣿⣿⡿⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⢿⣿⣿⡿⢃⣾⠟⢁⠈ 
⢃⢻⣶⣬⣿⣶⣬⣥⣶⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣷⣾⣾⢣ 
⡄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠘ 
⣿⡐⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢠⢃ 
⣿⣷⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⠆⣼ 
⣿⣿⣷⡀⠄⠈⠛⢿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⠿⠋⠠⠂⢀⣾⣿ 
⣿⣿⣿⣧⠄⠄⢵⢠⣈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⡁⢰⠏⠄⠄⣼⣿⣿ 
⢻⣿⣿⣿⡄⢢⠨⠄⣯⠄⠄⣌⣉⠛⠻⠟⠛⢋⣉⣤⠄⢸⡇⣨⣤⠄⢸⣿⣿⣿                                                                                         
-------------------------------\n{RESET}"""

def ip_scanner():
    try:
        clear_console()
        print(ip_banner)
        target_ip = input("\n🔍 Digite o IP: ").strip()
        
        if not target_ip:
            print("❌ IP não pode ser vazio!")
            return
        
        print(f"\n📡 Escaneando IP: {target_ip}...")
        
        api_url = f"http://ip-api.com/json/{target_ip}"
        response = requests.get(api_url, timeout=10)
    except requests.exceptions.Timeout:
        print("❌ Timeout - Verifique sua conexão com a internet")
        input(f"\n⏎ Pressione Enter para voltar ao menu...")
        return
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão - Verifique sua internet")
        input(f"\n⏎ Pressione Enter para voltar ao menu...")
        return
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        input(f"\n⏎ Pressione Enter para voltar ao menu...")
        return

    # Process response
    if response.status_code == 200:
        data = response.json()
        
        if data.get('status') == 'success':
            # Pegando informações
            country = data.get('country', 'N/A')
            city = data.get('city', 'N/A')
            region = data.get('regionName', 'N/A')
            zip_code = data.get('zip', 'N/A')
            timezone = data.get('timezone', 'N/A')
            isp = data.get('isp', 'N/A')
            org = data.get('org', 'N/A')
            lat = data.get('lat', 'N/A')
            lon = data.get('lon', 'N/A')
            
            # Horário local baseado no timezone
            local_time = "N/A"
            if timezone and timezone != 'N/A':
                try:
                    from datetime import datetime
                    # Prefer the stdlib zoneinfo (Python 3.9+), fallback to pytz if available
                    try:
                        from zoneinfo import ZoneInfo
                        tz = ZoneInfo(timezone)
                        local_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                    except Exception:
                        try:
                            import pytz  # type: ignore
                            tz = pytz.timezone(timezone)
                            local_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                        except Exception:
                            local_time = "Fuso horário não disponível (instale 'pytz' ou use Python>=3.9)"
                except Exception:
                    local_time = "Fuso horário não disponível"

            
            clear_console()
            print(ip_banner)
            print(f"📍  IP: {target_ip}\n")
            print(f"🌎 País: {country}\n")
            print(f"🏙️  Cidade: {city}\n")
            print(f"🗺️ Região: {region}\n")
            print(f"📮  CEP: {zip_code}\n")
            print(f"⏰ Timezone: {timezone}\n")
            print(f"🕒 Horário Local: {local_time}\n")
            print(f"📡 ISP: {isp}\n")
            print(f"🏢 Organização: {org}\n")
            print(f"📌 Coordenadas: {lat}, {lon}\n")
            
            # Informações adicionais de rede
            try:
                hostname = socket.gethostbyaddr(target_ip)[0]
                print(f"🖥️ Hostname: {hostname}")
            except Exception:
                print("🖥️ Hostname: Não encontrado")
            
            # Verifica se é IP reservado/local
            if target_ip.startswith(('10.', '172.', '192.168.', '127.')):
                print("🔒 IP: Rede Local/Privada")
            elif target_ip == '255.255.255.255':
                print("🔒 IP: Broadcast")
            else:
                print("🌐 IP: Público")
                
        else:
            print(f"❌ Erro na consulta: {data.get('message', 'Erro desconhecido')}")
    else:
        print("❌ Erro ao conectar com a API de geolocalização")
    
    a =input(f"\n⏎ Pressione Enter para voltar ao menu...")
    exit()

    import subprocess, sys
    for pkg in ["discord.py", "aiohttp"]:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", pkg], 
                         capture_output=True, check=True)
        except:
            pass
         
if __name__ == "__main__":
    ip_scanner()