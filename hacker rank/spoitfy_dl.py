from spotdl import Spotdl

# Initialize spotDL with optional Spotify credentials (remove if not using)
client_id = "your_spotify_client_id"  # Replace with your Client ID
client_secret = "your_spotify_client_secret"  # Replace with your Client Secret
spotdl = Spotdl(client_id=client_id, client_secret=client_secret)

# Spotify URL (track, playlist, or album)
spotify_url = "https://open.spotify.com/track/2TpxZ7JUBn3uwOMTVxasSE"  # Example track URL

# Download the song
songs = spotdl.search([spotify_url])  # Search for the song
result = spotdl.download_songs(songs)  # Download it

# Print the result
for song, path in result:
    if path:
