import cv2
import datetime

camera = "rtsp://admin:abcd1234@192.168.9.10:554/h264/ch4/main/av_stream"

cap = cv2.VideoCapture(camera)

# catch camera
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print("Capture_FPS:", fps, ", Capture_SIZE:", size)

fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
outVideo = cv2.VideoWriter('saveRTSP.avi',fourcc,fps,size)

if cap.isOpened():
    rval,frame = cap.read()
    print('ture')
else:
    rval = False
    print('False')


tot=1
c=1
i=0

# To set read_frames: 25fps * 60seconds * 2 = 3000 frames: total 2 minutes 
while i<3000: 
    rval,frame = cap.read()
    cv2.imshow('test',frame)
      
    tot+=1
    i+=1
    print('tot=',tot)

    outVideo.write(frame)
    cv2.waitKey(1)
      
cap.release()
outVideo.release()
cv2.destroyAllWindows()
