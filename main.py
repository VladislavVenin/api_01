import requests


host = 'https://wttr.in'
places = ['san-francisco', 'london', 'svo', 'Череповец']
params = "?nTqmM&lang=ru"
for i in places:
    get = f"/{i}{params}"
    response = requests.get(host+get)
    print(response.text)
