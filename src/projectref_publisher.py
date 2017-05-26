import requests
import json

#reading configurations
with open('config.json') as conf_file:    
    conf = json.load(conf_file)

#reading temporary export
introtext = open('ref.htm','r').read()

#defining api-call
headers ={'X-Dreamfactory-API-Key': conf['api-key-lts']}
data={"introtext": introtext}
url="https://api.lts.no/api/v2/db-ltsnohgk_joom/_table/mk1_content/16"

#executing patch command
response = requests.patch(url=url, headers=headers, data=data)

#printing status-code of the response
print(str(response.status_code))
