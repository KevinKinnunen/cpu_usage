#!/usr/bin/env python3

import os
import psutil
import argparse
import time

beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
beep(1) 

a = "cpu_usage.py is running!\n"
i = str(["PID", "name", "memory"])
print (a)

with open("cpu_usage_rapport.txt", "a+") as file:
    file.write(a)

process = psutil.Process(os.getpid())
x = (process.memory_info().rss/1024.0**2)
print("MBs = {}".format(float(x)))
x = (process.memory_info().rss/1024.0**3)
print("GBs = {}".format(float(x)))

parser = argparse.ArgumentParser(description='Memory check within sec/min')
parser.add_argument('-M', '--memory', type=float, metavar='', help='Memory check (MB/GBs)')
parser.add_argument('-T', '--timer', type=int, metavar='', help='Timer to send info (60 = 1min)')
args = parser.parse_args()

def print_memoryinfo():
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.pid
            processMem = proc.memory_info().rss/1024.0**2
            with open("cpu_usage_rapport.txt", "a+") as file:
                file.write("{} :::: {} ::: {}\n".format(processID, processName, processMem))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def mem(memory, timer):
    memory = 50 #Mbs
    timer = 3600 #5min
    if (memory > 0):
        x = (process.memory_info().rss/1024.0**2)
    elif (memory <= 0):
        x = (process.memory_info().rss/1024.0**3)
    if (x >= memory):
        beep(1)
    if (timer):
        time.sleep(timer)
        with open("cpu_usage_rapport.txt", "a+") as file:
            if (x >= memory):
                file.write("Memory is higher than {}\n".format(float(memory)))
            elif (x <= memory):
                file.write("Memory is lower than {}\n".format(float(memory)))
            file.write(i + "\n")
            return mem

def mem2(memory, timer):
    memory = 125 #1Gb in Mbs
    timer = 3600 #60min
    if (memory > 0):
        x = (process.memory_info().rss/1024.0**2)
    elif (memory <= 0):
        x = (process.memory_info().rss/1024.0**3)
    if (x >= memory):
        beep(1)
    if (timer):
        time.sleep(timer)
        with open("cpu_usage_rapport.txt", "a+") as file:
            if (x >= memory):
                file.write("Memory is higher than {}\n".format(float(memory)))
            elif (x <= memory):
                file.write("Memory is lower than {}\n".format(float(memory)))
            file.write(i + "\n")
            return mem2

if __name__ == '__main__':
    while True:
        print(mem(args.memory, args.timer))
        print(mem2(args.memory, args.timer))
        print_memoryinfo()
