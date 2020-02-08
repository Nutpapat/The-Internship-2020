import requests
from bs4 import BeautifulSoup
def sort(des):
    return len(des[1])
def main():
    """ Main function """
    url = 'https://theinternship.io/'
    response = requests.get(url)
    logo = BeautifulSoup(response.text, "html.parser")
    partners = []
    for logo_item in logo.select('.partner > .logo-box > a > img'):
        partners.append(logo_item.get('src'))
    for index, des_item in enumerate(logo.select('.list-company')):
        partners[index] = [partners[index] ,des_item.getText()]
    partners.sort(key=sort)
    for output in partners:
        print(output[0])
main()
