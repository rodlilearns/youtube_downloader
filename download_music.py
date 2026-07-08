import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable

def download_youtube_audio(url, output_path="Downloads"):
    """
    Downloads the highest quality audio from a YouTube video and saves it as an MP3.
    """
    try:
        print("\nFetching video details...")
        yt = YouTube(url, on_progress_callback=on_progress)
        
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")
        
        # Get the highest quality audio stream available
        print("Downloading audio stream...")
        audio_stream = yt.streams.get_audio_only()
        
        # Download the file (it defaults to .mp4/.webm format)
        downloaded_file = audio_stream.download(output_path=output_path)
        
        # Convert the file extension to .mp3 so music players recognize it seamlessly
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        
        # Overwrite if the mp3 already exists, otherwise rename
        if os.path.exists(new_file):
            os.remove(new_file)
        os.rename(downloaded_file, new_file)
        
        print(f"\nSuccessfully downloaded and saved to: {new_file}")
        
    except VideoUnavailable:
        print("\nError: The video is unavailable. Check the URL or age restrictions.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    # Simple loop to keep the program running for multiple downloads
    while True:
        user_url = input("\nEnter YouTube URL (or type 'q' to quit): ").strip()
        if user_url.lower() == 'q':
            print("Goodbye!")
            break
            
        if not user_url:
            print("Please enter a valid URL.")
            continue
            
        # Downloads to a local 'Downloads' folder by default
        download_youtube_audio(user_url, output_path="Downloads")