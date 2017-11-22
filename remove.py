#!/usr/bin/env python
import os
import sys
variable = sys.argv[1]

try:
    os.remove("/home/pi/imagenesCloset/" + variable +".jpg")
    print("true")
except:
    print("false")
    pass
