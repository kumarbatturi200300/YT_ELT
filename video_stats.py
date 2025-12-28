import requests
import json
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path = "./.env")

API_KEY = os.getenv("API_KEY")

def get_uploads_playlist_id():
    try:
        CHANNEL_HANDLE = "MrBeast"
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'
        response = requests.get(url)
        #print(response)
        response.raise_for_status()
        data = response.json()
        #print(json.dumps(data, indent =  4))
        channel_playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return channel_playlist_id
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == '__main__':
    print(get_uploads_playlist_id())