import subprocess
import argparse
import sys


def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--easy", action="store_true")
    parser.add_argument("-m", "--medium", action="store_true")
    parser.add_argument("-H", "--hard", action="store_true")  # -h help ile çakışmaması için
    return parser.parse_args()
inputs = get_input()
if not inputs.easy and not inputs.medium and not inputs.hard:
    print("please select a level")
    sys.exit()

print("welcome to lokidres's super secure ping system")
payload = input("please enter your payload: ")





if inputs.easy:
    print("[EASY] No filters applied")
    subprocess.call(f"ping -c 2 {payload}", shell=True)


elif inputs.medium:
    print("[MEDIUM] Basic character filter")
    blocked = [';', '&', '|']
    for char in blocked:
        if char in payload:
            print(f"firewall blocked: {char}")
            sys.exit()
    subprocess.call(f"ping -c 2 {payload}", shell=True)


elif inputs.hard:
    print("[HARD] Advanced filter with bypasses")
    blocked = [';', '&', '|', '`', '{', '}']
    for char in blocked:
        if char in payload:
            print(f"firewall blocked: {char}")
            sys.exit()


    if not any(c.isdigit() for c in payload):
        print("Invalid IP format")
        sys.exit()

    subprocess.call(f"ping -c 2 {payload}", shell=True)