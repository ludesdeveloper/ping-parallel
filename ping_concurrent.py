#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor


def ping(ip_prefix, i):
    response = subprocess.call(["ping", "-c", "1", ip_prefix+"."+str(i)])
    ip_status = ""
    if response == 0:
        ip_status = ip_prefix+"."+str(i)+" is Up"
    else:
        ip_status = ip_prefix+"."+str(i)+" is Down"
    return ip_status


def concurrent_action(ip_prefix, workers):
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(ping, ip_prefix, i)
                   for i in range(1, 255)]
        print(futures)
        for future in futures:
            try:
                results.append(future.result())
            except TypeError as e:
                print(e)
    for i in results:
        print(i)
    return results


arguments = sys.argv
if arguments[2] == "c":
    results = concurrent_action(arguments[1], int(arguments[3]))
    write = open("result.txt", "w")
    for i in results:
        write.write(i+"\n")
    write.close()
elif arguments[2] == "b":
    for i in range(1, 255):
        results = concurrent_action(arguments[1]+"."+str(i), int(arguments[3]))
        print(results)
elif arguments[2] == "a":
    for a in range(1, 255):
        for b in range(1, 255):
            concurrent_action(arguments[1]+"." +
                              str(a)+"."+str(b), int(arguments[3]))
