import os
from pytubefix import Channel, Playlist
from pytubefix.helpers import reset_cache

reset_cache()

SOURCES_FILE = "videos_to_download.txt"
HISTORY_FILE = "history.txt"
BASE_OUTPUT_FOLDER = "Downloads/Videos"
MAX_VIDEOS_PER_SOURCE = 3

def load_list(filename):
    """Loads lines from text file cleanly, ignoring comments"""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def save_to_history(video_id):
    """Appends a newly downloaded video ID to the history file."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{video_id}\n")

def check_and_download_videos(base_output_path=BASE_OUTPUT_FOLDER, limit=MAX_VIDEOS_PER_SOURCE):
    urls = load_list(SOURCES_FILE)
    history = set(load_list(HISTORY_FILE)) 
    
    if not urls:
        print(f"Please add YouTube URLs to '{SOURCES_FILE}' first.")
        return

    print(f"Scanning {len(urls)} sources (checking latest {limit} videos each)...\n")

    for url in urls:
        try:
            # 1. Detect if the URL is a Playlist or Channel
            if "playlist?list=" in url.lower():
                # source = Playlist(url, use_oauth=True, allow_oauth_cache=True)
                source = Playlist(url)
                folder_name = source.title
                print(f"📋 Checking Playlist: {folder_name}")
            else:
                # source = Channel(url, use_oauth=True, allow_oauth_cache=True)
                source = Playlist(url)
                folder_name = source.channel_name
                print(f"📺 Checking Channel: {folder_name}")

            # 2. Slice to grab only the latest N videos
            latest_videos = source.videos[:limit]

            for video in latest_videos:
                if video.video_id not in history:
                    print(f"\n🎥 New video discovered! -> '{video.title}'")
                    print("Starting download...")

                    # Fetch progressive MP4 stream (audio + video combined)
                    video_stream = video.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                    
                    if not video_stream:
                        video_stream = video.streams.get_highest_resolution()

                    # Save in Videos/<Channel or Playlist Name>/
                    save_folder = os.path.join(base_output_path, folder_name)
                    os.makedirs(save_folder, exist_ok=True)

                    downloaded_file = video_stream.download(output_path=save_folder)

                    save_to_history(video.video_id)
                    history.add(video.video_id)
                    print(f"✓ Saved to {downloaded_file} and updated history.")
                else:
                    print(f"Already downloaded: {video.title} (Skipping)")

        except Exception as e:
            print(f"❌ Error scanning {url}: {e}")
        
        print("-" * 30)

if __name__ == "__main__":
    check_and_download_videos()