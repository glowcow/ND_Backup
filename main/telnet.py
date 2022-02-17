#!/bin/python3

from main.config import bc
import base64, time, telnetlib

class telnet:
    def opt1(cmd, host, username, password): # For Huawei & TP-Link devices
        try:
            username = base64.b64decode(username).decode("ascii") + "\r"
            password = base64.b64decode(password).decode("ascii") + "\r"
            tn = telnetlib.Telnet(host, port = 23, timeout = 5)
            #print(f'{bc.GREEN}[+]{bc.ENDC} Connecting to {host}...')
            tn.read_until(b'User')
            tn.write(username.encode("ascii"))
            time.sleep(1)
            tn.read_until(b'Password')
            tn.write(password.encode("ascii"))
            time.sleep(1)
            tn.read_until(b'>')
            #print(f'{bc.GREEN}[+]{bc.ENDC} Connection was established successfully to {host}')
            tn.write(cmd.encode("ascii"))
            time.sleep(11)
            out = tn.read_very_eager().decode("ascii")
            tn.close()
            #print(f'{bc.RED}[!]{bc.ENDC} Disconnected from {host}')
            return out
        except:
            #print(f'{bc.RED}[!]{bc.ENDC} Unknown Telnet Error on {host}')
            return False