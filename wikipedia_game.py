import requests
import validators
import time

from bs4 import BeautifulSoup
from collections import deque

def get_links_from(url):
    """This method gets the links contained in the body of the given url.
    The URL is assumed to be a wikipedia page. This method returns a list of links as strings.
    """
    links = []
    html_doc = requests.get(url)
    html_doc = html_doc.content
    # print(html_doc)
    soup = BeautifulSoup(html_doc, 'html.parser')
    for link in soup.find_all('a'):
        link = link.get('href')
        # make sure it is not a div of class: "reflist columns references-column-width"
        # make sure it is not a table of class: "box-BLP_unsourced_section plainlinks metadata ambox ambox-content ambox-BLP_unsourced"
        goodLink = False

        # if any of these conditions are false, then it is not a 'good link'
        if link:
            notPortal = ("Portal" not in link and "Special" not in link and "Wikipedia" not in link and "Help" not in link and "File:" not in link)
            notWeird = ("box-BLP_unsourced_section plainlinks metadata ambox ambox-content ambox-BLP_unsourced" not in link and "Talk" not in link and "Category" not in link)
            notReferences = ("reflist columns references-column-width" not in link and "wikimedia.org" not in link)
            notCitation = not ("cite_note" in link)
            notOtherWebsite = not ("https" in link)
            if notWeird and notReferences and notCitation and notOtherWebsite and notPortal:
                goodLink = True

        if goodLink:
            wikiPage = "/wiki/" in link
            if wikiPage:
                link = "https://en.wikipedia.org" + link

    return links

def get_links_to(url):
    """Uses Wikipedia's What Links Here tool to return all the pages that link to the
    inputted Wikipedia URL.
    """
    url_base = "https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/"
    tail = url.split("/")[-1]
    r = requests.get(url_base + tail + "&limit=10000")
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    all_links = soup.find_all('a')
    links = []
    for link in all_links:
        href = link.get("href")
        if href and href.startswith("/wiki"):
            links.append(href)
    return links

def run_bfs(end_url, start_url):
    """Run BFS to find the shortest path from start_url to end_url by clicking
    links on the page. This method returns a list of links one needs to click to get
    from start_url to end_url. An empty list is returned if there is no path between
    start_url and end_url.
    """
    link_queue = deque([start_url])
    link_path = [start_url]
    # Keep track of previous links to output path to end_url
    visited_link_dict = {start_url: None}
    while link_queue:
        current_url = link_queue.popleft()
        links_on_page = get_links_from(current_url)
        if not links_on_page: continue
        if end_url in links_on_page:
            prev_link = current_url
            while visited_link_dict[prev_link]:
                link_path.append(prev_link)
                prev_link = visited_link_dict[prev_link]
            link_path.append(end_url)
            return link_path
        for url in links_on_page:
            # Repeats are disallowed since they are necessarily a longer path
            print(url)
            if url not in visited_link_dict.keys():
                visited_link_dict[url] = current_url #pages that link to the url
                link_queue.append(url)
    return []

def get_page_title(url):
    """Returns the title of the Wikipedia page based on the given url.
    """
    tail = url.split("/")[-1]
    tail = tail.replace("_", " ")
    return tail

if __name__ == "__main__":
    kevin_bacon_url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
<<<<<<< HEAD
    start_url = "https://en.wikipedia.org/wiki/Arabian_Sea"
    shortest_path = run_bfs(kevin_bacon_url, start_url)
    print("Shortest path from", get_page_title(start_url), "to",
            get_page_title(kevin_bacon_url) + ":\n" + str(shortest_path))
=======
    start_url = "https://en.wikipedia.org/wiki/Hollywood"
    #shortest_path = run_bfs(kevin_bacon_url, start_url)
    #print("Shortest path from", get_page_title(start_url), "to",
    #        get_page_title(kevin_bacon_url) + ":\n" + str(shortest_path))
    print(get_links_to(kevin_bacon_url))
>>>>>>> 3572aa5... Add links_to function
