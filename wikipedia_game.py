import requests

from collections import deque

def get_links(url):
    """This method gets the links contained in the body of the given url.
    The URL is assumed to be a wikipedia page. This method returns a list of links as strings.
    """
    pass

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
        links_on_page = get_links(current_url)
        if not links_on_page: continue
        if end_url in links_on_page:
            prev_link = end_url
            while prev_link:
                prev_link = visited_link_dict[prev_link]
                link_path.append(prev_link)
            return link_path
        for url in links_on_page:
            # Repeats are disallowed since they are necessarily a longer path
            if url not in visited_link_dict.keys():
                visited_link_dict[url] = current_url
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
    start_url = "https://en.wikipedia.org/wiki/Nicole_Kassell"
    shortest_path = run_bfs(kevin_bacon_url, start_url)
    print("Shortest path from", get_page_title(start_url), "to",
            get_page_title(kevin_bacon_url) + ":\n" + str(shortest_path))
