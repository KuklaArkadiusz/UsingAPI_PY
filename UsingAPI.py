import requests
from bs4 import BeautifulSoup

titles=('topstories','newstories','beststories')
check_duplicates=[]

for title in titles:
    n=requests.get(f'https://hacker-news.firebaseio.com/v0/{title}.json?print=pretty')
    y=n.json()
    numbers=y[:10]
    print(f'--{title}--\n')
    count=0
    for i in numbers:
        count+=1
        response=requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty')
        d=response.json()
        print(d['title'])
        if d['title'] not in check_duplicates: 
            check_duplicates.append(d['title'])
        else:
            count-=1
            continue
        if 'url' in d:
            print(d['url'])
        else:
            soup = BeautifulSoup(d['text'],features="html.parser")
            soup.get_text()
            x=str(soup).split()[:80]
            print(*x) 
        print("")
        if count ==5:   
            break
            
