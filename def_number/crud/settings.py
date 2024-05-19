import configparser
import psycopg2
import os

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
config_file_path = os.path.join(current_directory, "../../conf.conf")

config = configparser.ConfigParser()
config.read(config_file_path)
config_data = config["database"]

dbname = config_data["dbname"]
user = config_data["user"]
password = config_data["password"]
host = config_data["host"]


def connect_to_db():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    return conn
