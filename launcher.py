import os

user_input = input("Which program do you want to launch?\n"
                   "[cut, resize, monoaudio, extractYUV] \n")

os.system('python ' + user_input + '.py')
