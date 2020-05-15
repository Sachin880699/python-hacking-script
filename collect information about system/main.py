#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import getpass
import os
import platform
import shutil
from requests import get

version = platform.version()
platform = platform.platform()
system_user_name = getpass.getuser()
running_process = subprocess.getoutput('ps')
public_ip = get('https://api.ipify.org').text
public_ip = ('My public IP address is:', public_ip)
public_ip = str(public_ip)
(total_disk, used_disk, free_disk) = shutil.disk_usage('/')

total_disk = 'Total: %d GiB' % (total_disk // 2 ** 30)
used_disk = 'Used: %d GiB' % (used_disk // 2 ** 30)
free_disk = 'Free: %d GiB' % (free_disk // 2 ** 30)
system_uptime = subprocess.getoutput('uptime')

with open('log.txt', 'a') as f:
    f.write('----------------------------Basic Info-------------------')

    # f.write(machine)

    f.write('\n')
    f.write(version)
    f.write('\n')
    f.write(platform)
    f.write('\n')
    f.write(system_user_name)
    f.write('\n')
    f.write(running_process)
    f.write('\n')
    f.write(public_ip)
    f.write('\n')
    f.write(public_ip)
    f.write('\n')
    f.write(total_disk)
    f.write('\n')
    f.write(used_disk)
    f.write('\n')
    f.write(free_disk)
    f.write('\n')
    f.write(system_uptime)
    f.write('\n')

Music = '/home/' + system_user_name + '/Music/'
Desktop = '/home/' + system_user_name + '/Desktop/'
Videos = '/home/' + system_user_name + '/Videos/'
Documents = '/home/' + system_user_name + '/Documents/'
Downloads = '/home/' + system_user_name + '/Downloads/'

Music_size = subprocess.check_output(['du', '-sh',
        Music]).split()[0].decode('utf-8')
Desktop_size = subprocess.check_output(['du', '-sh',
        Desktop]).split()[0].decode('utf-8')
Videos_size = subprocess.check_output(['du', '-sh',
        Videos]).split()[0].decode('utf-8')
Documents_size = subprocess.check_output(['du', '-sh',
        Videos]).split()[0].decode('utf-8')
Downloads_size = subprocess.check_output(['du', '-sh',
        Downloads]).split()[0].decode('utf-8')

# ------------------here to start Desktop--------------------

list_of_all_file = os.listdir(Desktop)
list_of_all_file = ' ,'.join(map(str, list_of_all_file))


with open('log.txt', 'a') as f:

    f.write('---------------------------------------Collect info about Desktop--------------------------------------------'
            )
    f.write('\n')
    f.write(Desktop_size)
    f.write('\n')
    f.write(list_of_all_file)
    f.write('\n')

# ----------------------from here start Music-------------

list_of_all_file = os.listdir(Music)
list_of_all_file = ' ,'.join(map(str, list_of_all_file))

with open('log.txt', 'a') as f:

    f.write('---------------------------------------Collect info about Music--------------------------------------------------'
            )
    f.write('\n')
    f.write(Music_size)
    f.write('\n')
    f.write(list_of_all_file)
    f.write('\n')


with open('log.txt', 'a') as f:

    f.write('---------------------------------------Collect info about Downloads--------------------------------------------------'
            )
    f.write('\n')
    f.write(Downloads_size)
    f.write('\n')
    f.write(list_of_all_file)
    f.write('\n')


with open('log.txt', 'a') as f:

    f.write('---------------------------------------Collect info about Documents--------------------------------------------------'
            )
    f.write('\n')
    f.write(Documents_size)
    f.write('\n')
    f.write(list_of_all_file)
    f.write('\n')


with open('log.txt', 'a') as f:

    f.write('---------------------------------------Collect info about Videos--------------------------------------------------'
            )
    f.write('\n')
    f.write(Videos_size)
    f.write('\n')
    f.write(list_of_all_file)
    f.write('\n')
