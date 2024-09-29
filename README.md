# YouTube Playlist Duration Calculator

This Python script calculates the total duration of videos in a specified YouTube playlist using the YouTube Data API. It aggregates the durations of all videos in the playlist and outputs the total duration.

## Features

- Fetches all videos in a YouTube playlist.
- Calculates the total duration of the playlist in hours, minutes, and seconds.
- Uses the YouTube Data API for video information retrieval.

## Prerequisites

- Python 3.x
- YouTube Data API key (you can obtain this by creating a project on the [Google Developers Console](https://console.developers.google.com/))

## Installation

1. Clone the repository:

    git clone https://github.com/yourusername/Youtube_playlist_time_calculator.git
   
3. Navigate to the project directory:

    cd Youtube_playlist_time_calculator

3. Install the required packages:

    pip install google-api-python-client isodate


## Usage:

1. Open the script (demo.py) and replace the API_KEY with your actual YouTube API key:
   
    API_KEY = "YOUR_API_KEY"
   
2. Replace the playlist_id with your desired YouTube playlist ID:
   
    playlist_id = "YOUR_PLAYLIST_ID"  # Example: "PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_"
  
3. Run the script:
   
    python demo.py

