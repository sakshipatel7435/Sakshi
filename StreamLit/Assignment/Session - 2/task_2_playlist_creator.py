# 2. Build a Streamlit sidebar in a file called playlist_creator.py where the user can enter a playlist name using a text input, select the number 
# of songs with a number input, and choose a music genre from a dropdown (selectbox) with options like 'Pop', 'Rock', 'Hip-Hop', 'Classical'. When the
# user clicks a 'Create Playlist' button, display their choices on the main page.

import streamlit as st

st.title("My Music Playlists")

st.sidebar.header("Playlist Settings")
playlist_name = st.sidebar.text_input("Enter Playlist Name")
song_count = st.sidebar.number_input("Number of Songs", min_value=1, max_value=100, value=10)
genre = st.sidebar.selectbox("Music Genre", ["Pop", "Rock", "Hip-Hop", "Classical"])
create_btn = st.sidebar.button("Create Playlist")

if create_btn:
    st.success(f"Playlist **'{playlist_name}'** successfully created!")
    st.write(f"**Genre:** {genre}")
    st.write(f"**Total Songs:** {song_count}")
