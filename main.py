from src.downloader import download_youtube_video
from src.frameextractor import extract_frames
from src.detector import detect_players_and_ball

def main():
    url = "https://www.youtube.com/live/MtHBhozLOtk?si=lyvYWnvhPzV01zko"
    video_path = download_youtube_video(url)
    extract_frames(video_path)
    detect_players_and_ball("data/frames")

if __name__ == "__main__":
    main()