import requests


def send_request():
    res = requests.get("https://api.restful-api.dev/objects?id=3&id=5&id=10")
    return res.json()


if __name__ == "__main__":
    result = send_request()
    for record in result:
        print(record)
