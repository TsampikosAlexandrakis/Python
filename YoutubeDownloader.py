from subprocess import call
from time import sleep

url = input("Video URL : ")
file_type = input("Type mp3 for audio and mp4 for video : ")

if file_type == "mp3" or file_type == "MP3":
    command = str("youtube-dl -x --audio-format mp3 --audio-quality 0 " + url + " -c")
    call(command)
elif file_type == "mp4" or file_type == "MP4":
    command = str("youtube-dl --recode-video mp4 " + url + " -c")
    call(command)
else:
    print("NO VALID FORMAT!")
    sleep(1)
    exit
