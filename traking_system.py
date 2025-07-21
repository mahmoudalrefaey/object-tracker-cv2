import cv2
import sys

cap = cv2.VideoCapture(0)

# check if the webcam is opened correctly
if not cap.isOpened():
    print("(Error) Could not open webcam")
    sys.exit(1)
    
# read first frame for ROI
val, frame = cap.read()

# select ROI
try:
    roi = cv2.selectROI("roi", frame)
    cv2.destroyWindow("roi")
except Exception as e:
    print(f"(Error) Exception during ROI selection: {e}")
    sys.exit(1)
    
# initialize CSRT tracker algorithm
try:
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, roi)
except Exception as e:
    print(f"Error during tracker initialization: {e}")
    sys.exit(1)
    
# main loop
while True:
    # read frame from webcam
    val, frame = cap.read()
    
    # update tracker
    success, box = tracker.update(frame)
    
    # draw bounding box
    if success:
        x, y, w, h = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking..", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost tracking!", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
    # display frame
    cv2.imshow("Live Tracking", frame)
    
    # exit if ESC is pressed
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()