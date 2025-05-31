from pytube import YouTube
import os

def download_youtube_video(url: str, output_path: str = "data/videos", filename: str = "input_video.mp4"):
    os.makedirs(output_path, exist_ok=True)
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4", res="720p").first()

    if stream is None:
        raise Exception("720p mp4 stream not found. Try a different video or resolution.")

    output_file = stream.download(output_path, filename=filename)
    print(f"Downloaded video to: {output_file}")
    return output_file

# 사용 예시
if __name__ == "__main__":
    test_url = "https://www.youtube.com/live/MtHBhozLOtk?si=GzQu6-uRoWhixQC5"
    download_youtube_video(test_url)