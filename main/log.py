#!/bin/python3

from main.config import log_var, bc
import os, getpass, time, re

class log:
    usr = os.getlogin()
    usr_eff = getpass.getuser()
    def write(result):
        try:
            wr_date = time.strftime('%Y-%b')
            log_date = time.strftime('%d-%b-%Y %H:%M:%S')
            file = open(f'{log_var.path}{wr_date}.log', 'a')
            file.write(f'{log.usr_eff}({log.usr})|{log_date}|{"="*50}\n')
            if result:
                for each in result.split('\n'):
                    file.write(f'{log.usr_eff}({log.usr})|{log_date}| {each}\n')
            else:
                file.write(f'{log.usr_eff}({log.usr})|{log_date}| {result}\n')
            file.close()
        except PermissionError:
            print(f'{bc.RED}[!]{bc.ENDC} Log file permission error on open')