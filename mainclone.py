from facial_landmarks import FL
from facial_to_np import shaping
from threading import Thread
from torpor_ratio import ratio, mouthratio
from alert_sound import alarm
from videostream import VideoStream
import numpy as np
import time
import dlib
import cv2

args = {'shape_predictor': 'shape_predictor_68_face_landmarks.dat', 'alarm': 'alarm_final.wav', 'webcam': 0}

TORPOR_THRESH = 0.3
TORPOR_THRESH_MOUTH_Lower= 21
TORPOR_THRESH_MOUTH_Upper= 100

FRAMES = 20
FRAMES_MOUTH = 20

COUNTER = 0
COUNTER_MOUTH = 0

ALARM_MODE = False
ALARM_MODE_MOUTH = False

print("Facial Landmark Prediction System Loading...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

FACIAL_LANDMARKS=FL()
# retrieve the indexes of the facial landmarks for the left and right eye
(lStart, lEnd) = FACIAL_LANDMARKS["left_eye"]
(rStart, rEnd) = FACIAL_LANDMARKS["right_eye"]
(mStart,mEnd) = FACIAL_LANDMARKS["mouth"]

print("Video Stream Loading...")
vs = VideoStream(src=args["webcam"]).start()
time.sleep(1.0)

# loop over frames from the video stream
while True:

	frame = vs.read()
	(h, w) = frame.shape[:2]
	frame = cv2.resize(frame, (w,h), interpolation=cv2.INTER_AREA)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	rects = detector(gray, 0)

	# loop over the face detections
	for rect in rects:
		
		shape = predictor(gray, rect)
		shape = shaping(shape)

		
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		mouth=shape[mStart:mEnd]
		leftEye_ = ratio(leftEye)
		rightEye_ = ratio(rightEye)

		mouth_ratio = mouthratio(mouth)
		eye_ratio = (leftEye_ + rightEye_) / 2.0

		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		mouthHull = cv2.convexHull(mouth)

		cv2.drawContours(frame, [leftEyeHull], -1, (255, 255, 255), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (255, 255, 255), 1)
		cv2.drawContours(frame, [mouthHull], -1, (0, 255, 255), 2)


		if mouth_ratio > TORPOR_THRESH_MOUTH_Lower:
			COUNTER_MOUTH +=1

			if COUNTER_MOUTH>=FRAMES_MOUTH:
				# if not ALARM_MODE_MOUTH:
				# 	ALARM_MODE_MOUTH=True

				# 	if args["alarm"] != "":
				# 		t = Thread(target=alarm,
				# 			args=(args["alarm"],))
				# 		t.deamon = True
				# 		t.start()

				# cv2.putText(frame, "MOUTH ALERT!", (10, 30),
				# 	cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

				cv2.putText(frame, "Focus on Driving", (10,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2, 1, False)

		else:
			COUNTER_MOUTH = 0
			ALARM_MODE_MOUTH = False


		if eye_ratio < TORPOR_THRESH:
			COUNTER += 1

			if COUNTER >= FRAMES:
				if not ALARM_MODE:
					ALARM_MODE = True

					if args["alarm"] != "":
						t = Thread(target=alarm,
							args=(args["alarm"],))
						t.deamon = True
						t.start()

				cv2.putText(frame, "WAKE UP!", (10, 30),
					cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)


		else:
			COUNTER = 0
			ALARM_MODE = False


		cv2.putText(frame, "Eye Ratio: {:.2f}".format(eye_ratio), (300, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	if key == ord("l"):
		break

cv2.destroyAllWindows()
vs.stop()