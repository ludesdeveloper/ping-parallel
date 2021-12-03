#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from concurrent.futures import ThreadPoolExecutor


def single_ping(ip_prefix, i):
    response = subprocess.call(['ping', '-c', '1', ip_prefix+'.'+str(i)])
    ip_status = ''
    if response == 0:
        ip_status = ip_prefix+'.'+str(i)+' is Up'
    else:
        ip_status = ip_prefix+'.'+str(i)+' is Down'
    return ip_status


def concurrent_action(ip_prefix):
    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(single_ping, ip_prefix, i)
                   for i in range(1, 255)]
        print(futures)
        for future in futures:
            try:
                results.append(future.result())
            except TypeError as e:
                print(e)
    for i in results:
        print(i)


concurrent_action('192.168.1')
