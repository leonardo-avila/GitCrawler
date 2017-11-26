import csv, requests, json

with open('crawlerContributorsVSCODE', 'r') as f:
    data = csv.reader(f)
    for row in data:
        print(len(row))
        r = requests.get("https://api.github.com/users/" + row[1] + "/repos?page=1&per_page=5")
        url = json.loads(r.text)
        with open('crawlerGetRepos','a') as wr:
            writeit = csv.writer(wr, delimiter=',', lineterminator="\n")
            for item in url:
                repos = str(item['full_name'])
                l = requests.get("https://api.github.com/users/" + repos +"/languages")
                lurl = json.loads(l.text)
                for i in lurl:
                    lang = str([i])
                    writeit.writerow([lang] + [row[1]])

