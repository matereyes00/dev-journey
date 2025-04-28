import streamlit as st
import pandas as pd
import spotify_analysis

import utils.books_utils as books_config
# import utils.spotify_utils as spotify_config
import utils.youtube_utils as youtube_config
import utils.tv_utils as tv_config
st.set_page_config(layout='wide')

st.markdown("""
    <style>
    body {
        background-color: #FAE3D9; 
    }
    </style>
""", unsafe_allow_html=True)

video_details = youtube_config.youtube_fetch()
tweets_df = pd.read_csv('data/twitter_sentiment_analysis.csv')
yt_sentiment = pd.read_csv('data/youtube_sentiment_analysis.csv')
episodes_df = pd.read_csv('data/the_summer_i_turned_pretty_episodes.csv')
imdb_reviews_df = pd.read_csv('data/cleaned_reviews.csv')

st.markdown(
    """
    <h1 style='color: #D4A373;'>🌸The Summer I Turned Pretty Dashboard🐚</h1>
    """,
    unsafe_allow_html=True
)
st.subheader("By: Matê 💻")
col1, col2 = st.columns([1, 3])  # col1 will be 3 times wider than col2
with col1:
    st.markdown(
    """
    <h1 style='color:#F2AE72;'>📼 Have you seen the latest trailer?</h1>
    """, unsafe_allow_html=True)

    youtube_config.show_latest_trailer(video_details)
with col2:
    st.markdown(
    """
    <h1 style='color:#F2AE72;'>📼 How are we feeling?</h1>
    """, unsafe_allow_html=True)
    youtube_config.sentiment_analysis(yt_sentiment)

df = spotify_analysis.trailer_songs_fetch('data/spotify_tracks.csv')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        spotify_analysis.team_conrad_or_jerimiah(df)
        st.markdown(
            """ 
                <h2 style='color:#CB8F40;'>Youtube</h2>
            """, unsafe_allow_html=True)
        youtube_config.team_conrad_or_jeremiah(yt_sentiment)
        st.markdown(
            """ 
                <h2 style='color:#CB8F40;'>IMDb</h2>
            """, unsafe_allow_html=True)
        tv_config.team_conrad_or_jeremiah(imdb_reviews_df)
    with col2:
        spotify_analysis.discover_artists(df)

st.title("🎧 Sounds of the show")
col1, col2 = st.columns([1, 1])
st.components.v1.html('<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWVEaynofUD86?utm_source=generator" width="100%" height="400" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>')

youtube_config.generate_likes_and_views_chart(video_details)

tv_config.episode_rating(episodes_df)

st.header("Explore more of Jenny Han")
st.subheader("Jenny Han Cinematic Universe")
st.write("### Movies")
jenny_han_adaptations_df = pd.read_csv('data/jenny_han_cinematic_universe.csv')
tv_config.fetch_jenny_han_cinematic_universe(jenny_han_adaptations_df)
st.write("### Books")
jenny_han_books_df = pd.read_csv('data/jenny_han_books.csv')
books_config.show_jenny_han_books(jenny_han_books_df)

st.write("#### 🌊 Feel free to reach out to me at martina.reyes.thesis@gmail.com")