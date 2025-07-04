import requests
import time

my_image = 'for_homework.jpg'
base_url = 'http://127.0.0.1:8080'

def upload_image():
    with open(my_image, 'rb') as image:
        files = {'image': image}
        response = requests.post(url=f'{base_url}/upload', files=files)

    if response.status_code == 201:
        image_url = response.json().get('image_url')
        print(f"Image upload ✅\nStatus code: {response.status_code}\nImage URL: {image_url}\n{'-'*80}")
        return image_url
    else:
        print(f"Error while loading⚠️\nStatus code: {response.status_code}\n{'-'*80}")
        return None


def get_image_url(filename):
    headers = {'Content-Type': 'text'}
    response = requests.get(f'http://127.0.0.1:8080/image/{filename}', headers=headers)

    if response.status_code == 200:
        print(f"Link received ✅\nStatus code: {response.status_code}\n"
              f"Image URL in JSON format: {response.json().get('image_url')}\n{'-'*80}")
    else:
        print(f"Error retrieving URL⚠️\nStatus code: {response.status_code}\n{'-'*80}")


def delete_image(filename):
    response = requests.delete(f'{base_url}/delete/{filename}')

    if response.status_code == 200:
        print(f"Image deleted ✅\nStatus code: {response.status_code}\nJSON message: {response.json()}")
    else:
        print(f"Error while deleting⚠️\nStatus code: {response.status_code}")

if __name__ == '__main__':
    uploaded_url = upload_image()
    time.sleep(1)
    if uploaded_url:
        filename = my_image
        get_image_url(filename)
        time.sleep(1)
        delete_image(filename)