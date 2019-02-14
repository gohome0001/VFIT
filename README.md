# video-frame-insert-tool
tool for Inserting specific image as a single video frame

Can be used for...
- Subliminal advertisement
- franks 
- etc.

Will support MPEG codec

# USE ffmpeg
please don't give attention to this project..

with a single command of `ffmpeg`, you can do it!
```
$ ffmpeg -i video -i image \
       -filter_complex \
         "[1]setpts=4.40/TB[im];[0][im]overlay=eof_action=pass" -c:a copy out.mp4
```

ffmpeg is such a great tool..

There will be no updates since 19/02/14
