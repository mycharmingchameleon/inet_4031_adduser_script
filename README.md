# INET 4031 – Lab 8: Automating User Creation README
Lab 8 Part 2

# Program Description
Python program designed to streamline the process of adding multiple users and groups to a Linux system. This script reads from an input file and automatically performs all necessary user and group creation commands instead of modifying each user mannualy. This can be used as a tool for system admins that have a large amount of user that need provision.

#Program Operation
Input file is read through the program line by line, the data feilds are seperated by ':' colons. Lines beginning with # are ignored by the script.

username – Login name for the user
password – Password for the user account
last_name – User’s last name
first_name – User’s first name
group_list – Comma-separated list of groups the user should belong to (use - if no groups)

# Program Execution
Dry run: The [ os.system(cmd) ] commented out in the create-users.py script. Prints the commands that would be executed.
Live run: The [ os.system(cmd) ] uncommented in the create-users.py script. Program creates users and groups into the appropriate files. 

# Verification Commands
grep user0 /etc/passwd
grep user0 /etc/group

# Author
Mridul Shrestha
University of Minnesota
INET 4031 – Lab 8: Automating User Creation
Oct 30, 2025
