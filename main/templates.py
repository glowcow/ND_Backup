#!/bin/python3

from main.config import ftp

class bkp():
    def __init__(self, vend, *args):
        if vend == 'huawei':
            date, name, city = args
            self.huawei = f'save\ry\rsave config.cfg\ry\rtftp {ftp.ip} vpn-instance MGMT put flash:/config.cfg {ftp.path_1}{date}_{name}({city}).cfg\r'
        if vend == 'mikrotik':
            date, name, city = args
            self.mikrotik = f'/export file=exportfile_{date}_{name}.rsc;\n:delay 5;\n/tool fetch address={ftp.ip} src-path=exportfile_{date}_{name}.rsc mode=ftp upload=yes user={ftp.usr} pass={ftp.psw} dst-path="{ftp.path_2}{date}_{name}({city}).rsc";\n:delay 2;\n'
        if vend == 'tp_link':
            date, name, city = args
            self.tp_link = f'enable\rcopy running-config startup-config\rcopy startup-config tftp ip-address {ftp.ip} filename {ftp.path_3}{date}_{name}({city}).cfg\r'