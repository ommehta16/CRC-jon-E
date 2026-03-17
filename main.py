import cv2, time, sys, easyocr
import ssl

import numpy as np

ssl._create_default_https_context = ssl._create_unverified_context

print("Ready!")
cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")


reader = easyocr.Reader(['en'])

time.sleep(1)
if not cap.isOpened():
	sys.exit(1)


while True:
	ret, frame = cap.read()
	if not ret:
		print("End of feed")
		break
	# print("got frame")
	results:list[tuple[list[list[float,float]],str,float]]=reader.readtext(frame)

	for box in results:
		bounds, text, prob = box
		# print("Bounds:", bounds)
		if prob<0.8: continue
		cv2.rectangle(frame,np.asarray(bounds[0],np.uint16),np.asarray(bounds[2],np.uint16),(255,0,0))
		cv2.putText(frame,text,np.asarray(bounds[0],np.uint16),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),thickness=2)
		# cv2.putText(frame,text,np.asarray(bounds[0],np.uint16),cv2.FONT_HERSHEY_COMPLEX,12,(0,0,0))
		
	# if len(text):
		# print(text)

	cv2.imshow("frame",frame)
	if cv2.waitKey(1) in [ord('q'),27]:
		print("quit")
		break
	
	# print("shown frame")
	# time.sleep(1)

	# if text:
	# 	print(text)