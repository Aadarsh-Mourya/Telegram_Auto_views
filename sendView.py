import requests
from re import search
import time, random
import logging
from fake_useragent import UserAgent

ua = UserAgent()

class Api():
    real_views, proxy_errors, token_errors = 0, 0, 0

    def __init__(self, channel, post) -> None:
        self.url = 'https://t.me/'
        self.channel, self.post = channel, post

    @classmethod
    def views(cls, self):
        telegram_request = requests.get(
            f'{self.url}{self.channel}/{self.post}', 
            params={'embed': '1', 'mode': 'tme'},
            headers={
                'referer': f'{self.url}{self.channel}/{self.post}', 
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0'  # changes here
            }
        )
        cls.real_views = search(
            '<span class="tgme_widget_message_views">([^<]+)', 
            telegram_request.text
        ).group(1)
        return cls.real_views

    # changes here
    # Validate the proxy by sending a request to ipinfo.io
    def validate_proxy(self, proxy, proxy_type):

        try:
            response = requests.get(
                'https://ipinfo.io/ip',
                headers={
                    'referer': f'{self.url}{self.channel}/{self.post}', 
                    'user-agent':  ua.random     # ---------- changes here -------------
                },
                proxies={
                    'http': f'{proxy_type}://{proxy}', 
                    'https': f'{proxy_type}://{proxy}'
                },
                timeout=20
            )
            
            if response.status_code == 200 :
                with open('validated_proxies3.txt', 'a') as file:
                    file.write(f'{proxy_type}://{proxy}\n')
                return True
           
        except requests.exceptions.ConnectTimeout as e:
            logging.error(f"Validation Proxy timed out during connection{proxy} : {e}")
        except requests.exceptions.ReadTimeout as e:
            logging.error(f"Validation Proxy waiting for response {proxy} : {e}")
        except requests.exceptions.ProxyError as e:
            logging.error(f"Validation Proxy error {proxy} : {e}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Validation error with proxy {proxy} : {e}")
        return False
    
    # global proxyPool
    # proxyPool={
    #     "http": "PREMIUM_PROXY_URL",
    #     "https": "PREMIUM_PROXY_URL"
    # }

    def send_view(self, proxy, proxy_type, attempt = 0):                
        
        random_user_agent = ua.random
        if attempt == 0:
            if not self.validate_proxy(proxy, proxy_type):
                    # Api.proxy_errors += 1
                return
        
        time.sleep(random.uniform(3, 8))
        try:
            session = requests.session()
            response = session.get(
                f'{self.url}{self.channel}/{self.post}', 
                params={'embed': '1', 'mode': 'tme'},
                headers={
                    'referer': f'{self.url}{self.channel}/{self.post}',
                    'user-agent': random_user_agent,   # ---------- changes here -------------
                    'language': 'en-US,en;q=0.9',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'accept-encoding': 'gzip, deflate, br',
                    'cache-control': 'max-age=0'
                },
                proxies={
                    'http': f'{proxy_type}://{proxy}',
                    'https': f'{proxy_type}://{proxy}'
                },
                
                timeout=20
            )   

            cookies_dict = session.cookies.get_dict()
            session.get(
                'https://t.me/v/', 
                params={'views': str(search('data-view="([^"]+)', response.text).group(1))}, 
                cookies={
                    'stel_dt': '-240', 
                    'stel_web_auth': 'https%3A%2F%2Fweb.telegram.org%2Fz%2F',
                    'stel_ssid': cookies_dict.get('stel_ssid', None), 
                    'stel_on': cookies_dict.get('stel_on', None)
                },
                headers={
                    'referer': f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                    'user-agent': random_user_agent,    # ---------- changes here -------------
                    'x-requested-with': 'XMLHttpRequest',
                },
                proxies={
                    'http': f'{proxy_type}://{proxy}', 
                    'https': f'{proxy_type}://{proxy}'
                },
             
                timeout=20
            )  
            
        except AttributeError as e: 
            logging.error(f"Attribute error {proxy}: {e}")
            Api.token_errors += 1

        except requests.exceptions.RequestException as e: 
            logging.error(f"Request error {proxy}: {e}") #changes here

            time.sleep(min(60, (2 ** attempt) + random.uniform(1, 5)))
            if attempt < 2:  # Retry up to 3 times
                self.send_view(proxy, proxy_type, attempt + 1)
            else:
                Api.proxy_errors += 1
               # return
        time.sleep(random.uniform(5, 12)) # Random sleep to mimic human behave
