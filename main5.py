from typing import Dict
import json
import requests
import time
import pypyodbc
#TODO: add more proxy-list sites, and more proxy chekers

api_token = ''
api_url_base = 'https://api.getproxylist.com/proxy?last_check=5&speed=2'#'http://pubproxy.com/api/proxy'

check_api_token = '8wquj7m1fYIcDIyBA4P2T4sj5NInAHMF8GToNQNQ'
#check_proxy_api_url = 'https://www.abuseipdb.com/check/[IP]/json?key=[API_KEY]&days=[DAYS]'
url_base = 'https://www.abuseipdb.com/check/'

headers = {'Content-Type': 'application/json',
            'Autorization': 'Bearer {0}'.format(api_token)}
proxy_check_headers = {'Content-Type': 'application/json',
            'Autorization': 'Bearer {0}'.format(check_api_token)}


def get_proxy_data():
    api_url = api_url_base
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

while True:



    proxy_data = get_proxy_data()
    proxy_ip_addr = proxy_data['ip']
    proxy_port = proxy_data['port']
    proxy_proto = proxy_data['protocol']
    proxy_country = proxy_data['country']
    proxy_anonymity = proxy_data['anonymity']

    check_proxy_api_url = '{0}{1}/json'.format(url_base, proxy_ip_addr)
    print(check_proxy_api_url)
    response = requests.get(check_proxy_api_url, headers=proxy_check_headers)
    if response.status_code == 200:
        check_proxy_result = json.loads(response.content.decode("utf-8"))
    else:
        check_proxy_result = None

    if proxy_data is not None:
        print("Your proxy ip: ")
        print(proxy_ip_addr, ':', proxy_port)
        print(proxy_proto)
        print(proxy_country)
        print(proxy_anonymity)

    if check_proxy_result is not None:
        print("Your check info: ")
        print(check_proxy_result)
    else:
        print("Your proxy are good!)")
        print(proxy_data)
    time.sleep(1)
