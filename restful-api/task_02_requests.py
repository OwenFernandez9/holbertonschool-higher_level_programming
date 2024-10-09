#!/usr/bin/python3
import requests


def fetch_and_print_posts():
    posts = requests.get("https://jsonplaceholder.typicode.com/posts/")
    print(posts.status_code)

    if posts.status_code == 200:
        p = posts.json()

        for post in p:
            print(post['title'])


def fetch_and_save_posts():
    posts = requests.get("https://jsonplaceholder.typicode.com/posts/")
    if posts.status_code == 200:
        p = posts.json

    estruct_posts = []

    for post in p:
        new_post = {
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        }
        estruct_posts.append(new_post)

    with open('posts.csv' 'w') as file:
        writer = csv.DictWriter(file, filednames=['id', 'title', 'body'])
        writer.writerheader()
        writer.writerows(estruct_posts)
