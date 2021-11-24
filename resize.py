import os


def resize():
    size = input("what size do you want the final video to be?\n "
                 "[1280x720, 640×480, 360x240, 160x120]\n"
                 "please enter widthxheight: ")
    command = 'ffmpeg -i BBB.mp4 -s ' + size + ' -c:a copy resized.mp4'
    os.system(command)
    print("resize successful")

resize()
