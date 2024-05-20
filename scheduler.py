

import requests
import schedule
import time
import csv
import logging
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phone_service.settings')
import django
django.setup()
import phone_service.settings as settings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from def_number.models import PhoneProvider
from def_number.crud.create import add_providers

logger = logging.getLogger("parser")

load_files_urls = getattr(settings, 'NUMBER_DATA_URLS', {})
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def load_file(url, type):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        with open(f"def_number/src/number_codes/{type}.csv", "wb") as f:
            f.write(response.content)
        logger.info(f"load_file loaded file {type}")
    else:
        logger.error(f"load_file {response.status_code}")

def init_file(type):
    logger.info(f"init_file init_type {type}")
    providers = []
    with open(f"def_number/src/number_codes/{type}.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # Пропуск первой строки
        for row in reader:
            phone_provider = PhoneProvider(
                ndc=int(row[0]),
                snA=int(row[1]),
                snB=int(row[2]),
                capacity=int(row[3]),
                provider=str(row[4]),
                region=str(row[5]),
                territory_gar=str(row[6]),
                inn=int(row[7]) if row[7] else None,
            )
            providers.append(phone_provider)
    add_providers(providers)

def parse_data():
    try:
        logger.info("parse_data start parsing number codes")
        for type in load_files_urls:
            load_file(load_files_urls[type], type)
            init_file(type)

        logger.info("parse_data parsing and inserting ended successfully")
    except Exception as ex:
        logger.error(f"parse_data: error with parsing data - {ex}")

parse_data()
schedule.every().day.do(parse_data)

# Запуск цикла планировщика
while schedule.get_jobs():
    schedule.run_pending()
    time.sleep(1)
