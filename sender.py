from django.conf import settings
import django_api.settings as app_settings
settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)
import django
django.setup()
import json
import subprocess
import requests
from requests import post , get
import os
import sys
from os import system, name
import httpx
import time
from subprocess import PIPE, Popen
import logging
from api.models import WorkerModel
from datetime import datetime


fruitpass = sys.argv[1]
logging.basicConfig(level=logging.INFO ,format='%(asctime)s - %(funcName)s - %(message)s')
def Num1():

    while True:
        worker = WorkerModel.objects.get(fruitpass = fruitpass)
        delta = worker.license_date -datetime.today().date()
        if delta.days >= 0 :
            if worker.status == 'on' : 
                try : 

                    r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 11; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{worker.fruitpass}"}
                    p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
                    st = httpx.post('http://iran.fruitcraft.ir/cards/collectgold' , data=p,headers=r)
                    uu = httpx.get('http://iran.fruitcraft.ir/cards/collectgold', headers=r)
                    logging.info('*** SENDED ***')
                    time.sleep(worker.second)
                    
                except : 
                    logging.info('error fruitpass .')
                    break
                
                
            else : 
                logging.info('workder khamoshe .')

                break
            
        else : 
            logging.info('user eshterak nadare .')
            worker.status = 'off'
            worker.pid = 0
            worker.chat_id = 0
            worker.license_date = datetime.now()
            worker.fruitpass = 'None'
            worker.second = 0
            worker.save()
            subprocess.Popen(['kill' , '-9' , f'{str(worker.pid)}'])
            break

Num1()