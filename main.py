import requests
import urllib.parse


def main():
    host = 'https://wttr.in'
    places = ['san francisco', 'london', 'svo', 'Череповец']
    keys = {
        "nTqmM": "",
        "lang": "ru",
    }
    for place in places:
        try:
            response = requests.get(urllib.parse.urljoin(host, place), params=keys)
        except requests.exceptions.ConnectionError:
            print("bad url")
            break
        if response.ok:
            print(response.text)


if __name__ == '__main__':
    main()


