import requests
import parse
from parse import Parse


#url = "http://olympus.realpython.org/profiles/aphrodite"

def requestUrl():
    back = "http://"
    url = str(input("Please enter a url to scrape: "))
    for i in range(7):
        if(url[i] != back[i]):
            url = back + url
            break
    return url

def scrape():
    #this is just the main of this so I can import it 
    url = requestUrl()
    inp = Parse(url)
    #page = requests.get(url_1)
    inp.parse()

def main():
    scrape()

main()