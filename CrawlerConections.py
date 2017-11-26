import csv, requests, json
#Limitando o número de repositórios devido ao limite de requisições da API do GitHub.

with open('crawlerContributorsVSCODE', 'r') as f:
    data = csv.reader(f)
    for row in data:
        print(len(row))
        r = requests.get("https://api.github.com/users/" + row[1] + "/repos?page=1&per_page=5")
        url = json.loads(r.text)
        with open('crawlerGetRepos','w') as wr:
            writeit = csv.writer(wr, delimiter=',', lineterminator="\n")
            for item in url:
                repos = str(item['url'])
                print(repos)
                l = requests.get(repos +"/languages")
                lurl = json.loads(l.text)
                print(lurl)
                for i in lurl:
                    lang = i
                    writeit.writerow([lang] + [row[1]])

