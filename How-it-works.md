# How it works

## ffmpeg
Couldn't have done it without this Tool. thx...

This tool is almost a shell script.

But I'm not familiar with shell script, and python has better extensiblity, I chosed python.

## abstracted flow
1. split the orgin video into two pieces. (at the split point, the frame will be added.)
2. create a single-frame video
3. merge three video files. (audio will be shifted..maybe like miliseconds)

there will be side-features like checking the resolution of the video, frame rate, file format, whatever..

## Detail flow
suppose there are no exception

1. get two inputs : video file, single image file.
- get some madatas of each file
- check compatibiltiy
2. get additional input : time to insert an image
- split the video file into two, with the given time
- create a single-frame video
- add three videos (split1 + single_frame + split2)
3. get additional input : path to save result file
- save the video file to given path.

can get the inputs interactively, or from some configuration file.
