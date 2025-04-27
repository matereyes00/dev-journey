import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os
import dotenv
import requests
import time  # To be respectful to the API

def fetch_jenny_han_cinematic_universe(df):
    num_columns = 5  # You can adjust the number of posters per row
    poster_rows = [df[i:i + num_columns] for i in range(0, len(df), num_columns)]

    for row_df in poster_rows:
        cols = st.columns(num_columns)
        for i, (index, row) in enumerate(row_df.iterrows()):
            poster_url = row['Poster']
            title = row['Title']
            year = row['Year']
            with cols[i % num_columns]:
                if poster_url != 'N/A':
                    st.image(poster_url, caption=f"{title} ({year})",width=100, use_container_width=True)
                else:
                    st.write(f"**{title}**: Poster not available.")
        # if poster_url != 'N/A':
        #     st.image(poster_url, caption=f"{title} ({year})", width=300)  # Adjust width as needed
        # else:
        #     st.write(f"**{title}**: Poster not available.")

def episode_rating(df):
    st.markdown("<h1 style='text-align: center; color: #F08080;'>☀️ The Summer I Turned Pretty: Episode Ratings 🌸</h1>", unsafe_allow_html=True)

    # Two-column layout
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('Revisit your favorite Belly, Conrad and Jeremiah moments')
        st.markdown("### 🎬 Filters")
        # Season selector
        seasons = df['Season'].unique()
        selected_seasons = st.multiselect(
            "Season(s):",
            options=sorted(seasons),
            default=sorted(seasons)
        )

        # Rating sort selector
        sort_order = st.radio(
            "Sort Rating:",
            options=['Highest to Lowest', 'Lowest to Highest']
        )

    with col2:
        # Filter and sort data
        filtered_df = df[df['Season'].isin(selected_seasons)]
        ascending = True if sort_order == 'Lowest to Highest' else False
        filtered_df = filtered_df.sort_values(by='Rating', ascending=ascending)

        if filtered_df.empty:
            st.warning("No episodes found for the selected filters. Try changing them.")
            return

        # Create label for x-axis
        filtered_df['Label'] = filtered_df.apply(
            lambda row: f"S{row['Season']}E{row['Episode']} - {row['Title']}", axis=1
        )

        # Plot styling
        sns.set_style("whitegrid")
        pastel_palette = ['#FFB6B9', '#FAE3D9', '#BBDED6', '#8AC6D1']

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(
            data=filtered_df,
            x='Label',
            y='Rating',
            palette=pastel_palette * (len(filtered_df) // len(pastel_palette) + 1),
            ax=ax
        )

        ax.set_title("Episode Ratings", fontsize=18, color='#FF7F7F', weight='bold', pad=15)
        ax.set_xlabel("Episode", fontsize=13, color='#444')
        ax.set_ylabel("IMDb Rating", fontsize=13, color='#444')
        ax.tick_params(axis='x', rotation=45)
        ax.tick_params(colors='#666')
        ax.set_ylim(0, 10)
        plt.xticks(ha='right')
        plt.tight_layout()

        st.pyplot(fig)
        st.markdown(f"<p style='text-align: center; color: #888;'>🎞️ {len(filtered_df)} episode(s) shown from selected season(s).</p>", unsafe_allow_html=True)
