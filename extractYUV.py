# !/usr/bin/python
# -*- coding:utf-8 -*-
import os


class ExtractYUV:

    # not used at the moment
    def display_histogram(self):
        os.system("ffplay BBB.mp4 -vf format=gbrp,histogram")

    def extract_yuv(self):
        print("extract")
        os.system('ffplay BBB.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"')

    extract_yuv()
