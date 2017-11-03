import requests, csv
from bs4 import BeautifulSoup


def writeFile (pk, amigo=" "):
	with open('users_filmow_friends.csv', 'a') as f:
	    writeit = csv.writer(f, delimiter=',', lineterminator='\n')
	    if(amigo == " "):
	    	writeit.writerow([pk])
	    else:
	    	writeit.writerow([pk] + [amigo])

def findFriends(pk, link): 
	for i in range (1,3):
		url = "https://filmow.com" + link + "amigos/?pagina=" + str(i)
		r = requests.get(url)
		print (r.url, r.status_code)
		plain_text = r.text
		soup = BeautifulSoup (plain_text, "html.parser")

		if(r.status_code == 200): #if (soup.find ('ul', {'class': 'row people-list users-list'})):
			for ul in soup.findAll ('ul', {'class': 'row people-list users-list'}):
				#Encontra usuarios sem amigos
				if(ul.find('li', {'class': 'alert'})):
					writeFile(pk)
				else:
					for li in ul.findAll('li', {'class': 'span1 people-list-item users-list-item tip-user'}):
						amigos = li.get('data-user-pk')
						writeFile(pk, amigos)
		
		else:
			break

with open('users_filmow.csv', 'r') as f:
	data = csv.reader(f, delimiter=',')
	for row in data:
		findFriends(row[0], row[1])