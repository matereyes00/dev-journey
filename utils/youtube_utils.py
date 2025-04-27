import streamlit as st
import pandas as pd
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
import plotly.express as px


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

def show_latest_trailer(video_details):
    for video_id, details in video_details.items():
        if 'Season 3' in details['title']:
            st.write(f"{details['title']}")
            video_url = None
            if "https://youtu.be/" in details['description']:
                start_index = details['description'].find("https://youtu.be/")
                end_index = details['description'].find(" ", start_index)
                video_url = details['description'][start_index:end_index if end_index != -1 else None]

            # If a video URL was found, create a clickable thumbnail
            if video_url:
                st.markdown(f"""
                    <a href="{video_url}" target="_blank">
                        <img src="{details['thumbnail_url']}" alt="{details['title']}" style="width: 100%; max-width: 400px; border-radius: 8px;">
                    </a>
                """, unsafe_allow_html=True)
            else:
                st.write("No video URL found.")

def generate_likes_and_views_chart(video_details):
    # Prepare data for the chart in a long format
    chart_data = []
    for video_id, details in video_details.items():
        if "error" not in details:
            chart_data.append({'title': details['title'], 'metric': 'views', 'count': int(details['views'])})
            chart_data.append({'title': details['title'], 'metric': 'likes', 'count': int(details['likes'])})
    if chart_data:
        df = pd.DataFrame(chart_data)

        # Add a radio button for metric selection
        metric_choice = st.radio(
            "Select metric to display:",
            ('views', 'likes'),
            index=0,  # Default to 'views'
        )

        # Filter the DataFrame based on the selected metric
        df_filtered = df[df['metric'] == metric_choice]

        # Find the maximum count value for the selected metric
        max_count = df_filtered['count'].max() * 1.1

        fig = px.bar(df_filtered,
                        y='title',  # Swapped x and y
                        x='count',  # Swapped x and y
                        color='metric',
                        barmode='group',
                        title='Current Views and Likes Comparison for TSITP Official Teaser Trailers',
                        labels={'title': 'Video Title', 'count': 'Count', 'metric': 'Metric'}
                    )

        # Update the layout to set the x-axis range and title font
        fig.update_layout(
            xaxis=dict(
                range=[0, max_count],
                title_font=dict(size=16),
                tickfont=dict(size=12),
                title='Count'
            ),
            yaxis=dict(
                title='Video Title',
                title_font=dict(size=16),
                tickfont=dict(size=12),
                color="#2d3c24",
            ),
            font_family="Helvetica",
            title_font=dict(size=30, color="#a23e1a"),
            plot_bgcolor="#f0f5f1",
            legend=dict(font=dict(size=12), title=dict(font=dict(size=16)))
        )

        st.plotly_chart(fig)
    else:
        st.warning("No valid video data available to create the chart.")


def get_team(tweet):
    if not isinstance(tweet, str):
        return
    tweet = tweet.lower()

    conrad_keywords = ['bonrad', 'conrad', 'belly and conrad', 'conrad and belly', 'conrad fisher', 'team conrad', 'i love conrad', 'conrad is the one', 'go conrad' 'connie', 'red']
    jeremiah_keywords = ['team jeremiah', 'jelly', 'jellyfish', 'jeremiah', 'belly and jeremiah', 'jeremiah and belly', 'jeremiah fisher', 'team jeremiah', 'i love jeremiah', 'jeremiah is better', 'go jeremiah', 'daylight', 'team jer', 'team jere']

    # Check for Conrad keywords
    if any(keyword in tweet for keyword in conrad_keywords):
        return 'Team Conrad'

    # Check for Jeremiah keywords
    if any(keyword in tweet for keyword in jeremiah_keywords):
        return 'Team Jeremiah'


        
def team_conrad_or_jeremiah(df):
    # st.dataframe(df)
    df['team'] = df['cleaned'].apply(get_team)
    team_counts = df['team'].value_counts().reset_index()
    team_counts.columns = ['team', 'count']

    color_map = {
        'Team Conrad': '#ADD3D3',   # Light Teal
        'Team Jeremiah': '#CB8F40', # Warm Brown/Orange
        # 'Other': '#D3D3D3'          # Light Gray for "Other"
    }

    fig = px.bar(
        team_counts,
        x='team',
        y='count',
        color='team',
        color_discrete_map=color_map,
        title="Team Conrad vs Team Jeremiah Mentions"
    )

    st.plotly_chart(fig)

def sentiment_analysis(df):
    # Group the data by the 'emotion' column
    # st.dataframe(df)
    emotion_groups = df.groupby('emotion').agg(
        comment_count=('raw_comment', 'size'),  # Count the number of comments for each emotion
        average_score=('score', 'mean')  # Average score for each emotion group
    ).reset_index()

    # Sort by the number of comments in descending order
    emotion_groups = emotion_groups.sort_values(by='comment_count', ascending=False)
    # Remove irrelevant emotions
    emotions_to_remove = ['empty', 'neutral', '😱']
    emotion_groups = emotion_groups[~emotion_groups['emotion'].isin(emotions_to_remove)]

    # Display the grouped data
    emotion_options = emotion_groups['emotion'].tolist()
    selected_emotion = st.selectbox("Select an Emotion", emotion_options)

    # Filter the comments based on the selected emotion
    selected_comments = df[df['emotion'] == selected_emotion]

    # Display the comments for the selected emotion
    st.subheader(f"Comments for '{selected_emotion.capitalize()}' Emotion")

    # Show the raw comments
    st.write(selected_comments[['raw_comment']])
    # Optional: You can display the average score for that emotion
    average_score = selected_comments['score'].mean()
    st.write(f"Average Sentiment Score for '{selected_emotion.capitalize()}': {average_score:.2f}")
    # Define the color palette
    # colors = [
    #     '#ADD3D3',  # Soft Blue (like the ocean)
    #     '#CB8F40',  # Sandy Brown
    #     '#F0F5F1',  # Off-White (like seafoam or light fabrics)
    #     '#E3856B',  # Soft Coral/Peach (sunset hues)
    #     '#A7C957',  # Light Green (coastal foliage)
    #     '#F2AE72',  # Pale Orange (another sunset shade)
    #     '#D4A373',  # Tan (beach sand)
    #     '#9BC1BC',  # Seafoam Green
    #     # '#F9E79F',  # Pale Yellow (sunshine)
    #     # '#DBBADD'   # Lilac/Lavender (soft summer flowers)
    # ]
    st.bar_chart(emotion_groups.set_index('emotion')['comment_count'], color="#DBBADD")