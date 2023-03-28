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
from threading import Thread
import logging
from api.models import WorkerModel
from datetime import datetime
import pytz



fruitpass = sys.argv[1]

def Num1():


    # Namereq = requests.options("http://iran.fruitcraft.ir/player/getplayerinfo",headers=r)
    # deta = Namereq.content
    # value2 = deta.decode('utf-8')
    # convert2 = json.loads(deta)
    # Name = convert2["data"]["name"]

    while True:
        worker = WorkerModel.objects.get(fruitpass = fruitpass)
        delta = worker.license_date -datetime.today().date()
        if delta.days >= 0 :
###################################################### your code ############################################################
            print(worker.fruitpass)
            print(time.sleep(worker.second))

            # tz_London = pytz.timezone('Asia/Tehran')
            # datetime_London = datetime.now(tz_London)
            # r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 11; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{worker.fruitpass}"}
            # p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
            # st = httpx.post('http://iran.fruitcraft.ir/cards/collectgold' , data=p,headers=r)
            # uu = httpx.get('http://iran.fruitcraft.ir/cards/collectgold', headers=r)
            # try:
            #             data5 = uu.content
            #             value = data5.decode('utf-8')
            #             convert = json.loads(data5)
            #             allow = convert['status']
            #             Gold = convert['data']['player_gold']
            #             limit = convert['data']['gold_collection_allowed']
            #             if limit == False :
            #                 logging.basicConfig(level=logging.INFO)
            #                 logging.info(f"{datetime_London}"+"  !!!  Limit 1 !!!  ==> "+ f"{Gold}"+ " -- Name : "+Name)
            #                 time.sleep(3600)
            #             elif limit == True :
            #                 logging.basicConfig(level=logging.INFO)
            #                 logging.info(f"{datetime_London}"+"  +++  OK 1 +++  || Gold is  ==> "+ f"{Gold}"+ " -- Name : "+Name)
            # except:
            #             logging.basicConfig(level=logging.INFO)
            #             logging.info(f"{datetime_London}"+"  *** ERROR FRUITPASS ***  ")
            # time.sleep(worker.second)
###################################################### end code ############################################################

        else : 
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
        
        