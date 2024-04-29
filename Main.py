




import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/maps/search/architecture+firms+in+hyd/@17.4260058,78.3563414,12z/data=!3m1!4b1?entry=ttu"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

restaurants = soup.find_all("div", class_="section-result-details-container")

for restaurant in restaurants:
    name = restaurant.find("h3", class_="section-result-title").text.strip()
    address = restaurant.find("span", class_="section-result-location").text.strip()
    
    print("Name:", name)
    print("Address:", address)
    print("-" * 50)








