import os


def cut():
    seconds = input("How many seconds do you want to cut from the BBB video: \n")
    os.system('ffmpeg -ss 0 -i BBB.mp4 -c copy -t ' + str(seconds) + ' cut.mp4')
    print("sucess")

cut()

