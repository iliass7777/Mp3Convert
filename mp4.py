import sys
import yt_dlp

def download_mp4(url, output):
    ydl_opts = {
        'ffmpeg_location': r'C:\Users\pc\Downloads\ffmpeg\bin',
        'format': 'bestvideo+bestaudio/best',  # Télécharge la meilleure qualité de vidéo et audio
        'outtmpl': f"data/{output}",
        'merge_output_format': 'mp4',  # Force la sortie au format MP4
    }
    try:
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        ydl.download([url])
        print("Téléchargement en MP4 réussi !")
    except Exception as e:
        print(f"Erreur lors du téléchargement : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        output = sys.argv[2]
        download_mp4(url, output)
    else:
        print("Usage : python script.py <URL> <chemin de sortie>")
