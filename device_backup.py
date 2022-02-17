#!/bin/python3

from main.ssh import ssh
from main.telnet import telnet
from main.log import log
from main.config import radctl, mik_acc, bc
from main.templates import bkp
from multiprocessing import Pool
import time, re, tqdm, pandas

def xls_parse(file):
    try:
        data = pandas.read_excel(file).to_numpy().tolist()
    except FileNotFoundError:
        print(f'{bc.RED}[!]{bc.ENDC} Inventory file({file}) not found')
        return False
    except PermissionError:
        print(f'{bc.RED}[!]{bc.ENDC} Inventory file({file}) permission error')
    else:
        return data

def backup(device):
    date = time.strftime('%d-%b-%Y')
    name, city, vend, ip  = device
    if vend == 'huawei':
        cmd = bkp(vend, date, name, city)
        result = telnet.opt1(cmd.huawei, ip, radctl.username, radctl.password)
        if result != False:
            if not re.findall('TFTP: Uploading the file successfully.', result):
                return (f'{ip}|{name}({city}) - Backup error!')
        else:
            return (f'{ip}|{name}({city}) - Telnet Error!')
    elif vend == 'mikrotik':
        cmd = bkp(vend, date, name, city)
        s = ssh.init(ip, mik_acc.username_m, mik_acc.password_m, 2)
        if s != False:
            result = ssh.exec(cmd.mikrotik, s)
            if not re.findall('status: finished', result):
                return (f'{ip}|{name}({city}) - Backup error!')
            ssh.close(s)
        else:
            return (f'{ip}|{name}({city}) - SSH Error!')
    elif vend == 'tp_link':
        cmd = bkp(vend, date, name, city)
        result = telnet.opt1(cmd.tp_link, ip, radctl.username, radctl.password)
        if result != False:
            if not re.findall('Backup user config file OK.', result):
                return (f'{ip}|{name}({city}) - Backup error!')
        else:
            return (f'{ip}|{name}({city}) - Telnet Error!')
    else:
        return (f'{ip}|{name}({city}) Incorrect device vendor type({vend})')

def main():
    devices = xls_parse('inventory.xlsx')
    pool = Pool(processes=32)
    print(f'\n{"="*5}{bc.GREEN} Total devices to backup: {len(devices)} {bc.ENDC}{"="*5}\n')
    results = []
    for result in tqdm.tqdm(pool.imap_unordered(backup, devices), total=len(devices)):
        results.append(result)
    err_list = list(filter(bool,(results)))
    if len(err_list) != 0:
        msg = "\n".join(err_list)
        log.write(msg)
        print(f'\n{"="*5}{bc.RED} There are some errors, see log file for details {bc.ENDC}{"="*5}\n')
    else:
        print(f'\n{"="*5}{bc.CYAN} All done with no errors! {bc.ENDC}{"="*5}\n')

if __name__ == "__main__":
    main()