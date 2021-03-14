import os

def download_audio(request):
  SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'

  ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
      'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',

  }

  link = request.GET.get('video_url')

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download(["https://www.youtube.com/watch?v="+link])
