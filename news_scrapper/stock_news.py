from bs4 import BeautifulSoup
import requests


class Webpage():
    def __init__(self,name) -> None:
        self.name = name
        self.mainpage_titles = set()
        if self.name == "bbc":
            self.url = "https://www.bbc.com/news/business"
        
    def get_mainpage_data(self,titles=False):
        
        if self.name == "bbc":
            
                response = requests.get(self.url)
                if not response.status_code == 200:
                    print("https Error!")
                else:
                    Soup = BeautifulSoup(response.content,"html.parser")
                if titles == True:
                    for title in Soup.find_all("h3",class_="gs-c-promo-heading__title"):
                        self.mainpage_titles.add(title.text)
                    return self.mainpage_titles
                else:
                    for data in Soup.find_all("a",class_="gs-c-promo-heading"):
                        print(data["href"])


   
        


bbc_news = Webpage("bbc")
titles =bbc_news.get_mainpage_data(titles=True)

for a in titles:
    print(a)




    