#!/usr/bin/env python3
import shutil
import psutil
from network import *

def check_disk_usage():
    du = shutil.disk_usage('/')
    free = du.free/du.total * 100
    print("Free disk space: {} %".format(free))
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print("CPU usage per second: {} %".format(usage))
    return usage < 75

if not check_disk_usage() or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything OK")
else:
    print("Network checks failed")
