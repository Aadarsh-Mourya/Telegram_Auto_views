from configparser import ConfigParser
from threading import active_count
from time import sleep as swait
from os import system, name
from sendView import Api
from re import search
from sys import exit
import os

THREADS = 2000


error_file = open('errors.txt', 'a+', encoding='utf-8')
logger = lambda error: error_file.write(f'{error}\n')


def config_loader():
    try: 
        cfg = ConfigParser(interpolation=None)
        cfg.read("configHTTP.ini", encoding="utf-8")
        return (
            cfg["HTTP"].get("Sources").splitlines(),
            cfg["SOCKS4"].get("Sources").splitlines(), 
            cfg["SOCKS5"].get("Sources").splitlines()
        )
    except KeyError: 
        print(' [ Error ] config.ini not found!')
        swait(3)
        exit()


def input_loader():
    url = os.getenv('POST_URL')
    url_input = search(r'(https?:\/\/t\.me\/)?([^/]+)/(\d+)', url)
    if url_input: 
        _, channel, post = url_input.groups()
        return channel, post
    else: 
        print(' [ ERROR ] Channel Or Post Not Found!')
        swait(3)
        exit()


def display():
    print(' [ OUTPUT ] Started ( Wait few seconds to run threads )');swait(7)
    while int(active_count()) < THREADS-100: swait(0.1)
    system('cls' if name == 'nt' else 'clear')
    
    def inner():
        print(f'''
    [ Live Views ]: {Api.real_views}

    [ Token Errors ]:   {Api.token_errors}
    [ Proxies Errors ]: {Api.proxy_errors}

    [ Threads ]: {active_count()}
        ''')
    
    return inner


