import os
import sys
import operator
import socket

# Install the main files
os.chdir("/tmp")
os.system("git clone https://github.com/tanc7/sqlmap_improvement_project") # git clone public repo
os.system("mkdir /root/ArmsCommander")
os.system("mkdir /root/ArmsCommander/recon")
os.system("mkdir /root/ArmsCommander/recon/sqlmap_improvement_project")
os.chdir("/tmp/sqlmap_improvement_project")
os.system("sudo chmod 777 ./*")
os.system("cp -r ./* /root/ArmsCommander/recon/sqlmap_improvement_project")
os.system("cp -r sql_injection.py /usr/local/bin")
# Install required tools from Kali APT Repo
os.system("sudo apt-get update && sudo apt-get install tor tsocks sqlmap vega arachni")
# Install Python dependencies
os.system("sudo pip install termcolor")
# Start the program
os.system("sql_injection.py")
