import requests
import json
from bs4 import BeautifulSoup

def scrapeProfessors():

    # Define url and Headers in order to fake a true browser request
    professorsUrl = "http://www.disim.univaq.it/didattica/content.php?tipo=3&ordine=1&chiave=0&pid=25&did=8&lid=it&frmRicercaNome=&frmRicercaCognome=&frmRicercaLaurea=1&action_search=Filtra"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    # Make the request to the url passing the headers.
    request = requests.get(professorsUrl, headers=headers)

    # Check the status code of the response to make sure the request went well
    if request.status_code != 200:
        print("Error! Status "+request.status_code)
        return

    # Pass the whole cached page in 'request' to BeautifulSoup and get the only existent table in the page
    professorsTable = BeautifulSoup(request.text, "html.parser").find("table")

    # Array to write into the json file (will be transformed into an array of dictionaries)
    scrapedProfessors = []

    # These cells are a landmark in the scraping because they have the unique attribute 'colspan=2'
    firstsTD = professorsTable.find_all(colspan='2')
    for nameCell in firstsTD:
        # Scrape the nameCell
        name = nameCell.find("a").text
        # Scrape the phone
        phone = nameCell.find_next_sibling().text
        # Scrape the e-mail (PROBLEM HERE)
        email = nameCell.find_next_sibling().find_next_sibling().get_text(".")
        # Scrape the courses
        courses = nameCell.find_next_sibling().find_next_sibling().find_next_sibling().get_text(" ").replace('\n', '').replace('\u00a0', '')

        # Finally it appends a dictionary for every element scraped
        scrapedProfessors.append( {"nome": name, "telefono": phone, "e-mail": email, "corsi": courses, "ufficio": "0"  } )

    # Write everything to a json file
    with open('../json/professors.json', 'w') as fp:
        json.dump(scrapedProfessors, fp)

if __name__ == "__main__":
    scrapeProfessors()
