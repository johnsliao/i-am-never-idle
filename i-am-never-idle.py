#!usr/bin/env python

import time
import sys

from ctypes import Structure, windll, c_ulong, byref

class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]
    
def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))

    return pt.x, pt.y

def moveMouse(x,y):
    windll.user32.SetCursorPos(x+5,y+5)

times_run = 0

while True:
    times_run += 1
    x, y = queryMousePosition()
    moveMouse(x,y)
    
    if times_run > 96: # 8 hour day
        sys.exit(1)

    time.sleep(300)