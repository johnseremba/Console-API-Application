import requests


def main():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.content)

if __name__ == '__main__':
    main()