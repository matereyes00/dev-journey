import streamlit as st
import pandas as pd

def show_jenny_han_books(df):
    df['Title'] = df['Title'].astype(str)  # Convert 'Title' to string
    # --- State Management for "Show More" ---
    if 'show_all_books' not in st.session_state:
        st.session_state['show_all_books'] = False
    def show_more():
        st.session_state['show_all_books'] = True
    if not st.session_state['show_all_books']:
        st.button("Show More Books", on_click=show_more)
    # --- Displaying the Books in a Grid ---
    books_to_display = df if st.session_state['show_all_books'] else df.head(8) # Show all or the first 8
    num_rows = (len(books_to_display) + 3) // 6  # Calculate the number of rows needed
    for row_num in range(num_rows):
        cols = st.columns(6)
        for i in range(6):
            index = row_num * 6 + i
            if index < len(books_to_display):
                book = books_to_display.iloc[index]
                title = book['Title']
                cover_url = book['Cover URL']
                with cols[i]:
                    if isinstance(cover_url, str):  # Check if cover_url is a string
                        st.image(cover_url, width=100, use_container_width=True)
                    else:
                        st.write("Cover not available.")
                    st.markdown(f"""
                                <p style='font-size:18px;'>{title}</p>""", 
                            unsafe_allow_html=True)
                