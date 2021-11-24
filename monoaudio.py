#!/usr/bin/python
# -*- coding:utf-8 -*-
import os


#ask user what operation he wants to do
def user_input():
    valid_input = False
    while not valid_input:
        user_input = get_input()
        if user_input == "a":
            audio_codec()
            valid_input = True
        elif user_input == "m":
            monoaudio()
            valid_input = True
        elif user_input == "x":
            exit()
        else:
            print("please enter a correct parameter or [e] to exit")


def get_input():
    user_input = input("change audio codec or create mono audio version?\n"
                       "[a] audio codec\n"
                       "[m] mono audio\n"
                       "[x] exit\n")
    return user_input


# assuming that the user will provide an mp4 file, these are the audio codecs that are
# supported by ffmpeg
def audio_codec():
    acodec = input("which audio codec do you want to change to?\n"
                   "[Opus, MP2, MP3, LC-AAC, HE-AAC, AC3, E-AC3, TrueHD]\n")
    os.system('ffmpeg -i BBB.mp4 -acodec ' + str(acodec) + '  -vcodec copy audiocodec.mp4')


def monoaudio():
    os.system('ffmpeg -i BBB.mp4 -ac 1 mono_BBB.mp4')
    print("mono audio")


user_input()
