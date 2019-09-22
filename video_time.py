import cv2
import numpy as np
import time
def load_videos(video_file,mirror=False):
    # print "load_videos"
    capture = cv2.VideoCapture(video_file)
    capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
    cv2.namedWindow('Video Life2Coding',cv2.WINDOW_AUTOSIZE)
    while True:
        
        ret_val, frame = capture.read()
 
        #if mirror:
         #   frame = cv2.flip(frame, 1)
 
        cv2.imshow('Video Life2Coding', frame)
 
        if cv2.waitKey(1) == 27:
            break  # esc to quit
 
    cv2.destroyAllWindows()
    #read_flag, frame = capture.read()
    #vid_frames = []
    #i = 1
    # print read_flag

    #while (read_flag):
        # print i
    #    if i % 10 == 0:
    #        vid_frames.append(frame)
            #                print frame.shape
    #    read_flag, frame = capture.read()
    #    i += 1
    #vid_frames = np.asarray(vid_frames, dtype='uint8')[:-1]
    # print 'vid shape'
    # print vid_frames.shape
    #capture.release()
    #print (i)
    return vid_frames
load_videos('D:/Downloads/IMG_6619.TRIM-2.mp4')
