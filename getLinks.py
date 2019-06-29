from bs4 import BeautifulSoup
import requests 

def extractLinks(html_doc):
    links = []
    html_doc = requests.get(html_doc)
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
            # notWeird = (link['class'] != "box-BLP_unsourced_section plainlinks metadata ambox ambox-content ambox-BLP_unsourced")
            # notReferences = (link['class'] != "reflist columns references-column-width")
            notCitation = not ("cite_note" in link)
            
            if notCitation:
                goodLink = True

        if goodLink:
            wikiPage = "/wiki/" in link
            if wikiPage:
                links.append(link)
                print(link)

    return links

extractLinks("https://en.wikipedia.org/wiki/Kevin_Bacon")
