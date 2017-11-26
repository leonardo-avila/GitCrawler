from github import Github
import requests, csv, json

#Limitando tanto os usuários quanto os repositórios, devido ao limite de requisições da API do GitHub.
#h = Github()
#repo = h.get_user("Microsoft").get_repo("vscode").contributors_url
r = requests.get("https://api.github.com/repos/Microsoft/vscode/contributors?page=1&per_page=15")
with open("crawlerContributorsVSCODE", 'w') as f:
    writeit = csv.writer(f, delimiter=',', lineterminator='\n')
    repoJSON = json.loads(r.text)
    for item in repoJSON:
        pk = item['id']
        name = item['login']
        output = str(pk) + "," + name
        writeit.writerow([pk] + [name])
        print(output)
