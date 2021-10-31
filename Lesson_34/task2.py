"""
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
"""
import requests
import json
import time


def get_json(url) -> dict:
    resp = requests.get(url)
    if resp.ok:
        return resp.json()


def get_comments(data: dict) -> dict:
    comments = {'comments': []}
    for comment in data.get('data'):
        comments.get('comments').append({
            'author': comment.get('author'),
            'body': comment.get('body'),
            'created_date': time.ctime(comment.get('created_utc'))
        })
    return comments


def create_json_file(comments: dict) -> None:
    with open('comments.json', 'w') as file:
        json.dump(comments, file, indent=4)


if __name__ == '__main__':
    data = get_json('https://api.pushshift.io/reddit/comment/search/')
    create_json_file(get_comments(data))