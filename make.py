from datetime import datetime
from datetime import date

from time import sleep
from turtle import clear
from pydub import AudioSegment
from os.path import exists

import subprocess
import sys
bitrate = 0
print("Krunchy Audio Generator")

if not exists("ffmpeg.exe") or not exists("ffprobe.exe"):
    print("FFMPEG not installed or not fully installed.")
    print("Automatically running setup file.")
    sleep(2)
    clear()
    subprocess.run(["installlib.bat"])

print(" ")
print("Quality Level?")
level = input("Yes <------> 1 <------> 5 <------> 10 <------> 15 <------> 32 ")
print(level)
if level == "5":
     print("k")
     bitrate = bitrate - 4
elif level == "10":
     print("k")
     bitrate = bitrate - 1
elif level == "15":
     print("k")
elif level == "32":
     print("k")
elif level == "1":
     print("k") 
     bitrate = bitrate - 3
elif level == "yes":
     print("okay then") 
     bitrate = 8.0
else:
    raise ValueError("Invalid")
    


if level == "yes":
     bitrate = 8.0
     level = 0
else:
    bitrate = bitrate + (int(level) *10 /5 ) + 16

print(bitrate)
sound = AudioSegment.from_file("input.mp3")
time = datetime.now().strftime("%H%M%S")
date = date.today().strftime("%m%d%Y")
dt = time+"_"+date
sound.export("output-"+dt+".mp3", format="mp3", bitrate=str(int(bitrate)) + "k")
print("done")