from src.downloader import download_youtube_video
from src.frameextractor import extract_frames

def main():
    url = "https://www.youtube.com/live/MtHBhozLOtk?si=01Nywol_2dsmLtydso"  # 영상 링크로 교체
    video_path = download_youtube_video(url)
    extract_frames(video_path)

if __name__ == "__main__":
    main()