import os

def user_input():
    user_input = input("change audio codec or create mono audio version?\n"
                       "[a] audio codec\n"
                       "[m] mono audio\n"
                       "[e] exit\n")
    if user_input == "a":
        audio_codec()
    elif user_input == "m":
        monoaudio()
    elif user_input == "e":
        exit()
    else:
        print("please enter a correct parameter or [e] to exit")

def audio_codec():
    acodec = input("which audio codec do you want to change to?\n"
                   "[mp3,  ]\n")
    os.system('ffmpeg -i BBB.mp4 -acodec ' + str(acodec) + '  -vcodec copy audiocodec.mp4')


def monoaudio():
    os.system('ffmpeg -i BBB.mp4 -ac 1 mono_BBB.mp4')
    print("mono audio")

user_input()
