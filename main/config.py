#!/bin/python3

class bc:
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLINK = '\33[5m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class log_var:
    path = 'log/' #Path to local log faile

class radctl: #all values must be encoded in base64
    username = 'dGVzdA=='
    password = 'dGVzdA=='

class mik_acc: #all values must be encoded in base64
    username_m = 'dGVzdA=='
    password_m = 'dGVzdA=='

class ftp:
    usr = 'test' # User for FTP
    psw = 'test' # Password for FTP
    ip = '192.168.1.1' #TFTP & FTP Server address
    path_1 = 'Backup/TEST_BKP/' #Path to backup Huawei config files
    path_2 = 'Backup/TEST_BKP/' #Path to backup MikroTik config files
    path_3 = 'Backup/TEST_BKP/' #Path to backup TP-Link config files