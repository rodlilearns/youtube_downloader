import os
from pytubefix import Playlist

PLAYLISTS_FILE = "playlists.txt"
HISTORY_FILE = "history.txt"
OUTPUT_FOLDER = "Downloads"

def load_list(filename):
    """Loads lines from text file cleanly, ignoring comments"""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
def save_to_history(video_id):
    """Appends a newly downloaded video ID to the history database file."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{video_id}\n")

def check_and_download_music(base_output_path="Downloads/Music"):
    playlist_urls = load_list(PLAYLISTS_FILE)
    history = set(load_list(HISTORY_FILE)) 
    
    if not playlist_urls:
        print(f"Please add some album/playlist URLs to your '{PLAYLISTS_FILE}' first.")
        return

    print(f"Scanning {len(playlist_urls)} playlist sources for new tracks...")

    # Loop through PLAYLISTS_FILE and grab playlists
    for url in playlist_urls:
        try:
            pl = Playlist(url)
            print(f"\nChecking Playlist Album: {pl.title}")
            all_attributes = dir(pl)

            # To see what attributes are available for pl, uncomment the following stanza
            # for attribute in all_attributes:
            #     if not attribute.startswith("_"):
            #         print(attribute)

            for video in pl.videos:
                if video.video_id not in history:
                    print(f"\n🎵 New track discovered! -> '{video.title}'")
                    print("Starting download...")

                    audio_stream = video.streams.get_audio_only()
                    video_title = video.title
                    artist_name = video.author if video.author else pl.title
                    dividers = [" - ", " | ", " • "]
                    has_divider = any(d in video_title for d in dividers)
                    # Scrubbing
                    if has_divider:
                        used_divider = next(d for d in dividers if d in video_title)
                        parts = video_title.split(used_divider)
                        
                        # Clean up each piece
                        cleaned_parts = [p.replace("@", "").strip() for p in parts if p.lower().strip() != "topic"]
                        
                        # Universally assume: Left side is Artist, Right side is Song
                        artist_name = cleaned_parts[0]
                        song_title = cleaned_parts[-1]
                    else:
                        # 2. Fallback if there is no divider
                        song_title = video_title.replace("@", "").strip()
                        
                        # Use video author, cleaning up "- Topic" if present
                        raw_author = video.author if video.author else pl.title
                        if " - topic" in raw_author.lower():
                            artist_name = raw_author.split(" - ")[0]
                        else:
                            artist_name = raw_author
                            
                        artist_name = artist_name.replace("@", "").strip()

                    # Final failsafe: If the artist name accidentally got resolved to the record label,
                    # but the parent playlist title looks cleaner, we can manually check for it.
                    if "music" in artist_name.lower() or "records" in artist_name.lower():
                        # If the playlist is named "Music videos", don't use it. Else, use it!
                        if "music videos" not in pl.title.lower():
                            artist_name = pl.title

                    custom_filename = f"{artist_name} - {song_title}"
                    artist_folder = os.path.join(base_output_path, artist_name)
                    os.makedirs(artist_folder, exist_ok=True)

                    downloaded_file = audio_stream.download(
                        output_path=artist_folder,
                        filename=custom_filename
                    )
                    base, ext = os.path.splitext(downloaded_file)
                    new_file = base + '.mp3'

                    if os.path.exists(new_file):
                        os.remove(new_file)
                    os.rename(downloaded_file, new_file)

                    save_to_history(video.video_id)
                    history.add(video.video_id)
                    print(f"✓ Saved and added to history.")
                else:
                    print(f"Already downloaded: {video.title} (Skipping)")
        
        except Exception as e:
            print(f"❌ Error scanning playlist {url}: {e}")
        
        # visual divider between playlists
        print("-" * 30)

if __name__ == "__main__":
    check_and_download_music()