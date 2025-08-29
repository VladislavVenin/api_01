import requests
import urllib.parse


def main():
    host = input("Enter url(Leave the field blank to search https://wttr.in.): ") or "https://wttr.in"
    places = input("Enter places separated by space: ").split()
    keys = {}
    while True:
        key = input("Enter a key (or press Enter to finish): ")
        if key == "":
            break
        keys[key] = input(f"Enter the value for '{key}': ")

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
