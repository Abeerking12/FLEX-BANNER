import time
import sys
import random
import webbrowser

# ========= SETTINGS =========
CHANNEL_LINK = "https://whatsapp.com/channel/0029Vb75PfXChq6SdkyVaF0A"

# ========= FUNCTIONS =========

def type_writer(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def progress_bar(current, total, bar_length=30):
    fraction = current / total
    filled = int(bar_length * fraction)
    bar = "█" * filled + "-" * (bar_length - filled)
    percent = int(fraction * 100)

    sys.stdout.write(f"\r\033[1;31m[PROCESS] \033[1;37m|{bar}| {percent}%")
    sys.stdout.flush()

def banner():
    print("\033[H\033[J")
    print("\033[1;31m")
    print(" ███████╗██╗     ███████╗██╗  ██╗    ███████╗ ██████╗ ███╗   ██╗███████╗")
    print(" ██╔════╝██║     ██╔════╝╚██╗██╔╝    ██╔════╝██╔═══██╗████╗  ██║██╔════╝")
    print(" █████╗  ██║     █████╗   ╚███╔╝     ███████╗██║   ██║██╔██╗ ██║█████╗  ")
    print(" ██╔══╝  ██║     ██╔══╝   ██╔██╗     ╚════██║██║   ██║██║╚██╗██║██╔══╝  ")
    print(" ██║     ███████╗███████╗██╔╝ ██╗    ███████║╚██████╔╝██║ ╚████║███████╗")
    print(" ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
    print("\n        >>> FLEX ZONE TERMINAL <<<")
    print("\033[1;36m--------------------------------------------------")
    print(f" 🔗 JOIN CHANNEL: {CHANNEL_LINK}")
    print("--------------------------------------------------\033[0m")

def simulation():
    link = input("\033[1;33m[INPUT] Enter Target Channel Link: \033[0m")

    type_writer("\n[+] Initializing FLEX ZONE Protocol...", 0.03)
    type_writer("[+] Bypassing Security Layers...", 0.03)
    type_writer("[+] Establishing Encrypted Tunnel...", 0.03)

    logs = [
        "Scanning target metadata...",
        "Fetching server response...",
        "Analyzing traffic patterns...",
        "Injecting simulation packets...",
        "Verifying system integrity...",
    ]

    print("\n\033[1;36m[SCANNING]\033[0m")
    for log in logs:
        type_writer(f" -> {log}", 0.02)
        time.sleep(random.uniform(0.3, 0.6))

    print("\n\033[1;31m[EXECUTION]\033[0m")
    for i in range(1, 101):
        progress_bar(i, 100)
        time.sleep(random.uniform(0.01, 0.04))

    print("\n\n\033[1;31m[ALERT] System Overload Triggered!")
    print("\033[1;31m[ALERT] Multiple Flags Detected!")

    print("\033[1;32m\n[✓] PROCESS COMPLETED")
    print(f"\033[1;37m[✓] Target: \033[1;31m{link}")
    print("\033[1;33m[!] Status: Simulation Complete")

    input("\n\033[1;36mPress Enter to return menu...\033[0m")

# ========= MAIN MENU =========

while True:
    banner()

    print("\n\033[1;32m[1] CHANNEL BAN (Simulation)")
    print("[2] OPEN WHATSAPP CHANNEL")
    print("[0] EXIT\033[0m")

    choice = input("\n\033[1;33mSelect Option: \033[0m")

    if choice == "1":
        banner()
        simulation()

    elif choice == "2":
        print("\n\033[1;36mOpening your channel...\033[0m")
        webbrowser.open(CHANNEL_LINK)
        time.sleep(2)

    elif choice == "0":
        print("\n\033[1;31mExiting FLEX ZONE...\033[0m")
        break

    else:
        print("\n\033[1;31mInvalid Option!\033[0m")
        time.sleep(1)
