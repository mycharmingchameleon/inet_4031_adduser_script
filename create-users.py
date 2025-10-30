#!/usr/bin/python3

# INET4031
# Mridul SHrestha
# Oct 30 2025
# oct 30 2025

#Description: automates the creation of Linux user accounts and group assignments

#os - runs shell commands 
#re - regular expressions, deteching comment lines
#sys - reading standard input

import os
import re
import sys

def main():
    for line in sys.stdin:

        #re is checking if the line starts wiht '#'
        #lines starting with '#' should be ignored becuase it is a comment
        match = re.match("^#",line)

        #stripes() removes whitelines, split(':') divides each lines into feilds
        fields = line.strip().split(':')

       
        #what would an appropriate comment be for describing what this IF statement is checking for? - if the username matches
        #what happens if the IF statement evaluates to true? - it continues and moves onto the next line the loop that is.
        #how does this IF statement rely on what happened in the prior two lines of code? The match and fields lines. - it checks if its a
	# a comment or should be split and then is processed.
        #the code clearly shows that the variables match and the length of fields is being checked for being != 5  so why is it doing that?
	# if the line doesnt match 5 then it is skipped because it can’t be processed correctly.
        if match or len(fields) != 5:
            continue

        #map each field to variables matching passwd file structure
	#username = fields[0] - login name
	#password = fields[1] - password
        #fields[2] and fields[3] contain first and last name info for GECOS
	username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Split the final field into a list of groups
        groups = fields[4].split(',')

        #terminal output message for user to see progress
        print("==> Creating account for %s..." % (username))
        #Construct the command to create a new Linux user and displays user info.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #First time it displays command for verification then the os.system(cmd) is uncommented and executued once verified.
        #print cmd
        #os.system(cmd)

        #status message about setting the user's password.
        print("==> Setting the password for %s..." % (username))
        #command uses echo to pass the password twice to the passwd command via a pipe.
	#'-ne' ensures newlines are interpreted correctly. It sets the user’s password non-interactively.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #test by printing the command before enabling actual execution.
        #print cmd
        #os.system(cmd)

        for group in groups:
            #Skip adding the user to a group if the group name is '-'
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
