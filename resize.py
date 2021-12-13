# !/usr/bin/python
# -*- coding:utf-8 -*-
import os

def resize():
    size = input("what size do you want the final video to be?\n "
                 "[1280x720, 640×480, 360x240, 160x120]\n"
                 "please enter widthxheight: ")

    command = 'ffmpeg -i bbb_full.mp4 -s ' + size + ' -c:a copy '+ str(size) +'.mp4'
    os.system(command)
    print("resize successful")

resize()
