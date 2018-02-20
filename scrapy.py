from lxml import html
import requests
import os
import time
import re


URL = "https://johncrane.gitbooks.io/ninety-nine-elm-problems/content/"
ELM_FOLDER = './elmproblems/'
REGEX = "(?:/)(.\d{2}.?)(?:\.html)"


def start():
    urls = get_urls(URL)
    html.absolute_import
    for url in urls:
        print(url)
        name = re.search(REGEX, url).group(1)
        tree_detail = scrap_page(url)
        parse_detail(tree_detail, name, ELM_FOLDER)
        time.sleep(0.5)


def parse_detail(tree, name, folder):
    code = tree.xpath("(//pre/code)[last()]")[0]
    filename = name + '.elm'
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, filename)
    file = open(filepath, "w")
    file.write(code.text_content())
    file.close()


def get_urls(url):
    tree = scrap_page(URL)
    # All the problems' links
    linksTag = tree.xpath('//li[@data-level=1.4]/*/li/a')
    return [url + link.attrib['href'] for link in linksTag]


def scrap_page(url):
    page = requests.get(url)
    return html.fromstring(page.content)


if __name__ == '__main__':
    start()
