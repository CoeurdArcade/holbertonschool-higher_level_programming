#!/usr/bin/python3
import requests
import csv

def fetch_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return None

def fetch_and_print_posts():
    posts = fetch_posts()
    if posts:
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    posts = fetch_posts()
    if posts:
        structured_posts = []

        for post in posts:
            new_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(new_post)

        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_posts)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
