#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFactory, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI

"""
三台机械臂的同步运动
"""

swift1 = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
swift2 = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
swift3 = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})

swift1.waiting_ready()
swift2.waiting_ready()
swift3.waiting_ready()

swift_list = [swift1, swift2, swift3]


def multi_swift_cmd(cmd, *args, **kwargs):
    wait = kwargs.pop('wait', False)
    timeout = kwargs.get('timeout', None)
    for swift in swift_list:
        swift_cmd = getattr(swift, cmd)
        swift_cmd(*args, **kwargs, wait=False)
    if wait:
        for swift in swift_list:
            swift.flush_cmd(timeout)
    time.sleep(0.001)

speed = 1000000
timeout = 30

multi_swift_cmd('reset', speed=speed)
time.sleep(2)

while True:
    multi_swift_cmd('set_position', x=300, y=0, z=150, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=50, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=150, speed=speed, wait=True, timeout=timeout)

    multi_swift_cmd('set_position', x=200, y=100, z=100, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=50, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=150, speed=speed, wait=True, timeout=timeout)

    multi_swift_cmd('set_position', x=200, y=-100, z=100, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=50, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=150, speed=speed, wait=True, timeout=timeout)

    multi_swift_cmd('set_position', x=200, y=0, z=150, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=50, speed=speed, wait=True, timeout=timeout)
    multi_swift_cmd('set_position', z=150, speed=speed, wait=True, timeout=timeout)





