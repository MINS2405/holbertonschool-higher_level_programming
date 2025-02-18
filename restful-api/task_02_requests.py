import requests
import csv


# Récupère et imprime les titres des posts
def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post['title'])


# Récupère les posts et les enregistre dans un fichier CSV
def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=['id', 'title', 'body']
            )
            writer.writeheader()
            writer.writerows(posts)
