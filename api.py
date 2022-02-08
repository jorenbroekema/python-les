import requests
import json

response = requests.get('https://reqres.in/api/users?page=2')

if response.status_code == 200:
  data = response.json()['data']
  for user in data:
    print(user['first_name'])

dict = {
  'name': 'morpheus',
  'job': 'leader'
}

dictAsString = json.dumps(dict)

postResponse = requests.post('https://reqres.in/api/users', dictAsString)

print(postResponse)
if postResponse.status_code == 201:
  data = postResponse.json()
  print(data)