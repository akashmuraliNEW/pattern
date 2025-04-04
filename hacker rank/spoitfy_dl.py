from spotdl import Spotdl

# Download the song
songs = spotdl.search([spotify_url])  # Search for the song
result = spotdl.download_songs(songs)  # Download it

# Print the result
for song, path in result:
    if path:
        print(f"Downloaded '{song.display_name}' to {path}")
    else:
        print(f"Failed to download '{song.display_name}'")
