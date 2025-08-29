import requests
import urllib.parse
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-hs', "--host",
                        type=str,
                        help="url",
                        default="https://wttr.in")
    parser.add_argument('-p', "--places",
                        type=str,
                        help="places",
                        nargs='*',
                        default=['svo'])
    parser.add_argument('-k', "--keys",
                        type=str,
                        help="key=value pairs",
                        nargs='*')
    args = parser.parse_args()
    host = args.host
    places = args.places
    keys = args.keys
    if keys:
        keys = dict(item.split('=') for item in keys)

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

