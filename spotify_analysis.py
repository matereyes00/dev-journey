import streamlit as st
import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv

def trailer_songs_fetch(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df

def team_conrad_or_jerimiah(df):
    df_sorted = df.sort_values(by='popularity', ascending=False)
    st.header("Team who?")
    st.write("The popularity of a track is a value between 0 and 100, with 100 being the most popular")

    st.subheader("Spotify")
    num_songs = len(df_sorted)
    for i in range(0, num_songs,2): 
        cols = st.columns(2)  
        for j in range(2):
            if i + j < num_songs:
                row = df_sorted.iloc[i + j]  
                with cols[j]:
                    if row['track_name'] == 'Daylight':
                        st.subheader('Team Jerimiah')
                        st.image(row['album_image_url'], caption=row['track_name'], width=200)
                        st.write(f"**Popularity:** {row['popularity']}")
                    if row['track_name'] == "Red (Taylor's Version)":
                        st.subheader('Team Conrad')
                        st.image(row['album_image_url'], caption=row['track_name'], width=200)
                        st.write(f"**Popularity:** {row['popularity']}")

    return df_sorted  # Return the sorted DataFrame (optional)

def discover_artists(df):
    df_sorted = df.sort_values(by='popularity', ascending=False)
    st.subheader("Discover Taylor here")
    num_songs = len(df_sorted)
    for i in range(0, num_songs, 3): 
        cols = st.columns(3)  
        for j in range(3):
            if i + j < num_songs:
                row = df_sorted.iloc[i + j]  
                with cols[j]:
                    st.image(row['album_image_url'], caption=row['track_name'], width=100)
                    st.write(f"**Popularity:** {row['popularity']}")