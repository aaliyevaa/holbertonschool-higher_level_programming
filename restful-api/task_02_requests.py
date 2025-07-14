#!/usr/bin/env python3
"""Ftech posts from JSONplaceholder"""
import requests
import csv


def fetch_and_print_posts():
    """ Fetch and print titles of all posts"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])
    else:
        print("Failed to fetch posts")

    
def fetch_and_save_posts():
    """Fetch and save posts and save them to CSV file"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in data]
        with open('posts.csv.', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['id','title','body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)

        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()

