import numpy as np
import csv
from moviepy.editor import VideoFileClip
 
FILE = 'sample_red.MP4'
#FILE = 'Rick Astley - Never Gonna Give You Up.mp4'
clip = VideoFileClip(FILE)
data = clip.iter_frames(fps=None, with_times=True, progress_bar=True)
 
rgb_list = []
times_list = []
 
for time, rgb in data:
     times_list.append(time)
     rgb_list.append(rgb)

with open('framedata.csv','wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = ['time','RED', 'GREEN','BLUE']
    a.writerow(data)


frame_averages = []
for time, frame in zip(times_list, rgb_list):
    #print(time)
 
    line_averages = []
    for line in frame:
        line_average = np.average(line, axis=0)
        line_averages.append(line_average)
 
    line_averages = np.array(line_averages)
    frame_average = np.average(line_averages, axis=0)
    
    with open('framedata.csv','a') as fp:
        a = csv.writer(fp, delimiter=',')
        total = frame_average[0]+frame_average[1]+frame_average[2]
        data = [[time, (frame_average[0]/total)*100, (frame_average[1]/total)*100, (frame_average[2]/total)*100]]
        a.writerows(data)
    
    #print(frame_average)
    frame_averages.append(frame_average)
 
frame_averages = np.array(frame_averages)
movie_average = np.average(frame_averages, axis=0)

with open('data.csv','wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = [['colors', 'finalcolor'],['Red', movie_average[0]], ['Green', movie_average[1]], ['Blue', movie_average[2]]]
    a.writerows(data)

#print(movie_average)
