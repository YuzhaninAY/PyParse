
import requests

link1 = "https://www.lanta.ru/metals/"
link2 = "https://www.sberbank.ru/ru/person/investments/values/mon#/page/1/search?met1"


headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
response = requests.get(link2)

with open(f'index.html', 'w') as file:
    file.write(response.text)
