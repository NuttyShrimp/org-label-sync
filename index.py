import json
import config
import requests

if (not config.token) :
    print("TOKEN NOT FOUND IN ENV")
    exit(1)

for project in config.projects:
    res = requests.get(f'https://api.github.com/repos/{config.org}/{project}/labels', headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {config.token}"
    })
    skippedLabels=[]
    if res.status_code != 200:
        print(f"Failed to get labels for {project}")
        exit(1)
    labels = res.json()

    for label in labels:
        for newLabel in config.newLabels:
            if newLabel['name'] == label['name']:
                skippedLabels.append(label['name'])

    for label in [l for l in labels if not l in skippedLabels]:
        res = requests.delete(f"https://api.github.com/repos/{config.org}/{project}/labels/{label['name']}", headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {config.token}"
        })
        if res.status_code >= 300:
            print(f"failed to delete {label['name']} to {project}", res.status_code, res.json())
        else:
            print(f'Removed {label["name"]} from {project}')


    for label in [l for l in config.newLabels if not l['name'] in skippedLabels]:
        res = requests.post(f"https://api.github.com/repos/{config.org}/{project}/labels", headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {config.token}"
        }, data=json.dumps(label))
        if res.status_code >= 300:
            print(f"failed to add {label['name']} to {project}", res.status_code, res.json())
        else:
            print(f'Added {label["name"]} to {project}')
    
    print(f"skipped {skippedLabels} because they already existed")

