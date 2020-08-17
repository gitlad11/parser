import requests
from bs4 import BeautifulSoup

urlinput = input("что будем парсить?:")
url = "{}".format(urlinput.strip())
def get(url):
    
    try:
        req = requests.get(url)
        print(req.status_code)
    except Exception:
        print("неправильный url")
        return False
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, "html.parser")
            if soup is not None:
                print('your soup has been cooked!')
                return get_element(soup)
            else: 
                print('soup is spoiled')
                return False
get(url)

elinput = input("Какой элемент?:")
element = "{}".format(elinput.strip())
def get_element(soup, element):
    elem = soup.find_all(element)
    if elem is not None:
        dump = input("сохранить в json ?(yes,no):")
        if dump == "yes":
            with open("dump.json", "w") as write_file:
                json.dump(elem, write_file)
        else: 
            print('файл не будет сохранен')
    else: 
        print('элемент не найден')
get_element(element)




