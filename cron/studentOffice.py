import requests
import json
from bs4 import BeautifulSoup

def scrapeProfessors():

    # Define url and Headers in order to fake a true browser request
    officeInfoUrl = "http://www.univaq.it/section.php?id=607"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    # Make the request to the url passing the headers.
    request = requests.get(officeInfoUrl, headers=headers)

    # Check the status code of the response to make sure the request went well
    if request.status_code != 200:
        print("Error! Status "+request.status_code)
        return

    # Pass the whole cached page in 'request' to BeautifulSoup and get the only existent table in the page
    infoTable = BeautifulSoup(request.text, "html.parser").find(string="AREA SCIENTIFICA").parent.parent.find_next_sibling()

    # Array to write into the json file (will be transformed into an array of dictionaries)
    scrapedInfo = []

    print(infoTable)

    # Write everything to a json file
    with open('../json/studentOffice.json', 'w') as fp:
        json.dump(scrapedInfo, fp)

if __name__ == "__main__":
    scrapeProfessors()
