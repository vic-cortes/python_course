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

# Download file example
print("\n=== Download File ===")
file_url = "https://httpbin.org/json"
response = requests.get(file_url)
if response.status_code == 200:
    with open("downloaded_data.json", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
```
````