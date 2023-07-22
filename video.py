from pytube import YouTube
from pytube.exceptions import PytubeError

class DownloadVideo:
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def get_audio(self):
        youtube = self._download_youtube_video()
        audio = youtube.streams.filter(only_audio=True, file_extension='mp3').first()
        if audio:
            try:
                audio.download(output_path=self.output_path)
                print('Трек успешно скачан.')
            except PytubeError as e:
                print('Ошибка при скачивании трека:', e)
        else:
            print('Трек в формате mp3 не доступна для скачивания.')

    def get_video(self):
        youtube = self._download_youtube_video()
        video = youtube.streams.get_highest_resolution() 
        if video:
            try:
                video.download(output_path=self.output_path)
                print('Видео успешно скачано.')
            except PytubeError as e:
                print('Ошибка при скачивании видео:', e)

    def get_video_info(self):
        video_info = self._download_youtube_video()
        if video_info:
            return {
                'Название видео': video_info.title,
                'Автор': video_info.author
            }
        return None

    def _download_youtube_video(self):
        try:
            youtube = YouTube(self.url)
            return youtube
        except PytubeError as e:
            print('Ошибка при получении видео:', e)
            return None

if __name__ == '__main__':
    video_url = 'Ссылка на ютюб'
    output_directory = 'Путь для сохранения'
    
    downloader = DownloadVideo(video_url, output_directory)
    print(downloader.get_video_info())
    downloader.get_audio()
