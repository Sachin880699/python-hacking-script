#
# Python script to fetch system information
# Author -  ThePythonDjango.Com
# Tested with Python3 on Ubuntu 16.04
# 

import platform
import getpass
from getmac import get_mac_address as gma
import os

# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

# node
print("Node: " + platform.node())

# processor
print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)

# system
print("System: " + platform.system())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)

# Load
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())

# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

# uptime
uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

#get active user name
print(getpass.getuser())

# get mac address
print(gma())

#------check firewall status-
status = os.popen("service iptables status").read()

#--------get linux command history
for history in open('/home/'+user+'/.bash_history'):
    print(history, end='')
    

