---
layout: cover
---

# Módulos externos

---

# `requests` - Realizar peticiones HTTP fácilmente.

````md magic-move
```bash
pip install requests
```
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```
```python
import json

import requests

# Simple GET request
print("=== Simple GET Request ===")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

# GET request with parameters
print("\n=== GET with Parameters ===")
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(f"URL: {response.url}")
print(f"Found {len(response.json())} posts")
```

```python
import json

import requests

# POST request with JSON data
print("\n=== POST Request ===")
new_post = {
    "title": "My New Post",
    "body": "This is the content of my post",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(f"Status Code: {response.status_code}")
print(f"Created post ID: {response.json()['id']}")

# Request with headers
print("\n=== Request with Headers ===")
headers = {
    "User-Agent": "My Python App 1.0",
    "Accept": "application/json"
}
response = requests.get("https://httpbin.org/headers", headers=headers)
print(f"Headers sent: {response.json()['headers']['User-Agent']}")
```
```python
import json

import requests

# Handle different response types
print("\n=== Different Response Types ===")
# JSON response
api_response = requests.get("https://api.github.com/users/vic-cortes")
user_data = api_response.json()
print(f"GitHub user: {user_data['name']} ({user_data['public_repos']} repos)")

text_response = requests.get("https://httpbin.org/robots.txt")
print(f"Text response: {text_response.text[:50]}...")

print("\n=== Error Handling ===")
try:
    response = requests.get("https://httpbin.org/status/404", timeout=5)
    response.raise_for_status()  # Raises exception for bad status codes
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
```
```python
import json

import requests

# Session for multiple requests
print("\n=== Using Session ===")
session = requests.Session()
session.headers.update({"User-Agent": "My Session App"})

# Make multiple requests with same session
urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/headers"
]

for url in urls:
    response = session.get(url)
    print(f"URL: {url} - Status: {response.status_code}")

session.close()
```
```python
import json

import requests

file_url = "https://httpbin.org/json"
response = requests.get(file_url)

if response.status_code == 200:
    with open("downloaded_data.json", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
```
````

---

# `beautifulsoup4` – Scraping de páginas web.

````md magic-move
```bash
pip install beautifulsoup4
```

```python
import requests
from bs4 import BeautifulSoup

# Get webpage content
print("=== Web Scraping with BeautifulSoup ===")
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all quotes
quotes = soup.find_all('div', class_='quote')
print(f"Found {len(quotes)} quotes on the page")
```
```python
# Extract specific information
print("\n=== Extracting Quotes ===")
for i, quote in enumerate(quotes[:3], 1):  # Show first 3 quotes
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
    
    print(f"Quote {i}:")
    print(f"  Text: {text}")
    print(f"  Author: {author}")
    print(f"  Tags: {', '.join(tags)}")
    print()

# Working with HTML structure
print("=== HTML Structure Navigation ===")
# Find title
title = soup.find('title').get_text()
print(f"Page title: {title}")
```

```python
# Find all links
links = soup.find_all('a')
print(f"Total links found: {len(links)}")

# Get specific links
nav_links = soup.find_all('a', class_='tag')
print(f"Tag links: {[link.get_text() for link in nav_links[:5]]}")

# Using CSS selectors
print("\n=== Using CSS Selectors ===")
# Select quotes using CSS selector
css_quotes = soup.select('div.quote')
print(f"Quotes found with CSS selector: {len(css_quotes)}")

# Select author names
authors = soup.select('small.author')
author_names = [author.get_text() for author in authors]
print(f"Authors: {set(author_names)}")  # Use set to remove duplicates
```
```python
# Working with attributes
print("\n=== Working with Attributes ===")
# Get href attributes from links
quote_links = soup.find_all('a', string='(about)')
for link in quote_links[:3]:
    href = link.get('href')
    print(f"Author link: {href}")
```

```python
# Parsing HTML string directly
print("\n=== Parsing HTML String ===")
html_string = """
<div class="product">
    <h2>Laptop</h2>
    <p class="price">$999.99</p>
    <p class="description">High-performance laptop</p>
    <ul class="features">
        <li>16GB RAM</li>
        <li>512GB SSD</li>
        <li>Intel i7</li>
    </ul>
</div>
"""

product_soup = BeautifulSoup(html_string, 'html.parser')
product_name = product_soup.find('h2').get_text()
price = product_soup.find('p', class_='price').get_text()
features = [li.get_text() for li in product_soup.find_all('li')]

print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Features: {', '.join(features)}")
```
```python
# Error handling
try:
    # Try to find an element that doesn't exist
    nonexistent = soup.find('div', class_='nonexistent')
    if nonexistent:
        print(nonexistent.get_text())
    else:
        print("Element not found - returned None")
        
    # Safe way to get text
    safe_text = soup.find('div', class_='nonexistent')
    if safe_text:
        print(safe_text.get_text())
    else:
        print("Using safe check - element doesn't exist")
        
except AttributeError as e:
    print(f"AttributeError: {e}")

# Pretty print HTML
sample_html = "<div><p>Hello</p><span>World</span></div>"
pretty_soup = BeautifulSoup(sample_html, 'html.parser')
print("Original:", sample_html)
print("Pretty printed:")
print(pretty_soup.prettify())
```
````

---

# `flask` - Crear aplicaciones web livianas.

````md magic-move
```bash
pip install flask
```
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola desde Flask!"

# app.run()  # Solo ejecutar si corres la app
```
````

