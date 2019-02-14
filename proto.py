import os, subprocess, sys

TMPDIR = "./vfit"
TMP_MERGE = "tmp_merge"
TMP_MERGE_PATH = TMPDIR+'/'+TMP_MERGE
TMP_SINGLE = "tmp_test.mp4"
TMP_SINGLE_PATH = TMPDIR + '/' + TMP_SINGLE

OUTPUT_PATH = './output.mp4'

def initialize():
    if not os.path.exists(TMPDIR):
        os.makedirs(TMPDIR)
    os.system("touch "+TMP_MERGE_PATH)
    f = open(TMP_MERGE_PATH)
    f.close()
    del f

def get_res(file_path):
    command = "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1:nk=1 "+file_path
    r = subprocess.check_output(command,shell=True)
    return r.split('\n')
# ffmpeg -i filename -f ffmetadata result.txt
# filter with %dx%d (i.e. 1920x1080)
# or 
# ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1:nk=1 filename

def check_compatable(vid_path,img_path): # resolution check.
    img_res = get_res(img_path)
    if get_res(vid_path) == img_res:
        return img_res
    else:
        return False
    

def merge_vid(vid_path_list, save_path=OUTPUT_PATH):
    f = open(TMP_MERGE_PATH,'wb')
    for i in vid_path_list:
        f.writelines("file '%s'\n" % ('.'+i[len('TMPDIR'):]))
    f.close()
    command = "ffmpeg -f concat -safe 0 -i "+TMP_MERGE_PATH+" -c copy " + save_path
    r = subprocess.check_output(command, shell=True) # for further use..?
    return save_path
    # ffmpeg -f concat -safe 0 -i mylist.txt -c copy output

def create_vid(image_path,fps,res):
    command = "ffmpeg -r "+str(fps)+" -f image2 -s "+res+" -i "+image_path+" -vframes 1 -vcodec libx264 -crf 25 -pix_fmt yuv420p "+TMP_SINGLE_PATH
    subprocess.check_output(command, shell=True)
    return TMP_SINGLE_PATH
# ffmpeg -r fps -f image2 -s revolution(i.e. 720x480) -i filename -vframes 1 -vcodec libx264 -crf 25 -pix_fmt yuv420p test.mp4


def split_vid(vid_path, time1,time2=None):
#    command1 = "ffmpeg -ss 00:00:00 -i "+vid_path+" -to "+time1+" -c copy -copyts "+TMP_MERGE_PATH+"1.mp4"
#    command2 = "ffmpeg -ss "+time1+" -i "+vid_path+" -to "+time2+" -c copy -copyts "+TMP_MERGE_PATH+"2.mp4"

    command1 = "ffmpeg -ss 00:00:00 -i "+vid_path+" -to 00:00:02 -c copy -copyts "+TMP_MERGE_PATH+"1.mp4"
    command2 = "ffmpeg -ss 00:00:02 -i "+vid_path+" -to 00:00:02 -c copy "+TMP_MERGE_PATH+"2.mp4" 
    # TODO : make second command work as it should be.

    # os.system(command1)
    os.system(command2)
    return [TMP_MERGE_PATH+"1.mp4", TMP_MERGE_PATH+"2.mp4"]
# ffmpeg -i ORIGINALFILE.mp4 -acodec copy -vcodec copy -ss START -t LENGTH OUTFILE.mp4

def main(vid_path, img_path, time1, time2):
    initialize()
    img_res = check_compatable(vid_path,img_path)
    if not img_res:
        print "check the resolution of an image file"
        exit(1)
    img_res = img_res[0]+"x"+img_res[1]
    tvid2_path = create_vid(img_path,24,img_res)
    tvid1_path, tvid3_path = split_vid(vid_path, time1, time2)
    merge_path = [tvid1_path,tvid2_path,tvid3_path]
    outvid_path = merge_vid(merge_path)
    print "result : " + outvid_path
    # 

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "usage : video_path image_path vid_split_time(hh:mm:ss.fff) vid_end_time"
    vid_path = sys.argv[1]
    img_path = sys.argv[2]
    time1 = sys.argv[3]
    time2 = sys.argv[4]
    main(vid_path, img_path, time1, time2)
