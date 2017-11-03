import requests, csv
from bs4 import BeautifulSoup

i=1

with open('users_filmow.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')

    for i in range(1,3): #[1,2[
        url = "https://filmow.com/usuarios/?pagina=" + str(i)
        r = requests.get(url)
        print (r.url, r.status_code)
        plain_text = r.text 

        soup = BeautifulSoup (plain_text, "html.parser")

        for li in soup.findAll ('li', {'class': 'span1 people-list-item users-list-item tip-user'}):
            pk = li.get('data-user-pk')
            link = li.find_next('a').get('href')
            writeit.writerow([pk] + [link])

