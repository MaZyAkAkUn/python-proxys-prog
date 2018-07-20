import mechanicalsoup
from bs4 import BeautifulSoup
import urlparse3
import requests

browser = mechanicalsoup.Browser()
response = requests.get('https://account.mail.ru/signup')
page = response.text
#page = browser.get('https://account.mail.ru/signup')
#form = page.soup.form
soup = BeautifulSoup(page, "lxml")
form = soup.find_all('signup')
print(form)
#form.find("input", {"name": "firstname"})["value"] = 'Pavel'
#form.find("input", {"name": "lastname"})["value"] = 'Rytoski'
#responce = browser.submit(form, page.url)

