import streamlit as st
from dotenv import load_dotenv
import pandas as pd
import os
import plotly.express as px
from googleapiclient.discovery import build
import youtube_analysis 
import spotify_analysis

video_details = youtube_analysis.youtube_fetch()

# Streamlit UI
st.set_page_config(layout='wide')
st.title("The Summer I Turned Pretty Dashboard")

df = spotify_analysis.trailer_songs_fetch('data/spotify_tracks.csv')
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        spotify_analysis.team_conrad_or_jerimiah(df)
    with col2:
        spotify_analysis.discover_taylor(df)

# for video_id, details in video_details.items():
    # st.subheader(f"Video ID: {video_id}")
    # if "error" in details:
    #     st.error(details['error'])
    # else:
    #     st.image(details['thumbnail_url'], caption=details['title'])
    #     st.subheader(f"**Title:** {details['title']}")
        # st.write(f"**Channel:** {details['channel']}")
        # st.write(f"**Published At:** {details['published_at']}")
        # st.write(f"**Views:** {details['views']}")
        # st.write(f"**Likes:** {details['likes']}")
        # st.write(f"**Comments:** {details['comments']}")
        # with st.expander("Description"):
        #     st.write(details['description'])
        # st.markdown("---")
# st.image(thumbnail_url, width=640)
# st.header(title)
# st.subheader(f"by {channel}")
# st.write(f"Published at: {published_at}")

# col1, col2, col3 = st.columns(3)
# col1.metric("Views", f"{int(views):,}")
# col2.metric("Likes", f"{int(likes):,}")
# col3.metric("Comments", f"{int(comments):,}")

# with st.expander("Description"):
#     st.write(description)

# st.video(video_url)

# Prepare data for the chart
# Prepare data for the chart in a long format
chart_data = []
for video_id, details in video_details.items():
    if "error" not in details:
        chart_data.append({'title': details['title'], 'metric': 'views', 'count': int(details['views'])})
        chart_data.append({'title': details['title'], 'metric': 'likes', 'count': int(details['likes'])})
if chart_data:
    df = pd.DataFrame(chart_data)
    # Find the maximum count value
    max_count = df['count'].max()

    # Create the grouped bar chart
    fig = px.bar(df,
                    y='title',  # Swapped x and y
                    x='count',  # Swapped x and y
                    color='metric',
                    barmode='group',
                    title='Current Views and Likes Comparison for TSITP Official Teaser Trailers',
                    labels={'title': 'Video Title', 'count': 'Count', 'metric': 'Metric'}
                    )

    # Update the layout to set the x-axis range (now x-axis)
    fig.update_layout(
        xaxis=dict(  # Changed to xaxis
            range=[0, max_count]
        )
    )
    st.plotly_chart(fig)
else:
    st.warning("No valid video data available to create the chart.")