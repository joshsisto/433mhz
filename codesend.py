#! /usr/bin/env python3

import os
import time

codes = {
    'power': '16658433',
    'mode_plus': '16658437',
    'mode_minus': '16658443',
    'speed_plus': '16658441',
    'speed_minus': '16658439',
    'demo': '16658440',
    'color_plus': '16658442',
    'color_minus': '16658445',
    'bright_plus': '16658444',
    'bright_minus': '16658447',
    'white': '16658446',
    'red': '16658447',
    'green': '16658449',
    'purple': '16658450',
    'yellow': '16658451',
    'blue': '16658452',
    'pink': '16658453'
}


def remote_code(code):
    os.system('/usr/bin/codesend {}'.format(code))
    time.sleep(.25)


remote_code(codes["power"])

