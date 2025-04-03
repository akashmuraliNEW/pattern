from spotdl import Spotdl

# Initialize spotDL with optional Spotify credentials (remove if not using)
client_id = "5ddcddccf1f94a41bd2970641998ab9e"  # Replace with your Client ID
client_secret = "32681713fe2045a7b9b5ae5fba8bff86"  # Replace with your Client Secret
spotdl = Spotdl(client_id=client_id, client_secret=client_secret)

# Spotify URL (track, playlist, or album)
spotify_url = "https://open.spotify.com/track/2TpxZ7JUBn3uwOMTVxasSE"  # Example track URL

# Download the song
songs = spotdl.search([spotify_url])  # Search for the song
result = spotdl.download_songs(songs)  # Download it

# Print the result
for song, path in result:
    if path:
        print(f"Downloaded '{song.display_name}' to {path}")
    else:
        print(f"Failed to download '{song.display_name}'")