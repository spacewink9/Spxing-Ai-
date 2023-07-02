import random

class MusicService:
    def __init__(self):
        self.music_library = []  # List to store music tracks
        self.playlists = {}  # Dictionary to store user playlists

    def add_track(self, track):
        # Add a music track to the music library
        self.music_library.append(track)

    def create_playlist(self, playlist_name):
        # Create a new playlist
        self.playlists[playlist_name] = []

    def add_track_to_playlist(self, playlist_name, track):
        # Add a track to a playlist
        if playlist_name in self.playlists:
            self.playlists[playlist_name].append(track)
        else:
            print("Playlist not found.")

    def play_music(self, playlist_name=None):
        # Play music either from a playlist or the entire music library
        if playlist_name:
            if playlist_name in self.playlists:
                playlist = self.playlists[playlist_name]
                if playlist:
                    random_track = random.choice(playlist)
                    print(f"Now playing: {random_track}")
                else:
                    print("Playlist is empty.")
            else:
                print("Playlist not found.")
        else:
            if self.music_library:
                random_track = random.choice(self.music_library)
                print(f"Now playing: {random_track}")
            else:
                print("Music library is empty.")
