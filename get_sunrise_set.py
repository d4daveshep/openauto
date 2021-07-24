import requests
from bs4 import BeautifulSoup

web_url = "https://www.sunrise-and-sunset.com/en/sun/new-zealand/auckland"

page = requests.get(web_url)

print(page.status_code)
# print(page.status_code == 200)

soup = BeautifulSoup(page.content, 'html.parser')

# html = list(soup.children)[2]
# body = list(soup.children)[3]

table = soup.find('table', class_="table table-borderless")
# print(table.prettify())

tds = table.find_all('td')
sunrise_td = list(tds)[2]
sunset_td = list(tds)[3]

sunrise = (sunrise_td.contents[0]).strip()
sunset = (sunset_td.contents[0]).strip()

print(f"Sunrise is at: {sunrise}")
print(f"Sunset is at: {sunset}")
