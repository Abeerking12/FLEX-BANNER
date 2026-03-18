import time
import sys
import random

# Typing effect
def type_writer(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Progress bar
def progress_bar(current, total, bar_length=30):
    fraction = current / total
    filled = int(bar_length * fraction)
    bar = "█" * filled + "-" * (bar_length - filled)
    percent = int(fraction * 100)

    sys.stdout.write(f"\r\033[1;31m[PROCESS] \033[1;37m|{bar}| {percent}%")
    sys.stdout.flush()

# MAIN LOOP
while True:

    # Clear screen
    print("\033[H\033[J")

    # Banner
    print("\033[1;31m")
    print(" ███████╗██╗     ███████╗██╗  ██╗    ███████╗ ██████╗ ███╗   ██╗███████╗")
    print(" ██╔════╝██║     ██╔════╝╚██╗██╔╝    ██╔════╝██╔═══██╗████╗  ██║██╔════╝")
    print(" █████╗  ██║     █████╗   ╚███╔╝     ███████╗██║   ██║██╔██╗ ██║█████╗  ")
    print(" ██╔══╝  ██║     ██╔══╝   ██╔██╗     ╚════██║██║   ██║██║╚██╗██║██╔══╝  ")
    print(" ██║     ███████╗███████╗██╔╝ ██╗    ███████║╚██████╔╝██║ ╚████║███████╗")
    print(" ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
    print("\n        >>> FLEX ZONE TERMINAL <<<")
    print("\033[0m")

    # Input
    link = input("\033[1;33m[INPUT] Enter Target Channel Link (or type 'exit'): \033[0m")

    if link.lower() == "exit":
        print("\n\033[1;31m[!] Exiting FLEX ZONE...\033[0m")
        break

    # Simulation
    type_writer("\n[+] Initializing Secure Protocol...", 0.03)
    type_writer("[+] Bypassing Security Layers...", 0.03)
    type_writer("[+] Establishing Encrypted Tunnel...", 0.03)

    # Fake logs
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

    # Progress
    print("\n\033[1;31m[EXECUTION]\033[0m")
    for i in range(1, 101):
        progress_bar(i, 100)
        time.sleep(random.uniform(0.01, 0.04))

    # Final
    print("\n\n\033[1;31m[ALERT] System Overload Triggered!")
    print("\033[1;31m[ALERT] Multiple Flags Detected!")

    print("\033[1;32m\n[✓] PROCESS COMPLETED")
    print(f"\033[1;37m[✓] Target: \033[1;31m{link}")
    print("\033[1;33m[!] Status: Simulation Complete - Review Generated Logs")

    # Pause before restart
    input("\n\033[1;36mPress Enter to continue...\033[0m")
