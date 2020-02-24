import webbrowser
import sys
import os
from tkinter import messagebox
try:
    from bs4 import BeautifulSoup
    import requests
except ImportError:
    messagebox.showerror("Error", "Libraries not found")

class WebPage:

    def __init__(self, page):
        self.url = page
        self.initBS()

       
    def getLinkWithKeyWord(self, key):
        link = self.soup.findAll('a')
        sol = []
        for i in link:
            if i.text.find(key) != -1:
                sol.append(i)
        return sol
    
    def openWebPages(self, key):
        links = self.getLinkWithKeyWord(key)
        if len(links) > 1:
            for i in links:
                print(i.text)
        elif len(links) == 0:
            print("No sites found")
        else:
            self.openUrlLink(links[0])

    def openUrlLink(self, link):
        goLink = link.get('href')
        if goLink.find('http') == -1:
            goLink = self.url + goLink
        webbrowser.open(goLink)

    #inits
    def initBS(self):
        content = self.requestUrl()
        self.soup = BeautifulSoup(content.text, 'html.parser')

    def requestUrl(self):
        try:
            content = requests.get(self.url)
            return content
        except ConnectionError:
            print("Connection Error")
        except requests.HTTPError:
            print("Http error")
        except requests.Timeout:
            print("Connection timeout")


def getUrlFromConfig():
    try:
        dir_path = os.path.dirname(__file__)
        with open(dir_path + os.sep + 'config.ini') as file:
            for line in file:
                if line[0] != '#':
                    return line
    except FileNotFoundError:
        with open('config.ini', 'w') as file:
            file.write('# site for fast link opening')
    messagebox.showerror("Error","Corrupted config file")
      

def main():
    # url = getUrlFromConfig()
    if len(sys.argv) > 1:
        keyWord = sys.argv[1]
    else:
        keyWord = input("Key Word\n>>> ")
    try:
        l = WebPage("http://rti.etf.bg.ac.rs/").openWebPages(keyWord.upper())
    except:
        print('Error')
    
    


if __name__ == "__main__":
    main()
