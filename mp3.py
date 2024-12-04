
import yt_dlp
import sys
# ydl_opts = {
#     'ffmpeg_location': r'C:\Users\pc\Downloads\ffmpeg\bin',
#     'format': 'bestaudio/best',
#     'outtmpl': 'data/raw_files/%(title)s.%(ext)s',
#     'postprocessors': [
#         {
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }
#     ],
#     'prefer_ffmpeg': True,
# }

# ydl = yt_dlp.YoutubeDL(ydl_opts)
# ydl.download(['https://youtu.be/nvd1lJDCvEA?si=cNTIWRXQnDMSYq6-'])


# url='https://youtu.be/vV7Juy14GPA?si=vaJr-WsZqAOXzwC7'
def mp3(url,output):
    ydl_opts = {
    'ffmpeg_location': r'C:\Users\pc\Downloads\ffmpeg\bin',
    'format': 'bestaudio/best',
    'outtmpl': output,
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
    'prefer_ffmpeg': True,
}
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    ydl.download([url])
    
    print("Téléchargement et conversion en MP3 réussis !")

if __name__ == "__main__":
   
    if len(sys.argv) > 1:
        url = sys.argv[1]
        output=sys.argv[2]
        mp3(url,output)
    else:
        print("Aucune URL fournie.")