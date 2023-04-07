import os
import requests
from bs4 import BeautifulSoup


def download_images(topic, num_images, output_dir):
    url = f"https://unsplash.com/s/photos/{topic}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # print('response.text=', response.text)

    img_tags = soup.find_all("img", {"class": "tB6UZ a5VGX"})
    print(len(img_tags))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    downloaded = 0
    for img_tag in img_tags:
        img_url = img_tag["src"]
        img_data = requests.get(img_url).content
        filename = os.path.join(output_dir, f"{downloaded }.jpg")

        with open(filename, "wb") as f:
            f.write(img_data)
            print(f"Downloaded {filename}")

        downloaded += 1
        if downloaded >= num_images:
            break


if __name__ == "__main__":
    # topic = 'music'
    topic = "embroidery"
    num_images = 23
    output_dir = "downloaded_img"

    download_images(topic, num_images, output_dir)
