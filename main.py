import requests


def main():
    host = 'https://wttr.in'
    places = ['san-francisco', 'london', 'svo', 'Череповец']
    params = "?nTqmM&lang=ru"
    for i in places:
        get = f"/{i}{params}"
        response = requests.get(host+get)
        print(response.text)


if __name__ == '__main__':
    main()
