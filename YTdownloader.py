from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def download_and_convert_to_mp3(file_path):
    print("-----------------------------------------\n")
    print("Please note that this is prototype made in less than 1 hour. Further updates are coming .\n")
    print("Hello! Let's download and convert some YouTube videos to MP3.\n")
    print("-----------------------------------------\n")
    print("Please read the important notes in my Github @bouhamediheb\n")

    # Create a folder named "MP3" if it doesn't exist
    mp3_folder = 'MP3'
    os.makedirs(mp3_folder, exist_ok=True)

    with open(file_path, 'r') as file:
        video_urls = file.read().splitlines()

    for url in video_urls:
        try:
            yt = YouTube(url)
            
            if yt.age_restricted:
                print(f"Skipped age-restricted video: {yt.title}\n")
                continue

            video = yt.streams.filter().first()
            print(f"Downloading audio from: {yt.title}")

            try:
                video.download(output_path=mp3_folder)
            except Exception as e:
                print(f"Error downloading {url}: {e}")
                continue

            video_path = os.path.join(mp3_folder, f"{yt.title}.{video.subtype}" if video.subtype else f"{yt.title}.{video.extension}")
            audio_path = os.path.join(mp3_folder, f"{yt.title}.mp3")
            
            try:
                video_clip = VideoFileClip(video_path)
                video_clip.audio.write_audiofile(audio_path, codec='mp3')
                video_clip.close()
            except Exception as e:
                print(f"Error converting {video_path} to {audio_path}: {e}")
            
            os.remove(video_path)
            print(f"{yt.title} downloaded and converted to MP3 successfully!\n")

        except Exception as e:
            print(f"Error processing {url}: {e}\n")

download_and_convert_to_mp3('list.txt')
