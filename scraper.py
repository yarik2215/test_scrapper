import requests
from bs4 import BeautifulSoup

SITE_URL = 'https://www.djangoproject.com/download/'

def print_href(object):
    print('\t' + object.a.get('href'))


if __name__ == '__main__':
    request = requests.get(SITE_URL)
    if request.status_code != 200:
        raise ValueError(f'Status code = {request.status_code}')

    print(f'Status code = {request.status_code}')
    soup = BeautifulSoup(request.text, 'html.parser')

    ul = soup.find('div', {'role': 'complementary'}).find_all('ul')
    
    latest = ul[1]
    previous = ul[2]
    unsuported = ul[3]

    print('Latest release:')
    for li in latest.find_all('li'):
        print_href(li)
    
    print('Previous releases:')
    for li in previous.find_all('li'):
        print_href(li)

    print('Unsupported previous releases:')
    for li in unsuported.find_all('li'):
        print_href(li)

    
