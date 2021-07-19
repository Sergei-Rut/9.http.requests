from pprint import pprint
import requests


TOKEN = "AQAAAAAVN4muAADLW7NOo_YBik4WjlBSKkxsz7M"

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, disk_file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = (requests.get(upload_url, headers=headers, params=params)).json()
        href = response.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return print('Success')


if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    uploader = ya.upload(disk_file_path="test/test.txt", filename="test.txt")
