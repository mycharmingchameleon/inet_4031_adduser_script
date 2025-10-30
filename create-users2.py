#!/usr/bin/python3
import re
import os
import sys

# -----------------------------------------------
# INET 4031 – Automated User Creation Script v2
# Author: Mridul Shrestha
# Description:
#   This version introduces an interactive "Dry Run" feature.
#   The user is prompted at runtime to choose whether to perform a
#   dry run (test mode) or actually add users and groups to the system.
# -----------------------------------------------

# Ask user whether to perform a dry-run
print("Would you like to perform a dry-run? (Y/N): ")
dry_run_input = open("/dev/tty").readline().strip().lower()
dry_run = (dry_run_input == 'y')

if dry_run:
    print("\n--- DRY RUN MODE ENABLED ---")
    print("No system changes will be made.\n")
else:
    print("\n--- LIVE RUN MODE ---")
    print("Users and groups will be created on this system.\n")

# Process each line from the input file
for line in sys.stdin:
    line = line.strip()

    # Skip empty lines
    if line == "":
        continue

    # Skip commented-out users (lines starting with '#')
    if line.startswith("#"):
        if dry_run:
            print(f"Skipping line (commented out): {line}")
        continue

    # Split line into fields
    fields = line.split(":")
    if len(fields) != 5:
        # If the line does not have enough fields, handle accordingly
        if dry_run:
            print(f"Error: Invalid line (expected 5 fields): {line}")
        continue

    username, password, lastname, firstname, groups = fields

    # Create the user command
    cmd_add_user = f"sudo adduser --disabled-password --gecos '{firstname} {lastname}' {username}"
    cmd_passwd = f"echo '{username}:{password}' | sudo chpasswd"

    # Create the group commands (if any)
    if groups != "-" and groups != "":
        for group in groups.split(","):
            cmd_add_group = f"sudo groupadd -f {group}"
            cmd_add_to_group = f"sudo usermod -aG {group} {username}"

            # Handle Dry-Run logic for group creation
            if dry_run:
                print(f"[Dry-Run] Would run: {cmd_add_group}")
                print(f"[Dry-Run] Would run: {cmd_add_to_group}")
            else:
                os.system(cmd_add_group)
                os.system(cmd_add_to_group)
    else:
        if dry_run:
            print(f"[Dry-Run] No groups to add for user {username}")

    # Handle Dry-Run logic for user creation
    if dry_run:
        print(f"[Dry-Run] Would run: {cmd_add_user}")
        print(f"[Dry-Run] Would run: {cmd_passwd}")
    else:
        os.system(cmd_add_user)
        os.system(cmd_passwd)

print("\n--- Script Execution Complete ---")
if dry_run:
    print("No users or groups were actually created.")
else:
    print("Users and groups successfully added to the system.")
