from moviepy.editor import VideoFileClip

FILE = 'sample.MOV'
clip = VideoFileClip(FILE)
data = clip.iter_frames(fps=None, with_times=True, progress_bar=True)

for time, rgb in data:
    print('\n', time)
    print(rgb)
