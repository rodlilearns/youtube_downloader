# youtube_downloader
Download mp3 and mp4 from Youtube.

## Pre-requisites
1. Need the pytubefix module in the working environment.  
`pip3 install pytubefix`

## User Guide

### Download music single:  
`python3 download_music.py`  

### Download music playlists:  
1. Create `playlists.txt` in root working directory.  
2. Append playlist URLs to `playlists.txt`.  
  
Example `playlists.txt` file:  

```plaintext
# Eurovision
# 2026
https://www.youtube.com/watch?v=J3oGYo_mekw&list=PLmWYEDTNOGUJVnzG0gqW4x1-9p7ejEy67
# 2025
https://www.youtube.com/watch?v=gQOGxx6Fk9k&list=PLRIS7dI_vQcj_e31qUtuW18P8rpIYP0f7
# 2024
https://www.youtube.com/watch?v=IiHFnmI8pxg&list=PL7qAso9Bl0b_MDhKIpPJUOrdV6z1H3hv
```  
  
3. Create history.txt in root working directory.  
4. Run `python3 download_music_playlists.py`.  

### Download videos:  
1. Create `videos_to_download.txt` in root working directory.  
2. Append Channels' or Playlists' URLs to `videos_to_download.txt`.  
  
Example `videos_to_download.txt` file:  
  
```plaintext
# ABC News Loop
https://youtube.com/playlist?list=PLDTPrMoGHssD6wII6GfDuHq9XEAbMtItf&si=GDISFMDrgR5ziNd7
# ABC If You're Listening
https://youtube.com/playlist?list=PLDTPrMoGHssAfgMMS3L5LpLNFMNp1U_Nq&si=TJ04Ru9k5AAmRHcd
```  

3. Ensure history.txt exists in root working directory.  
4. Run `python3 download_videos.py`  
  
## References:  
* [pytubefix library](https://github.com/JuanBindez/pytubefix)
* [Legacy YouTube downloader library *No longer maintained*](https://github.com/pytube/pytube)
