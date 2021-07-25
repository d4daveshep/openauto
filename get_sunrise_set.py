import requests
from bs4 import BeautifulSoup

def get_sunrise_sunset():
    web_url = "https://www.sunrise-and-sunset.com/en/sun/new-zealand/auckland"

    page = requests.get(web_url)

    results = {'status_code':page.status_code}
    if page.status_code == 200:

        soup = BeautifulSoup(page.content, 'html.parser')

        table = soup.find('table', class_="table table-borderless")
        # print(table.prettify())

        tds = table.find_all('td')
        sunrise_td = list(tds)[2]
        sunset_td = list(tds)[3]

        sunrise = (sunrise_td.contents[0]).strip()
        sunset = (sunset_td.contents[0]).strip()

        # print(f"Sunrise is at: {sunrise}")
        # print(f"Sunset is at: {sunset}")
        results['sunrise'] = sunrise
        results['sunset'] = sunset

    return results

if __name__ == '__main__':
    results = get_sunrise_sunset()

    print(f"Status code = {results['status_code']:d}")
    print(f"Sunrise is at: {results['sunrise']}")
    print(f"Sunset is at: {results['sunset']}")

