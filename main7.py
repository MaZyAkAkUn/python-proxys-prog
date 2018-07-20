import time
import json
import requests

get_proxy_api_url = 'http://pubproxy.com/api/proxy'
check_api_token = '8wquj7m1fYIcDIyBA4P2T4sj5NInAHMF8GToNQNQ'
check_ip_api_url = 'https://www.abuseipdb.com/check/'
headers = {'Content-Type': 'application/json',
            'Autorization': 'Bearer'
           }
ip_check_headers = {'Content-Type': 'application/json',
            'Autorization': 'Bearer {0}'.format(check_api_token)}


http_proxy = "http://194.85.86.147:53281"
proxyDict ={
              "http": http_proxy
            }
def get_random_proxy_data():
    response = requests.get(get_proxy_api_url, headers=headers, proxies=proxyDict)
    if response.status_code == requests.codes.ok:
        print("Request get success.")
        proxy_data_response = json.loads(response.content.decode("utf-8"))
        proxy_data = proxy_data_response['data']
        proxy_info = proxy_data[0]
        pr_ip = proxy_info['ip']
        pr_port = proxy_info['port']
        pr_coun = proxy_info['country']
        pr_proto = proxy_info['type']
        pr_anon = proxy_info['proxy_level']
    else:
        print("Connection error: ")
        print(response.raise_for_status())
    return pr_ip, pr_port, pr_coun, pr_proto, pr_anon

def check_proxy_ip(proxy_ip_addr):
    check_proxy_api_url = '{0}{1}/json'.format(url_base, proxy_ip_addr)
    print(check_proxy_api_url)
    response = requests.get(check_proxy_api_url, headers=proxy_check_headers)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None



print(get_random_proxy_data())
pr_ip, pr_port, pr_coun, pr_proto, pr_anon = get_random_proxy_data()
