import subprocess
import datetime
import os

# voice function!
def VoiceFunction():
    input = subprocess.getoutput("termux-speech-to-text")
    print("You said:"+str(input))
    if input == "hello":
        os.system("termux-tts-speak {}".format("Hello I am Jarvis"))
# text function!
def TextFunction():
    text = input("Your msg: ")
    print(text)

# wishme function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        os.system("termux-tts-speak {}".format("Good Morning"))
    elif hour>=12 and hour<18:
        os.system("termux-tts-speak {}".format("Good Morning"))
    else:
        os.system("termux-tts-speak {}".format("Good Evening"))
    print("I am Jarvis Sir. Please tell me how may I help you")
    selection()

# def selection 
def selection():
    select = input("Please select which method you want to run as ur assistant..\n Voice or Text?: ")
    # if user input == voice..
    if select.lower() == "Voice":
        print("voice!")
        VoiceFunction()
    # if user input == text..
    elif select.lower() == "text":
        print("text!")
        TextFunction()

if __name__ == "__main__":
    wishMe()
