import mechanicalsoup
from bs4 import BeautifulSoup
browser = mechanicalsoup.Browser()
page = browser.get('https://www.facebook.com/')
form = page.soup.form

form.find("input", {"name": "email"})["value"] = "mazyaka.pub@gmail.com"
form.find("input", {"name": "pass"})["value"] = "VASKA6541"
responce = browser.submit(form, page.url)
print(responce.url)