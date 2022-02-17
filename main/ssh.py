#!/bin/python3

from main.config import bc
import time, base64, paramiko, socket

class ssh:
    timeout = 30
    def init(host, username, password, mode):
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            session.connect(hostname=host, username=base64.b64decode(username).decode("ascii"), password=base64.b64decode(password).decode("ascii"), timeout=ssh.timeout, banner_timeout=ssh.timeout, auth_timeout=ssh.timeout)
        except socket.timeout:
            #print(f'{bc.RED}[!]{bc.ENDC} Host: {host} is unreachable, timed out')
            return False
        except paramiko.AuthenticationException:
            #print(f'{bc.RED}[!]{bc.ENDC} Invalid credentials for {username} | {password}')
            return False
        except paramiko.ssh_exception.NoValidConnectionsError:
            #print(f'{bc.RED}[!]{bc.ENDC} Connection refused by {host}')
            return False
        except paramiko.ssh_exception.SSHException:
            # socket is open, but not SSH service responded
            #print(f'{bc.RED}[!]{bc.ENDC} Error reading SSH protocol banner on {host}')
            return False
        else:
            #print(f'{bc.GREEN}[+]{bc.ENDC} Connection was established successfully to {host}')
            if mode == 1:
                session = session.invoke_shell(width=250, height=25000)
                return session
            elif mode == 2:
                return session
            else:
                #print(f'{bc.RED}[!]{bc.ENDC} Incorrect SSH mode')
                return False

    def exec(cmd, session):
        stdin, stdout, stderr = session.exec_command(cmd, timeout=ssh.timeout)
        time.sleep(2)
        out = stdout.read().decode("ascii")
        return out

    def invoke(cmd, session):
        session.send(cmd+'\n')
        time.sleep(2)
        out = session.recv(999999).decode("ascii")
        return out

    def close(session):
        #print(f'{bc.RED}[!]{bc.ENDC} Disconnected')
        session.close()
        return True