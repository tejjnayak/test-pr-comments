# src/python/vulnerable_script.py
import os
import sys

def execute_command(user_input):
    os.system(f"ping {user_input}")

if __name__ == "__main__":
    user_input = sys.argv[1]
    execute_command(user_input)

