import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

url = 'https://allo.ua/ua/roboty-pylesosy/'
user = {'user-agent': fake_useragent.UserAgent().random}
response = requests.get(url, headers=user)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    all_products = soup.find("div", class_="products-layout__container products-layout--grid")
    products = all_products.find_all("div", class_="products-card")
    for product in products:
        title_products = product.find("a", class_="product-card__title")
        old_products = product.find("div", class_="v-pb")
        print(title_products.text)
        print(old_products.text)
        print(all_products)
        try:
            new_products = product.find("div", class_="v-pb__cur discout")
            print(new_products.text)
        except BaseException:
            print(title_products.text)
            print(old_products.text)
            print("Скидка закончилась")
            print()

        print()
