import moviepy.editor
from pathlib import Path

video_file = Path('test/source.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'test/{video_file.stem}.mp3')