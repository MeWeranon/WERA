import requests
api_url = 'https://jsonplaceholder.typicode.com/todo/1'

response = requests.get(api_url)

print(reponse.jason())
print(reponse.status_code())