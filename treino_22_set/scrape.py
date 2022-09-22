from urllib import response
import requests
from parsel import Selector


URL = 'https://quotes.toscrape.com'

def fetch(url):
  response = requests.get(url)
  response.raise_for_status()

  return response.text

def scrape_quotes():
  html = fetch(URL)
  selector = Selector(html)
  quote = selector.css('div.quote > span.text::text').get()

  return quote

if __name__ == '__main__':
  print(scrape_quotes())