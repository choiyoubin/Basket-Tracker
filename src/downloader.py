import yt_dlp
import os

def download_youtube_video(url: str, output_path: str = "data/videos", filename: str = "input_video.mp4"):
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, filename)

    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': output_file,
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"✅ Downloaded video to: {output_file}")
    return output_file