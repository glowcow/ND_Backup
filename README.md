# Network Device Backup Tool
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was created to automate the daily routine tasks for NOC engineer.
    
## Technologies
Project is created with:
* paramiko 2.8.0
* multiprocess 0.70
* pandas 1.3.4
    
## Setup
To run this project, git clone it locally.
Change variables in main/config.py.
Install packages via PIP ```pip3 install paramiko xlrd tqdm pandas openpyxl```
Customiz your ```inventory.xlsx``` and run ```python3 device_backup.py```