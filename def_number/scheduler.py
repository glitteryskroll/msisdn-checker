import csv
from crud.create import add_providers
from data_classes import PhoneProvider
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import schedule
import time
import configparser

config = configparser.ConfigParser()
config.read("../conf.conf")
load_files_urls = dict(config["number_data_urls"])
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def load_file(url, type):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        with open(f"src/number_codes/{type}.csv", "wb") as f:
            f.write(response.content)
        print("DEBUG load_file: loaded file - ", type)
    else:
        print("DEBUG load_file ERROR:", response.status_code)


def init_file(type):
    print("DEBUG: init_file - init_type", type)
    providers = []
    with open(f"src/number_codes/{type}.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # Skip first row
        for row in reader:
            phone_provider = PhoneProvider(
                ndc=int(row[0]),
                snA=int(row[1]),
                snB=int(row[2]),
                capacity=int(row[3]),
                provider=str(row[4]),
                region=str(row[5]),
                territory_gar=str(row[6]),
                inn=int(row[7]) if row[7] else "NULL",
            )
            providers.append(phone_provider)
    add_providers(providers)


def parse_data():
    try:
        print("DEBUG parse_data: start parsing number codes")
        for type in load_files_urls:
            load_file(load_files_urls[type], type)

        for type in load_files_urls:
            init_file(type)
        print("DEBUG parse_data: parsing and inserting ended successful")
    except Exception as ex:
        print("DEBUG parse_data: error with parsing data - ", ex)


schedule.every().day.at("09:00").do(parse_data)

while True:
    schedule.run_pending()
    time.sleep(1)
