from googleapiclient.discovery import build
import isodate

# Replace with your YouTube API key
API_KEY = "AIzaSyAUV58ZxmWaZngAgibnbgkYAG6Ty4zS3xI"
youtube = build("youtube", "v3", developerKey=API_KEY)


def get_playlist_videos_duration(playlist_id):
    total_duration = isodate.parse_duration("PT0S")

    # Get all videos in the playlist
    nextPageToken = None
    while True:
        pl_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken,
        )
        pl_response = pl_request.execute()

        video_ids = []
        for item in pl_response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])

        # Get video details for each video
        vid_request = youtube.videos().list(
            part="contentDetails", id=",".join(video_ids)
        )
        vid_response = vid_request.execute()

        for item in vid_response["items"]:
            duration = isodate.parse_duration(item["contentDetails"]["duration"])
            total_duration += duration

        nextPageToken = pl_response.get("nextPageToken")
        if not nextPageToken:
            break

    return total_duration


if __name__ == "__main__":
    playlist_id = "PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_"  # Replace with your playlist ID
    duration = get_playlist_videos_duration(playlist_id)
    print(f"Total Playlist Duration: {duration}")
