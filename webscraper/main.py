import requests
import parse
url = "http://olympus.realpython.org/profiles/aphrodite"
def main():
    page = requests.get(url)
    print(page.content)
    #parse(page.content)

main()