from moviepy.editor import *

video = VideoFileClip('强风大背头.mp4')
audio = video.audio
audio.write_audiofile('test.mp3')