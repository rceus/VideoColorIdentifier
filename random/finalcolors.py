import numpy as np
from moviepy.editor import VideoFileClip
import csv

FILE = 'sample.MOV'
clip = VideoFileClip(FILE)
data = clip.iter_frames(fps=None, with_times=True, progress_bar=True)

rgb_list = []
times_list = []
averages = {}

for time, rgb in data:
    times_list.append(time)
    rgb_list.append(rgb)

redFinalValue = 0
greenFinalValue = 0
blueFinalValue = 0

frames = 0
for time, frame in zip(times_list, rgb_list):
    print(time)
    line_average = np.array([0,0,0])
    line_count = 0
    for line in frame:
        line_average += (np.average(line, axis=0))
        line_count = line_count+1
    
    redFinalValue = redFinalValue + (line_average[0]/line_count)
    greenFinalValue = greenFinalValue + line_average[1]/line_count
    blueFinalValue = blueFinalValue + line_average[2]/line_count
    frames = frames + 1

print(frames)

print("Red")
print(redFinalValue/frames)
print("Green")
print(greenFinalValue/frames)
print("Blue")
print(blueFinalValue/frames)

"""
sumAll = redFinalValue + greenFinalValue + blueFinalValue
percetageRed = redFinalValue/sumAll
percetageGreen = greenFinalValue/sumAll
percetageBlue = blueFinalValue/sumAll
"""

with open('data.csv','wb') as fp:
    a = csv.writer(fp, delimiter=',')
    data = [['colors', 'finalcolor'],['Red', redFinalValue/frames], ['Green', greenFinalValue/frames], ['Blue', blueFinalValue/frames]]
    a.writerows(data)





