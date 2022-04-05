# Network Device Backup Tool
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Usage](#setup)

## General info
This project was created to automate the daily routine tasks for NOC engineer.
    
## Technologies
Project is created with:
* pandas 1.3.4
* openpyxl 3.0.9
* paramiko 2.10.3
* multiprocess 0.70.12.2
* tqdm 4.62.3
    
## Usage
To run this project, git clone it locally.
Change variables in main/config.py.
Install required packages via PIP ```pip3 install -r requirements.txt```
Customize your ```inventory.xlsx``` and run ```python3 device_backup.py```
