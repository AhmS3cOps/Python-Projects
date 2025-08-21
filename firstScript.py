import requests
from bs4 import BeautifulSoup

print("Starting the script...")

url ='https://news.ycombinator.com/'
print(f"fetching data from: {url}")

response = requests.get(url)
print(f"Received response with status code: {response.status_code}")


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Successfully parsed the HTML.")

    #Find all <a> tags and print their href attrbutes
    links = soup.find_all('a')
    print(f"Found {len(links)} links.")


    for index, link in enumerate(links, start=1):
        href = link.get('href')
        if href and 'item?id=' in href:
            print(f"{index}. {link.text} - {href}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")