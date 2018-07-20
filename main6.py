import pymysql.cursors
import json
import requests
import time
# Подключиться к базе данных.
api_url_base = 'http://pubproxy.com/api/proxy'#'http://pubproxy.com/api/proxy'

headers = {'Content-Type': 'application/json',
            'Autorization': 'Bearer {0}'.format('')}
http_proxy = "http://194.85.86.147:53281"
ftp_proxy = ""
proxyDict ={
              "http": http_proxy
            }

def get_proxy_data():
    api_url = api_url_base

    response = requests.get(api_url, headers=headers, proxies=proxyDict)
    pr_data = json.loads(response.content.decode("utf-8"))

    if response.status_code == 200:
        prox_data = pr_data['data']
        return prox_data[0]
    else:
        print("Responce is None")
        return None




connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='toor',
                             db='proxys',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

i =0
try:
    while True:
        proxy_data = get_proxy_data()
        print("Getting proxy data...")
        proxy_ip = proxy_data['ip']
        proxy_port = proxy_data['port']
        # proxy_protocol = proxy_data['protocol']
        proxy_country = proxy_data['country']
        proxy_anon = proxy_data['proxy_level']

        cursor = connection.cursor()
        print("Inserting data in database...")
        sql = "INSERT INTO proxy_data (IP, PORT, COUNTRY, ANONLVL) VALUES ('{0}', {1}, '{2}', '{3}');".format(proxy_ip, int(
            proxy_port), proxy_country, proxy_anon)  # SELECT IP, PORT FROM proxy_data "

        # Выполнить команду запроса (Execute Query).

        cursor.execute(sql)
        print("Inserted.")

        sqls = "SELECT * FROM proxy_data;"
        res = cursor.execute(sqls)
        cursor.close()
        print("Cursor closed.")
        print("Sleeping for 1 sec...")
        time.sleep(1)
        i=i+1
        if i==99:
            break

finally:
    connection.commit()
    connection.close()