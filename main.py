#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

# ping function


def ping(ip_prefix, i):
    response = subprocess.call(["ping", "-c", "1", ip_prefix+"."+str(i)])
    ip_status = ""
    if response == 0:
        ip_status = ip_prefix+"."+str(i)+" is Up"
    else:
        ip_status = ip_prefix+"."+str(i)+"is Down"
    return ip_status

# concurrent function


def concurrent_action(ip_prefix, workers):
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(ping, ip_prefix, i)
                   for i in range(1, 255)]
        for future in futures:
            try:
                results.append(future.result())
            except TypeError as e:
                print(e)
    return results


arguments = sys.argv
if arguments[2] == "c":
    results = concurrent_action(arguments[1], int(arguments[3]))
    write = open("result.txt", "w")
    for i in results:
        if "Up" in i:
            write.write(i+"\n")
    write.close()
elif arguments[2] == "b":
    results = []
    for i in range(1, 255):
        get_result = concurrent_action(
            arguments[1]+"."+str(i), int(arguments[3]))
        results.append(get_result)
    write = open("result.txt", "w")
    for result in results:
        for i in result:
            if "Up" in i:
                write.write(i+"\n")
    write.close()
elif arguments[2] == "a":
    results = []
    for a in range(1, 3):
        for b in range(1, 3):
            get_result = concurrent_action(
                arguments[1]+"."+str(a)+"."+str(b), int(arguments[3]))
            results.append(get_result)
    write = open("result.txt", "w")
    for result in results:
        for i in result:
            if "Up" in i:
                write.write(i+"\n")
    write.close()
