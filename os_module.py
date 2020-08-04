"Os commands:"
import os 

os.system("dir") # For running the command

os.listdir()
try:
    f = open('abc.txt','r')
except OSError:
    print("File not found")


os.mkdir("Python")
