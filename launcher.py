import cut
import resize
import extractYUV
import monoaudio
user_input = input("which program do you want to launch? ")

if user_input == "cut":
    cut()
elif user_input == "resize":
    resize()
elif user_input == "extract":
    extractYUV()
elif user_input == "mono":
    monoaudio()
