import requests
from bs4 import BeautifulSoup

def print_character_grid(doc_url):
    # Fetch the content of the Google Doc
    response = requests.get(doc_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the document. Status code: {response.status_code}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all tables in the document
    tables = soup.find_all('table')
    if not tables:
        print("No tables found in the document.")
        return

    # Assuming the first table contains the grid
    table = tables[0]

    # Iterate over each row in the table
    for row in table.find_all('tr'):
        # Extract text from each cell in the row
        cells = row.find_all(['td', 'th'])
        row_text = ''.join(cell.get_text(strip=True) for cell in cells)
        print(row_text)

# Example usage
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
print_character_grid(doc_url)
