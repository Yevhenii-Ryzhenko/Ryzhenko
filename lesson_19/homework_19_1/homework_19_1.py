import json
import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    image_urls = [photo["img_src"] for photo in data["photos"]]
    for i, link in enumerate(image_urls, start=1):
        image_response = requests.get(link)
        if image_response.status_code == 200:
            with open(f'mars_photo_{i}.jpg', 'wb') as file:
                file.write(image_response.content)
            print(f"Saved: mars_photo_{i}.jpg")
        else:
            print(f"Failed to download {link}")
else:
    print('Request error:', response.status_code)