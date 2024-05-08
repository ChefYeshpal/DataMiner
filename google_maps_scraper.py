import requests
from bs4 import BeautifulSoup

def scrape_google_maps(url):
    # Send GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information from the parsed HTML
        name_tag = soup.find('div', class_='x3AX1-LfntMc-header-title-title')
        name = name_tag.text.strip() if name_tag else None

        # Update the remaining extraction logic similarly
        
        # Print the scraped data
        print("Name:", name)
        # Print other extracted data
        
    else:
        print("Failed to fetch data")

# Example URL of the Google Maps page
url = "https://www.google.com/maps/search/architecture+firms+in+hyd/@17.4485515,78.3536946,12z/data=!3m1!4b1?entry=ttu"

# Call the function to scrape data from the URL
scrape_google_maps(url)

