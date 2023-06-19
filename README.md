# YT-subtitles-dataset

This project is used to create machine translation dataset from YouTube video that has subtitles in multiple languages. It can also be used for scraping youtube subtitles for other purposes. It uses web scraping and [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading so you are not subjected to YouTube API quota limitation.  

Note: Now everything is processed sequentially, implementing parallel downloading may help speed up downloading subtitles.  

`check_channel_subtitles.ipynb` - Check if video in that channel have subtitles  
`download_yt_subs.py` - Download subtitles from channel url  
`create_sentence_pair.ipynb` - Match up subtitles in similar time intervals into pair 
