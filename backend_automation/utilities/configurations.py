import configparser
import mysql.connector
from mysql.connector import Error

def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

# connect_config = {
#     'user':get_config()['SQL']['user'],
#     'password':get_config()['SQL']['password'],
#     'host':get_config()['SQL']['localhost'],
#     'database':get_config()['SQL']['database']
# }

def get_connection():
    connection = mysql.connector.connect(host = 'localhost', database = 'APIDevelop', user = 'root', password = 'root')
