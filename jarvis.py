import subprocess
import os

input = subprocess.getoutput("termux-speech-to-text")
print("You said: "+str(input))

if input == "hello":
   os.system("termux-tts-speak {}".format("Hello I am Jarvis"))
