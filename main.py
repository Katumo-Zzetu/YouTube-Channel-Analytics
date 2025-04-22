from googleapiclient.discovery import build
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv  

# Load variables from .env
load_dotenv()  



def get_youtube_api():
    api_key = os.environ.get('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube

def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()

    channel =  response['items'][0]
    
    channel_data = {
        'channel_name': channel['snippet']['title'],
        'subscribers': channel['statistics']['subscriberCount'],
        'views': channel['statistics']['viewCount'],
        'total_videos': channel['statistics']['videoCount'],
        'playlist_id': channel['contentDetails']['relatedPlaylists']['uploads'],
        'extraction_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    return channel_data

# --- EXECUTE THE SCRIPT ---
if __name__ == "__main__":
    # Use actual channel ID for @V3_ent
    channel_id='UCS-zdr8_cuUGNvOhLKUkjZQ'
    
    youtube = get_youtube_api()
    stats = get_channel_stats(youtube, channel_id)
    
    # Print results nicely
    print("YouTube Channel Stats:\n")
    for key, value in stats.items():
        print(f"{key}: {value}")

