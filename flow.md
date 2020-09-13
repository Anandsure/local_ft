# Flow of Project:

There are 2 routes:

1. File Uploader:
- Upload files from user system to server.
- Server saves the direct format under a storage area.
- If it's a video, the server automatically transcodes the video into an `hls stream` format.

2. Web Player:
- Should provide a list of converted videos.
- Will play off the hls stream format.
- Quality selection.