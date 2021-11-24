#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

#ask user what operation he wants to do
def user_input():
    valid_input = False
    while not valid_input:
        user_input = get_input()
        if user_input == "c":
            valid_input = True
            os.system('python cut.py')
        elif user_input == "r":
            valid_input = True
            os.system('python resize.py')
        elif user_input == "m":
            valid_input = True
            os.system('python monoaudio.py')
        elif user_input == "e":
            valid_input = True
            os.system('python extractYUV.py')
        elif user_input == "x":
            exit()
        else:
            print("please enter a correct parameter or [e] to exit")


def get_input():
    user_input = input("Chose a program to launch:\n"
                       "[c] cut\n"
                       "[r] resize\n"
                       "[m] change audio codec\n"
                       "[e] extract YUV histogram\n"
                       "[x] exit\n")
    return user_input

user_input()

