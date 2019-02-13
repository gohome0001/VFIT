import os, subprocess, sys

TMPDIR = "./vfit/"
TMP_MERGE = "tmp_merge"
TMP_MERGE_PATH = TMPDIR+'/'+TMP_MERGE
TMP_SINGLE = "tmp_test.mp4"
TMP_SINGLE_PATH = TMPDIR + '/' + TMP_SINGLE

OUTPUT_PATH = './output.mp4'

def initialize():
    if not os.path.exists(TMPDIR):
        os.makedirs(TMPDIR)
    f = open(TMP_MERGE_path)
    f.close()
    del f

def get_metadata(file_path):
    command = "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1:nk=1 "+file_path
    r = subprocess.check_output(command,shell=true)
    return r.split('\n')
# ffmpeg -i filename -f ffmetadata result.txt
# filter with %dx%d (i.e. 1920x1080)
# or 
# ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1:nk=1 filename

def check_compatable(vid_path,img_path): # resolution check.
    img_res = get_res(img_path)
    if get_res(vid_path) == image_res:
        return image_res
    else:
        return False
    

def merge_vid(vid_path_list, save_path):
    f = open(TMP_MERGE_PATH,'wb'):
        for i in vid_path_list:
            f.writeline("file '%s'" % i)
    f.close()
    command = "ffmpeg -f concat -safe 0 -i "+TMP_MERGE_PATH+" -c copy " + OUTPUT_PATH
    r = subprocess.check_output(command, shell=truea)
    # ffmpeg -f concat -safe 0 -i mylist.txt -c copy output

def create_vid(image_path,fps,res):
    command = "ffmpeg -r "+fps+" -f image2 -s "+res+" -i "+image_path+" -vframes 1 -vcodec libx264 -crf 25 -pix_fmt yuv420p "+TMP_SINGLE_PATH
    subprocess.check_output(command, shell=true)
    return TMP_SINGLE_PATH
# ffmpeg -r fps -f image2 -s revolution(i.e. 720x480) -i filename -vframes 1 -vcodec libx264 -crf 25 -pix_fmt yuv420p test.mp4


def split_vid(vid_path, time1, time2):
    commnad1 = "ffmpeg -i "+vid_path+".mp4 -acodec copy -vcodec copy -ss 00:00:00 -t "+time1+" "+TMP_MERGE_PATH+"1.mp4"
    command2 = "ffmpeg -i "+vid_path+".mp4 -acodec copy -vcodec copy -ss "+time1+" -t "+time2+" "+TMP_MERGE_PATH+"2.mp4"
    return [TMP_MERGE_PATH+"1.mp4", TMP_MERGE_PATH+"2.mp4"]
# ffmpeg -i ORIGINALFILE.mp4 -acodec copy -vcodec copy -ss START -t LENGTH OUTFILE.mp4

def main(vid_path, img_path):
    img_res = check_compatabe(vid_path,img_path)
    if !img_res:
        print "check the resolution of an image file"
        exit(1)
    # 19.02.13 unfinished..


if __name__ == "__main__":
    vid_path = sys.argv[1]
    img_path = sys.argv[2]
    time = sys.argv[3]
    main(vid_path, img_path, time)
