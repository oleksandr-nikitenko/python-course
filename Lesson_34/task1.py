"""
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc.
"""
import requests


def get_content(page: str) -> str:
    return requests.get(page).text


def save_to_file(content: str) -> None:
    with open('robots.txt', 'w') as file:
        file.write(content)


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol'
    content = get_content(url)
    save_to_file(content)
