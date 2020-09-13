# Local File Transfer

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/AnandSure/local_ft?logo=github&style=social)](https://github.com/AnandSure/) [![GitHub last commit](https://img.shields.io/github/last-commit/AnandSure/local_ft?style=social&logo=git)](https://github.com/AnandSure/) [![GitHub stars](https://img.shields.io/github/stars/AnandSure/local_ft?style=social)](https://github.com/AnandSure/local_ft/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AnandSure/local_ft?style=social&logo=git)](https://github.com/AnandSure/local_ft/network)

Make your own Netflix like server with an easy to use and modify library where you can share files and videos as well as stream them in seconds.

![Generic badge](https://img.shields.io/badge/Local_File-Transfer-orange) 

#### Link for [demo](#!) 
[![Generic badge](https://img.shields.io/badge/view-demo-orange)](#!)

## Inspiration:
Anand's uncle told him how tedious it was to share files and videos in his office by clients (he runs a firm which solves problems and bugs in websites and apps and hence gets demo videos and screenshots). They used to use Google Drive and Dropbox but in the end it took a lot of time and had memory restrictions too. This is when we decided to make Local File Transfer.

Also- Who doesn't want to make their own YouTube or Netflix?

## Features
- [x] Data Transfer.
- [x] Streaming via local RTC (Videos).
- [x] Audio Streaming.
- [x] Frame Compression (different qualities).
- [x] UI for streaming / File Transfer.
- [x] Integration of all independent modules.
- [x] Customisable DIY server.

## Requirements

[![GitHub top language](https://img.shields.io/github/languages/top/AnandSure/local_ft?logo=css&style=social)](https://github.com/AnandSure/)

The source code of this project is written in **`HTML/CSS/JS`**, and runs on a **`Flask`** server with `ffmpeg` as a dependency so you will need to install Flask through the requirements file and ffmpeg from the package-lock.json file.

## Instructions to Run
```
$ git clone https://github.com/AnandSure/local_ft
$ cd local_ft
$ npm install
$ cd streaming && pip3 install -r requirements.txt
$ cd static && mkdir media && cd ..
$ python3 run.py
```

## Accomplishments we are proud of
We were able to actually make the project work within such a small time frame.

## What we learnt and Challenges we faced
We learnt how YouTube works with the m3u8 stream format. It sends video in parts and loads only part by part. A whole video never loads. We stream it in packets.

It took us a while to figure this out.

## What next?
An option to share and preview PDFs, PPTs, CSVs, Excel and Word Documents.

## Made with :heart: by
[Anand Suresh](https://github.com/AnandSure), [Akshat Gupta](https://github.com/akshatvg) and [Sai Sandeep](https://github.com/raysandeep).


```bash



 _____ _                 _     __   __            
|_   _| |               | |    \ \ / /            
  | | | |__   __ _ _ __ | | __  \ V /___  _   _   
  | | | '_ \ / _` | '_ \| |/ /   \ // _ \| | | |  
  | | | | | | (_| | | | |   <    | | (_) | |_| |  
  \_/ |_| |_|\__,_|_| |_|_|\_\   \_/\___/ \__,_|  
                                                  
                                                  
______                                            
|  ___|                                           
| |_ ___  _ __                                    
|  _/ _ \| '__|                                   
| || (_) | |                                      
\_| \___/|_|                                      
                                                  
                                                  
______      _               _   _               _ 
| ___ \    (_)             | | | |             | |
| |_/ / ___ _ _ __   __ _  | |_| | ___ _ __ ___| |
| ___ \/ _ \ | '_ \ / _` | |  _  |/ _ \ '__/ _ \ |
| |_/ /  __/ | | | | (_| | | | | |  __/ | |  __/_|
\____/ \___|_|_| |_|\__, | \_| |_/\___|_|  \___(_)
                     __/ |                        
                    |___/                         

 


```

## License

**MIT &copy; [Anand Suresh](https://github.com/AnandSure/local_ft/blob/master/LICENSE)**

[![GitHub license](https://img.shields.io/github/license/AnandSure/local_ft?style=social&logo=github)](https://github.com/AnandSure/local_ft/blob/master/LICENSE) 

---------

```javascript

if (youEnjoyed) {
    starThisRepository();
}

```

-----------

