import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(r)
    print(type(r))

    categories = r.json()
    for category in categories:
        print(category['name'])