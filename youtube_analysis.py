import streamlit as st
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

def youtube_fetch():
    # Load .env
    load_dotenv()
    api_key = os.getenv('YOUTUBE_API_KEY')

    # YouTube API Setup
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Video URL
    season3 = 'https://www.youtube.com/watch?v=yr7NbcCPYjk'
    season2='https://www.youtube.com/watch?v=SH7pWVYW1A0'
    season1 ='https://www.youtube.com/watch?v=3sVWSRKB7Vo'
    tsitp_seasons = [season1, season2, season3]
    vid_ids = []
    for season in tsitp_seasons:
        video_id = season.split('v=')[-1]
        vid_ids.append(video_id)

    # Fetch metadata
    video_details = {}
    for video_id in vid_ids:
        try:
            request = youtube.videos().list(
                part='snippet,statistics',
                id=video_id
            )
            response = request.execute()
            if response['items']:
                video_data = response['items'][0]
                snippet = video_data['snippet']
                stats = video_data.get('statistics', {})

                video_details[video_id] = {
                    'title': snippet['title'],
                    'channel': snippet['channelTitle'],
                    'description': snippet['description'],
                    'thumbnail_url': snippet['thumbnails']['high']['url'],
                    'published_at': snippet['publishedAt'],
                    'views': stats.get('viewCount', 'N/A'),
                    'likes': stats.get('likeCount', 'N/A'),
                    'comments': stats.get('commentCount', 'N/A'),
                }
            else:
                video_details[video_id] = {"error": f"No data found for video ID: {video_id}"}
        except Exception as e:
            video_details[video_id] = {"error": f"An error occurred: {e}"}
    return video_details