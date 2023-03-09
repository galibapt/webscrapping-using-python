from requests_html import HTMLSession
from bs4 import BeautifulSoup

letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

for letter in letters:
    page_number = 1 
    list_words = []

    while True:
        url = f'https://www.merriam-webster.com/browse/dictionary/{letter}/{page_number}'
        session = HTMLSession()
        response = session.get(url)
        #print(response.status_code)
        print(f'parsing: {response.html.url}')
        
        soup = BeautifulSoup(response.html.html, 'html.parser')

        words = soup.select('div.mw-grid-table-list span')

        for word in words:
            list_words.append(word.contents[0])

        next_disabled = soup.select('.next.disabled')

        if next_disabled:
            print(list_words)
            break

        page_number += 1





