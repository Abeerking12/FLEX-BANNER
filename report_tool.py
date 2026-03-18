import time
import sys
import random

# Progress bar function
def progress_bar(current, total, bar_length=35):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '=' + '>'
    padding = int(bar_length - len(arrow)) * ' '
    ending = '\n' if current == total else '\r'

    sys.stdout.write(
        f"\033[1;31m[REPORTING] \033[1;37m[\033[1;32m{arrow}{padding}\033[1;37m] {int(fraction*100)}%{ending}"
    )
    sys.stdout.flush()

# Clear screen
print("\033[H\033[J")

# FLEX ZONE Banner Section
print("\033[1;34m")
print("  ______ _      ________   __   _______  ____  _   _ ______ ")
print(" |  ____| |    |  ____\\ \\ / /  |__   __|/ __ \\| \\ | |  ____|")
print(" | |__  | |    | |__   \\ V /      | |  | |  | |  \\| | |__   ")
print(" |  __| | |    |  __|   > <       | |  | |  | | . ' |  __|  ")
print(" | |    | |____| |____ / . \\      | |  | |__| | |\\  | |____ ")
print(" |_|    |______|______/_/ \\_\\     |_|   \\____/|_| \\_|______|")
print("\n            >>> POWERED BY: FLEX ZONE <<<")
print("\033[0m")

# Input Section
link = input("\033[1;33mEnter Target Channel Link: \033[0m")

# Fake Server Animation
print("\033[1;36m\n[*] Initializing FLEX ZONE Ban Protocol...")
time.sleep(1)
print("[*] Connecting to Satellite Servers...")
time.sleep(1.5)
print(f"[*] Target ID Verified: {link}")
print("[*] Proxy Status: \033[1;32mActive\033[1;36m")
time.sleep(1)

# Loading Process
total_reports = 100
for i in range(1, total_reports + 1):
    progress_bar(i, total_reports)
    time.sleep(random.uniform(0.02, 0.08))

# Final Message
print("\033[1;32m\n\n[+] SUCCESS: 10,000 Reports Sent Successfully!")
print(f"\033[1;37m[+] Target: \033[1;31m{link}")
print("\033[1;32m[+] System Message: Channel flagged by FLEX ZONE for permanent ban.\033[0m")
