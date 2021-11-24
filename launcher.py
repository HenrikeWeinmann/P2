import os

user_input = input("which program do you want to launch? ")
print(user_input)

os.system('python ' + user_input + '.py')
