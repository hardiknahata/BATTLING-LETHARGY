from threading import Thread
import cv2

class VideoStream:
	def __init__(self, src=0, resolution=(320, 240),
		framerate=32, **kwargs):
		
		self.stream = cv2.VideoCapture(src)
		(self.grabbed, self.frame) = self.stream.read()

		self.stopped = False

	def start(self):
		# start the threaded video stream
		t = Thread(target=self.update, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		# grab the next frame from the stream
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				return

			# otherwise, read the next frame from the stream
			(self.grabbed, self.frame) = self.stream.read()


	def read(self):
		# return the current frame
		return self.frame

	def stop(self):
		# stop the thread and release any resources
		self.stopped = True