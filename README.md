# youtube_downloader
Download mp3 and mp4 from Youtube.

## Pre-requisites
Need the pytubefix module in the working environment.  
`pip3 install pytubefix`

## User Guide

Download music single:  
`python3 download_music.py`  

Download music playlists:  
1. Create artists.txt in root working directory.  
2. Append playlist URLs to artists.txt.  
Example artists.txt file:  
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
4. Run `python3 download_music_playlists.py`  

## References:
* [pytubefix library](https://github.com/JuanBindez/pytubefix)
* [Legacy YouTube downloader library *No longer maintained*](https://github.com/pytube/pytube)
